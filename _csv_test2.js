/* 点一下 CSV 按钮，把导出的内容按标准 CSV 规则解析回来，检查行数/列数/来源。 */
const puppeteer = require('puppeteer-core');

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
    headless: 'new', args: ['--no-sandbox', '--no-proxy-server', '--proxy-bypass-list=*']
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
  await p.goto('http://127.0.0.1:8843/dog-nutrition/food-safety-chart/', { waitUntil: 'load', timeout: 60000 });
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
  console.log('有 Source 的行=', body.filter(r => /^https:\/\/wagwise\.org\//.test(r[4] || '')).length);
  console.log('Source 为空的行=', body.filter(r => !(r[4] || '').trim()).length);
  console.log('Food 列以 Tier 开头的行(应为0)=', body.filter(r => /^Tier/.test(r[1])).length);
  console.log('--- 前 3 行 ---'); body.slice(0, 3).forEach(r => console.log('  ', JSON.stringify(r)));
  console.log('--- 最后 2 行 ---'); body.slice(-2).forEach(r => console.log('  ', JSON.stringify(r)));
  await b.close();
})();
