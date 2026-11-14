# -*- coding: utf-8 -*-
"""Toxic-food dose calculator — body markup + script (2026-11-08).

Kept out of render.py for the same reason as choco_tool.py: this is ~700 lines
of markup plus one script, and render.py is build logic.

WHAT THIS IS FOR
    The chocolate calculator answers one food. This one answers the seven that
    make up the "toxic foods" cluster, because the search behaviour is the same:
    the owner is standing in the kitchen with a dog and a number they need in
    thirty seconds — grams per kilogram. Every page in the cluster repeats the
    same five paragraphs about "call your vet"; none of them does the division.

THE NUMBERS, AND WHERE THEY COME FROM
    Each band is anchored to a published threshold, not to a blog. Where the
    literature gives a range, the calculator uses the end that gets the dog
    seen, and the page says so:

      xylitol      >100 mg/kg hypoglycaemia, >500 mg/kg hepatic failure
                   (Merck Veterinary Manual; ASPCA APCC; 50 mg/kg is the
                   decontamination threshold in the same references)
      grapes       no established safe dose — any amount is treated as an
                   exposure. Recorded toxic: raisins from 2.8 g/kg, grapes
                   from 19.6 g/kg (median of a 43-dog retrospective)
      onion        15-30 g/kg produces clinically important haematological
                   change in dogs (Merck; Frontiers review)
      garlic       Merck: "garlic is 3-5 times more toxic than onion" — there
                   is no separately measured canine g/kg figure, so the onion
                   threshold is divided by 4 and the page says it is derived
      macadamia    signs from 0.7 g/kg; recorded range 2.2-62.4 g/kg
      caffeine     canine oral MLD50 140 mg/kg (range 120-200); signs from
                   roughly 20 mg/kg
      alcohol      lethal oral dose 5.5-7.9 g/kg of 100% ethanol; 1 mL of
                   ethanol weighs 0.789 g

    The garlic number is the only derived one, and it is labelled as derived in
    the prose. Everything else is quoted.
"""

