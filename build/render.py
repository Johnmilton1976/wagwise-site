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
import re
import json
import subprocess
import sys
import datetime
import hashlib
import html as _html

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles import SITE_NAME, PILLARS, ARTICLES, HOME, ABOUT, CONTACT, PRIVACY, EDITORIAL, RESOURCES, TOOL, FOOD_CHART, TOOL_CHOCO  # noqa
from choco_tool import CHOCO_BODY  # noqa

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
        "logo": DOMAIN + "/assets/og-image-wagwise.png",
        "description": "An independent pet care editorial resource.",
        # Only profiles where we actually publish long-form work. Quora answers and
        # a Blogger mirror were dropped: they are the two that read as "profile
        # built for link building" rather than evidence of a real publisher.
        "sameAs": [
            "https://medium.com/@steven.jones.19760904",
            "https://stevenjones205255.substack.com",
        ],
    },
    ensure_ascii=False,
    indent=2,
)

BYLINE_HTML = (
    '<div class="byline" style="margin:28px 0;padding:16px 18px;border-left:3px solid #3FA97E;'
    'background:#F4FAF7;border-radius:8px;font-size:14px;color:#4a554c;line-height:1.65">'
    "<strong>About this article.</strong> Compiled by the <a href=\"/about/editorial-standards/\">%s "
    "editorial team</a> from authoritative, publicly available sources including the American Kennel "
    "Club (AKC), the American Veterinary Medical Association (AVMA), the ASPCA, and the Merck "
    "Veterinary Manual. Where a guide draws on named veterinary experts at organisations such as "
    "Pet Poison Helpline or the ASPCA Animal Poison Control Center, those experts are cited by name "
    "in the Expert sources block below — we never claim a veterinarian reviewed an article they did "
    "not. %s is an independent editorial resource and <em>not</em> a veterinary practice. For "
    "diagnosis, treatment, or anything urgent, please consult a licensed veterinarian.</div>"
    ) % (ORG_NAME, ORG_NAME)

DEFAULT_CHECKED = "2026-10-16"


def _checked_label(iso):
    """'2026-10-16' -> '16 October 2026'. Keeps the citation date human and unambiguous."""
    iso = iso or DEFAULT_CHECKED
    try:
        y, m, d = [int(x) for x in iso.split("-")]
        months = ("January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December")
        return "%d %s %d" % (d, months[m - 1], y)
    except Exception:
        return iso


def _checked_short(iso):
    """'2026-10-16' -> '16 Oct 2026'. Card-sized version of the check date."""
    iso = iso or DEFAULT_CHECKED
    try:
        y, m, d = [int(x) for x in iso.split("-")]
        months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        return "%d %s %d" % (d, months[m - 1], y)
    except Exception:
        return iso


def img_src(slug):
    """Use a real raster photo if 朱朱 dropped one in, else the SVG placeholder.

    Drop a file named <slug>.webp / .jpg / .png into public/assets/img/ and
    re-run render.py — the article will pick it up automatically.

    Returns None when neither exists. The old unconditional SVG fallback emitted
    a URL for 25 pages whose placeholder file had already been deleted, so those
    pages served a 404 image in the <article> — worse than no image at all.
    """
    for ext in ("webp", "jpg", "jpeg", "png"):
        if os.path.exists(os.path.join(IMG_DIR, slug + "." + ext)):
            return "/assets/img/%s.%s" % (slug, ext)
    if os.path.exists(os.path.join(IMG_DIR, slug + ".svg")):
        return "/assets/img/%s.svg" % slug
    return None


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


def thumb_src(slug):
    """Card thumbnail (480x300, generated by build/make_thumbs.js). None if absent."""
    if os.path.exists(os.path.join(IMG_DIR, slug + "-thumb.jpg")):
        return "/assets/img/%s-thumb.jpg" % slug
    return None


def og_src(slug):
    """Per-page social card (1200x630, generated by build/make_thumbs.js).

    A page-specific image lifts click-through whenever a link is shared to
    WeChat / social — a generic site card is wasted real estate.
    """
    if os.path.exists(os.path.join(IMG_DIR, slug + "-og.jpg")):
        return DOMAIN + "/assets/img/%s-og.jpg" % slug
    return None


def hub_card(url, kicker, title, desc, slug, meta=""):
    """Uniform image card used on the homepage and pillar hubs (top image, text below).

    The thumbnail carries a descriptive alt rather than alt="": these cards are
    the site's main image-search surface (哥飞 D6/G1) and an empty alt throws
    that away.

    `meta` is an optional muted line under the description — used on the homepage
    to show the check date on each card, which is one of the trust signals a YMYL
    topic needs and the cards previously carried no date at all.
    """
    t = thumb_src(slug)
    img = ""
    cls = "noimg" if not t else ""
    if t:
        d = IMG_DIMS.get(slug + "-thumb", (480, 300))
        img = (
            '<img class="timg" src="%s" width="%d" height="%d" loading="lazy" '
            'decoding="async" alt="%s">' % (t, d[0], d[1], _html.escape(title, quote=True))
        )
    meta_html = '<div class="d">%s</div>' % meta if meta else ""
    return (
        '<a href="%s" class="%s">%s<div class="tpad"><div class="k">%s</div>'
        "<h3>%s</h3><p>%s</p>%s</div></a>"
        % (url, cls, img, kicker, title, desc, meta_html)
    )


# ---- image intrinsic dimensions (generated by build/img_dims.js) ------------
# Prevents layout shift (CLS) by emitting real width/height on every <img>.
IMG_DIMS = {}
_DIMS_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img_dims.json")
if os.path.exists(_DIMS_JSON):
    with open(_DIMS_JSON, encoding="utf-8") as _f:
        IMG_DIMS = json.load(_f)


def img_attrs(slug, eager=False):
    """Return sizing / loading attributes for a real raster image.

    SVG placeholders get nothing (vector scales freely, 31 of them are gone
    from the live site anyway). Real photos get real width/height plus
    decoding="async"; body images are lazy-loaded, the first-screen hero is
    not, because lazy-loading an LCP element delays it.
    """
    dims = IMG_DIMS.get(slug)
    if not dims:
        return ""
    w, h = dims
    base = ' width="%d" height="%d" decoding="async"' % (w, h)
    return base + ' fetchpriority="high"' if eager else base + ' loading="lazy"'


def breadcrumb_jsonld(items):
    """items: list of (name, url_path) from the site root down to this page."""
    elems = [
        {"@type": "ListItem", "position": i, "name": name, "item": DOMAIN + url}
        for i, (name, url) in enumerate(items, 1)
    ]
    return json.dumps(
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": elems},
        ensure_ascii=False,
        indent=2,
    )


NAV_ITEMS = [
    ("/", "Home"),
    ("/dog-training/", "Dog Training"),
    ("/dog-health/", "Dog Health"),
    ("/dog-nutrition/", "Nutrition"),
    ("/dog-care/", "Care & Grooming"),
    ("/cat/", "Cats"),
    ("/best/", "Reviews"),
    ("/about/", "About"),
]
# 哥飞 11-04 第二轮: the tool page sat at 55 internal links (tied #1) while
# pulling 9 impressions / 0 clicks in 28 days — the boilerplate nav+footer
# "Tools" entry on all ~83 pages was the entire source. Removed from both;
# the calculator keeps contextual entries: homepage hero button + money card,
# the two callout boxes below, and /sitemap/.
# 哥飞 2026-11-03: internal links were misallocated — dog-training had 55 while
# dog-nutrition (15 of the top-20 exposure pages) had 19. The two nutrition
# reference pages now sit in the footer on every page, same tier as the nav.
FOOTER_ITEMS = NAV_ITEMS + [
    ("/dog-nutrition/foods-toxic-to-dogs/", "Toxic foods list"),
    ("/dog-nutrition/food-safety-chart/", "Food safety chart"),
    ("/about/editorial-standards/", "Editorial standards"), ("/contact/", "Contact"), ("/privacy/", "Privacy"), ("/sitemap/", "All pages")]

