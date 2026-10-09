// Renders reel.html frame by frame with headless Chromium.
//   node render.cjs <outDir>                 -> every frame as JPEG (f_00000.jpg …)
//   node render.cjs <outDir> --at 0,4.2,21    -> PNG stills at the given seconds (for review)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const FPS = 30;
const DURATION = 44.0;
const WORKERS = 4;

(async () => {
  const outDir = path.resolve(process.argv[2] || 'frames');
  const atIdx = process.argv.indexOf('--at');
  const stills = atIdx > 0 ? process.argv[atIdx + 1].split(',').map(Number) : null;
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch();
  const url = 'file://' + path.resolve(__dirname, 'reel.html');
  const newPage = async () => {
    const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
    page.on('pageerror', e => { console.error('page error:', e.message); process.exitCode = 1; });
    await page.goto(url);
    await page.evaluate(() => window.ready);
    return page;
  };

  if (stills) {
    const page = await newPage();
    for (const t of stills) {
      await page.evaluate(t => window.render(t), t);
      await page.screenshot({ path: path.join(outDir, `still_${t.toFixed(2)}.png`) });
    }
    await browser.close();
    return;
  }

  const total = Math.round(FPS * DURATION);
  const per = Math.ceil(total / WORKERS);
  let done = 0;
  await Promise.all(Array.from({ length: WORKERS }, async (_, w) => {
    const page = await newPage();
    for (let i = w * per; i < Math.min(total, (w + 1) * per); i++) {
      await page.evaluate(t => window.render(t), i / FPS);
      await page.screenshot({ path: path.join(outDir, `f_${String(i).padStart(5, '0')}.jpg`), type: 'jpeg', quality: 95 });
      if (++done % 120 === 0) console.log(`${done}/${total} frames`);
    }
  }));
  await browser.close();
  console.log(`rendered ${total} frames to ${outDir}`);
})();
