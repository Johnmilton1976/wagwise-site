/* Production embed check, with the local proxy.

 * SEO知识库/embed_host_check.js launches Chrome with --no-proxy-server, which is
 * right for a localhost harness but cannot reach wagwise.org from this machine —
 * it fails with "Cannot read properties of null (reading 'scrollHeight')" on the
 * chocolate calculator too, so that error says nothing about the page. This one
 * sends Chrome through 127.0.0.1:7890 and reports the frame the way a host site
 * would see it.
 *
 * Usage: MSYS_NO_PATHCONV=1 node _prod_embed.js <path> <declaredHeight> [width...]
 */
const puppeteer=require('puppeteer-core');const http=require('http');
const BASE='https://wagwise.org', P=process.argv[2]||'/tools/toxic-food-dose-calculator/', D=parseInt(process.argv[3]||'980',10);
const cols=process.argv.slice(4).map(Number);
const host=w=>`<!doctype html><meta charset="utf-8"><style>body{margin:0}iframe{border:0;width:100%;display:block}</style>
<iframe id="f" src="${BASE}${P}?embed=1" width="100%" height="${D}"></iframe>
<script>addEventListener("message",function(e){var h=(e.data||{}).wagwiseHeight;if(h)document.getElementById("f").height=h});</script>`;
(async()=>{
const b=await puppeteer.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:'new',
  args:['--no-sandbox','--proxy-server=http://127.0.0.1:7890','--ignore-certificate-errors']});
for(const w of cols){
  const html=host(w);
  const srv=http.createServer((q,r)=>{r.writeHead(200,{'Content-Type':'text/html; charset=utf-8'});r.end(html)});
  await new Promise(res=>srv.listen(0,'127.0.0.1',res));
  const port=srv.address().port;
  const p=await b.newPage(); await p.setViewport({width:w,height:1000});
  try{ await p.goto('http://127.0.0.1:'+port+'/',{waitUntil:'load',timeout:60000}); }catch(e){ console.log(w,'host nav fail',e.message); }
  await new Promise(r=>setTimeout(r,1500));
  const frame=p.frames().find(f=>f.url().includes('wagwise.org'));
  let out={w,loaded:!!frame&&!frame.url().startsWith('chrome-error'),url:frame?frame.url().slice(0,60):null};
  if(frame&&!frame.url().startsWith('chrome-error')){
    try{
      out.inner=await frame.evaluate(()=>{
        const de=document.documentElement;
        const wrap=document.querySelector('.wrap.narrow')||document.body;
        const credit=document.querySelector('.embed-credit a');
        return {need:Math.ceil(wrap.getBoundingClientRect().bottom+8),sw:de.scrollWidth,cw:de.clientWidth,
                credit:credit?credit.href:null, embed:document.documentElement.className.includes('embed')};
      });
      out.frameH=await p.$eval('iframe',f=>f.height);
    }catch(e){ out.err=e.message; }
  }
  console.log(JSON.stringify(out));
  await p.close(); srv.close();
}
await b.close();
})();
