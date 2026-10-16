const sharp=require('sharp');
(async()=>{
  await sharp('C:/Users/Johnmilton/AppData/Local/Temp/src_full.png')
    .extract({left:0,top:2450,width:1000,height:900})
    .toFile('C:/Users/Johnmilton/AppData/Local/Temp/src_zone.png');
  console.log('ok');
})();