CONSENT_DEFAULT = (
    "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}"
    "gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',"
    "ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500});</script>"
)

# ---- Analytics — fill either value in and re-run render.py to switch it on ----
# Cloudflare Web Analytics token: cookieless, no consent banner required, free.
#   Cloudflare dashboard -> Analytics & Logs -> Web Analytics -> Add a site
#   -> "Enable with JS snippet" -> copy the token value.
CF_BEACON_TOKEN = ""
# GA4 measurement ID, e.g. "G-XXXXXXXXXX". Consent Mode v2 defaults above are denied,
# so Google only records once a visitor opts in through the cookie banner.
GA4_ID = ""


def analytics_html():
    out = []
    if GA4_ID:
        out.append(
            '<script async src="https://www.googletagmanager.com/gtag/js?id=%s"></script>\n'
            "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}"
            "gtag('js',new Date());gtag('config','%s');</script>\n" % (GA4_ID, GA4_ID)
        )
    if CF_BEACON_TOKEN:
        out.append(
            '<script defer src="https://static.cloudflareinsights.com/beacon.min.js" '
            "data-cf-beacon='{\"token\": \"%s\"}'></script>\n" % CF_BEACON_TOKEN
        )
    return "".join(out)

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


def head(title, desc, url_path, jsonld, og_type="article", article_jsonld=None,
         breadcrumb_jsonld_str=None, og_image=None, robots="index,follow"):
    canon = DOMAIN + url_path
    # Per-page social card when the page has its own photo (generated by
    # build/make_thumbs.js as <slug>-og.jpg, 1200x630); site-wide fallback otherwise.
    if og_image:
        og_url, og_w, og_h = og_image, 1200, 630
    else:
        og_url, og_w, og_h = DOMAIN + "/assets/og-image-wagwise.png", 1200, 630
    article_script = (
        '<script type="application/ld+json">\n%s\n</script>\n' % article_jsonld
    ) if article_jsonld else ""
    crumb_script = (
        '<script type="application/ld+json">\n%s\n</script>\n' % breadcrumb_jsonld_str
    ) if breadcrumb_jsonld_str else ""
    return (
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<title>%s</title>\n"
        '<meta name="description" content="%s">\n'
        '<meta name="robots" content="%s">\n'
        '<link rel="canonical" href="%s">\n'
        '<meta property="og:type" content="%s">\n'
        '<meta property="og:site_name" content="%s">\n'
        '<meta property="og:title" content="%s">\n'
        '<meta property="og:description" content="%s">\n'
        '<meta property="og:url" content="%s">\n'
        '<meta property="og:image" content="%s">\n'
        '<meta property="og:image:width" content="%d">\n'
        '<meta property="og:image:height" content="%d">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<meta name="twitter:title" content="%s">\n'
        '<meta name="twitter:description" content="%s">\n'
        '<meta name="twitter:image" content="%s">\n'
        '<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">\n'
        '<link rel="stylesheet" href="/assets/style.css?v=8">\n'
        '<script type="application/ld+json">\n%s\n</script>\n'
        '<script type="application/ld+json">\n%s\n</script>\n'
        "%s"
        "%s"
        "%s"
    ) % (
        title, desc, robots, canon, og_type, SITE_NAME, title, desc, canon,
        og_url, og_w, og_h, title, desc, og_url,
        jsonld, ORG_JSONLD, article_script, crumb_script, CONSENT_DEFAULT,
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
        "%s"
        "</body>\n</html>\n"
    ) % (
        head_html,
        SITE_NAME,
        nav_html(nav_current),
        body_html,
        footer_html(),
        SITE_NAME,
        analytics_html(),
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
        "image": DOMAIN + "/assets/og-image-wagwise.png",
        "datePublished": SITE_LAUNCH,
        "dateModified": SITE_LAUNCH,
    }
    # Machine-readable citations — lets search engines see the provenance of
    # every health claim without parsing the page.
    cites = []
    for label, url in a.get("sources", []):
        cites.append({"@type": "CreativeWork", "name": label, "url": url})
    for e in a.get("experts", []):
        cites.append({"@type": "MedicalOrganization", "name": e})
    if cites:
        d["citation"] = cites
    return json.dumps(d, ensure_ascii=False, indent=2)


# 哥飞 #5 (2026-10-26): turn the dog-age tool into a link magnet. These four
# nutrition pages carry the most demand, so they get a contextual entry point
# into the tool; the tool in turn links back to them. Internal link cycle =
# stickier visits + a page third parties have a reason to cite.
TOOL_LINK_SLUGS = {
    "can-dogs-eat-milk",
    "how-much-to-feed-my-dog",
}
TOOL_CALLOUT = (
    '<div class="tool-cta" style="margin:26px 0;padding:16px 18px;border:1px solid #cfe8db;'
    'background:#F4FAF7;border-radius:10px;font-size:15px;line-height:1.65;color:#2c3a32">'
    "<b>Quick check:</b> age changes what a dog can safely eat and how much. "
    '<a href="/tools/dog-age-calculator/">See your dog\u2019s life stage</a> with the dog age '
    "calculator \u2014 enter size and age to get puppy / young adult / mature / senior in one "
    "line, and copy the result to share.</div>"
)

# 哥飞 2026-11-03: the food safety chart is the site's most citable asset but
# had zero exposure and no body-level entry points. Every nutrition article
# now carries a contextual box into the chart and the toxic-foods list, so
# both reference pages earn real (non-boilerplate) internal links from the
# pages where a reader actually asks "what else is safe?".
CHART_CALLOUT = (
    '<div class="tool-cta" style="margin:26px 0;padding:16px 18px;border:1px solid #cfe8db;'
    'background:#F4FAF7;border-radius:10px;font-size:15px;line-height:1.65;color:#2c3a32">'
    "<b>Quick reference:</b> this guide is one of 47 entries in the "
    '<a href="/dog-nutrition/food-safety-chart/">dog food safety chart</a> \u2014 four '
    "risk tiers with the dose that matters, not just safe or toxic. For the emergency "
    'list, see <a href="/dog-nutrition/foods-toxic-to-dogs/">foods toxic to dogs</a>.</div>'
)

