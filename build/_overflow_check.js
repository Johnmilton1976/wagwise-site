// Diagnose mobile horizontal overflow on the wagwise homepage.
const puppeteer = require('puppeteer-core');

(async () => {
  const b = await puppeteer.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: 'new',
    args: ['--no-sandbox', '--no-proxy-server', '--disable-gpu'],
  });
  const p = await b.newPage();
  await p.setViewport({ width: 390, height: 844, isMobile: true, hasTouch: true });
  await p.goto('https://wagwise.org/', { waitUntil: 'networkidle2', timeout: 60000 });
  const r = await p.evaluate(() => {
    const d = document.documentElement;
    const vw = d.clientWidth;
    const wide = [];
    document.querySelectorAll('*').forEach((e) => {
      const rect = e.getBoundingClientRect();
      if (rect.right > vw + 1 || rect.left < -1) {
        wide.push({
          el: e.tagName + (e.className && typeof e.className === 'string' ? '.' + e.className.split(' ').join('.') : ''),
          left: Math.round(rect.left), right: Math.round(rect.right), w: Math.round(rect.width),
        });
      }
    });
    return { scrollW: d.scrollWidth, clientW: vw, wideCount: wide.length, wide: wide.slice(0, 14) };
  });
  console.log(JSON.stringify(r, null, 1));
  await p.screenshot({ path: '../outputs/wagwise_mobile_true.png' });
  await b.close();
})();
