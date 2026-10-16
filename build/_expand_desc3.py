#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 3 — close out the last 4 descriptions outside 150-160 (哥飞 D3).
Run: python build/_expand_desc3.py
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "build", "articles.py")
REN = os.path.join(ROOT, "build", "render.py")

ART_REPL = [
    # 149 -> 158
    ("plus clear sizing guidance.",
     "plus clear, practical sizing guidance."),
    # 162 -> 154
    ("and how much peanut butter is safe to give.",
     "and how much of it is safe to give."),
    # 144 -> 154
    ("the full veterinary disclaimer that applies to every guide published here.",
     "the full veterinary disclaimer that applies to every guide published on this site."),
]
REN_REPL = [
    # 142 -> 156
    ("so nothing is ever more than one click away from this page.",
     "so nothing on the whole site is ever more than one click away from this page."),
]


def apply(path, pairs):
    src = io.open(path, encoding="utf-8").read()
    ok = miss = amb = 0
    for old, new in pairs:
        c = src.count(old)
        if c == 0:
            miss += 1
            print("  MISS:", old[:70])
            continue
        if c > 1:
            amb += 1
            print("  AMBIGUOUS(%d):" % c, old[:70])
            continue
        src = src.replace(old, new, 1)
        ok += 1
    io.open(path, "w", encoding="utf-8", newline="\n").write(src)
    return ok, miss, amb


print("articles.py: 命中 %d / 未匹配 %d / 歧义 %d" % apply(ART, ART_REPL))
print("render.py:   命中 %d / 未匹配 %d / 歧义 %d" % apply(REN, REN_REPL))

print("\n=== 最终审计（meta description 需 150-160）===")
SRC_RE = re.compile(r'"description":\s*"((?:[^"\\]|\\.)*)"')
TOTAL = BAD = 0
for path in (ART, REN):
    src = io.open(path, encoding="utf-8").read()
    for m in SRC_RE.finditer(src):
        d = m.group(1)
        if d.startswith("An independent pet care editorial resource"):
            continue
        TOTAL += 1
        if not (150 <= len(d) <= 160):
            BAD += 1
            print("  [%3d] %s | %s" % (len(d), os.path.basename(path), d[:70]))

ren = io.open(REN, encoding="utf-8").read()
m = re.search(r'"(A complete index[^"]*)"', ren)
if m:
    TOTAL += 1
    if not (150 <= len(m.group(1)) <= 160):
        BAD += 1
        print("  [%3d] render.py sitemap | %s" % (len(m.group(1)), m.group(1)[:70]))

print("\n合规 %d / %d，区间外 %d" % (TOTAL - BAD, TOTAL, BAD))