# 哥飞 11-04 第二轮 (CSV W1): internal links were invested in a page that earns
# no queries while the pages that DO rank got nothing. Every nutrition article
# now carries two body-level links: one to the relevant /best/ buying guide
# (emergency-transport angle for toxic foods, treat-training angle for safe
# foods), one to a sibling food article. The tool-page callout stays only on
# the two highest-demand nutrition pages; toxic/safe clusters pair siblings by
# shared question logic, not alphabet.
#
# best_slug None = the article already has its /best/ body link (added 11-04:
# milk / chocolate / peanut-butter) — sibling only, never a duplicate.
FOOD_LINK_PLAN = {
    # --- danger cluster: toxic-dose → emergency-transport angle → dog crate
    "can-dogs-eat-alcohol":        ("best-dog-crate", "can-dogs-eat-xylitol"),
    "can-dogs-eat-caffeine":       ("best-dog-crate", "can-dogs-eat-chocolate"),
    "can-dogs-eat-chocolate":      (None, "can-dogs-eat-peanut-butter"),
    "can-dogs-eat-garlic":         ("best-dog-crate", "can-dogs-eat-onion"),
    "can-dogs-eat-grapes":         ("best-dog-crate", "can-dogs-eat-macadamia-nuts"),
    "can-dogs-eat-macadamia-nuts": ("best-dog-crate", "can-dogs-eat-walnuts"),
    "can-dogs-eat-walnuts":        ("best-dog-crate", "can-dogs-eat-almonds"),
    "can-dogs-eat-almonds":        ("best-dog-crate", "can-dogs-eat-macadamia-nuts"),
    "can-dogs-eat-onion":          ("best-dog-crate", "can-dogs-eat-garlic"),
    "can-dogs-eat-raw-dough":      ("best-dog-crate", "can-dogs-eat-alcohol"),
    "can-dogs-eat-xylitol":        ("best-dog-crate", "can-dogs-eat-grapes"),
    "can-dogs-eat-avocado":        ("best-dog-crate", "can-dogs-eat-mango"),
    "can-dogs-eat-cherries":       ("best-dog-crate", "can-dogs-eat-plums"),
    "can-dogs-eat-plums":          ("best-dog-crate", "can-dogs-eat-peaches"),
    "can-dogs-eat-peaches":        ("best-dog-crate", "can-dogs-eat-cherries"),
    "can-dogs-eat-tomato":         ("best-dog-crate", "can-dogs-eat-potato"),
    "can-dogs-eat-potato":         ("best-dog-crate", "can-dogs-eat-sweet-potato"),
    # --- safe foods: treat/walk angle → harness for pulling
    "can-dogs-eat-apples":         ("best-dog-harness-for-pulling", "can-dogs-eat-bananas"),
    "can-dogs-eat-bananas":        ("best-dog-harness-for-pulling", "can-dogs-eat-blueberries"),
    "can-dogs-eat-blueberries":    ("best-dog-harness-for-pulling", "can-dogs-eat-strawberries"),
    "can-dogs-eat-strawberries":   ("best-dog-harness-for-pulling", "can-dogs-eat-watermelon"),
    "can-dogs-eat-watermelon":     ("best-dog-harness-for-pulling", "can-dogs-eat-pineapple"),
    "can-dogs-eat-pineapple":      ("best-dog-harness-for-pulling", "can-dogs-eat-mango"),
    "can-dogs-eat-mango":          ("best-dog-crate", "can-dogs-eat-pineapple"),
    "can-dogs-eat-carrots":        ("best-dog-harness-for-pulling", "can-dogs-eat-green-beans"),
    "can-dogs-eat-green-beans":    ("best-dog-harness-for-pulling", "can-dogs-eat-peas"),
    "can-dogs-eat-peas":           ("best-dog-harness-for-pulling", "can-dogs-eat-broccoli"),
    "can-dogs-eat-broccoli":       ("best-dog-harness-for-pulling", "can-dogs-eat-cucumber"),
    "can-dogs-eat-cucumber":       ("best-dog-harness-for-pulling", "can-dogs-eat-carrots"),
    "can-dogs-eat-corn":           ("best-dog-harness-for-pulling", "can-dogs-eat-popcorn"),
    "can-dogs-eat-popcorn":        ("best-dog-harness-for-pulling", "can-dogs-eat-bread"),
    "can-dogs-eat-sweet-potato":   ("best-dog-harness-for-pulling", "can-dogs-eat-pumpkin"),
    "can-dogs-eat-pumpkin":        ("best-dog-harness-for-pulling", "can-dogs-eat-peas"),
    "can-dogs-eat-spinach":        ("best-dog-harness-for-pulling", "can-dogs-eat-broccoli"),
    "can-dogs-eat-chicken":        ("best-dog-harness-for-pulling", "can-dogs-eat-eggs"),
    "can-dogs-eat-eggs":           ("best-dog-harness-for-pulling", "can-dogs-eat-salmon"),
    "can-dogs-eat-salmon":         ("best-dog-harness-for-pulling", "can-dogs-eat-shrimp"),
    "can-dogs-eat-shrimp":         ("best-dog-harness-for-pulling", "can-dogs-eat-eggs"),
    "can-dogs-eat-ham":            ("best-dog-harness-for-pulling", "can-dogs-eat-chicken"),
    "can-dogs-eat-honey":          ("best-dog-harness-for-pulling", "can-dogs-eat-yogurt"),
    "can-dogs-eat-bread":          ("best-dog-harness-for-pulling", "can-dogs-eat-rice"),
    "can-dogs-eat-rice":           ("best-dog-harness-for-pulling", "can-dogs-eat-chicken"),
    "can-dogs-eat-cheese":         ("best-dog-harness-for-pulling", "can-dogs-eat-yogurt"),
    "can-dogs-eat-yogurt":         ("best-dog-harness-for-pulling", "can-dogs-eat-ice-cream"),
    "can-dogs-eat-ice-cream":      ("best-dog-harness-for-pulling", "can-dogs-eat-milk"),
    "can-dogs-eat-milk":           (None, "can-dogs-eat-cheese"),
    "can-dogs-eat-peanut-butter":  (None, "can-dogs-eat-milk"),
    # --- reference pages
    "how-much-to-feed-my-dog":     (None, "food-safety-chart"),
}

# Emergency-transport variants (toxic foods → crate guide). No claim of
# hands-on testing; "practical picks" matches the guide's own framing.
_BEST_CRATE_TXT = (
    "One more thing worth sorting out before you ever need it: a genuine toxicity "
    "scare usually ends in a car ride to the emergency vet, and a dog who feels "
    "awful is not a calm passenger. Our guide to the "
    '<a href="/best/dog-crate/">best dog crates</a> covers the secure, '
    "easy-to-clean options that make that trip less chaotic.",
    "If a dose ever does go wrong, you will be driving to an emergency clinic with "
    "a dog who feels wretched — worth having containment figured out in advance. "
    'The <a href="/best/dog-crate/">best dog crate</a> guide compares the models '
    "built for exactly that kind of trip.",
    "Prevention beats treatment here, and part of prevention is knowing you can "
    "move a sick dog safely. A crate that loads easily and cleans up fast earns "
    'its keep on vet runs — the <a href="/best/dog-crate/">best dog crate</a> '
    "guide shortlists practical picks, not hype.",
    "If this food lives somewhere your dog can reach, the scenario to plan for is "
    "the unplanned vet trip. The "
    '<a href="/best/dog-crate/">best dog crate for anxious dogs</a> in our guide '
    "holds up when a dog is panting, pacing or worse.",
)
# Treat/walk variants (safe foods → harness guide)
_BEST_HARNESS_TXT = (
    "As a training treat, this food works well — and treat sessions happen on "
    "walks, which is also where pulling gets learned. Our "
    '<a href="/best/dog-harness-for-pulling/">best dog harness for pulling</a> '
    "guide keeps the leash side as organised as the treat side.",
    "If you use this food as a high-value reward on walks, it is worth solving "
    "the pulling problem at the same time — the "
    '<a href="/best/dog-harness-for-pulling/">best dog harness for pulling</a> '
    "guide covers the options worth shortlisting.",
    "Small pieces of this food make an honest, low-calorie training reward, and "
    "most training happens mid-walk. The "
    '<a href="/best/dog-harness-for-pulling/">best no-pull harness</a> picks in '
    "our guide pair well with treat-based training.",
    "One practical note for reward-based walks: gear that fights you undoes the "
    "training. Our "
    '<a href="/best/dog-harness-for-pulling/">best dog harness for pulling</a> '
    "guide covers the designs we would shortlist.",
)

_SIB_TXT = (
    "The question owners ask next is usually about {sib}: here is the full "
    '<a href="{u}">{t}</a> answer.',
    'Reading next: <a href="{u}">{t}</a> — the risks, the amounts that matter and '
    "what to do if your dog already got some.",
    'Related: <a href="{u}">{t}</a> covers the other half of this question.',
    "If your dog likes this food, they have probably eyed {sib} too — the "
    '<a href="{u}">{t}</a> guide covers it.',
    "For the neighbouring question — <a href=\"{u}\">{t}</a> — the same "
    "dose-first logic applies.",
)


