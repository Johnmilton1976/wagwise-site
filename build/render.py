#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Render the WagWise Pet static site into ../public/ from articles.py data.

Run:  python build/render.py
Outputs a plain static HTML site (same shape as craftfee-site):
  public/index.html, public/<pillar>/index.html, public/<article-path>/index.html,
  public/about/index.html, public/privacy/index.html, public/404.html, public/sitemap.xml

All canonical / OG / sitemap URLs use the real domain (PLACEHOLDER = "wagwise.org").
The set-domain.py scaffold is kept only as a reusable template for future sites.
"""

import os
import json
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles import SITE_NAME, PILLARS, ARTICLES, HOME, ABOUT, PRIVACY, TOOL  # noqa

PLACEHOLDER = "wagwise.org"
DOMAIN = "https://" + PLACEHOLDER
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, "public")
IMG_DIR = os.path.join(PUBLIC, "assets", "img")

# ---- Editorial identity (honest E-E-A-T byline, no fabricated credentials) ----
SITE_LAUNCH = "2026-10-16"
ORG_NAME = "WagWise Pet"

ORG_JSONLD = json.dumps(
    {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": ORG_NAME,
        "url": DOMAIN + "/",
        "logo": DOMAIN + "/assets/og-image.svg",
        "description": "An independent pet care editorial resource.",
    },
    ensure_ascii=False,
    indent=2,
)

BYLINE_HTML = (
    '<div class="byline" style="margin:28px 0;padding:16px 18px;border-left:3px solid #3FA97E;'
    'background:#F4FAF7;border-radius:8px;font-size:14px;color:#4a554c;line-height:1.65">'
    "<strong>About this article.</strong> Compiled by the %s editorial team from authoritative, "
    "publicly available sources including the American Kennel Club (AKC), the American Veterinary "
    "Medical Association (AVMA), the ASPCA, and the Merck Veterinary Manual. %s is an independent "
    "editorial resource and <em>not</em> a veterinary practice. For diagnosis, treatment, or "
    "anything urgent, please consult a licensed veterinarian.</div>"
) % (ORG_NAME, ORG_NAME)


def img_src(slug):
    """Use a real raster photo if 朱朱 dropped one in, else the SVG placeholder.

    Drop a file named <slug>.webp / .jpg / .png into public/assets/img/ and
    re-run render.py — the article will pick it up automatically.
    """
    for ext in ("webp", "jpg", "jpeg", "png"):
        if os.path.exists(os.path.join(IMG_DIR, slug + "." + ext)):
            return "/assets/img/%s.%s" % (slug, ext)
    return "/assets/img/%s.svg" % slug


def hero_src(slug):
    """Same as img_src but only returns a path when a real raster exists.

    Used for pillar hero banners — we don't want an ugly broken SVG fallback
    if a pillar has no hero photo yet.
    """
    for ext in ("webp", "jpg", "jpeg", "png"):
        p = os.path.join(IMG_DIR, slug + "." + ext)
        if os.path.exists(p):
            return "/assets/img/%s.%s" % (slug, ext)
    return None

NAV_ITEMS = [
    ("/", "Home"),
    ("/dog-training/", "Dog Training"),
    ("/dog-health/", "Dog Health"),
    ("/dog-nutrition/", "Nutrition"),
    ("/dog-care/", "Care & Grooming"),
    ("/cat/", "Cats"),
    ("/best/", "Reviews"),
    ("/tools/dog-age-calculator/", "Tools"),
    ("/about/", "About"),
]
FOOTER_ITEMS = NAV_ITEMS + [("/privacy/", "Privacy")]

CONSENT_DEFAULT = (
    "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}"
    "gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',"
    "ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500});</script>"
)

# ---- slug -> (url, title) lookup -------------------------------------------
LOOKUP = {}
for _p in PILLARS.values():
    LOOKUP[_p["slug"]] = (_p["url"], _p["title"])
for _a in ARTICLES:
    LOOKUP[_a["slug"]] = (_a["url"], _a["title"])


def nav_html(current):
    parts = []
    for href, label in NAV_ITEMS:
        cls = ' class="on"' if current == href else ""
        parts.append('<a%s href="%s">%s</a>' % (cls, href, label))
    return "\n      ".join(parts)


def footer_html():
    return "\n      ".join('<a href="%s">%s</a>' % (h, l) for h, l in FOOTER_ITEMS)


def head(title, desc, url_path, jsonld, og_type="article", article_jsonld=None):
    canon = DOMAIN + url_path
    article_script = (
        '<script type="application/ld+json">\n%s\n</script>\n' % article_jsonld
    ) if article_jsonld else ""
    return (
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<title>%s</title>\n"
        '<meta name="description" content="%s">\n'
        '<meta name="robots" content="index,follow">\n'
        '<link rel="canonical" href="%s">\n'
        '<meta property="og:type" content="%s">\n'
        '<meta property="og:site_name" content="%s">\n'
        '<meta property="og:title" content="%s">\n'
        '<meta property="og:description" content="%s">\n'
        '<meta property="og:url" content="%s">\n'
        '<meta property="og:image" content="%s/assets/og-image.svg">\n'
        '<meta property="og:image:width" content="1200">\n'
        '<meta property="og:image:height" content="630">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<meta name="twitter:title" content="%s">\n'
        '<meta name="twitter:description" content="%s">\n'
        '<meta name="twitter:image" content="%s/assets/og-image.svg">\n'
        '<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">\n'
        '<link rel="stylesheet" href="/assets/style.css?v=2">\n'
        '<script type="application/ld+json">\n%s\n</script>\n'
        '<script type="application/ld+json">\n%s\n</script>\n'
        "%s"
        "%s"
    ) % (
        title, desc, canon, og_type, SITE_NAME, title, desc, canon,
        DOMAIN, title, desc, DOMAIN,
        jsonld, ORG_JSONLD, article_script, CONSENT_DEFAULT,
    )


def shell(head_html, nav_current, body_html):
    return (
        "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n%s\n</head>\n<body>\n"
        '<header class="site-head"><div class="wrap">'
        '<a class="brand" href="/">%s</a>'
        '<nav class="nav">\n      %s\n    </nav></div></header>\n'
        "<main>%s</main>\n"
        '<footer class="site-foot"><div class="wrap">'
        '<div class="fb">\n      %s\n    </div>'
        "<p>%s is an independent pet care resource. It is not a substitute for "
        "professional veterinary advice — for anything urgent, contact a licensed "
        "veterinarian. Read our affiliate note in the privacy policy.</p></div></footer>\n"
        '<script src="/assets/cookie-consent.js" defer></script>\n'
        "</body>\n</html>\n"
    ) % (
        head_html,
        SITE_NAME,
        nav_html(nav_current),
        body_html,
        footer_html(),
        SITE_NAME,
    )


def faq_jsonld(faq):
    qa = [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in faq
    ]
    return json.dumps(
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": qa},
        ensure_ascii=False,
        indent=2,
    )


def site_jsonld():
    return json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": SITE_NAME,
            "url": DOMAIN + "/",
            "description": HOME["description"],
        },
        ensure_ascii=False,
        indent=2,
    )


def article_jsonld(a):
    d = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": a["title"],
        "description": a["description"],
        "author": {"@type": "Organization", "name": ORG_NAME, "url": DOMAIN + "/"},
        "publisher": {"@type": "Organization", "name": ORG_NAME, "url": DOMAIN + "/"},
        "mainEntityOfPage": {"@type": "WebPage", "url": DOMAIN + a["url"]},
        "image": DOMAIN + "/assets/og-image.svg",
        "datePublished": SITE_LAUNCH,
        "dateModified": SITE_LAUNCH,
    }
    return json.dumps(d, ensure_ascii=False, indent=2)


def render_article(a):
    slug = a["slug"]
    if a.get("faq"):
        jsonld = faq_jsonld(a["faq"])
        og_type = "article"
    else:
        jsonld = site_jsonld()
        og_type = "website"
    h = head(a["title"], a["description"], a["url"], jsonld, og_type, article_jsonld(a))

    # FAQ inner block
    faq_html = ""
    if a.get("faq"):
        items = "".join(
            '<div class="faq-item"><div class="faq-q">%s</div>'
            '<div class="faq-a">%s</div></div>' % (q, ans)
            for q, ans in a["faq"]
        )
        faq_html = '<div class="faq"><h2>Frequently asked questions</h2>%s</div>' % items

    # Related reading
    rel_html = ""
    if a.get("related"):
        lis = "".join(
            '<li><a href="%s">%s</a></li>' % (LOOKUP[s][0], LOOKUP[s][1]) for s in a["related"]
        )
        rel_html = '<div class="related"><h2>Related reading</h2><ul>%s</ul></div>' % lis

    disc_html = ""
    if a.get("disclaimer"):
        disc_html = '<div class="disclaimer">%s</div>' % a["disclaimer"]

    byline_html = BYLINE_HTML

    pillar = PILLARS[a["pillar"]]
    crumb = (
        '<div class="crumbs"><a href="/">Home</a> › '
        '<a href="%s">%s</a> › %s</div>'
        % (pillar["url"], pillar["nav"], a["title"])
    )
    img = '<img class="article-img" src="%s" alt="%s">' % (img_src(slug), a["title"])

    body = (
        '<div class="wrap narrow">\n'
        "  %s\n"
        '  <div class="eyebrow">%s</div>\n'
        "  <h1>%s</h1>\n"
        '  <p class="lede">%s</p>\n'
        '  <div class="adzone">ADVERTISEMENT</div>\n'
        "  %s\n"
        '  <div class="doc">%s</div>\n'
        "  %s\n"
        "  %s\n"
        "  %s\n"
        "  %s\n"
        "</div>"
    ) % (
        crumb,
        a.get("eyebrow", ""),
        a["title"],
        a["lede"],
        img,
        a["body"],
        faq_html,
        rel_html,
        disc_html,
        byline_html,
    )
    return shell(h, a["url"], body)


def render_pillar(p):
    jsonld = site_jsonld()
    h = head(p["title"], p["description"], p["url"], jsonld, "website")
    crumb = '<div class="crumbs"><a href="/">Home</a> › %s</div>' % p["title"]
    cards = ""
    for s in p.get("links", []):
        url, title = LOOKUP[s]
        cards += (
            '<a href="%s"><div class="k">GUIDE</div><h3>%s</h3>'
            "<p>%s</p></a>"
            % (url, title, LOOKUP.get(s, (None, ""))[1])
        )
    # use article description as card text
    card_html = ""
    for s in p.get("links", []):
        url, title = LOOKUP[s]
        art = next((x for x in ARTICLES if x["slug"] == s), None)
        desc = art["lede"] if art else ""
        card_html += (
            '<a href="%s"><div class="k">GUIDE</div><h3>%s</h3><p>%s</p></a>'
            % (url, title, desc)
        )
    hero_html = ""
    hs = hero_src(p["slug"])
    if hs:
        hero_html = '<img class="hero" src="%s" alt="%s">' % (hs, p["title"])

    body = (
        '<div class="wrap">\n'
        "  %s\n"
        '  <div class="eyebrow">%s</div>\n'
        "  <h1>%s</h1>\n"
        '  <p class="lede">%s</p>\n'
        "  %s\n"
        '  <div class="hub">%s</div>\n'
        '  <div class="doc"><p>%s</p></div>\n'
        "</div>"
    ) % (crumb, p.get("eyebrow", ""), p["title"], p["description"], hero_html, card_html, p.get("intro", ""))
    return shell(h, p["url"], body)


def render_home():
    jsonld = site_jsonld()
    h = head(HOME["title"], HOME["description"], "/", jsonld, "website")
    pillar_cards = ""
    for s in HOME["pillars"]:
        p = PILLARS[s]
        pillar_cards += (
            '<a href="%s"><div class="k">SECTION</div><h3>%s</h3><p>%s</p></a>'
            % (p["url"], p["title"], p["description"])
        )
    feat_cards = ""
    for s in HOME["featured"]:
        url, title = LOOKUP[s]
        art = next((x for x in ARTICLES if x["slug"] == s), None)
        desc = art["lede"] if art else ""
        feat_cards += (
            '<a href="%s"><div class="k">ARTICLE</div><h3>%s</h3><p>%s</p></a>'
            % (url, title, desc)
        )
    body = (
        '<div class="wrap">\n'
        '  <div class="eyebrow">%s</div>\n'
        "  <h1>%s</h1>\n"
        '  <p class="lede">%s</p>\n'
        '  <div class="hub">%s</div>\n'
        '  <h2 style="margin-top:40px">Popular answers</h2>\n'
        '  <div class="hub">%s</div>\n'
        "</div>"
    ) % (
        HOME.get("eyebrow", ""),
        HOME["title"],
        HOME["description"],
        pillar_cards,
        feat_cards,
    )
    return shell(h, "/", body)


def render_static(url_path, nav_current, title, desc, body_html, og_type="website"):
    h = head(title, desc, url_path, site_jsonld(), og_type)
    body = '<div class="wrap narrow">%s</div>' % body_html
    return shell(h, nav_current, body)


CALC_BODY = """
<style>
.calc-card{max-width:540px;margin:24px 0;padding:24px;background:#fff;border:1px solid #e3e0d8;border-radius:14px;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.calc-card label{display:block;font-weight:600;margin:14px 0 6px;color:#243027}
.calc-card select,.calc-card input{font-size:16px;padding:10px 12px;border:1px solid #cfcabb;border-radius:9px;background:#fff;color:#243027}
.calc-row{display:flex;gap:10px;align-items:center}
.calc-card button{margin-top:18px;width:100%;padding:13px;background:#3FA97E;color:#fff;border:0;border-radius:10px;font-size:16px;font-weight:600;cursor:pointer}
.calc-card button:hover{background:#348c69}
.calc-result{margin-top:18px;padding:16px;border-radius:10px;background:#EAF5EF;color:#1f5c43;font-size:20px;font-weight:700;text-align:center}
.calc-note{font-size:14px;color:#6b6f66;margin-top:10px}
</style>
<div class="wrap narrow">
  <div class="eyebrow">TOOLS</div>
  <h1>Dog Age Calculator</h1>
  <p class="lede">Turn your dog's age into human years. Pick a size, enter the age, and we use the standard veterinary approximation, not the old multiply-by-seven rule.</p>
  <div class="calc-card">
    <label for="dog-size">Dog size</label>
    <select id="dog-size">
      <option value="small">Small (under 20 lb / 9 kg)</option>
      <option value="medium" selected>Medium (20-50 lb / 9-23 kg)</option>
      <option value="large">Large (50+ lb / 23+ kg)</option>
    </select>
    <label for="dog-age">Age</label>
    <div class="calc-row">
      <input id="dog-age" type="number" min="0" step="0.1" value="2">
      <select id="dog-unit">
        <option value="y" selected>Years</option>
        <option value="m">Months</option>
      </select>
    </div>
    <button id="dog-go" type="button">Calculate</button>
    <div id="dog-out" class="calc-result">About 24 human years old (estimate).</div>
    <p class="calc-note">Estimate only. Larger breeds age a little faster than small ones.</p>
  </div>
  <div class="doc">
    <h2>How the estimate works</h2>
    <p>Dogs do not age at a flat 7x rate. The widely used approximation treats the first year as about 15 human years and the second as roughly 9 more, then adds 4 to 6 per year afterward depending on size: smaller dogs age slower, larger dogs faster.</p>
    <h2>Why not just multiply by 7?</h2>
    <p>A one-year-old dog is already sexually mature and well past its infancy, so 7x badly understates the first years and overstates the later ones. The size-adjusted curve is closer to how dogs actually age.</p>
    <h2>A rough guide, not a rule</h2>
    <p>This tool gives a quick sense of your dog's life stage. It is not a medical fact and cannot tell you how healthy your dog is. For health questions, see our dog health guides or ask your veterinarian.</p>
  </div>
</div>
<script>
(function(){
  function calc(){
    var size=document.getElementById('dog-size').value;
    var age=parseFloat(document.getElementById('dog-age').value)||0;
    var unit=document.getElementById('dog-unit').value;
    if(unit==='m'){ age=age/12; }
    var hy;
    if(age<=1){ hy=Math.round(age*15); }
    else if(age<=2){ hy=Math.round(15+(age-1)*9); }
    else { var f={'small':4,'medium':5,'large':6}[size]; hy=Math.round(24+(age-2)*f); }
    document.getElementById('dog-out').textContent='About '+hy+' human years old (estimate).';
  }
  document.getElementById('dog-go').addEventListener('click',calc);
  calc();
})();
</script>
"""


def render_tool(t):
    h = head(t["title"], t["description"], t["url"], site_jsonld(), "website")
    return shell(h, t["url"], CALC_BODY)


def build_sitemap():
    urls = [(HOME["url"], 1.0, "daily")]
    for s in PILLARS:
        urls.append((PILLARS[s]["url"], 0.8, "weekly"))
    for a in ARTICLES:
        urls.append((a["url"], 0.8, "monthly"))
    urls.append((ABOUT["url"], 0.3, "yearly"))
    urls.append((PRIVACY["url"], 0.2, "yearly"))
    urls.append((TOOL["url"], 0.7, "yearly"))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u, pri, freq in urls:
        lines.append("  <url>")
        lines.append("    <loc>%s%s</loc>" % (DOMAIN, u))
        lines.append("    <changefreq>%s</changefreq>" % freq)
        lines.append("    <priority>%s</priority>" % pri)
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines)


def write_page(file_path, html):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    # Home
    write_page(os.path.join(PUBLIC, "index.html"), render_home())
    # Pillars
    for s, p in PILLARS.items():
        write_page(os.path.join(PUBLIC, s.lstrip("/"), "index.html"), render_pillar(p))
    # Articles
    for a in ARTICLES:
        # url like /dog-training/how-to-.../  -> strip leading/trailing slashes
        rel = a["url"].strip("/")
        write_page(os.path.join(PUBLIC, rel, "index.html"), render_article(a))
    # About / Privacy
    write_page(
        os.path.join(PUBLIC, "about", "index.html"),
        render_static(ABOUT["url"], "/about/", ABOUT["title"], ABOUT["description"], ABOUT["body"]),
    )
    write_page(
        os.path.join(PUBLIC, "privacy", "index.html"),
        render_static(PRIVACY["url"], "/privacy/", PRIVACY["title"], PRIVACY["description"], PRIVACY["body"]),
    )
    # 404
    write_page(
        os.path.join(PUBLIC, "404.html"),
        render_static("/404.html", None, "Page not found", "The page you looked for is not here.",
                      "<h1>404</h1><p>The page you were looking for doesn't exist. "
                      "<a href=\"/\">Return home</a>.</p>"),
    )
    # Sitemap
    write_page(os.path.join(PUBLIC, "sitemap.xml"), build_sitemap())

    # Tool page
    rel = TOOL["url"].strip("/")
    write_page(os.path.join(PUBLIC, rel, "index.html"), render_tool(TOOL))

    n = 1 + len(PILLARS) + len(ARTICLES) + 2 + 1 + 1 + 1
    print("Generated %d files into %s" % (n, PUBLIC))


if __name__ == "__main__":
    main()
