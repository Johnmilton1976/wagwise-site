/* Product contract: the reverse lookup on /tools/dog-age-calculator/ must
   actually work in a browser, track the shared size select, and stay hidden
   in embed mode (so the 540px iframe declaration remains valid). */
const puppeteer = require('puppeteer-core');
const path = require('path');

const FILE = 'file:///' + path.resolve(__dirname, 'public/tools/dog-age-calculator/index.html').replace(/\\/g, '/');

async function run(embed, browser) {
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 900 });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  await page.goto(FILE + (embed ? '?embed=1' : ''), { waitUntil: 'load' });

  const res = await page.evaluate(() => {
    const rev = document.getElementById('dog-rev-out');
    const card = document.getElementById('dog-hy');
    const doc = document.querySelector('.doc');
    return {
      revText: rev ? rev.textContent.trim() : null,
      revVisible: rev ? !!(rev.offsetWidth || rev.offsetHeight || rev.getClientRects().length) : false,
      inputVisible: card ? !!(card.offsetWidth || card.offsetHeight || card.getClientRects().length) : false,
      docVisible: doc ? !!(doc.offsetWidth || doc.offsetHeight || doc.getClientRects().length) : false,
      fwdText: document.getElementById('dog-out') ? document.getElementById('dog-out').textContent.trim() : null,
    };
  });

  if (!embed) {
    // Number inputs keep their old digits when a triple-click misses; always set
    // the value directly and dispatch `input` so the assertion can never pass
    // on a stale or concatenated value (5060 -> "1009.2" once fooled /9\.2/).
    const setVal = (id, v) => page.evaluate((id, v) => {
      const el = document.getElementById(id);
      el.value = v;
      el.dispatchEvent(new Event('input', { bubbles: true }));
    }, id, v);
    // 1) default must match the static 7.2-year placeholder
    if (!/^About 7\.2 years of dog age for a medium dog/.test(res.revText))
      errors.push('default reverse reading wrong: ' + res.revText);
    // 2) hy=60, medium: 24 + 36/5 -> 9.2 dog years
    await setVal('dog-hy', '60');
    const afterInput = await page.$eval('#dog-rev-out', e => e.textContent.trim());
    if (!/^About 9\.2 years of dog age for a medium dog/.test(afterInput))
      errors.push('hy=60 / medium should read 9.2 years, got: ' + afterInput);
    // 3) changing the shared size select must change the reverse reading:
    //    hy=60, large: 24 + 36/6 -> 8.0 dog years
    await page.select('#dog-size', 'large');
    const afterSize = await page.$eval('#dog-rev-out', e => e.textContent.trim());
    if (!/^About 8\.0 years of dog age for a large dog/.test(afterSize))
      errors.push('size change should give 8.0 years for large, got: ' + afterSize);
    // 4) forward calculator must still work: 5y large -> 24 + 3*6 = 42
    await setVal('dog-age', '5');
    const fwd = await page.$eval('#dog-out', e => e.textContent.trim());
    if (!/^About 42 human years/.test(fwd))
      errors.push('forward calculator should read 42 for 5y large, got: ' + fwd);
    console.log('  normal   : reverse="' + res.revText + '"');
    console.log('  hy=60    : ' + afterInput);
    console.log('  size=large: ' + afterSize);
    console.log('  forward 5y: ' + fwd);
    if (!res.inputVisible || !res.revVisible) errors.push('reverse widget not visible on the normal page');
  } else {
    // embed mode: .doc hidden => 540px iframe declaration stays valid
    if (res.docVisible || res.inputVisible) errors.push('embed mode leaks doc / reverse widget');
    const credit = await page.evaluate(() => {
      const c = document.querySelector('.embed-credit');
      return c ? Math.ceil(c.getBoundingClientRect().bottom + 8) : -1;
    });
    console.log('  embed    : .doc visible=' + res.docVisible + ', credit bottom=' + credit + 'px (declared 540)');
    if (credit > 540) errors.push('embed content exceeds declared 540px: ' + credit);
  }

  await page.close();
  return errors;
}

async function runNarrow(browser, width) {
  const page = await browser.newPage();
  await page.setViewport({ width, height: 800 });
  await page.goto(FILE, { waitUntil: 'load' });
  const r = await page.evaluate(() => {
    const card = document.getElementById('dog-hy').closest('.calc-card');
    const b = card.getBoundingClientRect();
    return {
      docScroll: document.documentElement.scrollWidth,
      cardRight: Math.round(b.right),
      inputRight: Math.round(document.getElementById('dog-hy').getBoundingClientRect().right),
      revRight: Math.round(document.getElementById('dog-rev-out').getBoundingClientRect().right),
    };
  });
  console.log('  ' + width + 'px: scrollWidth=' + r.docScroll + ', card right=' + r.cardRight +
              ', input right=' + r.inputRight + ', result right=' + r.revRight);
  await page.close();
  const errs = [];
  if (r.docScroll > width + 1) errs.push(width + 'px: horizontal overflow, scrollWidth=' + r.docScroll);
  if (r.inputRight > width + 1 || r.revRight > width + 1)
    errs.push(width + 'px: reverse widget clipped');
  return errs;
}

(async () => {
  const browser = await puppeteer.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: true,
    args: ['--no-sandbox', '--disable-dev-shm-usage'],
  });
  let all = [];
  console.log('=== normal page ===');
  all = all.concat(await run(false, browser));
  console.log('=== embed=1 ===');
  all = all.concat(await run(true, browser));
  console.log('=== narrow viewports ===');
  for (const w of [320, 388, 720]) all = all.concat(await runNarrow(browser, w));
  await browser.close();
  if (all.length) {
    console.log('\nFAIL (' + all.length + ')');
    all.forEach(e => console.log('  - ' + e));
    process.exit(1);
  }
  console.log('\nPASS: reverse lookup + embed contract');
})().catch(e => { console.error(e); process.exit(1); });