TOXIN_BODY = """
<style>
/* Embeddable mode. Scoped to this page on purpose: the rules belong to this
   tool, so shipping them here avoids re-versioning the site-wide stylesheet
   and rewriting 89 unrelated files. */
html.embed .site-head,html.embed .site-foot,html.embed .crumbs,
html.embed .lede,html.embed .eyebrow,html.embed .doc,html.embed .cfc-bar{display:none!important}
html.embed main{padding:0}
html.embed .wrap.narrow{max-width:none;padding:14px 14px 6px}
html.embed h1{font-size:19px;line-height:1.3;margin:0 0 10px}
html.embed .calc-card{margin:0 0 10px;padding:18px}
html.embed body{padding-bottom:0!important}
/* The credit sits outside .doc so it survives the embed trim. Without it a
   framed copy carries no link back, which defeats the point of offering it. */
.embed-credit{display:none}
html.embed .embed-credit{display:block;font-size:12.5px;color:#6b6f66;margin:8px 0 0}
.calc-card{max-width:600px;margin:24px 0;padding:24px;background:#fff;border:1px solid #e3e0d8;border-radius:14px;box-shadow:0 1px 3px rgba(0,0,0,.05)}
.calc-card label{display:block;font-weight:600;margin:14px 0 6px;color:#243027;font-size:14px}
.calc-card label:first-child{margin-top:0}
.calc-card select,.calc-card input{font-size:16px;padding:10px 12px;border:1px solid #cfcabb;border-radius:9px;background:#fff;color:#243027;width:100%;box-sizing:border-box;min-width:0}
.calc-row{display:flex;gap:10px;align-items:center}
.calc-row input{flex:1;min-width:0}
.calc-row select{width:auto;flex:1 1 0;min-width:0}
.calc-result{margin-top:18px;padding:16px;border-radius:10px;background:#EAF5EF;color:#1f5c43;font-size:19px;font-weight:700;text-align:center;line-height:1.45}
.calc-result small{display:block;font-size:13px;font-weight:500;margin-top:6px;color:#41685a;line-height:1.5}
.calc-result.watch{background:#FBF3DF;color:#7A5A15}
.calc-result.watch small{color:#7A5A15}
.calc-result.bad{background:#FBE9E3;color:#8C3A1B}
.calc-result.bad small{color:#8C3A1B}
.calc-note{font-size:14px;color:#6b6f66;margin-top:10px}
.calc-sub{font-size:14px;color:#4b5b50;margin:2px 0 0;line-height:1.55}
.tx-table{width:100%;max-width:100%;table-layout:fixed;border-collapse:collapse;margin:14px 0;font-size:14px}
.tx-table th,.tx-table td{border-bottom:1px solid #e3e0d8;padding:8px 6px;text-align:left;vertical-align:top;overflow-wrap:break-word}
.tx-table th{background:#f6f4ee;font-weight:600;font-size:13px}
.tx-table td.n{font-variant-numeric:tabular-nums}
#tx-abv-wrap{display:none}
@media(max-width:520px){
  .tx-table th:first-child,.tx-table td:first-child{width:34%}
  .calc-card{padding:18px}
  .calc-row{flex-wrap:wrap}
  .calc-row select{flex:1 1 100%}
  .doc table.tx-table{display:table;overflow:visible}
  .tx-table{font-size:13px}
  .tx-table th,.tx-table td{padding:7px 4px}
}
</style>
<div class="wrap narrow">
  <div class="eyebrow">TOOLS</div>
  <h1>Dog poisoning dose calculator: 7 toxic foods by weight</h1>
  <p class="lede">Every "can dogs eat X" page gives you a verdict. What a vet needs is a number: grams or milligrams per kilogram of dog. Pick the food, put in the weight and the amount, and this returns that number against the published threshold — for xylitol, grapes, onion, garlic, macadamia, caffeine and alcohol.</p>

  <div class="calc-card">
    <label for="tx-weight">Your dog's weight</label>
    <div class="calc-row">
      <input id="tx-weight" type="number" min="0.5" step="0.1" value="10">
      <select id="tx-wunit">
        <option value="kg" selected>kg</option>
        <option value="lb">lb</option>
      </select>
    </div>

    <label for="tx-food">What did your dog eat?</label>
    <select id="tx-food">
      <option value="xylitol">Xylitol — sugar-free gum, mints, some nut butters</option>
      <option value="grapes">Grapes or raisins</option>
      <option value="onion">Onion — raw, cooked, powder, soup mix</option>
      <option value="garlic">Garlic — raw, roasted, powder, garlic bread</option>
      <option value="macadamia">Macadamia nuts</option>
      <option value="caffeine">Caffeine — coffee, tea, energy drink, tablets</option>
      <option value="alcohol">Alcohol — beer, wine, spirits, mouthwash</option>
    </select>

    <div id="tx-abv-wrap">
      <label for="tx-abv">What kind of drink or product</label>
      <select id="tx-abv">
        <option value="5">Beer, about 5% alcohol</option>
        <option value="12" selected>Wine, about 12% alcohol</option>
        <option value="20">Liqueur, about 20% alcohol</option>
        <option value="21">Mouthwash, about 21% alcohol</option>
        <option value="40">Spirits, about 40% alcohol</option>
        <option value="70">Hand sanitiser, about 70% alcohol</option>
        <option value="0">Rising bread dough — I don't know the percentage</option>
      </select>
    </div>

    <div id="tx-amount-wrap">
      <label for="tx-amount">How much was eaten</label>
      <div class="calc-row">
        <input id="tx-amount" type="number" min="0" step="any" value="100">
        <select id="tx-unit"></select>
      </div>
      <p class="calc-sub" id="tx-unit-hint"></p>
    </div>

    <div id="tx-out" class="calc-result">Enter the weight and the amount.<small>The result appears here.</small></div>
    <p class="calc-note" id="tx-note">Estimate only. It cannot know how full your dog's stomach was, what else was in the same mouthful, or how sensitive that individual is. If the number is in a red band, phone rather than read.</p>
  </div>

  <div class="doc">
    <h2 id="why">Why the answer is a number and not "toxic"</h2>
    <p>The word "toxic" is doing two different jobs on pet websites, and the confusion costs dogs. Sometimes it means <em>there is no dose at all</em> — grapes are the real example, where no amount has ever been established as safe. More often it means <em>there is a dose, and it is a bigger number than people assume</em>. A 10&nbsp;kg dog needs roughly one whole onion to reach the published threshold; the same dog needs well under half a gram of xylitol, which is one or two pieces of sugar-free gum. Both are filed under "toxic foods" on every chart, and the practical distance between them is a factor of three hundred.</p>
    <p>So this tool does one thing: it converts what your dog ate into <strong>amount per kilogram of body weight</strong>, and puts that against the number in the veterinary literature. That is the figure a vet or a poison line will ask you for, and it is the figure that decides whether you are watching the dog at home or driving to a clinic at eleven at night.</p>

    <h2 id="table">The reference table: what it takes, per kilogram</h2>
    <p>Read down the last column first. It is the amount that matters for a 10&nbsp;kg dog — the size of a beagle or a small border collie — and it is the number most owners are surprised by. All seven are in the table, with the one you selected picked out — because the useful comparison is across the seven, not down a single page.</p>
    <table class="tx-table" id="tx-ref">
      <tr><th>Food</th><th>Threshold in the literature</th><th>For a 10&nbsp;kg dog</th></tr>
    </table>

    <h2 id="xylitol">Xylitol: the one where a single piece of gum matters</h2>
    <p>Xylitol is a sugar alcohol, and in dogs — not in people, not in cats — it triggers a rapid release of insulin. The threshold used in the veterinary literature is <strong>more than 100&nbsp;mg per kg for hypoglycaemia</strong> and <strong>more than 500&nbsp;mg per kg for liver failure</strong>, with gut decontamination recommended from 50&nbsp;mg per kg. For a 10&nbsp;kg dog that is 1&nbsp;g of xylitol to put it in the hypoglycaemia band, and 5&nbsp;g to put it in the liver-failure band.</p>
    <p>That sounds like a lot until you look at a packet. Sugar-free gum is typically 0.2 to 1&nbsp;g of xylitol per piece, so <strong>two pieces can reach the decontamination threshold for a 10&nbsp;kg dog</strong>, and a pack can reach the liver band. Sugar-free peanut butter, mints, cough syrup, some liquid medicines, chewable vitamins and even some toothpaste carry it too. The label word to look for is xylitol, but also birch sugar, birch bark extract and wood sugar — all the same compound.</p>
    <p>Two details that change what you do. Onset can be as fast as 30 minutes when the xylitol is in gum or a chew, or as late as 12 to 18 hours when it is bound up in a baked product, so a dog that looks fine at the two-hour mark has not cleared anything. And <strong>activated charcoal does not bind xylitol</strong>, so the usual "the vet will give charcoal" reassurance does not apply here — this one is glucose monitoring, not charcoal.</p>

    <h2 id="grapes">Grapes and raisins: the absence of a number is the finding</h2>
    <p>Grapes are the opposite case. There is no established toxic dose, and that is not a gap in the research that a calculator can fill — it is the finding. In the case series, some dogs have eaten a kilogram of raisins with no signs, and others have died from a handful. The lowest recorded raisin dose producing kidney failure is around <strong>2.8&nbsp;g per kg</strong>; recorded grape doses run from 19.6 to 148.4&nbsp;g per kg with a median around 40. The mechanism is still not settled, and the current guidance from every veterinary body is the same: <strong>treat any ingestion as an exposure</strong>.</p>
    <p>So this calculator refuses to give grapes a green band. Any amount above zero comes back as red, and the dose is shown as context rather than as a verdict. That is deliberate. A calculator that told you "12 grapes for a 10&nbsp;kg dog is below the threshold" would be manufacturing a number the literature does not contain, and the cost of being wrong is a dog in kidney failure four days later.</p>
    <p>One more thing the charts usually miss: <strong>raisins are worse than grapes per gram</strong>, by roughly a factor of seven, because drying removes the water and concentrates what is left. A small box of raisins is a serious exposure in a way that the same weight of fresh grapes is not.</p>

    <h2 id="allium">Onion and garlic: the 3-to-5 rule nobody explains</h2>
    <p>Onion, garlic, leek, chives and shallots all contain the same organosulfur oxidants, and they damage red blood cells by oxidation — Heinz body formation, then haemolytic anaemia a few days later. Cooking, drying and powdering do not remove it; if anything, powder is the most concentrated form in a kitchen.</p>
    <p>The published canine threshold is <strong>15 to 30&nbsp;g of raw onion per kg</strong> to produce clinically important blood changes. For garlic there is no separately measured canine figure in the standard references — instead, Merck states that <strong>garlic is 3 to 5 times more toxic than onion</strong> gram for gram, which is where every "garlic is 5&times; worse" claim on the internet comes from. This calculator uses the midpoint, divides the onion threshold by four, and labels the result as derived, because presenting a derived number as a measured one is exactly the habit that makes pet-health content untrustworthy.</p>
    <p>The practical consequence is uncomfortable: the threshold is high enough that a bit of garlic powder in a stew is not an emergency, and low enough that a dog which eats garlic bread regularly is accumulating damage. Allium anaemia is <strong>cumulative</strong> — small amounts daily do what one large amount does. Signs are delayed by one to five days, which is why the phone call happens after the dog has already been unwell for a while.</p>

    <h2 id="rest">Macadamia, caffeine, alcohol</h2>
    <p><strong>Macadamia nuts</strong> cause a neurological syndrome that looks alarming and almost never kills: weakness that is worst in the back legs, tremors, vomiting, a raised temperature. Signs have been reported from <strong>0.7&nbsp;g per kg</strong>, with recorded doses from 2.2 to 62.4&nbsp;g per kg, and most dogs are normal again in 24 to 48 hours with supportive care. The trap is chocolate-covered macadamias, where the theobromine lands on top — use the <a href="/tools/chocolate-toxicity-calculator/">chocolate calculator</a> for that half.</p>
    <p><strong>Caffeine</strong> is the same methylxanthine family as theobromine and roughly three times as potent per milligram, which is why a caffeine tablet is a worse event than the same weight of milk chocolate. Signs start from around <strong>20&nbsp;mg per kg</strong> — restlessness, vomiting, a lot of urine — and the canine oral MLD50 is <strong>140&nbsp;mg per kg</strong>, with a reported range of 120 to 200. One 200&nbsp;mg tablet is 20&nbsp;mg per kg for a 10&nbsp;kg dog: the bottom of the symptomatic band from a single pill. Coffee grounds, used tea bags, energy drinks and pre-workout powder are the usual sources; slug bait made from caffeine tablets is the unusual one.</p>
    <p><strong>Alcohol</strong> is dosed in grams of pure ethanol, and the arithmetic trips people up because the volume and the strength are two separate numbers. The lethal oral dose in dogs is <strong>5.5 to 7.9&nbsp;g per kg of 100% ethanol</strong>, and one millilitre of ethanol weighs 0.789&nbsp;g — so 25&nbsp;mL of 40% spirits is about 7.9&nbsp;g of ethanol, which is the whole lethal dose for a 1&nbsp;kg dog and a mild dose for a 30&nbsp;kg one. Rising bread dough is the source owners never think of: the yeast produces ethanol in the warm stomach while the dough expands, so it is an alcohol exposure and a gastric distension at the same time.</p>

    <h2 id="call">What to have ready before you phone</h2>
    <p>Four numbers, in this order. Every poison line and every clinic opens with the same questions, and having them ready is worth more than a paragraph of description:</p>
    <ol>
      <li><strong>The dog's weight</strong>, as accurately as you can. A 10% error almost never changes the decision; being out by a factor of two does, and owners routinely underestimate small dogs.</li>
      <li><strong>The product, with its label.</strong> "Xylitol" is not an amount; "0.66&nbsp;g of xylitol per piece, four pieces" is. The same goes for cocoa percentage on chocolate, alcohol percentage on a drink, and the net weight on a pack of raisins.</li>
      <li><strong>How much went down</strong>, in grams where you can. A wrapper plus a kitchen scale beats an estimate, and an estimate beats "some".</li>
      <li><strong>How long ago</strong>, because the useful window for inducing vomiting is roughly two hours and it is the only intervention that depends on the clock.</li>
    </ol>
    <h3>What not to do</h3>
    <p>Do not induce vomiting unless a vet tells you to. It is not the right move for a caustic, for a dog that is already drowsy or twitching, or for a flat-faced breed, and it is useless after two hours. Do not give milk, oil, bread or salt water — none of them bind anything, and salt water carries its own poisoning risk. And do not wait for symptoms as a test: for xylitol the hypoglycaemia can arrive in half an hour, and for allium the anaemia arrives in three days, by which point the window for decontamination is long gone.</p>

    <h2 id="sources">Sources and review</h2>
    <p>Thresholds are taken from the veterinary literature rather than from other pet websites, and each band in the calculator can be traced to one of these:</p>
    <ul>
      <li><strong>Xylitol</strong> — Merck Veterinary Manual, <em>Xylitol Toxicosis in Dogs</em>: hypoglycaemia above about 100&nbsp;mg/kg (45&nbsp;mg/lb), hepatic failure above 500&nbsp;mg/kg (227&nbsp;mg/lb). The 50&nbsp;mg/kg decontamination threshold and the 30&nbsp;mg/kg low-end case report come from the ASPCA APCC data summarised in <em>Frontiers in Veterinary Science</em>, <em>Household Food Items Toxic to Dogs and Cats</em> (2016).</li>
      <li><strong>Grapes and raisins</strong> — same review, Table&nbsp;1: raisins from 2.8&nbsp;g/kg, grapes 19.6&ndash;148.4&nbsp;g/kg (median 40.6), from a 43-dog retrospective. Conclusion quoted directly: any quantity should be handled aggressively.</li>
      <li><strong>Onion</strong> — 15&ndash;30&nbsp;g/kg in dogs, 5&nbsp;g/kg in cats; Merck Veterinary Manual, <em>Garlic and Onion (Allium spp) Toxicosis</em>, and the same review.</li>
      <li><strong>Garlic</strong> — Merck states garlic is 3&ndash;5&times; more toxic than onion. <strong>The g/kg figure on this page is derived from that ratio, not measured</strong>, and is labelled as derived wherever it appears.</li>
      <li><strong>Macadamia</strong> — signs from 0.7&nbsp;g/kg, recorded range 2.2&ndash;62.4&nbsp;g/kg (same review).</li>
      <li><strong>Caffeine</strong> — canine oral MLD50 140&nbsp;mg/kg, reported range 120&ndash;200&nbsp;mg/kg (<em>Journal of Medical Toxicology</em> case report, and the dvm360 toxicology proceedings). Symptomatic from roughly 20&nbsp;mg/kg.</li>
      <li><strong>Ethanol</strong> — lethal oral dose 5.5&ndash;7.9&nbsp;g/kg of 100% ethanol; 1&nbsp;mL ethanol = 0.789&nbsp;g. Merck Veterinary Manual, <em>Toxicoses From Alcohols</em>.</li>
    </ul>
    <p>Where the sources give a range, the calculator uses the end that gets the dog seen sooner, and the band text says which end. This is general information, not veterinary advice, and it cannot examine your dog. If your dog is small, already unwell, pregnant, or has eaten more than one of these at once, phone first and read afterwards. Last reviewed 8 November 2026.</p>

    <h2 id="embed">Put this calculator on your own site</h2>
    <p>Vet clinics, breeders, trainers and pet blogs are welcome to embed it. The snippet is the whole tool, it sets no cookie, and the script only tightens the height:</p>
    <div class="callout">
      <p style="font-size:13px;word-break:break-all">&lt;iframe id="ww-toxin" src="https://wagwise.org/tools/toxic-food-dose-calculator/?embed=1" width="100%" height="980" style="border:1px solid #e3e0d8;border-radius:14px" title="Dog poisoning dose calculator: toxic foods by body weight"&gt;&lt;/iframe&gt;
&lt;script&gt;addEventListener("message",function(e){if(e.data&amp;&amp;e.data.wagwiseHeight){var f=document.getElementById("ww-toxin");if(f)f.height=e.data.wagwiseHeight+2}});&lt;/script&gt;</p>
      <p style="font-size:13px">980px is the measured height of the card at 320px, the narrowest column this is likely to sit in, so the frame is complete without the script. With it, the box shrinks to about 613px on a full-width column instead of leaving a white gap.</p>
      <p style="font-size:13px;word-break:break-all">&lt;p&gt;Calculator by &lt;a href="https://wagwise.org/tools/toxic-food-dose-calculator/"&gt;WagWise Pet&lt;/a&gt; &mdash; dose per kilogram for seven toxic foods.&lt;/p&gt;</p>
    </div>

    <h2 id="quick">Quick answers</h2>
    <h3>How much xylitol is toxic to a dog?</h3>
    <p>Above about 100&nbsp;mg per kg of body weight for hypoglycaemia and above 500&nbsp;mg per kg for liver failure, with gut decontamination recommended from 50&nbsp;mg per kg. For a 10&nbsp;kg dog that is 1&nbsp;g to 5&nbsp;g — two to ten pieces of typical sugar-free gum.</p>
    <h3>How many grapes will hurt a dog?</h3>
    <p>There is no established number, which is the point. Some dogs have eaten a kilogram of raisins without signs and others have died from a handful, and the lowest recorded raisin dose causing kidney failure is around 2.8&nbsp;g per kg. Any ingestion is treated as an exposure.</p>
    <h3>Is a little bit of onion or garlic dangerous?</h3>
    <p>For dogs the published onion threshold is 15 to 30&nbsp;g per kg in a single dose, and garlic is 3 to 5 times more toxic per gram. A small amount once is rarely an emergency, but the damage is cumulative — regular table scraps with onion or garlic do what one large dose does.</p>
    <h3>How much alcohol will kill a dog?</h3>
    <p>The lethal oral dose is 5.5 to 7.9&nbsp;g of pure ethanol per kg. Since a millilitre of ethanol weighs 0.789&nbsp;g, that is about 25&nbsp;mL of 40% spirits for a 1&nbsp;kg dog and roughly 750&nbsp;mL for a 30&nbsp;kg dog — the small end arrives by accident.</p>
    <h3>Should I make my dog vomit after eating something toxic?</h3>
    <p>Not unless a vet tells you to. Vomiting only helps inside roughly two hours, it is dangerous for a dog that is already drowsy or twitching, and it is the wrong move for caustics and flat-faced breeds. And for xylitol it changes little, because activated charcoal does not bind it.</p>

<script type="application/ld+json">{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "How much xylitol is toxic to a dog?", "acceptedAnswer": {"@type": "Answer", "text": "Above about 100 mg per kg of body weight for hypoglycaemia and above 500 mg per kg for liver failure, with gut decontamination recommended from 50 mg per kg. For a 10 kg dog that is 1 g to 5 g — two to ten pieces of typical sugar-free gum."}}, {"@type": "Question", "name": "How many grapes will hurt a dog?", "acceptedAnswer": {"@type": "Answer", "text": "There is no established number, which is the point. Some dogs have eaten a kilogram of raisins without signs and others have died from a handful, and the lowest recorded raisin dose causing kidney failure is around 2.8 g per kg. Any ingestion is treated as an exposure."}}, {"@type": "Question", "name": "Is a little bit of onion or garlic dangerous to a dog?", "acceptedAnswer": {"@type": "Answer", "text": "For dogs the published onion threshold is 15 to 30 g per kg in a single dose, and garlic is 3 to 5 times more toxic per gram. A small amount once is rarely an emergency, but the damage is cumulative — regular table scraps with onion or garlic do what one large dose does."}}, {"@type": "Question", "name": "How much alcohol will kill a dog?", "acceptedAnswer": {"@type": "Answer", "text": "The lethal oral dose is 5.5 to 7.9 g of pure ethanol per kg. Since a millilitre of ethanol weighs 0.789 g, that is about 25 mL of 40% spirits for a 1 kg dog and roughly 750 mL for a 30 kg dog — the small end arrives by accident."}}, {"@type": "Question", "name": "Should I make my dog vomit after eating something toxic?", "acceptedAnswer": {"@type": "Answer", "text": "Not unless a vet tells you to. Vomiting only helps inside roughly two hours, it is dangerous for a dog that is already drowsy or twitching, and it is the wrong move for caustics and flat-faced breeds. And for xylitol it changes little, because activated charcoal does not bind it."}}]}</script>

    <h2 id="next">The rest of this cluster</h2>
    <p>Each of these seven has a full guide behind it, and each one is written around the dose rather than the verdict: <a href="/dog-nutrition/can-dogs-eat-xylitol/">xylitol</a>, <a href="/dog-nutrition/can-dogs-eat-grapes/">grapes and raisins</a>, <a href="/dog-nutrition/can-dogs-eat-garlic/">garlic</a>, <a href="/dog-nutrition/can-dogs-eat-alcohol/">alcohol</a>, <a href="/dog-nutrition/can-dogs-eat-caffeine/">caffeine</a>, <a href="/dog-nutrition/can-dogs-eat-macadamia-nuts/">macadamia nuts</a> and <a href="/dog-nutrition/can-dogs-eat-chocolate/">chocolate</a>. If you only want the ranking rather than the arithmetic, the <a href="/dog-nutrition/food-safety-chart/">48-food safety chart</a> puts all of them in four tiers; the full emergency list is on <a href="/dog-nutrition/foods-toxic-to-dogs/">foods toxic to dogs</a>.</p>
  </div>
  <p class="embed-credit">Calculator by <a href="https://wagwise.org/tools/toxic-food-dose-calculator/">WagWise Pet</a> &mdash; dose per kilogram for seven toxic foods.</p>
</div>
<script>
(function(){
  /* Each food has: the unit the band is quoted in, the bands themselves, the
     units an owner can realistically type, and one line of "what that looks
     like" for a 10 kg dog. Thresholds are the published ones; garlic is the
     only derived figure and its text says so. */
  var FOOD = {
    xylitol: {
      label:'xylitol', unit:'mg/kg',
      bands:[{max:50,cls:'watch',t:'below the decontamination threshold'},
             {max:100,cls:'bad',t:'in the decontamination band'},
             {max:500,cls:'bad',t:'above the hypoglycaemia threshold'},
             {max:1e9,cls:'bad',t:'above the liver-failure threshold'}],
      advice:function(d){
        if(d<50) return 'Below the 50 mg/kg decontamination threshold, but a published case report puts signs as low as 30 mg/kg. Phone your vet and give them the grams of xylitol and the dog\u2019s weight.';
        if(d<100) return 'Gut decontamination is recommended from this dose. Phone now — do not wait for the dog to look unwell.';
        if(d<500) return 'Hypoglycaemia is expected. This is a hospital visit with blood glucose measured every 1\u20132 hours for at least 12 hours.';
        return 'Liver failure becomes a real risk above 500 mg/kg. Emergency clinic now; liver enzymes need checking for 72 hours.';
      },
      /* 1 g = 1000 mg. Units map to grams of product-free xylitol. */
      units:[{v:'g',label:'grams of xylitol',m:1000},{v:'mg',label:'milligrams of xylitol',m:1}],
      hint:'Check the packet. Sugar-free gum is typically 0.2\u20131 g of xylitol per piece; sugar-free peanut butter and mints vary more.',
      canon:'mg', factor:1000,
      ref:[['Hypoglycaemia','&gt;100 mg/kg'],['Liver failure','&gt;500 mg/kg']],
      def:1, what:'two pieces of sugar-free gum'
    },
    grapes: {
      label:'grapes or raisins', unit:'g/kg',
      bands:[{max:1e9,cls:'bad',t:'any amount — no safe dose is established'}],
      advice:function(){ return 'There is no threshold to compare against, so this is an exposure at any dose. Phone your vet or a poison line now, and say whether it was grapes or raisins \u2014 raisins are about seven times more concentrated per gram.'; },
      units:[{v:'g',label:'grams',m:1},
             {v:'grape',label:'grapes (about 5 g each)',m:5},
             {v:'raisin',label:'raisins (about 0.5 g each)',m:0.5}],
      hint:'Counting is fine here. One grape is about 5 g, one raisin about 0.5 g, and a small box of raisins is around 40 g.',
      canon:'g', factor:1,
      ref:[['Lowest recorded, raisins','2.8 g/kg'],['Recorded, grapes','19.6\u2013148.4 g/kg'],['Median, grapes','40.6 g/kg']],
      def:50, what:'a handful'
    },
    onion: {
      label:'onion', unit:'g/kg',
      bands:[{max:15,cls:'watch',t:'below the single-dose threshold'},
             {max:30,cls:'bad',t:'in the reported threshold band'},
             {max:1e9,cls:'bad',t:'above the reported threshold band'}],
      advice:function(d){
        if(d<15) return 'Below the 15 g/kg single-dose threshold, but Allium damage is cumulative. If this is a regular thing — table scraps, gravy, soup — phone and mention how often.';
        if(d<30) return 'This is inside the published 15\u201330 g/kg band where clinically important blood changes occur. Vet visit, and expect blood work 3\u20135 days later when the anaemia peaks.';
        return 'Above the published band. Vet today; haemolytic anaemia develops over days and a transfusion is sometimes needed.';
      },
      units:[{v:'g',label:'grams of onion',m:1},
             {v:'onion',label:'medium onions (about 150 g)',m:150}],
      hint:'Raw, cooked, dehydrated, powdered and soup mix all count \u2014 cooking does not destroy the compound. Powder is the most concentrated form in a kitchen.',
      canon:'g', factor:1,
      ref:[['Clinical changes','15\u201330 g/kg'],['Cats','5 g/kg']],
      def:100, what:'one whole medium onion'
    },
    garlic: {
      label:'garlic', unit:'g/kg',
      bands:[{max:3.75,cls:'watch',t:'below the derived threshold'},
             {max:7.5,cls:'bad',t:'in the derived threshold band'},
             {max:1e9,cls:'bad',t:'above the derived threshold band'}],
      advice:function(d){
        if(d<3.75) return 'Below the derived threshold, but garlic is the most concentrated Allium in a kitchen and the damage is cumulative. Phone if this is regular, or if the dog is an Akita, Shiba or Jindo \u2014 those breeds are more susceptible.';
        if(d<7.5) return 'Inside the derived band where blood changes are expected. Vet visit, with a red-cell check 3\u20135 days out.';
        return 'Above the derived band. Vet today. Expect pale gums and dark urine to appear days later, not hours.';
      },
      units:[{v:'g',label:'grams of garlic',m:1},
             {v:'clove',label:'cloves (about 5 g each)',m:5}],
      hint:'No canine g/kg figure has been measured for garlic. This uses Merck\u2019s statement that garlic is 3\u20135\u00d7 more toxic than onion, so the onion threshold divided by 4. Treat it as an estimate.',
      canon:'g', factor:1,
      ref:[['Derived threshold','3.75\u20137.5 g/kg'],['Merck ratio','3\u20135\u00d7 onion']],
      def:5, what:'about seven cloves'
    },
    macadamia: {
      label:'macadamia nuts', unit:'g/kg',
      bands:[{max:0.7,cls:'watch',t:'below the lowest reported dose'},
             {max:2.2,cls:'bad',t:'above the lowest reported dose'},
             {max:1e9,cls:'bad',t:'inside the recorded toxic range'}],
      advice:function(){
        return 'Signs are weakness in the back legs, tremors, vomiting and a raised temperature within 12 hours. It rarely kills and most dogs are normal in 24\u201348 hours with supportive care \u2014 but phone, because chocolate-covered macadamias add theobromine on top.';
      },
      units:[{v:'g',label:'grams of nut',m:1},
             {v:'nut',label:'nuts (about 2.5 g each)',m:2.5}],
      hint:'A macadamia kernel is roughly 2 to 3 g. If they were chocolate-covered, run the chocolate calculator as well.',
      canon:'g', factor:1,
      ref:[['First signs','0.7 g/kg'],['Recorded range','2.2\u201362.4 g/kg']],
      def:3, what:'three nuts'
    },
    caffeine: {
      label:'caffeine', unit:'mg/kg',
      bands:[{max:20,cls:'watch',t:'below the symptomatic dose'},
             {max:40,cls:'bad',t:'in the mild-signs band'},
             {max:80,cls:'bad',t:'in the cardiac band'},
             {max:1e9,cls:'bad',t:'approaching the lethal range'}],
      advice:function(d){
        if(d<20) return 'Below the level where signs usually start, but caffeine is about three times as potent as theobromine per milligram and small dogs clear it slowly. Watch for restlessness and phone if anything changes.';
        if(d<40) return 'Restlessness, vomiting and heavy urination are expected. Phone your vet; most dogs at this dose are managed with observation.';
        if(d<80) return 'Cardiac band \u2014 racing heart, arrhythmia. Vet visit the same day, with a heart rate check.';
        return 'Severe. The canine oral MLD50 is 140 mg/kg (range 120\u2013200), so this is a substantial fraction of a lethal dose. Emergency clinic now.';
      },
      units:[{v:'mg',label:'milligrams of caffeine',m:1},
             {v:'coffee',label:'cups of brewed coffee (about 95 mg)',m:95},
             {v:'tablet',label:'200 mg caffeine tablets',m:200}],
      hint:'Brewed coffee is about 95 mg per cup, espresso about 63 mg per shot, a 250 mL energy drink 80 mg, and a standard caffeine tablet 200 mg. Coffee grounds and used tea bags are far more concentrated than the drink.',
      canon:'mg', factor:1,
      ref:[['Signs start','~20 mg/kg'],['MLD50','140 mg/kg (120\u2013200)']],
      def:1, what:'one 200 mg tablet'
    },
    alcohol: {
      label:'alcohol', unit:'g/kg of ethanol',
      bands:[{max:1,cls:'watch',t:'below the level where signs usually start'},
             {max:2.5,cls:'bad',t:'in the ataxia band'},
             {max:5,cls:'bad',t:'in the severe depression band'},
             {max:1e9,cls:'bad',t:'at or past the lethal dose'}],
      advice:function(d){
        if(d<1) return 'Below the level where signs usually start, but dogs clear ethanol slowly and hypoglycaemia is a risk. Watch for wobbling, drooling and drowsiness, and phone if anything appears.';
        if(d<2.5) return 'Ataxia and sedation are expected. Phone your vet; keep the dog warm and do not induce vomiting if it is already drowsy.';
        if(d<5) return 'Severe CNS depression band \u2014 hypothermia, acidosis and slow breathing. Emergency clinic.';
        return 'At or past the published lethal oral dose of 5.5\u20137.9 g/kg of pure ethanol. Emergency clinic immediately.';
      },
      units:[{v:'ml',label:'millilitres of the drink',m:1}],
      hint:'Volume alone is not the dose \u2014 the strength matters, which is why the selector above asks for it. Rising bread dough counts too: the yeast keeps making ethanol in the stomach.',
      canon:'g', factor:1,
      ref:[['Lethal oral dose','5.5\u20137.9 g/kg'],['1 mL ethanol','0.789 g']],
      def:200, what:'about 25 mL of 40% spirits'
    }
  };

  var ETHANOL_DENSITY = 0.789;

  var wEl=document.getElementById('tx-weight'), wuEl=document.getElementById('tx-wunit'),
      fEl=document.getElementById('tx-food'), aEl=document.getElementById('tx-amount'),
      uEl=document.getElementById('tx-unit'), hintEl=document.getElementById('tx-unit-hint'),
      abvEl=document.getElementById('tx-abv'), abvWrap=document.getElementById('tx-abv-wrap'),
      amtWrap=document.getElementById('tx-amount-wrap'),
      out=document.getElementById('tx-out'), note=document.getElementById('tx-note'),
      refEl=document.getElementById('tx-ref');

  /* Accepts an element or a raw value. Called with aEl.value in two places,
     which used to read .value off a string and return 0 for every input. */
  function num(el){ var v=parseFloat(el && el.value!==undefined ? el.value : el); return isNaN(v)||v<0?0:v; }
  function round(v,dp){ var m=Math.pow(10,dp===undefined?1:dp); return Math.round(v*m)/m; }

  function kg(){
    var w=num(wEl);
    return wuEl.value==='lb' ? w/2.20462 : w;
  }

  /* Grams of the thing the band is quoted in. Xylitol and caffeine are quoted
     in mg, so their amounts carry a factor; alcohol is volume x strength x
     density; everything else is already grams. */
  function amountInCanon(){
    var f=FOOD[fEl.value];
    var raw=num(aEl.value);
    var u=f.units.filter(function(x){return x.v===uEl.value;})[0] || f.units[0];
    var base=raw*u.m;
    if(fEl.value==='alcohol'){
      var abv=parseFloat(abvEl.value);
      if(isNaN(abv)) abv=12;
      return base*(abv/100)*ETHANOL_DENSITY;
    }
    return base;
  }

  function bandOf(f,d){
    for(var i=0;i<f.bands.length;i++){ if(d<f.bands[i].max) return f.bands[i]; }
    return f.bands[f.bands.length-1];
  }

  /* Each food gets a typical amount. Without it every food opens on 100 g,
     which for xylitol is a number no household ever holds. The amount is only
     replaced when it still holds the previous food's default, so a number the
     reader typed survives a change of food. */
  var lastFood=fEl.value, firstFill=true;

  function fillUnits(){
    var f=FOOD[fEl.value];
    var prev=uEl.value;
    uEl.innerHTML=f.units.map(function(u){
      return '<option value="'+u.v+'">'+u.label+'</option>';
    }).join('');
    var keep=f.units.filter(function(u){return u.v===prev;})[0];
    uEl.value=keep?prev:f.units[0].v;
    hintEl.innerHTML=f.hint;
    abvWrap.style.display = fEl.value==='alcohol' ? 'block' : 'none';
    var cur=parseFloat(aEl.value);
    if(firstFill || isNaN(cur) || cur===FOOD[lastFood].def){ aEl.value=f.def; }
    firstFill=false; lastFood=fEl.value;
  }

  function calc(){
    var f=FOOD[fEl.value];
    var k=kg();
    var a=num(aEl.value);
    if(!k || !a){
      out.className='calc-result';
      out.innerHTML='Enter the weight and the amount.<small>The result appears here.</small>';
      return;
    }
    var d=amountInCanon()/k;
    var b=bandOf(f,d);
    var shown = f.canon==='mg' ? round(d,0)+' mg/kg' : (d<1?round(d,2):round(d,1))+' g/kg';

    out.className='calc-result'+(b.cls==='good'?'':' '+b.cls);
    if(fEl.value==='grapes'){
      out.innerHTML='Any amount &mdash; no safe dose<small>'+
        'That works out to '+shown+' of '+f.label+' for a '+round(k,1)+' kg dog. '+
        f.advice(d)+'</small>';
    } else {
      out.innerHTML=shown+' &mdash; '+b.t+
        '<small>'+f.advice(d)+'</small>';
    }
    note.textContent='Rule of thumb for this food: a 10 kg dog reaches the first threshold at about '+
      f.what+'. '+(fEl.value==='garlic'
        ? 'This food\u2019s g/kg figure is derived from the onion threshold, not measured.'
        : 'Estimate only \u2014 it cannot know how full the stomach was or what else was in the same mouthful.');
  }

  /* The reference table is rebuilt on every food change so the middle column
     and the right-hand column can never drift apart from each other. */
  function buildRef(){
    var f=FOOD[fEl.value];
    var rows='<tr><th>Food</th><th>Threshold in the literature</th><th>For a 10&nbsp;kg dog</th></tr>';
    Object.keys(FOOD).forEach(function(key){
      var g=FOOD[key];
      var isMe = key===fEl.value;
      rows+='<tr'+(isMe?' style="background:#fbfaf6"':'')+'><td><strong>'+g.label+'</strong>'+
        '</td><td>'+g.ref.map(function(r){return r[0]+': '+r[1];}).join('<br>')+
        '</td><td class="n">'+g.what+'</td></tr>';
    });
    refEl.innerHTML=rows;
  }

  function all(){ calc(); }

  fEl.addEventListener('change', function(){ fillUnits(); calc(); });
  ['tx-weight','tx-amount'].forEach(function(id){
    document.getElementById(id).addEventListener('input', calc);
  });
  ['tx-wunit','tx-unit','tx-abv'].forEach(function(id){
    document.getElementById(id).addEventListener('change', calc);
  });

  /* Shared links: ?food=onion&w=10&wu=kg&a=150&au=onion&abv=40 .
     Values are read straight into the selects, so a value that is not in the
     list silently leaves the default — which is why the food key is checked
     against FOOD rather than trusted. */
  try{
    var q=new URLSearchParams(location.search);
    var qf=q.get('food');
    if(qf && FOOD[qf]) fEl.value=qf;
    fillUnits();
    var qw=parseFloat(q.get('w'));
    if(!isNaN(qw) && qw>0){
      if(q.get('wu')==='lb'){ wEl.value=round(qw*2.20462,1); wuEl.value='lb'; }
      else { wEl.value=qw; wuEl.value='kg'; }
    }
    var qa=parseFloat(q.get('a'));
    if(!isNaN(qa) && qa>=0){
      aEl.value=qa;
      var qau=q.get('au');
      if(qau && FOOD[fEl.value].units.some(function(u){return u.v===qau;})) uEl.value=qau;
    }
    var qabv=q.get('abv');
    if(qabv && abvEl.querySelector('option[value="'+qabv+'"]')) abvEl.value=qabv;
  }catch(e){ fillUnits(); }

  buildRef();
  all();

  if(location.search.indexOf('embed=1')>-1){
    document.documentElement.className+=' embed';
    var rt=null;
    var report=function(){
      /* scrollHeight returns the frame's own height when the content is shorter
         than the frame, so it can only ever grow a box — and on a wide column
         the box needs to shrink. The last visible block's bottom is the height
         the frame actually needs. */
      clearTimeout(rt);
      rt=setTimeout(function(){
        try{
          var wrap=document.querySelector('.wrap.narrow')||document.body;
          parent.postMessage({wagwiseHeight: Math.ceil(wrap.getBoundingClientRect().bottom+8)}, '*');
        }catch(e){}
      },120);
    };
    window.addEventListener('load', report);
    window.addEventListener('resize', report);
    document.addEventListener('input', report);
    document.addEventListener('change', report);
    if(window.ResizeObserver) new ResizeObserver(report).observe(document.body);
    setTimeout(report, 200);
  }
})();
</script>
"""