def food_link_html(slug):
    """Two body-level links per nutrition article: /best/ guide + sibling food."""
    plan = FOOD_LINK_PLAN.get(slug)
    if not plan:
        return ""
    best_slug, sib_slug = plan
    parts = []
    if best_slug:
        pool = _BEST_CRATE_TXT if best_slug == "best-dog-crate" else _BEST_HARNESS_TXT
        parts.append(pool[sum(ord(c) for c in slug) % len(pool)])
    if sib_slug:
        if sib_slug == "food-safety-chart":
            u, t = FOOD_CHART["url"], FOOD_CHART["title"]
        else:
            u, t = LOOKUP[sib_slug]
        name = t.split("?")[0].replace("Can Dogs Eat ", "").strip().lower()
        if sib_slug == "food-safety-chart":
            name = "what the rest of the pantry looks like"
        parts.append(_SIB_TXT[sum(ord(c) for c in sib_slug) % len(_SIB_TXT)]
                     .format(u=u, t=t, sib=name))
    if not parts:
        return ""
    return "<p>%s</p>" % " ".join(parts)


def render_article(a):
    slug = a["slug"]
    pillar = PILLARS[a["pillar"]]
    if a.get("faq"):
        jsonld = faq_jsonld(a["faq"])
        og_type = "article"
    else:
        jsonld = site_jsonld()
        og_type = "website"
    bc = breadcrumb_jsonld(
        [("Home", "/"), (pillar["nav"], pillar["url"]), (a["title"], a["url"])]
    )
    og_img = og_src(slug)
    h = head(a["title"], a["description"], a["url"], jsonld, og_type,
             article_jsonld(a), bc, og_image=og_img)

    # FAQ inner block
    faq_html = ""
    body_html = a["body"]
    if a.get("faq"):
        # Six articles repeat the heading inside their own body, which produced
        # two consecutive "Frequently asked questions" H2s on one page. Strip the
        # body copy of it; the wrapper below owns that heading.
        # Cut at the match start so the body keeps its original trailing layout —
        # an rstrip here would rewrite the tail of all 66 FAQ articles and stamp
        # every one of them as edited today.
        _m = re.search(r"(?is)\s*<h2>\s*frequently asked questions\s*</h2>\s*$", body_html)
        if _m:
            body_html = body_html[:_m.start()]
        items = "".join(
            '<div class="faq-item"><div class="faq-q">%s</div>'
            '<div class="faq-a">%s</div></div>' % (q, ans)
            for q, ans in a["faq"]
        )
        faq_html = '<div class="faq"><h2>Frequently asked questions</h2>%s</div>' % items

    # Related reading
    # 哥飞 round-2 (11-04): the cat pages rank best on the site yet received no
    # internal links at all — nine cat guides with no sibling links is an orphan
    # cluster. Cat articles therefore link to every other cat guide (hand-picked
    # related first, then the rest of the pillar), not just the three chosen.
    rel_html = ""
    if a["pillar"] == "cat":
        order = [s for s in a.get("related", []) if s != slug]
        order += [x["slug"] for x in ARTICLES
                  if x["pillar"] == "cat" and x["slug"] != slug and x["slug"] not in order]
        lis = "".join(
            '<li><a href="%s">%s</a></li>' % (LOOKUP[s][0], LOOKUP[s][1]) for s in order
        )
        rel_html = ('<div class="related"><h2>All cat guides</h2>'
                    '<p class="srcnote">Nine guides make up this section. Start with the one '
                    "that matches your problem, then follow the links inside it.</p>"
                    "<ul>%s</ul></div>" % lis)
    elif a.get("related"):
        lis = "".join(
            '<li><a href="%s">%s</a></li>' % (LOOKUP[s][0], LOOKUP[s][1]) for s in a["related"]
        )
        rel_html = '<div class="related"><h2>Related reading</h2><ul>%s</ul></div>' % lis

    disc_html = ""
    if a.get("disclaimer"):
        disc_html = '<div class="disclaimer">%s</div>' % a["disclaimer"]

    # Sources — real, verifiable citations. YMYL health content needs traceable
    # provenance, so every factual claim traces back to a named public source.
    src_html = ""
    if a.get("sources"):
        lis = "".join(
            '<li><a href="%s" target="_blank" rel="noopener">%s</a></li>' % (u, label)
            for label, u in a["sources"]
        )
        src_html = (
            '<div class="sources"><h2>Sources</h2><ul>%s</ul>'
            '<p class="srcnote">Facts in this article were checked against the public '
            "references above on %s. These organisations are independent and are not "
            "affiliated with WagWise Pet. See our <a href=\"/about/editorial-standards/\">"
            "editorial standards</a> for how we research and correct guides.</p></div>"
            % (lis, _checked_label(a.get("checked")))
        )

    # Expert sources — named veterinary experts / specialist teams at the
    # authoritative orgs we cite. This is honest attribution (we cite their
    # published guidance), NOT a fabricated "reviewed by Dr. X" claim. It closes
    # the YMYL E-E-A-T gap 哥飞 flagged without inventing individual authors.
    exp_html = ""
    if a.get("experts"):
        lis = "".join("<li>%s</li>" % e for e in a["experts"])
        exp_html = (
            '<div class="experts"><h2>Expert sources</h2><ul>%s</ul>'
            '<p class="srcnote">The named veterinary experts and specialist teams above are '
            "the authors of the published guidance we summarise. WagWise Pet is an "
            "independent editorial resource and is not affiliated with them; we have not "
            "represented that any individual reviewed this specific article.</p></div>"
            % lis
        )

    byline_html = BYLINE_HTML
    tool_cta = TOOL_CALLOUT if slug in TOOL_LINK_SLUGS else ""
    chart_cta = (CHART_CALLOUT if a["pillar"] == "dog-nutrition"
                 and slug != "foods-toxic-to-dogs" else "")
    food_links = food_link_html(slug)

    crumb = (
        '<div class="crumbs"><a href="/">Home</a> › '
        '<a href="%s">%s</a> › %s</div>'
        % (pillar["url"], pillar["nav"], a["title"])
    )
    _src = img_src(slug)
    img = ('<img class="article-img" src="%s"%s alt="%s">'
           % (_src, img_attrs(slug), a["title"])) if _src else ""

    body = (
        '<div class="wrap narrow">\n'
        "  %s\n"
        '  <div class="eyebrow">%s</div>\n'
        "  <h1>%s</h1>\n"
        '  <p class="lede">%s</p>\n'
        # 2026-10-18: removed the empty ADVERTISEMENT placeholder div here —
        # Google was scraping the word "ADVERTISEMENT" into SERP snippets.
        # Re-add properly (ad code + placement) when AdSense goes live.
        "  %s\n"
        '  <div class="doc">%s</div>\n'
        "  %s\n"
        "  %s\n"
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
        body_html + food_links + chart_cta + tool_cta,
        faq_html,
        rel_html,
        src_html,
        exp_html,
        disc_html,
        byline_html,
    )
    return shell(h, a["url"], body)


