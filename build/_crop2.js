const sharp=require('sharp');
(async()=>{
  const f='C:/Users/Johnmilton/AppData/Local/Temp/src_full.png';
  await sharp(f).extract({left:0,top:3200,width:1000,height:1700}).toFile('C:/Users/Johnmilton/AppData/Local/Temp/src_mid.png');
  console.log('ok');
})();
