const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  outputDir: './artifacts/test-results',
  reporter: [['list'], ['json', { outputFile: 'artifacts/results.json' }]],
  use: { baseURL: 'http://127.0.0.1:4173', deviceScaleFactor: 1, colorScheme: 'dark', reducedMotion: 'reduce' },
  webServer: { command: 'python3 -m http.server 4173 --directory ../..', url: 'http://127.0.0.1:4173', reuseExistingServer: true }
});