def render_pillar(p):
    jsonld = site_jsonld()
    bc = breadcrumb_jsonld([("Home", "/"), (p["title"], p["url"])])
    h = head(p["title"], p["description"], p["url"], jsonld, "website", None, bc,
             og_image=og_src(p["slug"]))
    crumb = '<div class="crumbs"><a href="/">Home</a> › %s</div>' % p["title"]
    # article cards (with thumbnails) feeding the hub grid below
    card_html = ""
    for s in p.get("links", []):
        url, title = LOOKUP[s]
        art = next((x for x in ARTICLES if x["slug"] == s), None)
        desc = art["lede"] if art else ""
        card_html += hub_card(url, "GUIDE", title, desc, s)
    hero_html = ""
    hs = hero_src(p["slug"])
    if hs:
        hero_html = '<img class="hero" src="%s"%s alt="%s">' % (
            hs, img_attrs(p["slug"], eager=True), p["title"]
        )

    # Section pages are the entry point Google uses to judge whether a topic
    # hub is substantive. A one-line intro left them at 138–296 words, so each
    # pillar now carries a real body above the card grid.
    doc_top = p.get("body") or ('<p>%s</p>' % p.get("intro", ""))
    after = p.get("after", "")
    body = (
        '<div class="wrap">\n'
        "  %s\n"
        '  <div class="eyebrow">%s</div>\n'
        "  <h1>%s</h1>\n"
        '  <p class="lede">%s</p>\n'
        "  %s\n"
        '  <div class="doc">%s</div>\n'
        '  <h2 id="guides">Every guide in this section</h2>\n'
        '  <div class="hub">%s</div>\n'
        "  %s\n"
        "</div>"
    ) % (crumb, p.get("eyebrow", ""), p["title"], p["description"], hero_html, doc_top, card_html, after)
    return shell(h, p["url"], body)


def render_home():
    jsonld = site_jsonld()
    h = head(HOME["title"], HOME["description"], "/", jsonld, "website")
    # Hero — image eager + fetchpriority=high: it is the LCP element of the homepage.
    hd = IMG_DIMS.get("home-hero", (1600, 1200))
    hero = (
        '<div class="hero-home">\n'
        '  <div class="hh-txt">\n'
        '    <div class="eyebrow">%s</div>\n'
        "    <h1>Dog and cat care guides — written to be useful, not scary</h1>\n"
        '    <p class="lede">%s</p>\n'
        '    <div class="hh-btns">\n'
        '      <a class="btn" href="/dog-nutrition/can-dogs-eat-chocolate/">'
        "Is chocolate toxic? \u2192</a>\n"
        '      <a class="btn ghost" href="/tools/dog-age-calculator/">Dog age calculator</a>\n'
        "    </div>\n"
        "  </div>\n"
        '  <img class="hh-img" src="/assets/img/home-hero.jpg" width="%d" height="%d" '
        'fetchpriority="high" decoding="async" alt="Two dogs playing together on a sunny grass lawn">\n'
        "</div>"
    ) % (HOME.get("eyebrow", ""), HOME["description"], hd[0], hd[1])

    pillar_cards = ""
    for s in HOME["pillars"]:
        p = PILLARS[s]
        pillar_cards += hub_card(p["url"], "SECTION", p["title"], p["description"], s)
    feat_cards = ""
    for s in HOME["featured"]:
        url, title = LOOKUP[s]
        art = next((x for x in ARTICLES if x["slug"] == s), None)
        desc = art["lede"] if art else ""
        feat_cards += hub_card(url, "ARTICLE", title, desc, s)
    # Latest guides — 哥飞: homepage should list newest content to pull crawler
    # revisits and give new pages an entry point. New articles appended to
    # ARTICLES appear first here automatically.
    #
    # Slugs already used higher up the page are skipped: cat-meow was appearing
    # twice (Start here + Latest) out of only 17 unique internal links, so one of
    # the homepage's most valuable slots was pointing at a page it already linked.
    _MONEY_SLUGS = ("best-dog-crate", "best-dog-harness-for-pulling", "how-much-to-feed-my-dog")
    _CAT_SLUGS = set(PILLARS["cat"]["links"])
    _used = set(HOME["featured"]) | set(_MONEY_SLUGS) | _CAT_SLUGS
    latest = [a for a in ARTICLES[::-1] if a["slug"] not in _used][:6]
    latest_cards = ""
    for a in latest:
        latest_cards += hub_card(a["url"], "ARTICLE", a["title"], a["lede"], a["slug"],
                                 "Checked %s" % _checked_short(a.get("checked")))
    # Fixed homepage slots for the pages that carry commercial intent. These four
    # were the least-linked pages on the site while 70 articles competed for one
    # row of the homepage — so they get named slots instead.
    money_cards = ""
    _money = [(TOOL["url"], TOOL["title"], TOOL["description"],
               "dog-age-calculator", "TOOL"),
              (TOOL_CHOCO["url"], TOOL_CHOCO["title"], TOOL_CHOCO["description"],
               "chocolate-toxicity-calculator", "TOOL"),
              (FOOD_CHART["url"], FOOD_CHART["title"], FOOD_CHART["description"],
               "food-safety-chart", "REFERENCE")]
    for _slug, _kick in (("best-dog-crate", "BUYING GUIDE"),
                         ("best-dog-harness-for-pulling", "BUYING GUIDE"),
                         ("how-much-to-feed-my-dog", "FEEDING REFERENCE")):
        _a = next((x for x in ARTICLES if x["slug"] == _slug), None)
        if _a:
            _money.append((_a["url"], _a["title"], _a["lede"], _slug, _kick))
    for _url, _title, _desc, _slug, _kick in _money:
        money_cards += hub_card(_url, _kick, _title, _desc, _slug)

    # 哥飞 11-04 第二轮: the cat line is the site's most stable ranking content
    # (4 queries at 38–68) but got zero article-level links. Dedicated homepage
    # block under the dog sections: hub card + every cat guide.
    _cat = PILLARS["cat"]
    cat_cards = hub_card(_cat["url"], "SECTION", _cat["title"], _cat["description"], _cat["slug"])
    for _s in _cat["links"]:
        _u, _t = LOOKUP[_s]
        _a = next((x for x in ARTICLES if x["slug"] == _s), None)
        cat_cards += hub_card(_u, "GUIDE", _t, _a["lede"] if _a else "", _s)

    # The full A-Z list used to live here (73 links). It moved to /sitemap/, which
    # every page already links to in the footer — one hop for a crawler, but the
    # homepage no longer spreads its equity across 70 equally-weighted links.
    total_pages = len(ARTICLES) + 2
    see_all = (
        '  <p class="lede" style="margin-top:34px">'
        '<a href="/sitemap/"><strong>Browse all %d guides and tools \u2192</strong></a><br>'
        "Every page on WagWise, grouped by section.</p>\n"
    ) % total_pages

    # Trust strip — YMYL topic: a reader who has just met this site needs one
    # visible line telling them who writes this and how it is checked, before
    # they read a symptom or a dose. It used to live only in the footer.
    trust = (
        '  <p class="trust"><strong>How we write &amp; review:</strong> every health and '
        "nutrition claim is checked against named public references \u2014 ASPCA, the Merck "
        "Veterinary Manual, Cornell, International Cat Care \u2014 and each guide shows the "
        'date it was last checked. We do not invent credentials. '
        '<a href="/about/editorial-standards/">Our editorial standards \u2192</a></p>\n'
    )

    body = (
        '<div class="wrap">\n'
        "  %s\n"
        "  %s"
        '  <h2 id="sections">Browse by section</h2>\n'
        '  <div class="hub">%s</div>\n'
        '  <h2 style="margin-top:40px">Start here — the questions we get most</h2>\n'
        '  <div class="hub">%s</div>\n'
        '  <h2 style="margin-top:40px">Cat care guides</h2>\n'
        '  <div class="hub">%s</div>\n'
        '  <h2 style="margin-top:40px">Tools &amp; buying guides</h2>\n'
        '  <div class="hub">%s</div>\n'
        '  <h2 style="margin-top:40px">Latest guides</h2>\n'
        '  <div class="hub">%s</div>\n'
        "  %s\n"
        "</div>"
    ) % (hero, trust, pillar_cards, feat_cards, cat_cards, money_cards, latest_cards, see_all)
    return shell(h, "/", body)


