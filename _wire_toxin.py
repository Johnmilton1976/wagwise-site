# -*- coding: utf-8 -*-
"""One-shot: register the toxic-food dose calculator (2026-11-08).

Touches exactly seven places, and asserts on every one so a silent no-op is
impossible. Idempotent: re-running leaves the files as they are.

  1  articles.py   TOOL_TOXIN dict
  2  articles.py   one in-body link on each of the six cluster pages
  3  articles.py   one in-body link on the toxic-foods hub (218 inlinks)
  4  render.py     import
  5  render.py     homepage tool card
  6  render.py     sitemap.xml entry
  7  render.py     /sitemap/ page card
  8  render.py     render_toxin_tool() + pages.append
  9  _redirects    /tools/xxx -> /tools/xxx/ 301
"""
import io
import re
import sys

ART = "build/articles.py"
REN = "build/render.py"
RED = "public/_redirects"

TOOL_DICT = '''
# ---------------------------------------------------------------------------
# Fourth tool (2026-11-08): toxic-food dose calculator.
#
# Why this one: the 28 pages GSC reports as "crawled, not indexed" are all in the
# can-dogs-eat family, and the measured difference between the indexed and the
# unindexed half is internal links (14.7 vs 8.1), not word count or originality
# (47 pages, 1,081 pairwise comparisons, highest overlap 0.216). Chasing all 28
# would be 28 x a ten-cent ad click. The five toxicity pages are the only ones in
# that family with real advertiser value — pet insurance, emergency clinics, poison
# lines — so they get a tool instead of a rewrite, and the tool is the asset that
# can be embedded elsewhere, which is the only link acquisition that works here.
#
# It is deliberately not a second chocolate calculator: chocolate already has one.
# These seven are quoted in five different units, which is the reason owners get
# them wrong — mg/kg for xylitol, g/kg for allium, grams of ethanol for a drink.
# ---------------------------------------------------------------------------
TOOL_TOXIN = {
    "url": "/tools/toxic-food-dose-calculator/",
    "title": "Dog Poisoning Dose Calculator: 7 Toxic Foods by Weight",
    "description": "Turn what your dog ate into grams or milligrams per kilogram and compare it with the published threshold — xylitol, grapes, onion, garlic, macadamia, caffeine, alcohol.",
    "eyebrow": "TOOLS",
}

'''

# Page-specific sentence inserted after the first dose table in each body.
LINKS = {
    "can-dogs-eat-xylitol": '<p>If you are holding a packet rather than a number, the <a href="/tools/toxic-food-dose-calculator/">toxic food dose calculator</a> converts grams of xylitol into milligrams per kilogram for your dog\'s weight and says which of the three thresholds you are in.</p>',
    "can-dogs-eat-grapes": '<p>Because there is no threshold to compare against, the <a href="/tools/toxic-food-dose-calculator/">toxic food dose calculator</a> refuses to give grapes a safe band at all — it shows the grams per kilogram as context and returns red for any amount above zero.</p>',
    "can-dogs-eat-garlic": '<p>Garlic has no separately measured canine figure, so the <a href="/tools/toxic-food-dose-calculator/">toxic food dose calculator</a> derives it from the onion threshold using Merck\'s 3&ndash;5&times; ratio and labels it as derived, then gives you grams per kilogram for your dog.</p>',
    "can-dogs-eat-alcohol": '<p>Volume is not the dose, which is why drinks get measured wrong: the <a href="/tools/toxic-food-dose-calculator/">toxic food dose calculator</a> takes the millilitres and the strength and returns grams of pure ethanol per kilogram against the 5.5&ndash;7.9&nbsp;g/kg lethal figure.</p>',
    "can-dogs-eat-caffeine": '<p>Cups, tablets and milligrams are three different inputs for the same question — the <a href="/tools/toxic-food-dose-calculator/">toxic food dose calculator</a> converts all of them to mg per kilogram and puts the result against the 140&nbsp;mg/kg canine MLD50.</p>',
    "can-dogs-eat-macadamia-nuts": '<p>The 0.7&nbsp;g/kg figure is where signs start, and three nuts is enough for a 10&nbsp;kg dog — the <a href="/tools/toxic-food-dose-calculator/">toxic food dose calculator</a> works it out for your dog\'s weight, and takes the chocolate half of a chocolate-covered macadamia separately.</p>',
    "foods-toxic-to-dogs": '<p>Every row on this page is a dose, not a verdict, and the ones where the arithmetic changes the answer are all in one place: the <a href="/tools/toxic-food-dose-calculator/">toxic food dose calculator</a> converts xylitol, grapes, onion, garlic, macadamia, caffeine and alcohol into grams or milligrams per kilogram for your dog\'s weight.</p>',
}


def patch_articles():
    s = io.open(ART, encoding="utf-8", newline="").read()
    crlf = "\r\n" in s
    s = s.replace("\r\n", "\n")
    before = s

    if "TOOL_TOXIN = {" not in s:
        anchor = "# ---------------------------------------------------------------------------\n# Reference asset: the 47-food safety chart (2026-11-02)."
        assert anchor in s, "wrong anchor for TOOL_TOXIN: the FOOD_CHART comment block moved"
        s = s.replace(anchor, TOOL_DICT.lstrip("\n") + anchor, 1)

    for slug, para in LINKS.items():
        marker = '"url": "/dog-nutrition/%s/"' % slug
        assert marker in s, "article not found: " + slug
        i = s.index(marker)
        j = s.index('"body": """', i)
        end = s.index('"""', j + 11)
        seg = s[j:end]
        if "toxic-food-dose-calculator" in seg:
            continue
        k = seg.find("</table>")
        assert k > -1, "no dose table in " + slug
        k += len("</table>")
        seg2 = seg[:k] + "\n" + para + seg[k:]
        s = s[:j] + seg2 + s[end:]

    # The dict must sit before render.py imports it, and after TOOL_FEED.
    assert s.index("TOOL_FEED = {") < s.index("TOOL_TOXIN = {") < s.index("FOOD_CHART = {")
    if crlf:
        s = s.replace("\n", "\r\n")
    io.open(ART, "w", encoding="utf-8", newline="").write(s)
    print("articles.py  %+d bytes" % (len(s) - len(before)))


