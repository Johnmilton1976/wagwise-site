// 生成全站卡片缩略图 + 首页 hero 图
// 用法: NODE_PATH=<workspace>/node_modules node build/make_thumbs.js
// 规则: img/<slug>.jpg -> img/<slug>-thumb.jpg (480x300 cover, q75, sharp 注意力裁剪聚焦主体)
//       首页 hero: 源目录 pexels-brixiv-8606146.jpg -> img/home-hero.jpg (1600x1200 4:3, q80)
// 新增文章配图后重跑一次即可（幂等，覆盖旧缩略图）。
const sharp = require("sharp");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const DIR = path.join(ROOT, "public", "assets", "img");
const SRC = "D:/Personal/微信生意相关/SEO/宠物照片/";
const HERO_SRC = SRC + "pexels-brixiv-8606146.jpg"; // 草地双狗，明亮温暖

(async () => {
  let n = 0;
  const files = fs
    .readdirSync(DIR)
    .filter((f) => /\.jpe?g$/i.test(f) && !f.includes("-thumb.") && f !== "home-hero.jpg");
  for (const f of files) {
    const out = f.replace(/\.jpe?g$/i, "") + "-thumb.jpg";
    await sharp(path.join(DIR, f))
      .resize(480, 300, { fit: "cover", position: sharp.strategy.attention })
      .jpeg({ quality: 75, mozjpeg: true })
      .toFile(path.join(DIR, out));
    n++;
  }
  await sharp(HERO_SRC)
    .resize(1600, 1200, { fit: "cover" })
    .jpeg({ quality: 80, mozjpeg: true })
    .toFile(path.join(DIR, "home-hero.jpg"));
  console.log("thumbs:", n, "+ home-hero.jpg");
})();
