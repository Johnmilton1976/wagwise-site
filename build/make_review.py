# 生成「配图对照表.html」：19 篇文章 → 实际配图预览（本地 file:// 引用，用于朱朱核对）
import os, sys, html
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from articles import ARTICLES, PILLARS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "public", "assets", "img")
FILEBASE = "file:///" + IMG.replace("\\", "/")

ORDER = ["dog-training", "dog-health", "dog-nutrition", "dog-care", "cat", "best"]

def asset(slug):
    for ext in ("jpg", "jpeg", "webp", "png"):
        p = os.path.join(IMG, slug + "." + ext)
        if os.path.exists(p):
            return FILEBASE + "/" + slug + "." + ext, "photo"
    return FILEBASE + "/" + slug + ".svg", "placeholder"

rows = []
real = ph = 0
for key in ORDER:
    arts = [a for a in ARTICLES if a["pillar"] == key]
    if not arts: continue
    ptitle = PILLARS[key]["title"]
    rows.append('<h2 class="grp">%s <span class="cnt">%d</span></h2><div class="grid">' % (html.escape(ptitle), len(arts)))
    for a in arts:
        src, kind = asset(a["slug"])
        if kind == "photo": real += 1
        else: ph += 1
        badge = '<span class="b ok">真图</span>' if kind == "photo" else '<span class="b no">占位(缺图)</span>'
        rows.append(
            '<div class="card"><div class="thumb"><img src="%s" loading="lazy" alt=""></div>'
            '<div class="meta"><div class="t">%s</div>'
            '<div class="sub"><code>%s</code> %s</div></div></div>'
            % (src, html.escape(a["title"]), a["slug"] + ("" if kind == "photo" else ""), badge)
        )
    rows.append('</div>')

doc = """<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8">
<title>宠物站配图对照表 · WagWise Pet</title>
<style>
 body{margin:0;background:#FBFAF7;color:#23262B;font:15px/1.5 -apple-system,"Segoe UI",Roboto,"Microsoft YaHei",sans-serif;padding:28px}
 h1{font-size:24px;margin:0 0 4px}
 .lead{color:#6B7177;margin:0 0 6px}
 .sum{margin:10px 0 22px;font-weight:600}
 .sum .ok{color:#3FA97E}.sum .no{color:#C0392B}
 .grp{font-size:17px;margin:26px 0 12px;padding-bottom:6px;border-bottom:2px solid #E7E3DA}
 .grp .cnt{font-size:12px;color:#9AA0A6;font-weight:400}
 .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
 .card{background:#fff;border:1px solid #EDE9E0;border-radius:12px;overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,.04)}
 .thumb{aspect-ratio:16/9;background:#F2EFE8;overflow:hidden}
 .thumb img{width:100%;height:100%;object-fit:cover;display:block}
 .meta{padding:10px 12px 12px}
 .t{font-weight:600;font-size:14px;line-height:1.35}
 .sub{margin-top:6px;font-size:12px;color:#8A9096;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
 code{background:#F2EFE8;padding:1px 5px;border-radius:4px;font-size:11px;color:#5A6068}
 .b{font-size:11px;padding:1px 7px;border-radius:99px;font-weight:600}
 .b.ok{background:#E4F4EC;color:#2E8B63}.b.no{background:#FDECEA;color:#C0392B}
</style></head><body>
<h1>宠物站 · 配图对照表</h1>
<p class="lead">WagWise Pet — 19 篇文章的实际配图预览（本地视图，非线上）</p>
<p class="sum">真图 <span class="ok">__REAL__</span> 篇 &nbsp;|&nbsp; 占位待补 <span class="no">__PH__</span> 篇</p>
__ROWS__
</body></html>"""
doc = doc.replace("__REAL__", str(real)).replace("__PH__", str(ph)).replace("__ROWS__", "\n".join(rows))

out = os.path.join(ROOT, "docs", "配图对照表.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(doc)
print("WROTE", out, "| real", real, "placeholder", ph)
