#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-shot: inject a `sources` field into food-safety articles in articles.py.

All URLs below were HTTP-verified on 2026-10-16 (ASPCA new path after their
site reshuffle; Pet Poison Helpline / Merck / Cornell returned 200).
AKC pages are Cloudflare-protected against datacenter IPs but load fine in a
real browser; the three AKC URLs used here were confirmed to exist.
Run once:  python build/_add_sources.py
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "build", "articles.py")

A = "ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets"
A_U = "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"
M = "Merck Veterinary Manual — Food Hazards"
M_U = "https://www.merckvetmanual.com/toxicology/food-hazards"
C = "Cornell Riney Canine Health Center — Canine Health Information"
C_U = "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"
AKV = "AKC — Fruits and Vegetables Dogs Can and Can't Eat"
AKV_U = "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"

SOURCES = {
    "foods-toxic-to-dogs": [(A, A_U), (M, M_U), (C, C_U)],
    "can-dogs-eat-chocolate": [
        ("Pet Poison Helpline — Chocolate", "https://www.petpoisonhelpline.com/poison/chocolate/"),
        ("Merck Veterinary Manual — Chocolate Toxicosis in Animals",
         "https://www.merckvetmanual.com/toxicology/food-hazards/chocolate-toxicosis-in-animals"),
        (A, A_U),
    ],
    "can-dogs-eat-grapes": [
        ("Pet Poison Helpline — Grapes", "https://www.petpoisonhelpline.com/poison/grapes/"),
        ("Pet Poison Helpline — Raisins", "https://www.petpoisonhelpline.com/poison/raisins/"),
        (A, A_U),
    ],
    "can-dogs-eat-avocado": [
        ("Pet Poison Helpline — Avocado", "https://www.petpoisonhelpline.com/poison/avocado/"),
        ("Merck Veterinary Manual — Avocado Toxicosis in Animals",
         "https://www.merckvetmanual.com/toxicology/food-hazards/avocado-toxicosis-in-animals"),
        (A, A_U),
    ],
    "can-dogs-eat-peanut-butter": [
        ("Pet Poison Helpline — Xylitol", "https://www.petpoisonhelpline.com/poison/xylitol/"),
        (A, A_U),
        (AKV, AKV_U),
    ],
    "can-dogs-eat-bananas": [
        ("AKC — Can Dogs Eat Bananas?", "https://www.akc.org/expert-advice/nutrition/can-dogs-eat-bananas/"),
        (AKV, AKV_U),
        (A, A_U),
    ],
    "can-dogs-eat-apples": [
        ("AKC — Can Dogs Eat Apples?", "https://www.akc.org/expert-advice/nutrition/can-dogs-eat-apples/"),
        (AKV, AKV_U),
        (A, A_U),
    ],
    "can-dogs-eat-watermelon": [(AKV, AKV_U), (A, A_U), (C, C_U)],
    "can-dogs-eat-carrots": [(AKV, AKV_U), (A, A_U), (C, C_U)],
    "can-dogs-eat-strawberries": [(AKV, AKV_U), (A, A_U), (C, C_U)],
    "can-dogs-eat-cheese": [(A, A_U), (C, C_U), (M, M_U)],
    "can-dogs-eat-eggs": [(A, A_U), (C, C_U), (M, M_U)],
    "can-dogs-eat-chicken": [(A, A_U), (C, C_U), (M, M_U)],
    "can-dogs-eat-milk": [(A, A_U), (C, C_U), (M, M_U)],
}

src = io.open(PATH, encoding="utf-8").read()
already = re.findall(r'"sources"', src)
if already:
    print("sources 字段已存在 %d 处，脚本跳过（避免重复插入）" % len(already))
    sys.exit(0)

done = 0
for slug, entries in SOURCES.items():
    anchor = '"slug": "%s",' % slug
    if anchor not in src:
        print("MISS anchor:", slug)
        continue
    # find the disclaimer line that belongs to this article (first one after the anchor)
    pos = src.find(anchor)
    dpos = src.find('"disclaimer"', pos)
    if dpos < 0:
        print("MISS disclaimer:", slug)
        continue
    # walk back to the start of that line to keep indentation tidy
    line_start = src.rfind("\n", 0, dpos) + 1
    indent = " " * 8
    block = indent + '"sources": [\n'
    for label, url in entries:
        block += indent + '    ("%s",\n%s     "%s"),\n' % (label, indent, url)
    block += indent + "],\n"
    src = src[:line_start] + block + src[line_start:]
    done += 1

io.open(PATH, "w", encoding="utf-8", newline="\n").write(src)
print("已为 %d 篇注入 sources" % done)
