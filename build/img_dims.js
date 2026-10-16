// 扫描 public/assets/img/ 下所有位图，输出 {slug: [width, height]} 到 build/img_dims.json
// 用法: NODE_PATH=<workspace>/node_modules node build/img_dims.js
const sharp = require("sharp");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const DIR = path.join(ROOT, "public", "assets", "img");
const OUT = path.join(__dirname, "img_dims.json");

(async () => {
  const files = fs.readdirSync(DIR).filter((f) => /\.(jpe?g|png|webp)$/i.test(f));
  const dims = {};
  for (const f of files) {
    const slug = f.replace(/\.[^.]+$/, "");
    try {
      const m = await sharp(path.join(DIR, f)).metadata();
      if (m.width && m.height) dims[slug] = [m.width, m.height];
    } catch (e) {
      console.error("SKIP", f, e.message);
    }
  }
  fs.writeFileSync(OUT, JSON.stringify(dims, null, 1) + "\n", "utf8");
  console.log("已写入 " + Object.keys(dims).length + " 条尺寸 -> " + OUT);
  console.log("示例:", Object.entries(dims).slice(0, 3).map(([k, v]) => k + "=" + v.join("x")).join("  "));
})();
