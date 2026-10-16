// 把朱朱选好的宠物照：压缩优化 → 按文章 slug 命名 → 写入 public/assets/img/
// 用法: NODE_PATH=<workspace>/node_modules node build/apply_photos.js
const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const SRC = "D:/Personal/微信生意相关/SEO/宠物照片";
const DST = "C:/Users/Johnmilton/WorkBuddy/2026-10-11-22-05-19/pet-care-site/public/assets/img";

// 文章 slug  ->  源文件名（27 张里挑选，确保不重复）
const MAP = {
  // ── Dog Training ──
  "how-to-crate-train-a-puppy":        "pexels-haberdoedas-33757042.jpg",              // 坐着的小奶狗
  "how-to-stop-puppy-biting":          "pexels-barnabas-davoti-31615494-35241318.jpg", // 咬玩具的金毛幼犬
  "how-to-leash-train-a-dog":          "pexels-leonardo-merlo-1124828-39403302.jpg",   // 沙滩上奔跑的狗
  // ── Dog Health ──
  "dog-vomiting-causes":               "pexels-barnabas-davoti-31615494-40098530.jpg", // 趴着的金毛
  "dog-ear-infection-symptoms":        "pexels-tokuo-nobuhiro-79378678-19594751.jpg",  // 侧脸（露耳朵）
  "dog-not-eating-but-drinking-water": "pexels-barnabas-davoti-31615494-40008193.jpg", // 趴在草地上
  "why-is-my-dog-shaking":             "pexels-leonardo-merlo-1124828-10700790.jpg",   // 草地上的白狗+小狗
  "why-do-dogs-eat-grass":             "pexels-peterdanthy-32476936.jpg",              // 花园木栏上的狗
  "why-do-dogs-eat-poop":              "pexels-gustavodenuncio-26607808.jpg",          // 户外沙地上的狗
  // ── Dog Nutrition ──
  "foods-toxic-to-dogs":               "pexels-rajathraj855-38253884.jpg",             // 探头望桌上的狗
  "can-dogs-eat-bananas":              "pexels-barnabas-davoti-31615494-40098527.jpg", // 叼球的狗
  "how-much-to-feed-my-dog":           "pexels-brixiv-4459788.jpg",                    // 等着开饭的狗
  // ── Dog Care ──
  "how-to-trim-dog-nails":             "pexels-rajesh-s-balouria-1289088-40102691.jpg",// 坐着的黑狗
  "how-to-brush-dog-teeth":            "pexels-pet-foto-644780685-17742005.jpg",       // 白比熊+法斗（美容感）
  // ── Cats ──
  "cat-litter-training":               "pexels-wonderofhisworld-40199459.jpg",         // 灰猫趴着
  "cat-scratching-furniture":          "pexels-nam-quan-nguy-n-459228913-16164485.jpg",// 两只猫趴在沙发上（家具场景）
  "cat-spraying-how-to-stop":          "pexels-lexa-shep-1842481100-29328554.jpg",     // 黑白猫侧卧
  // ── Best / Reviews ──
  "best-dog-crate":                    "pexels-yunustug-8192221.jpg",                  // 车里的小白狗（箱内感）
  "best-dog-harness-for-pulling":      "pexels-matreding-31173351.jpg",                // 戴项圈的狗
  // ── Can Dogs Eat (第 2 批·2026-10-16 补图) ──
  "can-dogs-eat-apples":               "pexels-alexasfotos-12983201.jpg",              // 户外一群狗
  "can-dogs-eat-avocado":              "pexels-chevanon-1108099.jpg",                  // 草地三只金毛幼犬
  "can-dogs-eat-carrots":              "pexels-daigofotos-32710699.jpg",               // 两只狗碰鼻
  "can-dogs-eat-cheese":               "pexels-daigofotos-32710703.jpg",               // 两只狗依偎
  "can-dogs-eat-chicken":              "pexels-fca-2163612907-39060903.jpg",           // 草地里的幼犬
  "can-dogs-eat-chocolate":            "pexels-masoodaslami-30810877.jpg",             // 牧羊犬+金毛
  "can-dogs-eat-eggs":                 "pexels-nancy-guth-269359-850602.jpg",          // 三只狗合影
  "can-dogs-eat-grapes":               "pexels-thejourneyofframes-31446328.jpg",       // 两只浅色狗
  "can-dogs-eat-milk":                 "pexels-vaishnavav99-36212354.jpg",             // 红项圈比格抬头
  "can-dogs-eat-peanut-butter":        "pexels-vikram-aditya-213772137-31486083.jpg",  // 两只狗碰鼻
  "can-dogs-eat-strawberries":         "pexels-guvo59-29060983.jpg",                   // 毯子上两只狗（第 3 批 2026-10-16 补）
  "can-dogs-eat-watermelon":           "pexels-rick-josey-130171209-12474970.jpg",     // 沙地奔跑的两只狗
  // 备用（未上站，留作未来新文章/支柱配图）：brixiv-8606146 / sudhirsangwan-34762859 / thejourneyofframes-31446330
  // 另有 2 张猫图备用（brunoabdiel / ezz7），不适用于狗文
};

// 支柱页头图（pillar slug -> 源文件名），6 个支柱各一张（6 张富余图里挑）
const HERO_MAP = {
  "dog-training":  "pexels-prathsnap-3062988.jpg",                  // 两只狗嬉闹（互动/训练）
  "dog-health":    "pexels-helenalopes-3895275.jpg",                // 健康可爱的狗
  "dog-nutrition": "pexels-kostas-konidakis-2103229-9792825.jpg",   // 等饭吃的狗（营养）
  "dog-care":      "pexels-raybilcliff-7323796.jpg",                // 趴着的狗（居家护理）
  "best":          "pexels-leonardo-merlo-1124828-14568803.jpg",    // 奔跑的两只狗（好物评测）
  "cat":           "pexels-arijit-29299971.jpg",                    // 橘白猫（猫区头图）
};

(async () => {
  let n = 0, totalIn = 0, totalOut = 0;
  const process = async (slug, file) => {
    const src = path.join(SRC, file);
    if (!fs.existsSync(src)) { console.log("MISSING SRC:", file); return; }
    const out = path.join(DST, slug + ".jpg");
    await sharp(src)
      .rotate()                                   // 尊重 EXIF 方向
      .resize({ width: 1600, withoutEnlargement: true })
      .jpeg({ quality: 82, mozjpeg: true })
      .toFile(out);
    const a = fs.statSync(src).size, b = fs.statSync(out).size;
    totalIn += a; totalOut += b; n++;
    console.log(slug.padEnd(36), (a/1024/1024).toFixed(1) + "MB -> " + (b/1024).toFixed(0) + "KB");
  };
  for (const [slug, file] of Object.entries(MAP)) await process(slug, file);
  for (const [slug, file] of Object.entries(HERO_MAP)) await process(slug, file);
  console.log("\nDONE " + n + " images | " + (totalIn/1024/1024).toFixed(1) + "MB -> " + (totalOut/1024/1024).toFixed(2) + "MB");
})();
