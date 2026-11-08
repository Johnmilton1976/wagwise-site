# -*- coding: utf-8 -*-
"""Expand /best/dog-harness-for-pulling/ from a front-clip pick list into the
harness page: every type, what each one is for, and how to size one."""
import io

P = "build/articles.py"
s = io.open(P, encoding="utf-8", newline="").read().replace("\r\n", "\n")

# ---------------------------------------------------------------- title / desc
old_title = '        "title": "Best Dog Harness for Pulling — Front-Clip Picks",'
new_title = '        "title": "Best Dog Harness for Pulling — Types, Sizing, Front vs Back",'
assert s.count(old_title) == 1
s = s.replace(old_title, new_title)

old_desc = '        "description": "The harness that actually reduces pulling is a front-clip design. Practical picks that balance control, comfort, and durability — plus how to fit one.",'
new_desc = ('        "description": "Only a front-clip harness reduces pulling. What the six harness types actually do, how to size one by chest girth, and the fit checks that keep a strong dog in it.",')
assert s.count(old_desc) == 1
s = s.replace(old_desc, new_desc)

# ------------------------------------------------------------------ types table
anchor = """        <h2>Why front-clip wins — mechanically, not as a slogan</h2>"""
assert s.count(anchor) == 1

types = """        <h2>Six kinds of harness, and the one problem each solves</h2>
        <p>Almost every harness sold is one of six designs. The design decides what the harness can do; the brand decides how well it does it. If your dog pulls, only the second row matters, and the rest of this page is about getting that row right.</p>
        <table>
          <thead><tr><th>Type</th><th>Lead attaches</th><th>What it is for</th><th>Where it fails</th></tr></thead>
          <tbody>
            <tr><td>Back-clip</td><td>On the shoulders</td><td>Everyday walking for a dog that already walks on a loose lead; long lines and hiking</td><td>Nothing about pulling. It gives a strong dog a comfortable anchor to lean into</td></tr>
            <tr><td>Front-clip (chest-clip)</td><td>On the chest</td><td>Teaching a dog not to pull. Tension turns the front end sideways</td><td>Needs a Y-shaped front panel. A straight strap across the shoulder restricts the gait</td></tr>
            <tr><td>Dual-clip</td><td>Front and back</td><td>Training now, a normal walk later — the same harness both ways</td><td>Costs more, and the second ring is often the weak point on cheap versions</td></tr>
            <tr><td>Step-in</td><td>On the back</td><td>Small dogs, seniors, and anything that dislikes having a harness pulled over its head</td><td>Less adjustable, so it fits fewer shapes; easy to back out of if loose</td></tr>
            <tr><td>Roman / H-style</td><td>On the back</td><td>Greyhounds, whippets, salukis — deep-chested dogs that back out of everything else</td><td>More straps to adjust, and it does nothing for pulling</td></tr>
            <tr><td>Head halter</td><td>Under the chin</td><td>Dogs strong enough to drag an adult, where a harness is not enough</td><td>Not a harness: needs its own conditioning, and most dogs resent it at first</td></tr>
          </tbody>
        </table>
        <div class="callout warn"><b>Watch for the seventh design.</b> Some harnesses sold as &ldquo;no-pull&rdquo; work by tightening across the chest when the dog pulls. That is a choke collar distributed over a wider area — it stops the pull by making pulling uncomfortable, which is the mechanism the rest of this page argues against.</div>

"""
s = s.replace(anchor, types + anchor)

# ---------------------------------------------------------------------- sizing
anchor2 = """        <h2>The fitting check — five points</h2>"""
assert s.count(anchor2) == 1

sizing = """        <h2>Sizing: measure the chest, not the dog</h2>
        <p>Harness sizes are not standardised. A medium from one maker overlaps a small from another, and the letter on the packet tells you nothing you can check. The only number that transfers between brands is the chest girth in centimetres, so measure it yourself and compare that to the maker's own chart.</p>
        <table>
          <thead><tr><th>Measurement</th><th>How to take it</th><th>Why it is the one that matters</th></tr></thead>
          <tbody>
            <tr><td>Chest girth</td><td>Standing dog, tape around the widest part of the ribcage, just behind the front legs. Snug against the coat, not tight</td><td>This is the size the harness is built around. Everything else adjusts to it</td></tr>
            <tr><td>Neck</td><td>Where a collar would sit, then add two fingers of room</td><td>Decides whether the harness goes over the head or steps in. Too tight here is what makes dogs refuse to be harnessed</td></tr>
            <tr><td>Back length</td><td>Base of the neck to base of the tail</td><td>Only needed for step-in harnesses and for coats worn under one</td></tr>
          </tbody>
        </table>
        <p>Weight is the input most sizing charts lead with, and it is the one that misleads. A 20 kg whippet and a 20 kg bulldog do not take the same harness — the whippet's chest is deep and narrow, the bulldog's is broad and shallow, and the difference in girth runs to double figures in centimetres. Two dogs of the same breed at the same weight can differ by a whole size depending on condition and coat.</p>
        <div class="callout"><b>Three rules that save a return.</b> Measure a standing dog after a walk, not a sitting one — the tape reads smaller when the dog is folded up. Buy with 4&ndash;6 cm of adjustment left at the girth, because a winter coat adds girth without adding weight. And remeasure a puppy monthly: a harness bought at four months is a different size by seven.</div>

"""
s = s.replace(anchor2, sizing + anchor2)

# ------------------------------------------------------------------------- FAQ
old_faq = """            ("Why does my dog keep slipping out of the harness?", "Usually too loose, or a design without a third belly strap. Check the escape test in a safe enclosed space — dogs that can reverse out will do it near traffic."),"""
assert s.count(old_faq) == 1
new_faq = old_faq + """
            ("How do I measure my dog for a harness?", "Measure the chest girth: a tape around the widest part of the ribcage, just behind the front legs, on a standing dog. Compare that number in centimetres to the maker's chart rather than buying by weight or by the letter on the packet, because S/M/L are not standardised between brands."),
            ("What is the difference between a front-clip and a back-clip harness?", "A back-clip attaches the lead above the shoulders, which suits a dog that already walks well and does nothing about pulling. A front-clip attaches on the chest, so tension turns the dog sideways instead of letting it lean into the lead."),"""
s = s.replace(old_faq, new_faq)

io.open(P, "w", encoding="utf-8", newline="\r\n").write(s)
print("patched articles.py")
