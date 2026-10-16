// 把 public/assets/og-image.svg 渲染成 og-image-wagwise.png (1200x630)
// 社媒爬虫（微信/FB/X）不支持 SVG，必须用 PNG。
// 用法: NODE_PATH=<workspace>/node_modules node build/render_og.js
const sharp = require("sharp");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const SRC = path.join(ROOT, "public", "assets", "og-image.svg");
const OUT = path.join(ROOT, "public", "assets", "og-image-wagwise.png");

(async () => {
  const svg = fs.readFileSync(SRC);
  await sharp(svg, { density: 144 })
    .resize(1200, 630, { fit: "contain", background: "#F7F5F0" })
    .png({ compressionLevel: 9 })
    .toFile(OUT);
  const st = fs.statSync(OUT);
  console.log("已生成 " + OUT + "  " + st.size + " 字节");
})();