def render_static(url_path, nav_current, title, desc, body_html, og_type="website",
                  crumb_label=None, robots="index,follow", crumb_path=None):
    crumb_html = ""
    bc = None
    if crumb_path:
        bc = breadcrumb_jsonld([("Home", "/")] + list(crumb_path) +
                               [(crumb_label or title, url_path)])
        _chain = "".join('<a href="%s">%s</a> \u203a ' % (u, l) for l, u in crumb_path)
        crumb_html = ('  <div class="crumbs"><a href="/">Home</a> \u203a %s%s</div>\n'
                      % (_chain, crumb_label or title))
    elif crumb_label:
        bc = breadcrumb_jsonld([("Home", "/"), (crumb_label, url_path)])
        crumb_html = '  <div class="crumbs"><a href="/">Home</a> \u203a %s</div>\n' % crumb_label
    h = head(title, desc, url_path, site_jsonld(), og_type, None, bc, robots=robots)
    body = '<div class="wrap narrow">\n%s%s</div>' % (crumb_html, body_html)
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
    <div id="dog-out" class="calc-result">About 24 human years old — young adult (estimate).</div>
    <button id="dog-share" type="button" style="margin-top:10px;background:#fff;color:#2f7a5d;border:1px solid #3FA97E">Copy shareable result</button>
    <p class="calc-note">Estimate only. Larger breeds age a little faster than small ones. The link updates as you type, so you can bookmark or share this exact reading.</p>
  </div>
  <div class="doc">
    <h2>How the estimate works</h2>
    <p>Dogs do not age at a flat 7&times; rate. The size-adjusted approximation we use treats the first year as about 15 human years and the second as roughly 9 more, then adds 4 to 6 per year afterward depending on size: smaller dogs age slower, larger dogs faster. That is why a 2-year-old small dog and a 2-year-old giant breed land in very different human-age ranges.</p>
    <h2>Why not just multiply by 7?</h2>
    <p>The 7&times; rule is a rough myth. A one-year-old dog is already sexually mature and past infancy, so 7&times; badly understates the early years and overstates the later ones. The size-adjusted curve — the one behind this calculator — bends by body size, because large and giant breeds age noticeably faster once they are adults. The shape of it is consistent with guidance from the American Veterinary Medical Association (AVMA) and the Cornell Riney Canine Health Center.</p>
    <h2>Life stage by size</h2>
    <p>The human-age output is really a stand-in for <em>life stage</em>, which is what should change how you care for the dog:</p>
    <table>
      <tr><th style="text-align:left">Life stage</th><th style="text-align:left">Small dog</th><th style="text-align:left">Medium dog</th><th style="text-align:left">Large / giant dog</th></tr>
      <tr><td>Puppy</td><td>0&ndash;1 yr</td><td>0&ndash;1 yr</td><td>0&ndash;1 yr</td></tr>
      <tr><td>Young adult</td><td>1&ndash;6 yr</td><td>1&ndash;5 yr</td><td>1&ndash;4 yr</td></tr>
      <tr><td>Mature adult</td><td>6&ndash;9 yr</td><td>5&ndash;8 yr</td><td>4&ndash;7 yr</td></tr>
      <tr><td>Senior</td><td>9+ yr</td><td>8+ yr</td><td>7+ yr</td></tr>
    </table>
    <p>A "senior" reading is a useful prompt to book more frequent vet checks, watch for <a href="/dog-health/">symptoms like vomiting or shaking</a>, and adjust diet and exercise.</p>
    <h2>Breed-size reference</h2>
    <p>The size you pick maps roughly to these common breeds:</p>
    <ul>
      <li><b>Small (under 9 kg / 20 lb):</b> Chihuahua, Yorkshire Terrier, Dachshund, Shih Tzu, Jack Russell Terrier.</li>
      <li><b>Medium (9&ndash;23 kg / 20&ndash;50 lb):</b> Beagle, Border Collie, Cocker Spaniel, English Bulldog, Australian Shepherd.</li>
      <li><b>Large (23 kg+ / 50 lb+):</b> Labrador Retriever, German Shepherd, Golden Retriever, Rottweiler, Great Dane (at the giant end).</li>
    </ul>
    <h2>What the number can and cannot tell you</h2>
    <p>This tool gives a quick sense of your dog's life stage. It is an estimate, not a medical fact, and cannot tell you how healthy your dog is. Two dogs with the same human-age reading can be in very different shape. Use the number to time life-stage care — more frequent check-ups in the senior range, and earlier attention to joint support for large breeds — rather than to predict a lifespan.</p>
    <h2>When age matters most</h2>
    <p>As dogs move into the mature and senior ranges, a few things become worth watching: slower recovery after exercise, changes in appetite or water intake, and the onset of arthritis or dental disease. Our <a href="/dog-health/">dog health guides</a> explain what is urgent versus what can wait, and our <a href="/dog-care/">care and grooming guides</a> cover the at-home habits that keep older dogs comfortable.</p>
    <h2>Food questions owners ask next</h2>
    <p>Life stage changes what a dog can safely eat and how much. These are the guides owners open most after checking their dog's age: <a href="/dog-nutrition/can-dogs-eat-milk/">can dogs drink milk</a>, <a href="/dog-nutrition/can-dogs-eat-chocolate/">can dogs eat chocolate</a>, <a href="/dog-nutrition/can-dogs-eat-grapes/">can dogs eat grapes</a>, and <a href="/dog-nutrition/how-much-to-feed-my-dog/">how much to feed my dog</a>.</p>
    <h2>Sources and review</h2>
    <p>This calculator follows the size-adjusted approximation described by the American Veterinary Medical Association (AVMA) and the Cornell Riney Canine Health Center. It is general information, not veterinary advice — for questions about your own dog's ageing, ask your veterinarian. Last reviewed 24 October 2026.</p>
  </div>
