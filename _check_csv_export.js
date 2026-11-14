/* Click "Download the data (CSV)" and parse the blob back with real CSV rules,
   so the export contract (48 rows, five columns, a Source URL on every row,
   no tier legend posing as a food) is checked by something other than the eye.

   Usage: NODE_PATH=./node_modules node _check_csv_export.js [baseUrl]
   Defaults to the production URL; pass http://127.0.0.1:8842 to test a build. */
const puppeteer = require('puppeteer-core');

const BASE = (process.argv[2] || 'https://wagwise.org').replace(/\/$/, '');
const PROD = BASE.includes('wagwise.org');
const PAGE = BASE + '/dog-nutrition/food-safety-chart/';

function parse(txt) {
  const out = []; let row = [], cur = '', q = false;
  for (let i = 0; i < txt.length; i++) {
    const c = txt[i];
    if (q) {
      if (c === '"') { if (txt[i + 1] === '"') { cur += '"'; i++; } else q = false; }
      else cur += c;
    } else if (c === '"') q = true;
    else if (c === ',') { row.push(cur); cur = ''; }
    else if (c === '\r') { /* skip */ }
    else if (c === '\n') { row.push(cur); out.push(row); row = []; cur = ''; }
    else cur += c;
  }
  if (cur !== '' || row.length) { row.push(cur); out.push(row); }
  return out;
}

(async () => {
  const b = await puppeteer.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: 'new',
    args: PROD
      ? ['--no-sandbox', '--proxy-server=http://127.0.0.1:7890', '--ignore-certificate-errors']
      : ['--no-sandbox', '--no-proxy-server', '--proxy-bypass-list=*']
  });
  const p = await b.newPage();
  await p.evaluateOnNewDocument(() => {
    window.__csv = null;
    const o = URL.createObjectURL;
    URL.createObjectURL = function (blob) {
      blob.text().then(t => { window.__csv = t; });
      return o.call(URL, blob);
    };
  });
  await p.goto(PAGE, { waitUntil: 'load', timeout: 60000 });
  await p.click('#fc-csv');
  await new Promise(r => setTimeout(r, 1000));
  const csv = await p.evaluate(() => window.__csv);
  if (!csv) { console.log('NO CSV'); await b.close(); return; }

  const rows = parse(csv.replace(/^\ufeff/, ''));
  const body = rows.slice(1);
  console.log('总行数(含表头)=', rows.length, '| 字节=', csv.length);
  console.log('表头=', JSON.stringify(rows[0]), '| 列数=', rows[0].length);
  console.log('数据行=', body.length);
  console.log('列数不等于 5 的行=', body.filter(r => r.length !== 5).length);
  const tiers = {}; body.forEach(r => { tiers[r[0]] = (tiers[r[0]] || 0) + 1; });
  console.log('Tier 分布=', JSON.stringify(tiers));
  console.log('Source 指向食物页的行=', body.filter(r => /\/dog-nutrition\/can-dogs-eat-/.test(r[4] || '')).length);
  console.log('Source 为空的行=', body.filter(r => !(r[4] || '').trim()).length);
  console.log('Food 列以 Tier 开头的行(应为0)=', body.filter(r => /^Tier/.test(r[1])).length);
  console.log('--- 前 3 行 ---'); body.slice(0, 3).forEach(r => console.log('  ', JSON.stringify(r)));
  console.log('--- 最后 2 行 ---'); body.slice(-2).forEach(r => console.log('  ', JSON.stringify(r)));

  const ok = rows[0].length === 5
    && body.length === 48
    && body.every(r => r.length === 5)
    && body.every(r => /\/dog-nutrition\/can-dogs-eat-/.test(r[4] || ''))
    && body.every(r => /^Tier [1-4]$/.test(r[0]))
    && !body.some(r => /^Tier/.test(r[1]));
  console.log(ok ? 'PASS 48 行 × 5 列，Tier 规整，每行带来源' : 'FAIL 导出不符合契约');
  await b.close();
  process.exit(ok ? 0 : 1);
})();
