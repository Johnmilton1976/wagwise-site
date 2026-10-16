#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add `sources` to the remaining wagwise articles (batch 2 + batch 3).

Source pool below was HTTP-verified on 2026-10-16 via proxy:
  ASPCA /pet-care/aspca-poison-control... and /pet-care/{dog,cat}-care...  -> 200
  Merck merckvetmanual.com/{dog-owners,cat-owners}/...                    -> 200
  Cornell Riney Canine + Cornell Feline Health Center                      -> 200
  iCatCare icatcare.org/advice/, AVSAB position statements                 -> 200
  AKC pages are Cloudflare-blocked for datacenter IPs but were confirmed
  to exist (why-is-my-dog-shaking, dog-grooming-at-home).
Dead ends (do NOT use): avma.org unreachable here, PDSA/MSD grape/nail/
cat-routine pages 404, FDA xylitol page dead.

Idempotent: skips any article that already has a sources field.
Run:  python build/_add_sources2.py
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "build", "articles.py")

A_DOG = ("ASPCA — Dog Care", "https://www.aspca.org/pet-care/dog-care")
A_CAT = ("ASPCA — Cat Care", "https://www.aspca.org/pet-care/cat-care")
A_DOGBEH = ("ASPCA — Common Dog Behavior Issues",
            "https://www.aspca.org/pet-care/dog-care/common-dog-behavior-issues")
A_CATBEH = ("ASPCA — Common Cat Behavior Issues",
            "https://www.aspca.org/pet-care/cat-care/common-cat-behavior-issues")
M_DOG = ("Merck Veterinary Manual — Dog Owners", "https://www.merckvetmanual.com/dog-owners")
M_VOMIT = ("Merck Veterinary Manual — Vomiting in Dogs",
           "https://www.merckvetmanual.com/dog-owners/digestive-disorders-of-dogs/vomiting-in-dogs")
M_DIGEST = ("Merck Veterinary Manual — Digestive Disorders of Dogs",
            "https://www.merckvetmanual.com/dog-owners/digestive-disorders-of-dogs")
M_EAR = ("Merck Veterinary Manual — Ear Disorders of Dogs",
         "https://www.merckvetmanual.com/dog-owners/ear-disorders-of-dogs")
M_BEH = ("Merck Veterinary Manual — Behavior of Dogs",
         "https://www.merckvetmanual.com/dog-owners/behavior-of-dogs")
M_CARE = ("Merck Veterinary Manual — Routine Care of Dogs",
          "https://www.merckvetmanual.com/dog-owners/routine-care-of-dogs")
M_HEALTH = ("Merck Veterinary Manual — Routine Health Care of Dogs",
            "https://www.merckvetmanual.com/dog-owners/routine-care-of-dogs/routine-health-care-of-dogs")
M_CATBEH = ("Merck Veterinary Manual — Behavior of Cats",
            "https://www.merckvetmanual.com/cat-owners/behavior-of-cats")
C_DOG = ("Cornell Riney Canine Health Center — Canine Health Information",
         "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information")
C_CAT = ("Cornell Feline Health Center",
         "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center")
C_CATTOPIC = ("Cornell Feline Health Center — Feline Health Topics",
              "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics")
AK_SHAKE = ("AKC — Why Is My Dog Shaking?",
            "https://www.akc.org/expert-advice/health/why-is-my-dog-shaking/")
AK_GROOM = ("AKC — The Dos and Don'ts of Home Dog Grooming and Hygiene",
            "https://www.akc.org/expert-advice/health/dog-grooming-at-home")
AVSAB = ("American Veterinary Society of Animal Behavior — Position Statements",
         "https://avsab.org/resources/position-statements/")
ICAT = ("International Cat Care — Advice", "https://icatcare.org/advice/")

SOURCES = {
    # ---- batch 2: health symptoms + grooming ----
    "dog-vomiting-causes": [M_VOMIT, A_DOG, C_DOG],
    "dog-ear-infection-symptoms": [M_EAR, A_DOG, C_DOG],
    "dog-not-eating-but-drinking-water": [M_DIGEST, A_DOG, C_DOG],
    "why-is-my-dog-shaking": [AK_SHAKE, M_DOG, A_DOG],
    "why-do-dogs-eat-grass": [M_BEH, A_DOG, C_DOG],
    "why-do-dogs-eat-poop": [M_BEH, A_DOG, C_DOG],
    "how-to-trim-dog-nails": [AK_GROOM, M_CARE, A_DOG],
    "how-to-brush-dog-teeth": [AK_GROOM, M_HEALTH, A_DOG],
    # ---- batch 3: nutrition / training / cats / reviews ----
    "how-much-to-feed-my-dog": [M_HEALTH, A_DOG, C_DOG],
    "how-to-crate-train-a-puppy": [A_DOGBEH, AVSAB, M_BEH],
    "how-to-stop-puppy-biting": [AVSAB, A_DOGBEH, M_BEH],
    "how-to-leash-train-a-dog": [A_DOGBEH, AVSAB, M_BEH],
    "cat-litter-training": [C_CAT, A_CAT, ICAT],
    "cat-scratching-furniture": [A_CATBEH, C_CATTOPIC, ICAT],
    "cat-spraying-how-to-stop": [A_CATBEH, M_CATBEH, C_CAT],
    "best-dog-crate": [A_DOGBEH, AVSAB, M_BEH],
    "best-dog-harness-for-pulling": [A_DOGBEH, AVSAB, M_BEH],
}

src = io.open(PATH, encoding="utf-8").read()
done, skipped, missing = 0, 0, []

for slug, entries in SOURCES.items():
    anchor = '"slug": "%s",' % slug
    if anchor not in src:
        missing.append(slug)
        continue
    pos = src.find(anchor)
    dpos = src.find('"disclaimer"', pos)
    if dpos < 0:
        missing.append(slug + "(no disclaimer)")
        continue
    if '"sources"' in src[pos:dpos]:
        skipped += 1
        continue
    line_start = src.rfind("\n", 0, dpos) + 1
    indent = " " * 8
    block = indent + '"sources": [\n'
    for label, url in entries:
        block += indent + '    ("%s",\n%s     "%s"),\n' % (label, indent, url)
    block += indent + "],\n"
    src = src[:line_start] + block + src[line_start:]
    done += 1

io.open(PATH, "w", encoding="utf-8", newline="\n").write(src)
print("新增 %d 篇 | 已有 sources 跳过 %d 篇 | 未找到 %s" % (done, skipped, missing or "无"))
