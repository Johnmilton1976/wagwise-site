// 生成全站卡片缩略图 + 社交分享图 + 首页 hero 图
// 用法: NODE_PATH=<workspace>/node_modules node build/make_thumbs.js
// 规则: img/<slug>.jpg -> img/<slug>-thumb.jpg (480x300 cover, q75, sharp 注意力裁剪聚焦主体)
//       img/<slug>.jpg -> img/<slug>-og.jpg    (1200x630 cover, q80 — 社媒/微信标准 1.91:1)
//       首页 hero: 源目录 pexels-brixiv-8606146.jpg -> img/home-hero.jpg (1600x1200 4:3, q80)
// 新增文章配图后重跑一次即可（幂等，覆盖旧文件）。
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
    .filter((f) => /\.jpe?g$/i.test(f) && !/-thumb\.|-og\./i.test(f) && f !== "home-hero.jpg");
  for (const f of files) {
    const base = f.replace(/\.jpe?g$/i, "");
    await sharp(path.join(DIR, f))
      .resize(480, 300, { fit: "cover", position: sharp.strategy.attention })
      .jpeg({ quality: 75, mozjpeg: true })
      .toFile(path.join(DIR, base + "-thumb.jpg"));
    await sharp(path.join(DIR, f))
      .resize(1200, 630, { fit: "cover", position: "centre" })
      .jpeg({ quality: 80, mozjpeg: true })
      .toFile(path.join(DIR, base + "-og.jpg"));
    n++;
  }
  await sharp(HERO_SRC)
    .resize(1600, 1200, { fit: "cover" })
    .jpeg({ quality: 80, mozjpeg: true })
    .toFile(path.join(DIR, "home-hero.jpg"));
  console.log("thumbs+og:", n, "pairs + home-hero.jpg");
})();

