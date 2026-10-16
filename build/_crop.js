const sharp=require('sharp');
(async()=>{
  const f='C:/Users/Johnmilton/AppData/Local/Temp/src_full.png';
  const m=await sharp(f).metadata();
  await sharp(f).extract({left:0,top:m.height-1500,width:m.width,height:1500}).toFile('C:/Users/Johnmilton/AppData/Local/Temp/src_bottom.png');
  console.log('cropped', m.width+'x'+m.height);
})();
