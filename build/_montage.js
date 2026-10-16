const sharp=require('sharp');
const fs=require('fs');
const DIR='D:/Personal/微信生意相关/SEO/宠物照片/';
const files=fs.readdirSync(DIR).filter(f=>f.endsWith('.jpg'));
const src=fs.readFileSync('build/apply_photos.js','utf8');
const used=new Set([...src.matchAll(/pexels-[a-z0-9\-]+\.jpg/gi)].map(m=>m[0]));
const unused=files.filter(f=>!used.has(f));
const CW=460, CH=320, COLS=3;
const rows=Math.ceil(unused.length/COLS);
const W=CW*COLS, H=CH*rows;
(async()=>{
  const comps=[];
  for(let i=0;i<unused.length;i++){
    const x=(i%COLS)*CW, y=Math.floor(i/COLS)*CH;
    const buf=await sharp(DIR+unused[i]).resize(CW,CH,{fit:'cover'}).toBuffer();
    comps.push({input:buf,left:x,top:y});
    const label=unused[i].replace('pexels-','').replace('.jpg','');
    const svg=Buffer.from(`<svg width="${CW}" height="34"><rect width="100%" height="100%" fill="#000" opacity="0.62"/><text x="8" y="23" font-family="sans-serif" font-size="17" fill="#fff">${label}</text></svg>`);
    comps.push({input:svg,left:x,top:y+CH-34});
  }
  await sharp({create:{width:W,height:H,channels:3,background:'#111'}})
    .composite(comps).jpeg({quality:76}).toFile('build/_unused_preview.jpg');
  console.log('OK', W+'x'+H, unused.length+' imgs');
})();
