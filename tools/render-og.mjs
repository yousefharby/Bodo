// Renders tools/og-image.html to public/img/og-image.jpg (1200x630).
// Usage: npm i -D playwright && npx playwright install chromium && node tools/render-og.mjs
import { chromium } from 'playwright';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
await page.goto(pathToFileURL(path.join(root, 'tools/og-image.html')).href);
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(500);
await page.screenshot({ path: path.join(root, 'public/img/og-image.jpg'), type: 'jpeg', quality: 88 });
await browser.close();
console.log('saved public/img/og-image.jpg');
