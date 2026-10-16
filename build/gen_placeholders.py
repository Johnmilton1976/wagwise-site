#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate placeholder hero images for each article so the local preview shows
real-looking cards instead of broken images.

These are intentionally generic: a soft pet-themed gradient, a paw motif, the
article title, and a clear "replace with a real photo" note. When 朱朱 supplies
real high-res photos, drop them in public/assets/img/<slug>.jpg (or .webp) and
update the <img> src in build/render.py + re-run render.py, OR keep the .svg
name and overwrite the file.

Run:  python build/gen_placeholders.py
"""

import os
import sys
import textwrap

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from articles import ARTICLES, SITE_NAME  # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "public", "assets", "img")

W, H = 1200, 675  # 16:9

# Palette (matches style.css pet theme)
BG_TOP = "#EAF6EF"
BG_BOT = "#FBFAF7"
GREEN = "#3FA97E"
GREEN_DK = "#2E7E5E"
INK = "#234039"
PAW = "#CFE9DC"


def wrap_title(title, width=22):
    """Wrap a title into <=width-char lines for SVG text."""
    words = title.split()
    lines, cur = [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= width:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def paw(cx, cy, s, fill, opacity=1.0):
    """A simple 4-pad + heel paw print as an SVG group."""
    pads = [
        (cx - s * 0.55, cy - s * 0.55, s * 0.32),
        (cx + s * 0.55, cy - s * 0.55, s * 0.32),
        (cx - s * 0.95, cy - s * 0.05, s * 0.30),
        (cx + s * 0.95, cy - s * 0.05, s * 0.30),
    ]
    heel = (cx, cy + s * 0.55, s * 0.55)
    parts = []
    for px, py, pr in pads + [heel]:
        parts.append('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" opacity="%.2f"/>'
                     % (px, py, pr, pr * 1.25, fill, opacity))
    return '<g transform="rotate(-12 %.1f %.1f)">%s</g>' % (cx, cy, "".join(parts))


def make_svg(slug, title):
    lines = wrap_title(title)
    # vertical centering of the title block
    line_h = 56
    total_h = line_h * len(lines)
    start_y = H / 2 - total_h / 2 + 22

    title_svg = []
    for i, ln in enumerate(lines):
        y = start_y + i * line_h
        title_svg.append(
            '<text x="%d" y="%.0f" font-family="Segoe UI, Helvetica, Arial, sans-serif" '
            'font-size="46" font-weight="700" fill="%s">%s</text>' % (90, y, INK, escape(ln))
        )
    title_block = "\n    ".join(title_svg)

    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
        'role="img" aria-label="%s">\n'
        '  <defs>\n'
        '    <linearGradient id="g" x1="0" y1="0" x2="0" y2="1">\n'
        '      <stop offset="0" stop-color="%s"/>\n'
        '      <stop offset="1" stop-color="%s"/>\n'
        '    </linearGradient>\n'
        '  </defs>\n'
        '  <rect width="%d" height="%d" fill="url(#g)"/>\n'
        '  %s\n'
        '  %s\n'
        '  <rect x="40" y="40" width="%d" height="%d" rx="18" fill="none" '
        'stroke="%s" stroke-width="3" stroke-dasharray="10 8" opacity="0.8"/>\n'
        '  <text x="%d" y="58" font-family="Segoe UI, Helvetica, Arial, sans-serif" '
        'font-size="20" font-weight="700" fill="%s" letter-spacing="1">PLACEHOLDER &#9656; replace with real photo</text>\n'
        '  <text x="%d" y="%d" font-family="Segoe UI, Helvetica, Arial, sans-serif" '
        'font-size="20" fill="%s">%s</text>\n'
        '  %s\n'
        '</svg>\n'
    ) % (
        W, H, W, H, escape(title),
        BG_TOP, BG_BOT,
        W, H,
        paw(W - 220, 175, 60, PAW, 0.9),
        paw(W - 150, 300, 42, PAW, 0.7),
        W - 80, H - 80, GREEN,
        90, GREEN_DK,
        90, H - 70, GREEN_DK, SITE_NAME,
        title_block,
    )
    return svg


def escape(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace('"', "&quot;"))


def main():
    os.makedirs(IMG_DIR, exist_ok=True)
    count = 0
    for a in ARTICLES:
        slug = a["slug"]
        title = a["title"]
        svg = make_svg(slug, title)
        path = os.path.join(IMG_DIR, slug + ".svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        count += 1
    print("Generated %d placeholder images into %s" % (count, IMG_DIR))


if __name__ == "__main__":
    main()