</div>
<script>
(function(){
  var sizeEl=document.getElementById('dog-size'), ageEl=document.getElementById('dog-age'),
      unitEl=document.getElementById('dog-unit'), out=document.getElementById('dog-out'),
      shareBtn=document.getElementById('dog-share');
  function stageOf(size,yrs){
    var mature={'small':6,'medium':5,'large':4}[size];
    var senior={'small':9,'medium':8,'large':7}[size];
    if(yrs<1){ return 'puppy'; }
    if(yrs<mature){ return 'young adult'; }
    if(yrs<senior){ return 'mature adult'; }
    return 'senior';
  }
  function calc(){
    var size=sizeEl.value, age=parseFloat(ageEl.value)||0, unit=unitEl.value;
    var yrs = unit==='m' ? age/12 : age;
    var hy;
    if(yrs<=1){ hy=Math.round(yrs*15); }
    else if(yrs<=2){ hy=Math.round(15+(yrs-1)*9); }
    else { var f={'small':4,'medium':5,'large':6}[size]; hy=Math.round(24+(yrs-2)*f); }
    var st=stageOf(size,yrs);
    out.innerHTML='About <b>'+hy+'</b> human years \u2014 <b>'+st+'</b> (estimate).';
    var yrsParam=(unit==='m' ? (age/12).toFixed(2) : age);
    try{
      var u=new URL(window.location.href);
      u.searchParams.set('size',size); u.searchParams.set('age',yrsParam);
      window.history.replaceState(null,'',u.toString());
    }catch(e){}
    if(shareBtn){
      shareBtn.dataset.text='My '+size+' dog is about '+hy+' human years old ('+st+'). Estimate yours: '+window.location.origin+'/tools/dog-age-calculator/?size='+size+'&age='+encodeURIComponent(yrsParam);
    }
  }
  try{
    var p=new URLSearchParams(window.location.search);
    if(['small','medium','large'].indexOf(p.get('size'))>-1){ sizeEl.value=p.get('size'); }
    if(p.get('age')!==null && p.get('age')!==''){ ageEl.value=p.get('age'); unitEl.value='y'; }
  }catch(e){}
  document.getElementById('dog-go').addEventListener('click',calc);
  ageEl.addEventListener('input',calc);
  sizeEl.addEventListener('change',calc);
  unitEl.addEventListener('change',calc);
  if(shareBtn){
    shareBtn.addEventListener('click',function(){
      var t=shareBtn.dataset.text||out.textContent;
      try{ if(navigator.clipboard){ navigator.clipboard.writeText(t); } }catch(e){}
      shareBtn.textContent='Copied \u2713';
      setTimeout(function(){ shareBtn.textContent='Copy shareable result'; },1600);
    });
  }
  calc();
})();
</script>
"""


def tool_jsonld(name, url_path, desc):
    """A calculator is a WebApplication. Until now both tool pages declared only
    the site-wide WebSite entity, which tells search engines nothing about the
    page being a tool rather than an article."""
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": name,
        "url": DOMAIN + url_path,
        "description": desc,
        "applicationCategory": "HealthApplication",
        "operatingSystem": "Any (modern web browser)",
        "browserRequirements": "Requires JavaScript",
        "isAccessibleForFree": True,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "publisher": {"@type": "Organization", "name": SITE_NAME},
    }, ensure_ascii=False)


def render_tool(t):
    bc = breadcrumb_jsonld([("Home", "/"), (t["title"], t["url"])])
    h = head(t["title"], t["description"], t["url"], site_jsonld(), "website",
             tool_jsonld(t["title"], t["url"], t["description"]), bc)
    body = CALC_BODY.replace(
        '<div class="wrap narrow">',
        '<div class="wrap narrow">\n  <div class="crumbs"><a href="/">Home</a> \u203a Dog age</div>',
        1,
    )
    return shell(h, t["url"], body)


def render_choco_tool(t):
    """Second tool page: chocolate toxicity by body weight.

    The body lives in choco_tool.py — it is markup plus one script, and keeping
    it out of this file keeps the build logic readable.
    """
    bc = breadcrumb_jsonld([("Home", "/"), (t["title"], t["url"])])
    h = head(t["title"], t["description"], t["url"], site_jsonld(), "website",
             tool_jsonld(t["title"], t["url"], t["description"]), bc)
    body = CHOCO_BODY.replace(
        '<div class="wrap narrow">',
        '<div class="wrap narrow">\n  <div class="crumbs"><a href="/">Home</a> \u203a '
        'Chocolate toxicity</div>',
        1,
    )
    return shell(h, t["url"], body)


def render_food_chart(fc):
    """The 47-food tiered reference table.

    Rows are rendered from FOOD_CHART["tiers"], and each row links to its own
    article via LOOKUP so the URL can never drift from the source of truth.
    """
    bc = breadcrumb_jsonld([("Home", "/"), ("Dog nutrition", "/dog-nutrition/"),
                            (fc["title"], fc["url"])])
    h = head(fc["title"], fc["description"], fc["url"], site_jsonld(), "website", None, bc)

    tiers = ""
    for i, tier in enumerate(fc["tiers"], 1):
        # Anchor text is the exact query ("Can dogs eat grapes?", not the bare
        # food name): these are the 47 target keywords of the section and the
        # chart is the page with enough authority to pass the signal down.
        rows = "".join(
            '<tr><td><a href="%s">Can dogs eat %s?</a></td><td>%s</td><td>%s</td></tr>\n'
            % (LOOKUP["can-dogs-eat-" + s][0], s.replace("-", " "), form, num)
            for s, form, num in tier["rows"]
        )
        tiers += (
            '<h2 id="tier-%d">%s</h2>\n<p>%s</p>\n<table class="chart-tbl">\n'
            '<tr><th style="text-align:left">Food</th>'
            '<th style="text-align:left">What is safe</th>'
            '<th style="text-align:left">The number that matters</th></tr>\n'
            '%s</table>\n\n' % (i, tier["label"], tier["intro"], rows)
        )

    body = (
        '<div class="wrap narrow">\n'
        '  <div class="crumbs"><a href="/">Home</a> \u203a '
        '<a href="/dog-nutrition/">Dog nutrition</a> \u203a Food safety chart</div>\n'
        # The whole reference block sits inside .doc: the table styles
        # (.doc table / th / td) are scoped to that wrapper, so without it the
        # 47-row chart renders as unstyled text with no cell padding.
        '<div class="doc">\n'
        + fc["head"] + tiers + fc["tail"] +
        '\n</div>\n</div>'
    )
    return shell(h, "/dog-nutrition/", body)


# ---------------------------------------------------------------------------
# lastmod strategy (哥飞 2026-10-26): a sitemap where every URL shares the same
# <lastmod> date is a trust signal failure — Google quietly stops believing the
# field. git-commit dates were wrong here because render.py rewrites every page
# on every build, so one commit stamped all 79 URLs the same day.
#
# Fix: keep a content fingerprint per page (.lastmod.json). Only pages whose
# rendered HTML actually changed get today's date; every other page keeps the
# date it had. First run seeds itself from the currently published sitemap +
# the files on disk, so nothing gets falsely stamped.
#
# 2026-11-01 correction: fingerprint the BODY only (<main>…</main>), not the
# whole document. Template-level edits — bumping style.css?v=5→6, trimming the
# Organization sameAs list in the JSON-LD — touch all 79 pages at once and used
# to stamp every <lastmod> with the same day, which is exactly the failure this
# mechanism exists to prevent. Body-only hashing means a template change costs
# zero lastmod credibility.
# ---------------------------------------------------------------------------
MANIFEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".lastmod.json")

_BODY_RE = re.compile(r"<main>(.*?)</main>", re.S)


def _body(html):
    """The <main> contents — everything that is real page content, not chrome."""
    m = _BODY_RE.search(html)
    return m.group(1) if m else html


def _sha(html):
    return hashlib.sha1(_body(html).encode("utf-8")).hexdigest()


def _sha_file(path):
    try:
        # Normalise CRLF -> LF: write_page() runs in text mode, so on Windows the
        # file on disk uses \r\n while the freshly-rendered string uses \n.
        b = open(path, "rb").read().replace(b"\r\n", b"\n")
        return _sha(b.decode("utf-8", "replace"))
    except Exception:
        return ""


def _load_manifest():
    try:
        with open(MANIFEST_PATH, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save_manifest(m):
    try:
        with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
            json.dump(m, f, indent=1, sort_keys=True)
    except Exception as e:
        print("  ! could not write manifest: %s" % e)


def _bootstrap_manifest():
    """Seed hashes from disk + dates from the published sitemap (first run only)."""
    m = {}
    try:
        txt = open(os.path.join(PUBLIC, "sitemap.xml"), encoding="utf-8").read()
    except Exception:
        return m
    for loc, lm in re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", txt):
        path = loc.replace(DOMAIN, "").strip("/")
        rel = "public/%s/index.html" % path if path else "public/index.html"
        fp = os.path.join(ROOT, rel)
        if os.path.exists(fp):
            m[rel] = {"h": _sha_file(fp), "d": lm[:10]}
    return m


def build_sitemap(manifest):
    today = datetime.date.today().isoformat()
    # (url, priority, changefreq, repo path of the generated file)
    urls = [(HOME["url"], 1.0, "daily", "public/index.html")]
    for s in PILLARS:
        urls.append((PILLARS[s]["url"], 0.8, "weekly",
                     "public/%s/index.html" % s))
    for a in ARTICLES:
        urls.append((a["url"], 0.8, "monthly",
                     "public/%s/index.html" % a["url"].strip("/")))
    urls.append((ABOUT["url"], 0.3, "yearly", "public/about/index.html"))
    urls.append((CONTACT["url"], 0.3, "yearly", "public/contact/index.html"))
    urls.append((PRIVACY["url"], 0.2, "yearly", "public/privacy/index.html"))
    urls.append((EDITORIAL["url"], 0.3, "yearly", "public/about/editorial-standards/index.html"))
    urls.append((RESOURCES["url"], 0.3, "yearly", "public/resources/index.html"))
    urls.append((TOOL["url"], 0.7, "yearly",
                 "public/%s/index.html" % TOOL["url"].strip("/")))
    urls.append((TOOL_CHOCO["url"], 0.8, "monthly",
                 "public/%s/index.html" % TOOL_CHOCO["url"].strip("/")))
    urls.append((FOOD_CHART["url"], 0.8, "monthly",
                 "public/%s/index.html" % FOOD_CHART["url"].strip("/")))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for u, pri, freq, rel in urls:
        lines.append("  <url>")
        lines.append("    <loc>%s%s</loc>" % (DOMAIN, u))
        lines.append("    <lastmod>%s</lastmod>" % ((manifest.get(rel) or {}).get("d") or today))
        lines.append("    <changefreq>%s</changefreq>" % freq)
        lines.append("    <priority>%s</priority>" % pri)
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines)


def write_page(file_path, html):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)


def render_sitemap():
    """HTML sitemap — one page linking to EVERY page on the site.

    哥飞's #1 indexing trick: Google trusts following links far more than it
    trusts sitemap.xml. A single human-readable page that links to all pages is
    the strongest "discover everything" signal.
    """
    jsonld = site_jsonld()
    h = head("WagWise Pet — All Guides & Tools (Sitemap)",
             "A complete index of every dog and cat care guide, review, and tool on WagWise Pet, so nothing on the whole site is ever more than one click away from this page.",
             "/sitemap/", jsonld, "website", robots="noindex,follow")
    cards = ('<a href="/"><div class="k">HOME</div><h3>' + HOME["title"] +
             '</h3><p>' + HOME["description"] + '</p></a>')
    for s, p in PILLARS.items():
        cards += ('<a href="' + p["url"] + '"><div class="k">SECTION</div><h3>' +
                  p["title"] + '</h3><p>' + p["description"] + '</p></a>')
    for a in ARTICLES:
        cards += ('<a href="' + a["url"] + '"><div class="k">ARTICLE</div><h3>' +
                  a["title"] + '</h3><p>' + a["lede"] + '</p></a>')
    cards += ('<a href="' + TOOL["url"] + '"><div class="k">TOOL</div><h3>' +
              TOOL["title"] + '</h3><p>' + TOOL["description"] + '</p></a>')
    cards += ('<a href="' + TOOL_CHOCO["url"] + '"><div class="k">TOOL</div><h3>' +
              TOOL_CHOCO["title"] + '</h3><p>' + TOOL_CHOCO["description"] + '</p></a>')
    cards += ('<a href="' + FOOD_CHART["url"] + '"><div class="k">REFERENCE</div><h3>' +
              FOOD_CHART["title"] + '</h3><p>' + FOOD_CHART["description"] + '</p></a>')
    cards += ('<a href="/about/"><div class="k">ABOUT</div><h3>About WagWise Pet</h3><p>' +
              ABOUT["description"] + '</p></a>')
    cards += ('<a href="/contact/"><div class="k">CONTACT</div><h3>Contact WagWise Pet</h3><p>' +
              CONTACT["description"] + '</p></a>')
    cards += ('<a href="/privacy/"><div class="k">LEGAL</div><h3>Privacy Policy</h3><p>' +
              PRIVACY["description"] + '</p></a>')
    cards += ('<a href="/resources/"><div class="k">RESOURCES</div><h3>Dog Care Resources We Trust</h3><p>' +
              RESOURCES["description"] + '</p></a>')
    body = (
        '<div class="wrap">\n'
        '  <div class="eyebrow">SITE INDEX</div>\n'
        '  <h1>All guides &amp; tools</h1>\n'
        '  <p class="lede">One page that links to every guide, review and tool on WagWise Pet.</p>\n'
        '  <div class="hub">' + cards + '</div>\n'
        "</div>"
    )
    return shell(h, "/sitemap/", body)


def main():
    today = datetime.date.today().isoformat()
    manifest = _load_manifest()
    if not manifest:
        manifest = _bootstrap_manifest()
        if manifest:
            print("Seeded lastmod manifest from published sitemap (%d pages)" % len(manifest))

    # Collect every page as (path relative to public/, html) so we can fingerprint
    # before writing — only genuinely-changed pages get a fresh <lastmod>.
    pages = [("index.html", render_home())]
    for s, p in PILLARS.items():
        pages.append(("%s/index.html" % s.lstrip("/"), render_pillar(p)))
    for a in ARTICLES:
        rel = a["url"].strip("/")
        pages.append(("%s/index.html" % rel, render_article(a)))
    pages.append(("about/index.html", render_static(
        ABOUT["url"], "/about/", ABOUT["title"], ABOUT["description"],
        ABOUT["body"], crumb_label="About")))
    pages.append(("contact/index.html", render_static(
        CONTACT["url"], "/contact/", CONTACT["title"], CONTACT["description"],
        CONTACT["body"], crumb_label="Contact")))
    pages.append(("privacy/index.html", render_static(
        PRIVACY["url"], "/privacy/", PRIVACY["title"], PRIVACY["description"],
        PRIVACY["body"], crumb_label="Privacy")))
    pages.append(("about/editorial-standards/index.html", render_static(
        EDITORIAL["url"], "/about/editorial-standards/",
        EDITORIAL["title"], EDITORIAL["description"],
        EDITORIAL["body"], crumb_label="About")))
    pages.append(("resources/index.html", render_static(
        RESOURCES["url"], "/resources/", RESOURCES["title"],
        RESOURCES["description"], RESOURCES["body"], crumb_label="Resources")))
    pages.append(("404.html", render_static(
        "/404.html", None, "Page not found", "The page you looked for is not here.",
        "<h1>404</h1><p>The page you were looking for doesn't exist. "
        "<a href=\"/\">Return home</a>.</p>", robots="noindex,follow")))
    pages.append(("%s/index.html" % TOOL["url"].strip("/"), render_tool(TOOL)))
    pages.append(("%s/index.html" % TOOL_CHOCO["url"].strip("/"),
                  render_choco_tool(TOOL_CHOCO)))
    pages.append(("%s/index.html" % FOOD_CHART["url"].strip("/"),
                  render_food_chart(FOOD_CHART)))

    changed = 0
    for rel_public, html in pages:
        rel = "public/" + rel_public
        h = _sha(html)
        prev = manifest.get(rel)
        if prev and prev.get("h") == h:
            d = prev.get("d", today)
        else:
            d = today
            changed += 1
        manifest[rel] = {"h": h, "d": d}
        write_page(os.path.join(PUBLIC, rel_public), html)

    _save_manifest(manifest)

    # Sitemap (XML for engines + HTML page for crawlers/UX, 哥飞: link-following beats sitemap.xml)
    write_page(os.path.join(PUBLIC, "sitemap.xml"), build_sitemap(manifest))
    write_page(os.path.join(PUBLIC, "sitemap", "index.html"), render_sitemap())

    print("Generated %d files into %s (%d content-changed today)" % (len(pages), PUBLIC, changed))


if __name__ == "__main__":
    main()
