/* 用浏览器真实的打印媒体渲染一次，检查：页数、每页是否重复表头、页首有无标题、
   有没有导航/按钮/嵌入块混进去。用法：
     node _check_print.js [baseUrl] [outPdf]
   默认打线上页面，输出到 _tmp/print-check.pdf。 */
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const BASE = (process.argv[2] || 'https://wagwise.org').replace(/\/$/, '');
const OUT = process.argv[3] || '_tmp/print-check.pdf';
const URL_ = BASE + '/dog-nutrition/food-safety-chart/';
const LOCAL = /127\.0\.0\.1|localhost/.test(BASE);

(async () => {
  const b = await puppeteer.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: 'new',
    args: ['--no-sandbox'].concat(LOCAL ? ['--no-proxy-server'] : ['--proxy-server=http://127.0.0.1:7890', '--ignore-certificate-errors'])
  });
  const p = await b.newPage();
  await p.goto(URL_ + '?cb=' + Date.now(), { waitUntil: 'load', timeout: 60000 });
  await new Promise(r => setTimeout(r, 800));

  // 打印前应被隐藏、但仍留在 DOM 里的东西，逐个数一遍可见性
  const hidden = await p.evaluate(() => {
    const sel = ['.site-head', '.site-foot', '.crumbs', '.chart-tools', '.embed-block', '.embed-credit', '.cfc-bar'];
    return sel.map(s => {
      const el = document.querySelector(s);
      return { sel: s, present: !!el };
    });
  });

  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  await p.emulateMediaType('print');

  // 打印媒体下的实际计算样式
  const probe = await p.evaluate(() => {
    const out = {};
    const g = (s, prop) => {
      const el = document.querySelector(s);
      return el ? getComputedStyle(el)[prop] : 'MISSING';
    };
    out.headDisplay = g('.site-head', 'display');
    out.footDisplay = g('.site-foot', 'display');
    out.toolsDisplay = g('.chart-tools', 'display');
    out.embedDisplay = g('.embed-block', 'display');
    out.theadDisplay = g('.chart-tbl thead', 'display');
    out.tableFontSize = g('.chart-tbl', 'fontSize');
    out.docOverflow = g('.doc', 'overflow');
    out.docMaxH = g('.doc', 'maxHeight');
    const firstRow = document.querySelector('.chart-tbl tbody tr');
    out.firstRowDisplay = firstRow ? getComputedStyle(firstRow).display : 'MISSING';
    out.tables = document.querySelectorAll('.chart-tbl').length;
    out.rows = document.querySelector('.chart-tbl') ? document.querySelector('.chart-tbl').rows.length : 0;
    out.title = (document.querySelector('h1') || {}).textContent || '';
    return out;
  });

  await p.pdf({ path: OUT, format: 'A4', printBackground: false, margin: { top: '12mm', bottom: '12mm', left: '10mm', right: '10mm' } });
  await b.close();

  console.log('== 打印媒体下的计算样式 ==');
  Object.entries(probe).forEach(([k, v]) => console.log('  ' + k.padEnd(16), v));
  console.log('== DOM 中仍存在的隐藏元素 ==');
  hidden.forEach(h => console.log('  ' + h.sel.padEnd(16), h.present ? 'present' : 'absent'));
  console.log('== 输出 ==');
  console.log('  ' + OUT, fs.statSync(OUT).size, 'bytes');
})().catch(e => { console.error(e); process.exit(1); });
