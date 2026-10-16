#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Expand every sub-150-character meta description to 150-160 (哥飞 D3).

Descriptions stay unique, keep the core keyword near the front, and answer the
search intent — no keyword stuffing. Exact-string replacement, each verified to
match exactly once before writing. Run: python build/_expand_desc.py
"""
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "build", "articles.py")
REN = os.path.join(ROOT, "build", "render.py")

REPL = [
    # ---- articles ----
    ("A calm method to trim dog nails at home, how short is safe, and what to do if you cut the quick.",
     "A calm, step-by-step method to trim your dog's nails at home, how short is actually safe, what to do if you cut the quick, and how often to trim."),
    ("Apples are a safe, low-calorie dog treat. Why you should remove the seeds and core, and how much to offer.",
     "Yes — apples are a safe, low-calorie dog treat rich in fiber and vitamin C. Why you should always remove the seeds and core, and how much to offer."),
    ("Cooked eggs are a nutritious dog food boost. Why raw eggs are a poor choice, and how to serve them safely.",
     "Cooked eggs are a nutritious, protein-rich food topper for dogs. Why raw eggs are a poor choice, how many a dog can eat per week, and how to serve them."),
    ("Why dogs throw up, when a single vomit is no big deal, and the red-flag symptoms that mean a vet visit now.",
     "Why dogs throw up, when a single vomit is no big deal, the red-flag symptoms that mean a vet visit right now, and how to tell upset from serious."),
    ("Strawberries are a safe, vitamin-rich dog treat. Why to keep them occasional and avoid the sugary toppings.",
     "Strawberries are a safe, vitamin-rich dog treat most dogs love. Why to keep them occasional, how many to offer, and why to skip sugary toppings."),
    ("Seedless watermelon flesh is a hydrating, low-calorie summer treat for dogs. Why to skip the rind and seeds.",
     "Seedless watermelon flesh is a hydrating, low-calorie summer treat most dogs love. Why to skip the rind and seeds, and how much is actually safe."),
    ("Peanut butter is a favorite dog treat, but xylitol is deadly. How to choose a safe jar and how much to give.",
     "Peanut butter is a favorite dog treat, but xylitol in some brands is deadly. How to read the label, choose a safe jar, and how much to give safely."),
    ("Stop leash pulling with the stop-and-go method and a front-clip harness. Calm walks in a week, not a struggle.",
     "Stop leash pulling with the stop-and-go method and a front-clip harness. A step-by-step plan for calm walks in a week, not a daily struggle."),
    ("Plain cooked chicken is a staple dog food protein. Why bones and seasoning are the danger, and how to serve it.",
     "Plain cooked chicken is a staple protein in dog food and a go-to for upset stomachs. Why bones and seasoning are the danger, and how to serve it."),
    ("Chocolate's theobromine is poisonous to dogs. Why dark chocolate is worst, and what to do if your dog eats any.",
     "Chocolate contains theobromine, which is poisonous to dogs. Why dark and baking chocolate are worst, the symptoms to watch for, and what to do next."),
    ("Carrots are one of the healthiest dog snacks — raw or cooked, low calorie, and good for teeth. How to serve them.",
     "Carrots are one of the healthiest dog snacks around — raw or cooked, low in calories, and good for teeth. How to serve them and how much is too much."),
    ("Practical cat care guides: litter training, stopping furniture scratching, and how to stop a cat spraying indoors.",
     "Straightforward cat care guides for real household problems: litter box training, stopping furniture scratching, and how to stop a cat spraying indoors."),
    ("How to spot a dog ear infection — head shaking, odor, redness — and what safe cleaning and vet treatment look like.",
     "How to spot a dog ear infection — head shaking, odor, redness, discharge — plus what safe home cleaning looks like and when a vet needs to see it."),
    ("Grapes and raisins can cause sudden kidney failure in dogs, even in small amounts. What to do if your dog eats one.",
     "Grapes and raisins can cause sudden kidney failure in dogs, even in tiny amounts. Why there is no safe dose, and exactly what to do if yours eats one."),
    ("Why a dog may skip food but still drink, from mild causes to serious ones, and when not eating becomes an emergency.",
     "Why a dog may stop eating but keep drinking water — from mild causes like stress to serious illness — and when not eating becomes a true emergency."),
    ("Most cats litter train themselves. Set up the box right, place it well, and fix the few things that cause accidents.",
     "Most cats litter train themselves. How to set up the box right, where to place it, and how to fix the few things that cause accidents outside the box."),
    ("The human foods that can poison a dog: chocolate, grapes, onions, xylitol, and more — plus what to do if they eat one.",
     "The human foods that can poison a dog — chocolate, grapes, onions, garlic, xylitol, alcohol — and the emergency steps to take if your dog eats one."),
    ("Most dogs can have a little cheese, but lactose intolerance and fat make moderation the rule. Which cheeses are safer.",
     "Most dogs can eat a little cheese, but lactose intolerance and fat make moderation the rule. Which cheeses are safer, and what a safe portion looks like."),
    ("Our practical picks for dog crates and no-pull harnesses, chosen for safety and ease of use rather than marketing hype.",
     "Practical, honest picks for dog crates and no-pull harnesses — chosen for safety, fit, and ease of daily use, not marketing hype or affiliate payout."),
    ("Coprophagia is common and usually behavioral. Learn the causes — boredom, mimicry, diet — and practical ways to stop it.",
     "Coprophagia is common and usually behavioral rather than a sign of illness. The real causes — boredom, mimicry, diet — and practical ways to stop it."),
    ("Everyday dog care you can do at home: brushing teeth, trimming nails safely, bathing, and ear cleaning — without a fight.",
     "Everyday dog care you can do at home: brushing teeth, trimming nails safely, bathing, and cleaning ears — all without turning it into a fight."),
    ("Bananas are safe for dogs as an occasional treat. How much, the peels, and why moderation matters for sugar and calories.",
     "Bananas are safe for dogs as an occasional treat. How much to give, why the peel should always go in the bin, and how sugar and calories add up."),
    ("Dogs shake for many reasons — cold, stress, excitement, pain, or illness. Here is how to tell the harmless from the urgent.",
     "Dogs shake for many reasons — cold, stress, excitement, pain, nausea, or illness. How to tell harmless shivers from symptoms that need a vet."),
    ("Brushing a dog's teeth prevents gum disease — the most common adult dog problem. A simple daily routine and dog-safe paste.",
     "Brushing a dog's teeth prevents gum disease, the most common problem in adult dogs. A simple routine, how often to do it, and which paste is safe."),
    ("The harness that actually reduces pulling is a front-clip design. Our practical picks balance control, comfort, and durability.",
     "The harness that actually reduces pulling is a front-clip design. Practical picks that balance control, comfort, and durability — plus how to fit one."),
    ("Spraying is scent-marking, not a litter problem. Reduce stress, clean with enzymes, and use pheromones and neutering to stop it.",
     "Spraying is scent-marking, not a litter box problem. How to reduce stress, clean with enzymes, and use pheromones and neutering to stop it for good."),
    ("Our straightforward dog crate picks for puppies, anxious dogs, and travel — focused on safety, durability, and ease of cleaning.",
     "Straightforward dog crate picks for puppies, anxious dogs, and travel — chosen for safety, durability, and easy cleaning, plus sizing guidance."),
    ("Most adult dogs are lactose intolerant, so milk tends to cause diarrhea. Small amounts of plain yogurt are a safer dairy option.",
     "Most adult dogs are lactose intolerant, so milk usually causes diarrhea and gas. Why plain yogurt and small amounts of cheese are safer dairy options."),
    ("Avocado flesh is less risky than the skin, pit, and leaves, but the choking and fat risks make it a treat to skip for most dogs.",
     "Avocado flesh is less risky than the skin, pit, and leaves, but the choking hazard and high fat content make it a treat that most dogs should skip."),
    ("Puppy biting and nipping is normal teething behavior. Here is how to redirect it, teach bite inhibition, and when it should stop.",
     "Puppy biting and nipping is normal teething behavior, not aggression. How to redirect it, teach bite inhibition, and when the phase should end."),
    ("Cats scratch to mark territory and shed claw sheaths — not to ruin your sofa. Redirect to posts and make furniture less appealing.",
     "Cats scratch to mark territory and shed old claw sheaths — not to ruin your sofa. How to redirect them to posts and make furniture less appealing."),
    ("What to feed your dog, how much, and which human foods are safe or dangerous. Covers toxic foods, bananas, and daily feeding amounts.",
     "What to feed your dog, how much, and which human foods are safe or dangerous. Covers toxic foods, safe treats, and daily feeding amounts by weight."),
    ("Step-by-step dog and puppy training guides: crate training, leash manners, and stopping biting and pulling with positive reinforcement.",
     "Step-by-step dog and puppy training guides: crate training, leash manners, and stopping biting and pulling — all built on positive reinforcement."),
    ("A practical feeding guide: daily amounts by body weight, how often to feed puppies vs adults, and the signs you have the portion right.",
     "A practical feeding guide: daily amounts by body weight, how often to feed puppies versus adults, and the body signs that show the portion is right."),
    ("A calm, no-tears method to crate train a puppy: how long it takes, how to make the crate inviting, and exactly what to do on the first night.",
     "A calm, no-tears method to crate train a puppy: how long it really takes, how to make the crate inviting, and exactly what to do on the first night."),
    ("Dogs eat grass for boredom, an upset stomach, or just because it tastes good. Usually harmless, but frequent vomiting after grass needs a look.",
     "Dogs eat grass out of boredom, an upset stomach, or simply because it tastes good. Usually harmless — but frequent vomiting after grass needs a vet."),
    # ---- static pages ----
    ("Straightforward dog and cat care answers: training, health symptoms, nutrition, grooming, and honest product picks — written to be useful, not scary.",
     "Straightforward dog and cat care answers: training, health symptoms, nutrition, grooming, and honest product picks — written to be useful and calm, not scary."),
    ("Why WagWise Pet exists: clear, calm pet care information for everyday dog and cat owners, with sources and no fear-mongering.",
     "Why WagWise Pet exists: clear, calm pet care information for everyday dog and cat owners, with cited sources, no fear-mongering, and no false promises."),
    ("How WagWise Pet handles cookies, analytics, and affiliate links, and the veterinary disclaimer that applies to all content.",
     "How WagWise Pet handles cookies, analytics, and affiliate links, plus the veterinary disclaimer that applies to every guide published here."),
    ("Convert your dog's age to human years by size. A quick, plain-language estimate using the standard veterinary approximation, not the old 7x rule.",
     "Convert your dog's age to human years by size. A quick, plain-language estimate using the standard veterinary approximation, not the outdated 7x rule."),
    # ---- sitemap page (lives in render.py) ----
    ("Every dog and cat care guide, review, and tool on WagWise Pet, listed in one place.",
     "A complete index of every dog and cat care guide, review, and tool on WagWise Pet, so nothing is ever more than one click away from this page."),
]

def apply(path, pairs):
    src = io.open(path, encoding="utf-8").read()
    ok = miss = 0
    for old, new in pairs:
        c = src.count(old)
        if c == 0:
            miss += 1
            print("  MISS:", old[:60])
            continue
        if c > 1:
            print("  AMBIGUOUS(%d):" % c, old[:60])
            continue
        src = src.replace(old, new, 1)
        ok += 1
    io.open(path, "w", encoding="utf-8", newline="\n").write(src)
    return ok, miss

print("articles.py:")
o1, m1 = apply(ART, REPL)
print("render.py:")
o2, m2 = apply(REN, [REPL[-1]])
print("\n替换成功 %d 条（articles %d + render %d），未匹配 %d 条" % (o1 + o2, o1, o2, m1 + m2))
