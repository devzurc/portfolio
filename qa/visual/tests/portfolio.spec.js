const { test, expect } = require('@playwright/test');

const viewports = [
  [1920,1080], [1440,900], [1280,800], [1024,768],
  [768,1024], [430,932], [390,844], [375,812]
];

for (const [width, height] of viewports) {
  test(`${width}x${height} has stable layout`, async ({ page }) => {
    const failures = [];
    page.on('console', message => { if (message.type() === 'error') failures.push(message.text()); });
    page.on('pageerror', error => failures.push(error.message));
    page.on('requestfailed', request => failures.push(`${request.method()} ${request.url()}`));
    await page.setViewportSize({ width, height });
    await page.goto('/');
    await page.evaluate(() => document.fonts.ready);
    await page.locator('.fade-in').evaluateAll(nodes => nodes.forEach(node => node.classList.add('visible')));
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= document.documentElement.clientWidth)).toBeTruthy();
    expect(failures).toEqual([]);
    await page.screenshot({ path: `artifacts/implementation/${width}x${height}.png`, fullPage: true });
  });
}

test('language, metadata, mobile disclosure, anchors, and form', async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('/');
  await page.getByRole('button', { name: 'PT' }).first().click();
  await expect(page.locator('html')).toHaveAttribute('lang', 'pt-BR');
  await expect(page).toHaveTitle(/Engenheiro de Dados/);
  await page.locator('#burgerBtn').click();
  await expect(page.locator('#mobile-menu')).toHaveAttribute('aria-hidden', 'false');
  await expect(page.locator('#burgerBtn')).toHaveAttribute('aria-expanded', 'true');
  await page.keyboard.press('Escape');
  await expect(page.locator('#mobile-menu')).toHaveAttribute('aria-hidden', 'true');
  for (const id of ['hero','projects','skills','experience','certifications','job-fit','contact']) {
    await expect(page.locator(`#${id}`)).toHaveCount(1);
  }
  await page.locator('#contact-form button[type=submit]').click();
  await expect(page.locator('#form-feedback')).not.toBeEmpty();
});