def patch_render():
    s = io.open(REN, encoding="utf-8", newline="").read()
    crlf = "\r\n" in s
    s = s.replace("\r\n", "\n")
    before = len(s)

    s = s.replace("FOOD_CHART, TOOL_CHOCO, TOOL_FEED  # noqa",
                  "FOOD_CHART, TOOL_CHOCO, TOOL_FEED, TOOL_TOXIN  # noqa", 1)
    if "from toxin_tool import" not in s:
        s = s.replace("from feed_tool import FEED_BODY  # noqa",
                      "from feed_tool import FEED_BODY  # noqa\nfrom toxin_tool import TOXIN_BODY  # noqa", 1)

    if "TOOL_TOXIN[" not in s.split("def build_sitemap")[0]:
        old = ('              (TOOL_FEED["url"], TOOL_FEED["title"], TOOL_FEED["description"],\n'
               '               "dog-food-calculator", "TOOL"),\n')
        assert old in s
        s = s.replace(old, old +
                      '              (TOOL_TOXIN["url"], TOOL_TOXIN["title"], TOOL_TOXIN["description"],\n'
                      '               "toxic-food-dose-calculator", "TOOL"),\n', 1)

    old = ('    urls.append((TOOL_FEED["url"], 0.8, "monthly",\n'
           '                 "public/%s/index.html" % TOOL_FEED["url"].strip("/")))\n')
    assert old in s
    if 'TOOL_TOXIN["url"], 0.8' not in s:
        s = s.replace(old, old +
                      '    urls.append((TOOL_TOXIN["url"], 0.8, "monthly",\n'
                      '                 "public/%s/index.html" % TOOL_TOXIN["url"].strip("/")))\n', 1)

    old = ('    cards += (\'<a href="\' + TOOL_FEED["url"] + \'"><div class="k">TOOL</div><h3>\' +\n'
           '              TOOL_FEED["title"] + \'</h3><p>\' + TOOL_FEED["description"] + \'</p></a>\')\n')
    assert old in s
    if 'TOOL_TOXIN["url"] + \'"><div class="k">TOOL' not in s:
        s = s.replace(old, old +
                      '    cards += (\'<a href="\' + TOOL_TOXIN["url"] + \'"><div class="k">TOOL</div><h3>\' +\n'
                      '              TOOL_TOXIN["title"] + \'</h3><p>\' + TOOL_TOXIN["description"] + \'</p></a>\')\n', 1)

    if "def render_toxin_tool" not in s:
        anchor = "def render_food_chart(fc):"
        func = '''def render_toxin_tool(t):
    """Fourth tool page: dose per kilogram across the toxic-food cluster.

    Body lives in toxin_tool.py for the same reason as the chocolate and food
    calculators — markup plus one script, kept out of the build logic.
    """
    bc = breadcrumb_jsonld([("Home", "/"), (t["title"], t["url"])])
    h = head(t["title"], t["description"], t["url"], site_jsonld(), "website",
             tool_jsonld(t["title"], t["url"], t["description"]), bc)
    body = TOXIN_BODY.replace(
        '<div class="wrap narrow">',
        '<div class="wrap narrow">\\n  <div class="crumbs"><a href="/">Home</a> \\u203a '
        'Poisoning dose</div>',
        1,
    )
    return shell(h, t["url"], body)


'''
        s = s.replace(anchor, func + anchor, 1)

    old = ('    pages.append(("%s/index.html" % TOOL_FEED["url"].strip("/"),\n'
           '                  render_feed_tool(TOOL_FEED)))\n')
    assert old in s
    if "render_toxin_tool(TOOL_TOXIN)" not in s:
        s = s.replace(old, old +
                      '    pages.append(("%s/index.html" % TOOL_TOXIN["url"].strip("/"),\n'
                      '                  render_toxin_tool(TOOL_TOXIN)))\n', 1)

    if crlf:
        s = s.replace("\n", "\r\n")
    io.open(REN, "w", encoding="utf-8", newline="").write(s)
    print("render.py    %+d bytes" % (len(s) - before))


def patch_redirects():
    s = io.open(RED, encoding="utf-8", newline="").read()
    line = "/tools/toxic-food-dose-calculator /tools/toxic-food-dose-calculator/ 301"
    if line in s:
        print("_redirects   already present")
        return
    anchor = "/tools/dog-food-calculator /tools/dog-food-calculator/ 301"
    assert anchor in s
    nl = "\r\n" if "\r\n" in s else "\n"
    s = s.replace(anchor, anchor + nl + line, 1)
    io.open(RED, "w", encoding="utf-8", newline="").write(s)
    print("_redirects   +1 rule (no-slash 301)")


if __name__ == "__main__":
    patch_articles()
    patch_render()
    patch_redirects()
    print("done — now run: python build/render.py")
