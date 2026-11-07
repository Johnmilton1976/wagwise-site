const puppeteer = require('puppeteer-core');
const BASE = 'http://127.0.0.1:8899';
(async () => {
  const b = await puppeteer.launch({
    executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe',
    headless: 'new',
    args: ['--no-sandbox','--no-proxy-server','--disable-gpu'],
  });
  const out = {};

  // 1) 390px 横向溢出
  const pages = ['/dog-nutrition/food-safety-chart/','/tools/chocolate-toxicity-calculator/','/','/best/dog-crate/'];
  const p1 = await b.newPage();
  await p1.setViewport({width:390,height:844,isMobile:true,hasTouch:true});
  out.mobile = {};
  for (const u of pages){
    await p1.goto(BASE+u,{waitUntil:'networkidle2',timeout:60000});
    out.mobile[u] = await p1.evaluate(()=>document.documentElement.scrollWidth);
  }
  await p1.close();

  // 2) embed 高度 + 隐藏项
  const p2 = await b.newPage();
  await p2.setViewport({width:390,height:900,isMobile:true,hasTouch:true});
  out.embed = {};
  for (const u of ['/dog-nutrition/food-safety-chart/?embed=1','/tools/chocolate-toxicity-calculator/?embed=1']){
    await p2.goto(BASE+u,{waitUntil:'networkidle2',timeout:60000});
    out.embed[u] = await p2.evaluate(()=>({
      h: document.documentElement.scrollHeight,
      w: document.documentElement.scrollWidth,
      head: getComputedStyle(document.querySelector('.site-head')).display,
      foot: getComputedStyle(document.querySelector('.site-foot')).display,
      h1: (document.querySelector('h1')||{}).textContent,
    }));
  }
  // 3) 参数回填
  await p2.goto(BASE+'/tools/chocolate-toxicity-calculator/?weight=12&unit=kg&type=baking&amount=40&amtunit=g',{waitUntil:'networkidle2'});
  out.params = await p2.evaluate(()=>({
    weight: document.getElementById('ch-weight').value,
    type: document.getElementById('ch-type').value,
    amount: document.getElementById('ch-amount').value,
    result: document.getElementById('ch-out').textContent.slice(0,90),
    url: location.href,
  }));
  await p2.screenshot({path:'../outputs/chart_embed_1107.png'});
  console.log(JSON.stringify(out,null,1));
  await b.close();
})();
