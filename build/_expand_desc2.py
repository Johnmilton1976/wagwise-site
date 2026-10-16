#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 2 — nudge the remaining sub-150 descriptions into the 150-160 band (哥飞 D3).

Round 1 rewrote them but landed at 139-149. This pass appends a short, natural
clause to each so every meta description sits inside 150-160 characters.
Exact-string replacement, each verified to match exactly once. Prints a full
length audit at the end.
Run: python build/_expand_desc2.py
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "build", "articles.py")
REN = os.path.join(ROOT, "build", "render.py")

REPL = [
    ("all built on positive reinforcement.",
     "all built on reward-based positive reinforcement."),
    ("and daily feeding amounts by weight.",
     "and daily feeding amounts by body weight."),
    ("all without turning it into a fight.",
     "all without turning it into a fight or a fuss."),
    ("not marketing hype or affiliate payout.",
     "not marketing hype or affiliate payouts."),
    ("and exactly what to do on the first night.",
     "and exactly what to do on the very first night."),
    ("and when the phase should end.",
     "and when the phase should finally end."),
    ("not a daily struggle.",
     "not a daily walk-time struggle."),
    ("and how to tell upset from serious.",
     "and how to tell upset from something serious."),
    ("and when a vet needs to see it.",
     "and when a vet really needs to see it."),
    ("and when not eating becomes a true emergency.",
     "and when not eating becomes a true medical emergency."),
    ("from symptoms that need a vet.",
     "from symptoms that need a vet's attention."),
    ("but frequent vomiting after grass needs a vet.",
     "but frequent vomiting after eating grass needs a vet."),
    ("and practical ways to stop it.",
     "and practical ways to stop it for good."),
    ("and the emergency steps to take if your dog eats one.",
     "and the emergency steps to take if your dog eats any of them."),
    ("and how sugar and calories add up.",
     "and why sugar and calories add up quickly."),
    ("and the body signs that show the portion is right.",
     "and the body condition signs that show the portion is right."),
    ("and how often to trim.",
     "and how often to trim each nail."),
    ("and which paste is safe.",
     "and which toothpaste is safe."),
    ("and make furniture less appealing.",
     "and make your furniture less appealing."),
    ("use pheromones and neutering to stop it for good.",
     "use pheromones and consider neutering to stop it for good."),
    ("and easy cleaning, plus sizing guidance.",
     "and easy cleaning, plus clear sizing guidance."),
    ("and how much to offer.",
     "and exactly how much to offer."),
    ("and how much is actually safe.",
     "and exactly how much is actually safe."),
    ("and how much to give safely.",
     "and how much peanut butter is safe to give."),
    ("How to serve them and how much is too much.",
     "How to serve them and just how much is too much."),
    ("and how to serve it.",
     "and how to serve it safely."),
    ("and why to skip sugary toppings.",
     "and why you should skip sugary toppings."),
    ("and what to do next.",
     "and exactly what to do next."),
    ("a treat that most dogs should skip.",
     "a treat that most dogs are better off skipping."),
    ("the veterinary disclaimer that applies to every guide published here.",
     "the full veterinary disclaimer that applies to every guide published here."),
]


def apply(path, pairs):
    src = io.open(path, encoding="utf-8").read()
    ok = miss = amb = 0
    for old, new in pairs:
        c = src.count(old)
        if c == 0:
            miss += 1
            print("  MISS:", old[:60])
            continue
        if c > 1:
            amb += 1
            print("  AMBIGUOUS(%d):" % c, old[:60])
            continue
        src = src.replace(old, new, 1)
        ok += 1
    io.open(path, "w", encoding="utf-8", newline="\n").write(src)
    return ok, miss, amb


print("articles.py:")
o1, m1, a1 = apply(ART, REPL)
print("  命中 %d / 未匹配 %d / 歧义 %d" % (o1, m1, a1))

# ---------------- audit ----------------
print("\n=== 长度审计（meta description 需 150-160）===")
SRC_RE = re.compile(r'"description":\s*"((?:[^"\\]|\\.)*)"')
TOTAL = BAD = 0
for path in (ART, REN):
    src = io.open(path, encoding="utf-8").read()
    for m in SRC_RE.finditer(src):
        d = m.group(1)
        # skip the Organization JSON-LD blurb, which is not a meta description
        if d.startswith("An independent pet care editorial resource"):
            continue
        TOTAL += 1
        if not (150 <= len(d) <= 160):
            BAD += 1
            print("  [%3d] %s | %s" % (len(d), os.path.basename(path), d[:70]))

# sitemap page description lives as a bare string in render.py
ren = io.open(REN, encoding="utf-8").read()
m = re.search(r'"(A complete index[^"]*)"', ren)
if m:
    TOTAL += 1
    if not (150 <= len(m.group(1)) <= 160):
        BAD += 1
        print("  [%3d] render.py sitemap | %s" % (len(m.group(1)), m.group(1)[:70]))

print("\n合规 %d / %d，区间外 %d" % (TOTAL - BAD, TOTAL, BAD))
