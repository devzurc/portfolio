const fs = require('node:fs');
const path = require('node:path');
const { PNG } = require('pngjs');

(async () => {
  const { default: pixelmatch } = await import('pixelmatch');
  const root = __dirname;
  const referenceDir = path.join(root, 'reference');
  const implementationDir = path.join(root, 'artifacts', 'implementation');
  const diffDir = path.join(root, 'artifacts', 'diff');
  const overlayDir = path.join(root, 'artifacts', 'overlay');
  fs.mkdirSync(diffDir, { recursive: true });
  fs.mkdirSync(overlayDir, { recursive: true });
  const manifest = { generatedAt: new Date().toISOString(), threshold: 0.1, results: [] };
  if (!fs.existsSync(referenceDir)) throw new Error('Missing qa/visual/reference; add authoritative PNGs before comparison.');
  for (const name of fs.readdirSync(referenceDir).filter(name => name.endsWith('.png'))) {
    const implementationPath = path.join(implementationDir, name);
    if (!fs.existsSync(implementationPath)) continue;
    const reference = PNG.sync.read(fs.readFileSync(path.join(referenceDir, name)));
    const implementation = PNG.sync.read(fs.readFileSync(implementationPath));
    if (reference.width !== implementation.width || reference.height !== implementation.height) {
      manifest.results.push({ name, status: 'dimension-mismatch', reference: [reference.width, reference.height], implementation: [implementation.width, implementation.height] });
      continue;
    }
    const diff = new PNG({ width: reference.width, height: reference.height });
    const pixels = pixelmatch(reference.data, implementation.data, diff.data, reference.width, reference.height, { threshold: 0.1 });
    const overlay = new PNG({ width: reference.width, height: reference.height });
    for (let i = 0; i < overlay.data.length; i += 4) for (let channel = 0; channel < 3; channel += 1) overlay.data[i + channel] = Math.round((reference.data[i + channel] + implementation.data[i + channel]) / 2);
    for (let i = 3; i < overlay.data.length; i += 4) overlay.data[i] = 255;
    fs.writeFileSync(path.join(diffDir, name), PNG.sync.write(diff));
    fs.writeFileSync(path.join(overlayDir, name), PNG.sync.write(overlay));
    manifest.results.push({ name, status: 'compared', differingPixels: pixels, ratio: pixels / (reference.width * reference.height) });
  }
  fs.writeFileSync(path.join(root, 'artifacts', 'comparison-manifest.json'), `${JSON.stringify(manifest, null, 2)}\n`);
  if (!manifest.results.length) throw new Error('No matching reference and implementation PNGs were found.');
  if (manifest.results.some(result => result.status !== 'compared' || result.ratio > 0.005)) process.exitCode = 1;
})();
