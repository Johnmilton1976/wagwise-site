# -*- coding: utf-8 -*-
"""Content data for WagWise Pet. Edit text here, then run render.py.

All prose is plain English, written to rank for long-tail search and to read
cleanly. Health articles carry a stronger veterinary disclaimer.
"""

SITE_NAME = "WagWise Pet"

# ---------------------------------------------------------------------------
# Pillars (hub pages). `links` lists the cluster article slugs under each.
# ---------------------------------------------------------------------------
PILLARS = {
    "dog-training": {
        "slug": "dog-training",
        "nav": "Dog Training",
        "title": "Dog Training Guides — Calm, Positive Methods",
        "url": "/dog-training/",
        "description": "Step-by-step dog and puppy training guides: crate training, leash manners, and stopping biting and pulling — all built on reward-based positive reinforcement.",
        "eyebrow": "DOG TRAINING",
        "intro": "Training is less about commands and more about teaching your dog what pays off. These guides use positive reinforcement, so your dog works with you instead of against you.",
        "links": ["how-to-crate-train-a-puppy", "how-to-stop-puppy-biting", "how-to-leash-train-a-dog"],
    },
    "dog-health": {
        "slug": "dog-health",
        "nav": "Dog Health",
        "title": "Dog Health & Symptoms — What to Watch For",
        "url": "/dog-health/",
        "description": "Common dog health symptoms explained: vomiting, ear infections, not eating, shaking, and odd behaviors like eating grass or poop — plus when to call the vet.",
        "eyebrow": "DOG HEALTH",
        "intro": "Most dog symptoms are minor and pass on their own. A few are emergencies. This section helps you tell the difference and act at the right time.",
        "links": [
            "dog-vomiting-causes", "dog-ear-infection-symptoms",
            "dog-not-eating-but-drinking-water", "why-is-my-dog-shaking",
            "why-do-dogs-eat-grass", "why-do-dogs-eat-poop",
        ],
    },
    "dog-nutrition": {
        "slug": "dog-nutrition",
        "nav": "Nutrition",
        "title": "Dog Nutrition — Feeding, Treats & Toxic Foods",
        "url": "/dog-nutrition/",
        "description": "What to feed your dog, how much, and which human foods are safe or dangerous. Covers toxic foods, safe treats, and daily feeding amounts by body weight.",
        "eyebrow": "DOG NUTRITION",
        "intro": "Good nutrition is the cheapest health insurance you can buy for a dog. Start with how much to feed, then learn which table scraps are safe and which can land you in the ER.",
        "links": [
            "foods-toxic-to-dogs", "can-dogs-eat-bananas", "how-much-to-feed-my-dog",
            "can-dogs-eat-apples", "can-dogs-eat-watermelon", "can-dogs-eat-cheese",
            "can-dogs-eat-peanut-butter", "can-dogs-eat-carrots", "can-dogs-eat-eggs",
            "can-dogs-eat-chicken", "can-dogs-eat-milk", "can-dogs-eat-strawberries",
            "can-dogs-eat-grapes", "can-dogs-eat-chocolate", "can-dogs-eat-avocado",
        ],
    },
    "dog-care": {
        "slug": "dog-care",
        "nav": "Care & Grooming",
        "title": "Dog Care & Grooming at Home",
        "url": "/dog-care/",
        "description": "Everyday dog care you can do at home: brushing teeth, trimming nails safely, bathing, and cleaning ears — all without turning it into a fight or a fuss.",
        "eyebrow": "DOG CARE",
        "intro": "A little regular handling prevents the big, expensive problems. These guides turn nail trims and tooth brushing into routines your dog tolerates.",
        "links": ["how-to-trim-dog-nails", "how-to-brush-dog-teeth"],
    },
    "cat": {
        "slug": "cat",
        "nav": "Cats",
        "title": "Cat Care Guides — Behaviour, Health & Everyday Problems",
        "url": "/cat/",
        "description": "Practical cat care guides: litter box training, furniture scratching, spraying, hairballs, and night-time meowing — with the medical causes to rule out first.",
        "eyebrow": "CAT CARE",
        "intro": "Cats are not small dogs. Their behavior usually has a reason — stress, territory, or a medical issue — and the fix starts with understanding it.",
        "links": ["cat-litter-training", "cat-scratching-furniture", "cat-spraying-how-to-stop", "cat-hairballs", "why-does-my-cat-meow-at-night"],
    },
    "best": {
        "slug": "best",
        "nav": "Reviews",
        "title": "Best Dog Products — Honest, Practical Picks",
        "url": "/best/",
        "description": "Practical, honest picks for dog crates and no-pull harnesses — chosen for safety, fit, and ease of daily use, not marketing hype or affiliate payouts.",
        "eyebrow": "REVIEWS",
        "intro": "We do not test every product on the market. These are the crates and harnesses we would buy for our own dogs, with the trade-offs spelled out.",
        "links": ["best-dog-crate", "best-dog-harness-for-pulling"],
    },
}

HEALTH_DISCLAIMER = (
    "This article is general information, not veterinary advice. If your dog is "
    "in severe distress — labored breathing, a swollen belly, collapse, or "
    "suspected poisoning — contact a veterinarian or emergency clinic right away."
)

# ---------------------------------------------------------------------------
# Articles (cluster pages). 19 seed articles across the pillars above.
# ---------------------------------------------------------------------------
ARTICLES = [
    # ---------------- Dog training ----------------
    {
        "slug": "how-to-crate-train-a-puppy",
        "pillar": "dog-training",
        "title": "How to Crate Train a Puppy — First Night Included",
        "url": "/dog-training/how-to-crate-train-a-puppy/",
        "description": "A calm, no-tears method to crate train a puppy: how long it really takes, how to make the crate inviting, and exactly what to do on the very first night.",
        "lede": "Crate training works best when the crate feels like a den, not a cage. Feed meals inside, reward calm time, and build up to a full night over one to two weeks.",
        "eyebrow": "DOG TRAINING",
        "body": """
        <h2>Why crate training helps</h2>
        <p>Dogs are den animals by instinct — a small, cozy space feels safe to them, not like punishment. A crate also speeds up house training (dogs avoid soiling their bed) and gives you a safe place to put a puppy when you cannot supervise.</p>
        <div class="callout">The goal is a dog that walks into the crate on its own. If your puppy cries the moment the door closes, you have moved too fast — back up a step.</div>

        <h2>Set up the crate right</h2>
        <ul>
          <li>Size it so your puppy can stand, turn, and lie down, but not pace. Too big and it may use a corner as a bathroom.</li>
          <li>Add a soft bed and a safe chew toy. Cover the top and three sides with a light blanket to make it den-like.</li>
          <li>Put it where the family is — a puppy alone in a far room will protest more.</li>
        </ul>

        <h2>The first week, step by step</h2>
        <p>Day 1-2: toss treats inside, let the puppy go in and out freely, no door closing. Day 3-4: close the door for 30 seconds while you stand next to it, then open. Day 5-7: build to 10-15 minutes with you in the room. Week 2: try leaving the room briefly, then a full nap, then the first night.</p>

        <h2>The first night</h2>
        <p>Bring the crate beside your bed for the first few nights. A puppy that can hear and smell you settles far faster. A potty trip at 3 a.m. is normal for an 8-10 week old — carry it out, no play, straight back in.</p>

        <h2>Common mistakes</h2>
        <ul>
          <li>Using the crate as time-out — it should mean safety, never punishment.</li>
          <li>Reacting to whining by letting the puppy out every time, which trains it to cry for freedom.</li>
          <li>Rushing the timeline and expecting a full night on day one.</li>
        </ul>
        """,
        "faq": [
            ("How long does it take to crate train a puppy?", "Most puppies accept the crate within a week and sleep through the night within two to three weeks. An older rescue dog can take longer if it has negative associations to confine."),
            ("Should I cover the crate at night?", "Covering the top and sides helps many dogs feel secure, but leave the door area open for airflow. Stop covering if your dog gets anxious or overheats."),
            ("Is it cruel to crate a dog?", "No — when introduced positively and not overused. A crate should be a voluntary safe space, not a place a dog is locked for eight hours a day."),
        ],
        "related": ["how-to-stop-puppy-biting", "how-to-leash-train-a-dog", "why-do-dogs-eat-poop"],
        "sources": [
            ("ASPCA — Common Dog Behavior Issues",
             "https://www.aspca.org/pet-care/dog-care/common-dog-behavior-issues"),
            ("American Veterinary Society of Animal Behavior — Position Statements",
             "https://avsab.org/resources/position-statements/"),
            ("Merck Veterinary Manual — Behavior of Dogs",
             "https://www.merckvetmanual.com/dog-owners/behavior-of-dogs"),
        ],
        "disclaimer": "Training advice only. If crate avoidance comes with fear, drooling, or panic, consult a positive-reinforcement trainer or veterinary behaviorist.",
    },
    {
        "slug": "how-to-stop-puppy-biting",
        "pillar": "dog-training",
        "title": "How to Stop Puppy Biting — Without Yelling",
        "url": "/dog-training/how-to-stop-puppy-biting/",
        "description": "Puppy biting and nipping is normal teething behavior, not aggression. How to redirect it, teach bite inhibition, and when the phase should finally end.",
        "lede": "Puppy biting is not aggression — it is teething and play. The fix is to redirect to a toy, reward gentle mouths, and make a brief withdrawal when teeth touch skin.",
        "eyebrow": "DOG TRAINING",
        "body": """
        <h2>Why puppies bite</h2>
        <p>Puppies explore with their mouths and bite harder than they mean to because they have not learned bite inhibition yet. Littermates teach this by yelping; you can teach it too.</p>

        <h2>The redirect-and-reward method</h2>
        <ul>
          <li>When teeth touch skin, say a calm \"ouch\" or just go silent, and offer a toy instead.</li>
          <li>If the puppy takes the toy, praise. If it keeps biting, stand up and turn away for 20-30 seconds — attention is the reward it wants.</li>
          <li>Keep a toy within reach so redirection is instant, not a search mission.</li>
        </ul>
        <div class="callout warn">Do not hit, hold the muzzle, or shout. Those can make a fearless puppy bite harder or a soft one become hand-shy.</div>

        <h2>Extra help for teething</h2>
        <p>Cold chew toys from the freezer soothe sore gums. Rotate toys so they stay interesting. A tired puppy bites less — short training games burn energy.</p>

        <h2>When should it stop?</h2>
        <p>Biting should fade by 5-6 months as adult teeth come in and bite inhibition sets. Persistent hard biting past that, or any skin break with a growl, is worth a trainer's eyes.</p>
        """,
        "faq": [
            ("At what age do puppies stop biting?", "Most puppies stop hard mouthing by 5 to 6 months, once adult teeth are in and bite inhibition is learned. Soft play-mouthing may linger longer."),
            ("Why does my puppy bite my ankles when I walk?", "It is herding and chase instinct plus boredom. Stop moving, redirect to a toy, and give more exercise and mental games."),
            ("Should I use a bitter spray?", "It can help as a backup, but the core fix is redirection and withdrawal of attention. Sprays alone rarely solve the habit."),
        ],
        "related": ["how-to-crate-train-a-puppy", "how-to-leash-train-a-dog", "dog-not-eating-but-drinking-water"],
        "sources": [
            ("American Veterinary Society of Animal Behavior — Position Statements",
             "https://avsab.org/resources/position-statements/"),
            ("ASPCA — Common Dog Behavior Issues",
             "https://www.aspca.org/pet-care/dog-care/common-dog-behavior-issues"),
            ("Merck Veterinary Manual — Behavior of Dogs",
             "https://www.merckvetmanual.com/dog-owners/behavior-of-dogs"),
        ],
        "disclaimer": "Behavior guidance only. A puppy that breaks skin, growls, or snaps from a calm state should be assessed by a qualified trainer.",
    },
    {
        "slug": "how-to-leash-train-a-dog",
        "pillar": "dog-training",
        "title": "How to Leash Train a Dog That Pulls",
        "url": "/dog-training/how-to-leash-train-a-dog/",
        "description": "Stop leash pulling with the stop-and-go method and a front-clip harness. A step-by-step plan for calm walks in a week, not a daily walk-time struggle.",
        "lede": "Dogs pull because pulling works — it gets them where they want to go. The fix is simple: the walk only continues when the leash is slack.",
        "eyebrow": "DOG TRAINING",
        "body": """
        <h2>Why dogs pull</h2>
        <p>To a dog, forward motion is the reward. The instant it leans into the leash and moves ahead, pulling paid off. We have to make slack, not tension, the thing that earns progress.</p>

        <h2>The stop-and-go method</h2>
        <ul>
          <li>The moment the leash goes tight, stop walking. Plant your feet.</li>
          <li>Wait until your dog looks back or the leash loosens, then praise and move on.</li>
          <li>Repeat. A 10-minute walk may take 30 at first — that is normal and it improves fast.</li>
        </ul>
        <div class="callout">Use a front-clip harness, not a choke or prong collar. Front-clip harnesses turn the dog toward you when it pulls, which is kinder and works.</div>

        <h2>Avoid the common trap</h2>
        <p>Do not keep walking while correcting — if you move forward as you pull the dog back, you have rewarded the pull. Stillness is the teacher.</p>

        <h2>Practice in low-distraction spots</h2>
        <p>Start in the living room, then the yard, then quiet streets, before busy parks. Adding distractions before the skill is solid sets everyone up to fail.</p>
        """,
        "faq": [
            ("What is the best leash for a dog that pulls?", "A front-clip harness paired with a standard 4-6 foot leash. Retractable leashes teach pulling and are best avoided for training."),
            ("How long until pulling stops?", "With consistent stop-and-go, most dogs walk loosely within one to two weeks. Excitable dogs take longer and need more reps."),
            ("Should I use a choke chain?", "No. Choke and prong collars can damage the trachea and neck and increase fear. A front-clip harness is safer and effective."),
        ],
        "related": ["best-dog-harness-for-pulling", "how-to-stop-puppy-biting", "dog-vomiting-causes"],
        "sources": [
            ("ASPCA — Common Dog Behavior Issues",
             "https://www.aspca.org/pet-care/dog-care/common-dog-behavior-issues"),
            ("American Veterinary Society of Animal Behavior — Position Statements",
             "https://avsab.org/resources/position-statements/"),
            ("Merck Veterinary Manual — Behavior of Dogs",
             "https://www.merckvetmanual.com/dog-owners/behavior-of-dogs"),
        ],
        "disclaimer": "Training guidance only. A sudden pulling change with coughing or gagging should be checked by a vet.",
    },

    # ---------------- Dog health ----------------
    {
        "slug": "dog-vomiting-causes",
        "pillar": "dog-health",
        "title": "Dog Vomiting Causes — What's Normal and What's Urgent",
        "url": "/dog-health/dog-vomiting-causes/",
        "description": "Why dogs throw up, when a single vomit is no big deal, the red-flag symptoms that mean a vet visit right now, and how to tell upset from something serious.",
        "lede": "A dog that vomits once, then acts normal, is usually fine. Vomiting paired with lethargy, repeated episodes, or a swollen belly is a different story.",
        "eyebrow": "DOG HEALTH",
        "body": """
        <h2>Common, usually mild causes</h2>
        <ul>
          <li>Eating too fast or too much.</li>
          <li>Grass, a new treat, or table scraps that disagreed.</li>
          <li>Car sickness or anxiety.</li>
        </ul>
        <p>One vomit followed by a normal appetite and energy rarely needs a clinic.</p>

        <h2>When to watch at home</h2>
        <p>Withhold food for a few hours, offer small sips of water, then a bland meal (boiled chicken and rice). If it stays down, resume normal food over a day or two.</p>
        <div class="callout warn">Red flags: vomiting many times in a day, blood, a tight swollen belly, weakness, or suspected poisoning (chocolate, grapes, xylitol). These can be emergencies — call a vet.</div>

        <h2>Vomiting vs regurgitation</h2>
        <p>Regurgitation is passive, undigested food right after eating, often from eating too fast. True vomiting is forceful and comes from the stomach. The difference helps your vet.</p>

        <h2>Prevention</h2>
        <p>Slow feeders curb fast eating. Keep trash and toxic foods out of reach. Routine vet checks catch chronic causes like allergies or reflux.</p>
        """,
        "faq": [
            ("Should I feed my dog after vomiting?", "Withhold food for 4-6 hours, then offer a small bland meal like boiled chicken and rice. If vomiting returns, call your vet."),
            ("When is dog vomiting an emergency?", "Repeated vomiting, blood, a swollen hard belly, collapse, or known toxin ingestion needs urgent veterinary care."),
            ("Why does my dog eat grass then throw up?", "Many dogs eat grass out of boredom or an upset stomach. Occasional grass vomiting is common and usually harmless, but frequent episodes deserve a check."),
        ],
        "related": ["dog-not-eating-but-drinking-water", "why-do-dogs-eat-grass", "foods-toxic-to-dogs"],
        "sources": [
            ("Merck Veterinary Manual — Vomiting in Dogs",
             "https://www.merckvetmanual.com/dog-owners/digestive-disorders-of-dogs/vomiting-in-dogs"),
            ("ASPCA — Dog Care",
             "https://www.aspca.org/pet-care/dog-care"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": HEALTH_DISCLAIMER,
    },
    {
        "slug": "dog-ear-infection-symptoms",
        "pillar": "dog-health",
        "title": "Dog Ear Infection Symptoms and Home Care",
        "url": "/dog-health/dog-ear-infection-symptoms/",
        "description": "How to spot a dog ear infection — head shaking, odor, redness, discharge — plus what safe home cleaning looks like and when a vet really needs to see it.",
        "lede": "The classic signs are head shaking, scratching at the ear, a sour smell, and red or waxy canals. Most infections need prescription drops, not just cleaning.",
        "eyebrow": "DOG HEALTH",
        "body": """
        <h2>Symptoms to spot</h2>
        <ul>
          <li>Frequent head shaking or tilting.</li>
          <li>Pawing or scratching at the ear.</li>
          <li>Redness, swelling, or brown waxy discharge.</li>
          <li>A strong, yeasty odor.</li>
        </ul>

        <h2>Why ears get infected</h2>
        <p>Floppy ears, moisture after swimming, and allergies are the big drivers. Yeast and bacteria both cause it, which is why the treatment differs.</p>
        <div class="callout">Do not pour oil, vinegar, or alcohol into the ear — and never if your dog is in pain or the eardrum may be damaged. A vet confirms the type and gives the right drops.</div>

        <h2>Cleaning at home</h2>
        <p>Use only a vet-approved ear cleaner: fill the canal, massage the base, let the dog shake, then wipe the outer ear. Never push cotton swabs deep.</p>

        <h2>Preventing repeat infections</h2>
        <p>Dry ears after baths and swimming, manage underlying allergies, and clean on a schedule your vet recommends rather than when it already smells.</p>
        """,
        "faq": [
            ("Can I treat a dog ear infection at home?", "Mild cases need vet-prescribed drops after confirming yeast vs bacteria. Home cleaning alone rarely clears an established infection."),
            ("What does an infected dog ear smell like?", "A sour, yeasty, or musty odor is the tell-tale sign, usually with wax and redness."),
            ("How do I clean my dog's ears safely?", "Use a vet-approved cleaner, fill and massage the canal, let them shake, wipe the outside. Never insert swabs deep into the ear."),
        ],
        "related": ["how-to-trim-dog-nails", "dog-not-eating-but-drinking-water", "foods-toxic-to-dogs"],
        "sources": [
            ("Merck Veterinary Manual — Ear Disorders of Dogs",
             "https://www.merckvetmanual.com/dog-owners/ear-disorders-of-dogs"),
            ("ASPCA — Dog Care",
             "https://www.aspca.org/pet-care/dog-care"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": HEALTH_DISCLAIMER,
    },
    {
        "slug": "dog-not-eating-but-drinking-water",
        "pillar": "dog-health",
        "title": "Dog Not Eating but Drinking Water — Should You Worry?",
        "url": "/dog-health/dog-not-eating-but-drinking-water/",
        "description": "Why a dog may stop eating but keep drinking water — from mild causes like stress to serious illness — and when not eating becomes a true medical emergency.",
        "lede": "A dog that drinks but refuses food for a day is often just under the weather. Skipping food for more than two days, or any lethargy with it, needs a vet.",
        "eyebrow": "DOG HEALTH",
        "body": """
        <h2>Benign reasons</h2>
        <ul>
          <li>Heat, a missed walk, or a change in routine.</li>
          <li>A new food they dislike.</li>
          <li>Mild stomach upset that passes.</li>
        </ul>

        <h2>When drinking-but-not-eating is concerning</h2>
        <p>If your dog drinks a lot of water yet eats nothing for over 48 hours, or seems tired, vomits, or loses weight, underlying issues like dental pain, infection, kidney trouble, or diabetes may be involved.</p>
        <div class="callout warn">A dog that stops eating entirely for more than two days — or a puppy that skips two meals — should see a vet. Puppies dehydrate fast.</div>

        <h2>What you can do</h2>
        <p>Warm the food, offer a bland meal, and check the mouth for broken teeth or sores. Track water intake; sudden gulping is a symptom worth noting.</p>

        <h2>Bottom line</h2>
        <p>One quiet day is fine. Persistent refusal, especially with thirst and low energy, is your signal to call the clinic.</p>
        """,
        "faq": [
            ("How long can a dog go without eating?", "A healthy adult can miss a day or two, but more than 48 hours — or any refusal in a puppy — warrants a vet visit."),
            ("Why is my dog drinking more but not eating?", "Increased thirst with appetite loss can point to infection, kidney issues, or diabetes. Note the pattern and get it checked if it lasts."),
            ("Should I force-feed my dog?", "No. Forcing food stresses a sick dog. Offer bland food; if they refuse for two days, let a vet diagnose the cause."),
        ],
        "related": ["dog-vomiting-causes", "how-much-to-feed-my-dog", "dog-not-eating-but-drinking-water"],
        "sources": [
            ("Merck Veterinary Manual — Digestive Disorders of Dogs",
             "https://www.merckvetmanual.com/dog-owners/digestive-disorders-of-dogs"),
            ("ASPCA — Dog Care",
             "https://www.aspca.org/pet-care/dog-care"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": HEALTH_DISCLAIMER,
    },
    {
        "slug": "why-is-my-dog-shaking",
        "pillar": "dog-health",
        "title": "Why Is My Dog Shaking? 8 Common Reasons",
        "url": "/dog-health/why-is-my-dog-shaking/",
        "description": "Dogs shake for many reasons — cold, stress, excitement, pain, nausea, or illness. How to tell harmless shivers from symptoms that need a vet's attention.",
        "lede": "Shaking can be as simple as being cold or as serious as pain or poisoning. The context — other symptoms, body temperature, behavior — tells you which.",
        "eyebrow": "DOG HEALTH",
        "body": """
        <h2>Harmless causes</h2>
        <ul>
          <li>Cold — small and short-haired dogs shiver to warm up.</li>
          <li>Excitement or anticipation (the zoomie shake before a walk).</li>
          <li>Stress or anxiety, including thunderstorms.</li>
        </ul>

        <h2>Medical causes to know</h2>
        <p>Pain, fever, nausea, low blood sugar (common in tiny breeds), and toxins like chocolate or xylitol can all cause trembling. So can old-age weakness.</p>
        <div class="callout warn">Sudden shaking with weakness, collapse, vomiting, or known toxin exposure is an emergency — call a vet now.</div>

        <h2>How to assess</h2>
        <ul>
          <li>Is your dog warm and calm? Probably benign.</li>
          <li>Shaking plus lethargy, panting, or hiding? Likely pain or illness.</li>
          <li>Shaking plus a known toxin? Treat as urgent.</li>
        </ul>

        <h2>What to do</h2>
        <p>Warm a cold dog, soothe an anxious one, and watch. If shaking persists without an obvious cause or comes with other symptoms, a vet visit is the safe call.</p>
        """,
        "faq": [
            ("Why is my dog shaking but acting normal?", "Excitement, mild cold, or stress can cause shivering with normal behavior. If it passes quickly, it is usually nothing."),
            ("When is dog shaking an emergency?", "Shaking with weakness, collapse, vomiting, or possible toxin ingestion needs immediate veterinary care."),
            ("Why does my small dog shake so much?", "Tiny breeds lose body heat fast and are prone to low blood sugar shakes. A sweater and regular meals often help."),
        ],
        "related": ["dog-not-eating-but-drinking-water", "why-do-dogs-eat-poop", "dog-vomiting-causes"],
        "sources": [
            ("AKC — Why Is My Dog Shaking?",
             "https://www.akc.org/expert-advice/health/why-is-my-dog-shaking/"),
            ("Merck Veterinary Manual — Dog Owners",
             "https://www.merckvetmanual.com/dog-owners"),
            ("ASPCA — Dog Care",
             "https://www.aspca.org/pet-care/dog-care"),
        ],
        "disclaimer": HEALTH_DISCLAIMER,
    },
    {
        "slug": "why-do-dogs-eat-grass",
        "pillar": "dog-health",
        "title": "Why Do Dogs Eat Grass? (And When to Stop Them)",
        "url": "/dog-health/why-do-dogs-eat-grass/",
        "description": "Dogs eat grass out of boredom, an upset stomach, or simply because it tastes good. Usually harmless — but frequent vomiting after eating grass needs a vet.",
        "lede": "Most dogs eat grass now and then and are perfectly fine. It is often boredom or instinct — not a sign your dog is sick.",
        "eyebrow": "DOG HEALTH",
        "body": """
        <h2>The main reasons</h2>
        <ul>
          <li>Boredom or habit — grass is just there.</li>
          <li>An upset stomach; some dogs self-soothe by grazing.</li>
          <li>A missing nutrient is rarely the cause in well-fed dogs.</li>
        </ul>

        <h2>Is it safe?</h2>
        <p>Plain grass is fine. The risk is what is on it — pesticides, fertilizers, and parasites from other animals' waste. Avoid treated lawns.</p>
        <div class="callout">If grass-eating comes with repeated vomiting, diarrhea, or appetite loss, it is worth a vet check rather than blaming the grass.</div>

        <h2>How to cut it down</h2>
        <p>More exercise and chew toys fix the bored grazers. A balanced diet and slow feeding help the tummy-grazers. Supervise yard time if it is a daily habit.</p>

        <h2>When to worry</h2>
        <p>Occasional grazing is normal. Daily, frantic eating with sickness is not — that pattern deserves a vet's eyes.</p>
        """,
        "faq": [
            ("Do dogs eat grass to make themselves throw up?", "Sometimes, but many grass-eaters never vomit. It is more often boredom or taste than a deliberate attempt to purge."),
            ("Is eating grass bad for dogs?", "Plain, untreated grass is safe. Avoid lawns with pesticides or fertilizer, which are the real hazard."),
            ("How do I stop my dog eating grass?", "Rule out illness first, then add exercise, toys, and mental games. Supervise and redirect during yard time."),
        ],
        "related": ["dog-vomiting-causes", "why-do-dogs-eat-poop", "foods-toxic-to-dogs"],
        "sources": [
            ("Merck Veterinary Manual — Behavior of Dogs",
             "https://www.merckvetmanual.com/dog-owners/behavior-of-dogs"),
            ("ASPCA — Dog Care",
             "https://www.aspca.org/pet-care/dog-care"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": HEALTH_DISCLAIMER,
    },
    {
        "slug": "why-do-dogs-eat-poop",
        "pillar": "dog-health",
        "title": "Why Do Dogs Eat Poop (Coprophagia) and How to Stop It",
        "url": "/dog-health/why-do-dogs-eat-poop/",
        "description": "Coprophagia is common and usually behavioral rather than a sign of illness. The real causes — boredom, mimicry, diet — and practical ways to stop it for good.",
        "lede": "Eating poop is gross but common, especially in puppies. It is usually behavioral — boredom, exploration, or copying the mother — and rarely a medical emergency.",
        "eyebrow": "DOG HEALTH",
        "body": """
        <h2>Why dogs do it</h2>
        <ul>
          <li>Puppies explore with their mouths and often outgrow it.</li>
          <li>Boredom or attention-seeking in under-stimulated dogs.</li>
          <li>Mimicry of a mother dog cleaning the den.</li>
          <li>Rarely, a diet lacking nutrients or a malabsorption issue.</li>
        </ul>

        <h2>Health check first</h2>
        <p>If it starts suddenly in an adult dog, a vet can rule out parasites or digestive problems. Most cases, though, are behavioral.</p>
        <div class="callout">Clean up promptly — the single most effective step. A yard with no accessible stool removes the opportunity entirely.</div>

        <h2>Practical fixes</h2>
        <ul>
          <li>Pick up stool immediately, every time.</li>
          <li>Teach \"leave it\" and reward for ignoring it.</li>
          <li>Add exercise and puzzle toys to cut boredom.</li>
          <li>Some owners use a taste-aversion supplement after a vet's okay.</li>
        </ul>
        """,
        "faq": [
            ("Is eating poop dangerous for dogs?", "It is usually not toxic, but it can spread parasites and stomach bugs. Prompt cleanup and deworming on schedule reduce the risk."),
            ("Will my puppy grow out of eating poop?", "Most puppies outgrow coprophagia by a year old once they are better stimulated and the habit is not reinforced."),
            ("What supplement stops dogs eating poop?", "Taste-aversion products exist; ask your vet first. The reliable fix is cleanup plus training, not a pill alone."),
        ],
        "related": ["why-do-dogs-eat-grass", "how-to-stop-puppy-biting", "foods-toxic-to-dogs"],
        "sources": [
            ("Merck Veterinary Manual — Behavior of Dogs",
             "https://www.merckvetmanual.com/dog-owners/behavior-of-dogs"),
            ("ASPCA — Dog Care",
             "https://www.aspca.org/pet-care/dog-care"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": HEALTH_DISCLAIMER,
    },

    # ---------------- Dog nutrition ----------------
    {
        "slug": "foods-toxic-to-dogs",
        "pillar": "dog-nutrition",
        "title": "Foods Toxic to Dogs — The List Every Owner Needs",
        "url": "/dog-nutrition/foods-toxic-to-dogs/",
        "description": "The human foods that can poison a dog — chocolate, grapes, onions, garlic, xylitol, alcohol — and the emergency steps to take if your dog eats any of them.",
        "lede": "The most dangerous are chocolate, grapes and raisins, onions and garlic, xylitol (in sugar-free gum), and alcohol. Even small amounts can be serious for a small dog.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>The big ones to never feed</h2>
        <ul>
          <li><strong>Chocolate</strong> — the darker it is, the worse. Causes heart rhythm problems.</li>
          <li><strong>Grapes and raisins</strong> — can trigger sudden kidney failure, even a few.</li>
          <li><strong>Onions and garlic</strong> — damage red blood cells; toxic in quantity.</li>
          <li><strong>Xylitol</strong> — sugar-free gum and peanut butter; causes crashing blood sugar and liver injury.</li>
          <li><strong>Alcohol and raw dough</strong> — even small amounts are dangerous.</li>
        </ul>
        <div class="callout warn">If your dog eats chocolate, grapes, xylitol, or anything on this list, call a vet or poison line right away. Do not wait for symptoms.</div>

        <h2>Usually fine in small amounts</h2>
        <p>Plain cooked chicken, rice, carrots, and apples (no seeds) are safe treats. The danger list above is the one to memorize.</p>

        <h2>What to do in an emergency</h2>
        <ul>
          <li>Note what and how much was eaten, and your dog's weight.</li>
          <li>Call your vet or an animal poison hotline with those details.</li>
          <li>Do not induce vomiting unless a professional tells you to.</li>
        </ul>
        """,
        "faq": [
            ("How much chocolate is toxic to a dog?", "It depends on the dog's size and the chocolate type. Dark chocolate is far more toxic than milk. Any amount in a small dog should prompt a vet call."),
            ("Are grapes really that dangerous?", "Yes — even a handful of grapes or raisins can cause acute kidney failure in some dogs. Treat any ingestion as serious."),
            ("Is xylitol in peanut butter? ", "Some brands use xylitol. Always read the label; choose a plain peanut butter with no xylitol for dog treats."),
        ],
        "related": ["can-dogs-eat-bananas", "how-much-to-feed-my-dog", "why-do-dogs-eat-poop"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": HEALTH_DISCLAIMER,
    },
    {
        "slug": "can-dogs-eat-bananas",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Bananas? Yes — in Moderation",
        "url": "/dog-nutrition/can-dogs-eat-bananas/",
        "description": "Bananas are safe for dogs as an occasional treat. How much to give, why the peel should always go in the bin, and why sugar and calories add up quickly.",
        "lede": "Yes, bananas are safe for dogs in small amounts. They are a healthy treat, but their sugar and fiber mean they should stay an occasional snack, not a daily staple.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Are bananas good for dogs?</h2>
        <p>Bananas offer potassium, vitamin B6, and fiber. They make a fine low-fat treat, especially for dogs that love fruit.</p>

        <h2>How much is safe</h2>
        <ul>
          <li>Small dogs: a few thin slices.</li>
          <li>Large dogs: up to half a banana, occasionally.</li>
          <li>Treats of any kind should be under 10% of daily calories.</li>
        </ul>
        <div class="callout">Skip the peel — it is hard to digest and can cause a blockage. And go easy on banana-based products with added sugar.</div>

        <h2>Ways to serve</h2>
        <p>Fresh slices, mashed into food, or frozen for a cooling chew on hot days. Mash and stuff into a toy for a slow treat.</p>

        <h2>When to skip</h2>
        <p>Diabetic dogs or those on a strict weight plan should avoid the extra sugar. Too much banana can also loosen stools because of the fiber.</p>
        """,
        "faq": [
            ("Can dogs eat banana peels?", "No — peels are tough to digest and can cause blockages. Stick to the fruit and discard the peel."),
            ("How much banana can a dog have?", "A few slices for small dogs, up to half a banana for large dogs, and only as an occasional treat."),
            ("Are bananas bad for dogs with diarrhea?", "Bananas' fiber can either help or loosen stools. For an upset belly, plain boiled chicken and rice is the safer first choice."),
        ],
        "related": ["foods-toxic-to-dogs", "how-much-to-feed-my-dog", "dog-vomiting-causes"],
        "sources": [
            ("AKC — Can Dogs Eat Bananas?",
             "https://www.akc.org/expert-advice/nutrition/can-dogs-eat-bananas/"),
            ("AKC — Fruits and Vegetables Dogs Can and Can't Eat",
             "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "how-much-to-feed-my-dog",
        "pillar": "dog-nutrition",
        "title": "How Much Should I Feed My Dog? (By Weight and Age)",
        "url": "/dog-nutrition/how-much-to-feed-my-dog/",
        "description": "A practical feeding guide: daily amounts by body weight, how often to feed puppies versus adults, and the body condition signs that show the portion is right.",
        "lede": "Start from your dog's target weight and the food's calorie label, then adjust by body condition — you should feel ribs but not see them.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Begin with the label, then adjust</h2>
        <p>Every bag has a feeding chart by weight. Use it as a starting point, not gospel — activity, age, and metabolism change the real need.</p>

        <h2>How often to feed</h2>
        <ul>
          <li>Puppies under 4 months: 3-4 small meals a day.</li>
          <li>Puppies 4-12 months: 2-3 meals.</li>
          <li>Adults: 2 meals a day is ideal for most.</li>
        </ul>

        <h2>The body-condition check</h2>
        <div class="callout good">You should be able to feel your dog's ribs with light pressure but not see them. From above, there should be a visible waist. No waist = too much food; visible ribs = too little.</div>

        <h2>Signs to adjust</h2>
        <ul>
          <li>Gaining or losing: shift portions by about 10% and re-check in two weeks.</li>
          <li>Always measure with a cup — \"a handful\" drifts fast.</li>
          <li>Count treats in the daily budget; they add up quietly.</li>
        </ul>
        """,
        "faq": [
            ("How many cups of food per day for a dog?", "It varies by food calorie density and dog size — follow the bag's chart by weight, then adjust by body condition."),
            ("How often should I feed my puppy?", "Three to four meals a day under four months, dropping to two by adulthood."),
            ("How do I know if I feed too much?", "Loss of a visible waist and difficulty feeling ribs means too much. Reduce portions about 10% and recheck in two weeks."),
        ],
        "related": ["foods-toxic-to-dogs", "can-dogs-eat-bananas", "dog-not-eating-but-drinking-water"],
        "sources": [
            ("Merck Veterinary Manual — Routine Health Care of Dogs",
             "https://www.merckvetmanual.com/dog-owners/routine-care-of-dogs/routine-health-care-of-dogs"),
            ("ASPCA — Dog Care",
             "https://www.aspca.org/pet-care/dog-care"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "General feeding guidance. Dogs with medical conditions need a vet-tailored plan.",
    },

    # ---------------- Dog care & grooming ----------------
    {
        "slug": "how-to-trim-dog-nails",
        "pillar": "dog-care",
        "title": "How to Trim Dog Nails Without the Struggle",
        "url": "/dog-care/how-to-trim-dog-nails/",
        "description": "A calm, step-by-step method to trim your dog's nails at home, how short is actually safe, what to do if you cut the quick, and how often to trim each nail.",
        "lede": "Trim small amounts frequently and you avoid the quick — the sensitive vein inside the nail. A scratchboard or grinder also works if clippers scare your dog.",
        "eyebrow": "DOG CARE",
        "body": """
        <h2>How short is safe</h2>
        <p>Cut only the white tip, well clear of the pink quick (or the dark center you can see in light nails). In dark nails, take tiny slivers and stop when you see a dark dot in the center.</p>

        <h2>Make it calm</h2>
        <ul>
          <li>Touch and hold paws daily so handling is normal, not a surprise.</li>
          <li>Use sharp clippers or a grinder; dull tools crush and hurt.</li>
          <li>Reward after every nail, not just at the end.</li>
        </ul>
        <div class="callout warn">If you nick the quick, it bleeds and stings. Press styptic powder or cornstarch on it; the dog is fine in a minute. Do not panic — that teaches fear.</div>

        <h2>Alternatives</h2>
        <p>A scratchboard (let the dog file its own nails on sandpaper) or a grinder avoids the clipper entirely and is gentler for many dogs.</p>

        <h2>How often</h2>
        <p>Every two to three weeks keeps quicks short. Long nails push the quick out, so regular tiny trims are better than infrequent big ones.</p>
        """,
        "faq": [
            ("How often should I trim my dog's nails?", "Every two to three weeks. Regular short trims keep the quick receded and make each session easier."),
            ("What if I cut the quick?", "Apply styptic powder or cornstarch to stop bleeding. It looks worse than it is; stay calm so your dog stays calm."),
            ("My dog hates nail clippers — what then?", "Try a grinder or a scratchboard so the dog files its own nails. Pair any method with treats until it is routine."),
        ],
        "related": ["how-to-brush-dog-teeth", "dog-ear-infection-symptoms", "how-to-leash-train-a-dog"],
        "sources": [
            ("AKC — The Dos and Don'ts of Home Dog Grooming and Hygiene",
             "https://www.akc.org/expert-advice/health/dog-grooming-at-home"),
            ("Merck Veterinary Manual — Routine Care of Dogs",
             "https://www.merckvetmanual.com/dog-owners/routine-care-of-dogs"),
            ("ASPCA — Dog Care",
             "https://www.aspca.org/pet-care/dog-care"),
        ],
        "disclaimer": "Grooming guidance only. Heavy bleeding or lameness after a trim should be checked by a vet.",
    },
    {
        "slug": "how-to-brush-dog-teeth",
        "pillar": "dog-care",
        "title": "How to Brush Your Dog's Teeth (And Why It Matters)",
        "url": "/dog-care/how-to-brush-dog-teeth/",
        "description": "Brushing a dog's teeth prevents gum disease, the most common problem in adult dogs. A simple routine, how often to do it, and which toothpaste is safe.",
        "lede": "Most adult dogs have some gum disease by age three. Two minutes of brushing most days prevents the pain, tooth loss, and cost that follow.",
        "eyebrow": "DOG CARE",
        "body": """
        <h2>Why it matters</h2>
        <p>Plaque hardens into tartar within days. Under it, gums inflame and teeth loosen. Daily brushing is the only home step that reliably prevents it.</p>

        <h2>The routine</h2>
        <ul>
          <li>Use dog toothpaste only — human paste foams and can upset the stomach.</li>
          <li>Let your dog lick the paste first so the brush is no surprise.</li>
          <li>Lift the lip and brush the outer surfaces in small circles; most dogs never need the inside.</li>
        </ul>
        <div class="callout">Start by just touching the teeth with a finger, then a finger brush, then a soft brush. Build over a week so it stays calm, not a wrestle.</div>

        <h2>If brushing is impossible</h2>
        <p>Dental chews, prescription diets, and water additives help but do not replace brushing. Professional cleanings under anesthesia handle established tartar.</p>

        <h2>How often</h2>
        <p>Ideally daily; even three times a week cuts disease risk sharply versus never.</p>
        """,
        "faq": [
            ("Can I use human toothpaste on my dog?", "No — use dog toothpaste. Human paste foams and can upset a dog's stomach if swallowed."),
            ("How often should I brush my dog's teeth?", "Daily is best; three times a week still helps a lot versus not brushing at all."),
            ("What if my dog won't let me brush?", "Ease in over a week with a finger and dog paste, then a soft brush. Dental chews are a partial backup."),
        ],
        "related": ["how-to-trim-dog-nails", "dog-ear-infection-symptoms", "dog-not-eating-but-drinking-water"],
        "sources": [
            ("AKC — The Dos and Don'ts of Home Dog Grooming and Hygiene",
             "https://www.akc.org/expert-advice/health/dog-grooming-at-home"),
            ("Merck Veterinary Manual — Routine Health Care of Dogs",
             "https://www.merckvetmanual.com/dog-owners/routine-care-of-dogs/routine-health-care-of-dogs"),
            ("ASPCA — Dog Care",
             "https://www.aspca.org/pet-care/dog-care"),
        ],
        "disclaimer": "Dental care guidance only. Bad breath with red gums may indicate disease needing a professional cleaning.",
    },

    # ---------------- Cat care ----------------
    {
        "slug": "cat-litter-training",
        "pillar": "cat",
        "title": "Cat Litter Training — Faster Than You Think",
        "url": "/cat/cat-litter-training/",
        "description": "Most cats litter train themselves. How to set up the box right, where to place it, and how to fix the few things that cause accidents outside the box.",
        "lede": "Cats are naturally clean and most use a litter box with almost no teaching. The work is in the setup: the right box, the right litter, and a good location.",
        "eyebrow": "CAT CARE",
        "body": """
        <h2>Set up for success</h2>
        <ul>
          <li>One box per cat, plus one extra, in quiet, accessible spots.</li>
          <li>Unscented clumping litter suits most cats; avoid strong perfumes.</li>
          <li>Keep it away from food and water.</li>
        </ul>

        <h2>Teaching a kitten or new cat</h2>
        <p>Place the cat in the box after meals and naps. If it goes elsewhere once, move that waste into the box so the scent guides it. Praise, never punish.</p>
        <div class="callout warn">Suddenly avoiding the litter box usually means a medical issue (a UTI is common) or stress. Rule out pain before assuming bad behavior.</div>

        <h2>Stopping accidents</h2>
        <ul>
          <li>Scoop daily; cats reject a dirty box.</li>
          <li>Keep the box where the cat already goes, then move it gradually.</li>
          <li>Clean accidents with an enzyme cleaner so the smell does not draw them back.</li>
        </ul>
        """,
        "faq": [
            ("How long does it take to litter train a cat?", "Most cats and kittens learn within days with a well-placed, clean box — they are naturally inclined to bury waste."),
            ("Why is my cat pooping outside the litter box?", "Usually a dirty box, a location it dislikes, or a medical issue like a UTI. Clean the box and rule out pain first."),
            ("How many litter boxes do I need?", "One per cat plus one extra. So two cats do best with three boxes in different spots."),
        ],
        "related": ["cat-spraying-how-to-stop", "cat-scratching-furniture", "dog-not-eating-but-drinking-water"],
        "sources": [
            ("Cornell Feline Health Center",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center"),
            ("ASPCA — Cat Care",
             "https://www.aspca.org/pet-care/cat-care"),
            ("International Cat Care — Advice",
             "https://icatcare.org/advice/"),
        ],
        "disclaimer": "Cat care guidance only. Sudden litter box avoidance warrants a vet check for urinary issues.",
    },
    {
        "slug": "cat-scratching-furniture",
        "pillar": "cat",
        "title": "How to Stop a Cat Scratching Furniture",
        "url": "/cat/cat-scratching-furniture/",
        "description": "Cats scratch to mark territory and shed old claw sheaths — not to ruin your sofa. How to redirect them to posts and make your furniture less appealing.",
        "lede": "Scratching is normal cat behavior you cannot train away — but you can redirect it. Give appealing posts and make the furniture boring.",
        "eyebrow": "CAT CARE",
        "body": """
        <h2>Why cats scratch</h2>
        <p>It marks territory (visually and with scent), stretches muscles, and removes old claw sheaths. Declawing is not a fix — it is amputation and is banned in many places for good reason.</p>

        <h2>Redirect, don't punish</h2>
        <ul>
          <li>Place a tall, sturdy scratching post right next to the furniture they target.</li>
          <li>Use catnip or silvervine on the post to draw them in.</li>
          <li>Praise and treat when they use it.</li>
        </ul>
        <div class="callout">Make targeted furniture uninviting: double-sided tape, a couch cover, or a citrus scent cats dislike. The post must be more attractive than the sofa.</div>

        <h2>Protect the claws another way</h2>
        <p>Soft plastic claw caps and regular nail trims reduce damage while you train. They do not stop the need to scratch, so posts stay essential.</p>
        """,
        "faq": [
            ("How do I stop my cat scratching the couch?", "Put an appealing post beside the couch, use catnip, and make the couch boring with tape or a cover. Reward post use."),
            ("Should I declaw my cat?", "No. Declawing removes the last bone of each toe and causes lasting pain. Redirect scratching instead."),
            ("Do claw caps work?", "Soft caps reduce furniture damage and are safe, but they do not replace the cat's need to scratch — keep the posts."),
        ],
        "related": ["cat-litter-training", "cat-spraying-how-to-stop", "why-do-dogs-eat-poop"],
        "sources": [
            ("ASPCA — Common Cat Behavior Issues",
             "https://www.aspca.org/pet-care/cat-care/common-cat-behavior-issues"),
            ("Cornell Feline Health Center — Feline Health Topics",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center/health-information/feline-health-topics"),
            ("International Cat Care — Advice",
             "https://icatcare.org/advice/"),
        ],
        "disclaimer": "Cat behavior guidance only. Sudden changes in scratching with over-grooming can signal stress or skin issues — ask a vet.",
    },
    {
        "slug": "cat-spraying-how-to-stop",
        "pillar": "cat",
        "title": "How to Stop a Cat Spraying Indoors",
        "url": "/cat/cat-spraying-how-to-stop/",
        "description": "Spraying is scent-marking, not a litter box problem. How to reduce stress, clean with enzymes, and use pheromones and consider neutering to stop it for good.",
        "lede": "Spraying is your cat marking territory with urine on vertical surfaces — different from litter accidents. The fix is reducing stress and conflict, not punishment.",
        "eyebrow": "CAT CARE",
        "body": """
        <h2>Spraying vs accidents</h2>
        <p>Spraying is a small amount on a wall or chair back, often with a quiver tail. Litter accidents are on the floor. They have different causes and fixes.</p>

        <h2>Common triggers</h2>
        <ul>
          <li>Other cats — outside the window or in the home.</li>
          <li>Stress from moves, new pets, or routine changes.</li>
          <li>Unneutered males and unspayed females spray most.</li>
        </ul>
        <div class="callout warn">First, a vet check — urinary pain can look like spraying. Once medical causes are out, address stress and marking.</div>

        <h2>What helps</h2>
        <ul>
          <li>Neuter or spay — cuts spraying dramatically.</li>
          <li>Use synthetic pheromone diffusers to lower anxiety.</li>
          <li>Block the view of outdoor cats and add vertical safe spaces.</li>
          <li>Clean marks with an enzyme cleaner so the scent does not invite re-marking.</li>
        </ul>
        """,
        "faq": [
            ("Is cat spraying the same as peeing outside the box?", "No. Spraying is a small amount on vertical surfaces for marking; accidents are on the floor, usually medical or litter-related."),
            ("Will neutering stop my cat spraying?", "Often yes, especially in males — neutering removes most hormone-driven marking. Established habits may need extra steps."),
            ("How do I clean cat spray?", "Use an enzyme cleaner, not regular cleaner, so the scent that triggers re-marking is fully removed."),
        ],
        "related": ["cat-litter-training", "cat-scratching-furniture", "cat-hairballs"],
        "sources": [
            ("ASPCA — Common Cat Behavior Issues",
             "https://www.aspca.org/pet-care/cat-care/common-cat-behavior-issues"),
            ("Merck Veterinary Manual — Behavior of Cats",
             "https://www.merckvetmanual.com/cat-owners/behavior-of-cats"),
            ("Cornell Feline Health Center",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center"),
        ],
        "disclaimer": HEALTH_DISCLAIMER,
    },

    # ---------------- Reviews / best ----------------
    {
        "slug": "best-dog-crate",
        "pillar": "best",
        "title": "Best Dog Crate 2026 — Practical Picks, Not Hype",
        "url": "/best/dog-crate/",
        "description": "Straightforward dog crate picks for puppies, anxious dogs, and travel — chosen for safety, durability, and easy cleaning, plus clear, practical sizing guidance.",
        "lede": "The best crate is the one your dog accepts and you can clean easily. We prefer sturdy wire crates with a divider for puppies and a secure plastic crate for travel.",
        "eyebrow": "REVIEWS",
        "body": """
        <h2>What actually matters</h2>
        <ul>
          <li><strong>Correct size</strong> — stand/turn/lie down room, with a divider to grow into for puppies.</li>
          <li><strong>Secure door latch</strong> — escape-proof for anxious dogs.</li>
          <li><strong>Easy cleanup</strong> — a removable tray saves you.</li>
        </ul>

        <h2>Our picks by need</h2>
        <p><strong>For puppies:</strong> a wire crate with a divider panel — shrink it now, expand as they grow, no second purchase. <strong>For anxious dogs:</strong> a solid plastic crate feels more den-like and blocks visual triggers. <strong>For car travel:</strong> a crash-tested plastic crate anchored with a seatbelt.</p>
        <div class="callout good">Avoid crates with sharp edges or flimsy latches. The cheapest crate that fails its latch costs more than a good one when your dog gets loose.</div>

        <h2>What we skip</h2>
        <p>Fancy furniture crates are pretty but often poor ventilation and hard to clean. Pretty is the last thing to optimize.</p>

        <h2>Bottom line</h2>
        <p>Buy once: a size-adjustable wire crate for home, and a travel crate only if you drive with your dog often.</p>
        """,
        "faq": [
            ("What size crate does my dog need?", "Big enough to stand, turn, and lie down. For a puppy, choose the adult size and use a divider to keep the space snug now."),
            ("Wire or plastic crate?", "Wire for home (airflow, visibility, divider options); plastic for anxious dogs and car travel (cozier, more secure)."),
            ("Do I need a crate for my dog?", "Not required, but it speeds house training and gives a safe space. Many dogs come to love theirs."),
        ],
        "related": ["how-to-crate-train-a-puppy", "best-dog-harness-for-pulling", "dog-care"],
        "sources": [
            ("ASPCA — Common Dog Behavior Issues",
             "https://www.aspca.org/pet-care/dog-care/common-dog-behavior-issues"),
            ("American Veterinary Society of Animal Behavior — Position Statements",
             "https://avsab.org/resources/position-statements/"),
            ("Merck Veterinary Manual — Behavior of Dogs",
             "https://www.merckvetmanual.com/dog-owners/behavior-of-dogs"),
        ],
        "disclaimer": "Product guidance is opinion based on general use; we may earn a commission from linked retailers at no cost to you. Always check current safety ratings.",
    },
    {
        "slug": "best-dog-harness-for-pulling",
        "pillar": "best",
        "title": "Best Dog Harness for Pulling — Front-Clip Picks",
        "url": "/best/dog-harness-for-pulling/",
        "description": "The harness that actually reduces pulling is a front-clip design. Practical picks that balance control, comfort, and durability — plus how to fit one.",
        "lede": "A front-clip harness turns a pulling dog back toward you, which gently discourages leaning in. We favor padded, adjustable, easy-on designs over trendy ones.",
        "eyebrow": "REVIEWS",
        "body": """
        <h2>Why front-clip wins</h2>
        <p>A clip on the chest redirects the dog's forward drive sideways, so pulling no longer moves them ahead. A back-clip harness, by contrast, lets them pull like a sled dog.</p>

        <h2>What to look for</h2>
        <ul>
          <li><strong>Front (chest) clip</strong> for pulling; some models offer both front and back.</li>
          <li><strong>Padded straps</strong> so it does not rub the armpits on long walks.</li>
          <li><strong>Adjustable</strong> at chest and girth for a snug, escape-proof fit.</li>
        </ul>
        <div class="callout good">Fit matters more than brand. Two fingers should slide under every strap; a loose harness lets a strong dog slip out.</div>

        <h2>What we avoid</h2>
        <p>Choke, prong, and tight martingale collars — they correct through discomfort and can injure the neck. A front-clip harness teaches without pain.</p>

        <h2>Bottom line</h2>
        <p>Pair the harness with the stop-and-go leash method. The gear helps; the consistency is what trains.</p>
        """,
        "faq": [
            ("What type of harness stops pulling?", "A front-clip (chest-clip) harness. It turns the dog toward you when they pull, discouraging the behavior without pain."),
            ("Are no-pull harnesses bad for dogs?", "Good padded front-clip harnesses are safe. Avoid ones that tighten harshly or choke; fit and padding are key."),
            ("Should I use a collar or harness?", "For pullers, a front-clip harness protects the neck. Keep ID tags on a flat collar underneath."),
        ],
        "related": ["how-to-leash-train-a-dog", "best-dog-crate", "why-is-my-dog-shaking"],
        "sources": [
            ("ASPCA — Common Dog Behavior Issues",
             "https://www.aspca.org/pet-care/dog-care/common-dog-behavior-issues"),
            ("American Veterinary Society of Animal Behavior — Position Statements",
             "https://avsab.org/resources/position-statements/"),
            ("Merck Veterinary Manual — Behavior of Dogs",
             "https://www.merckvetmanual.com/dog-owners/behavior-of-dogs"),
        ],
        "disclaimer": "Product guidance is opinion based on general use; we may earn a commission from linked retailers at no cost to you. Check fit and safety for your dog.",
    },
    # ---------------- Dog nutrition: "can dogs eat X" cluster ----------------
    {
        "slug": "can-dogs-eat-apples",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Apples? Yes — Seeds and Core Out",
        "url": "/dog-nutrition/can-dogs-eat-apples/",
        "description": "Yes — apples are a safe, low-calorie dog treat rich in fiber and vitamin C. Why you should always remove the seeds and core, and exactly how much to offer.",
        "lede": "Yes, apples are safe and healthy for dogs in moderation. The flesh is fine; the seeds and core are the parts to skip.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Are apples good for dogs?</h2>
        <p>Apple slices are a crunchy, low-calorie treat full of vitamin C, vitamin A, and fiber. Many dogs love the texture, and they make a good training reward for dogs watching their weight.</p>

        <h2>How to serve them</h2>
        <ul>
          <li>Wash and slice. Remove the seeds and the core.</li>
          <li>A few small slices for a small dog; a few more for a large dog.</li>
          <li>Treats should stay under 10% of daily calories.</li>
        </ul>
        <div class="callout">Apple seeds contain amygdalin, which releases cyanide as they are chewed. A seed or two is not a real danger, but do not let your dog crunch the core.</div>

        <h2>When to skip</h2>
        <p>If your dog has diabetes or a sensitive stomach, keep fruit minimal. Stop if you see an upset belly after a new treat.</p>
        """,
        "faq": [
            ("Can dogs eat apple skin?", "Yes — washed apple skin is fine and adds fiber. Just remove the seeds and core."),
            ("How many apple slices can a dog have?", "A few small slices for small dogs, more for large dogs, and only as an occasional treat below 10% of daily calories."),
            ("Why remove apple seeds for dogs?", "Seeds contain amygdalin, which can release cyanide; the core is also a choking risk."),
        ],
        "related": ["can-dogs-eat-bananas", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
        "sources": [
            ("AKC — Can Dogs Eat Apples?",
             "https://www.akc.org/expert-advice/nutrition/can-dogs-eat-apples/"),
            ("AKC — Fruits and Vegetables Dogs Can and Can't Eat",
             "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-watermelon",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Watermelon? Yes — Rind and Seeds Off",
        "url": "/dog-nutrition/can-dogs-eat-watermelon/",
        "description": "Seedless watermelon flesh is a hydrating, low-calorie summer treat most dogs love. Why to skip the rind and seeds, and exactly how much is actually safe.",
        "lede": "Yes, watermelon is safe for dogs — the red flesh only. Leave out the rind and the seeds, which can upset the stomach or cause a blockage.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is watermelon good for dogs?</h2>
        <p>The flesh is about 90% water, so it is a great way to add hydration on hot days. It also brings vitamin A, vitamin C, and a touch of potassium, with very few calories.</p>

        <h2>How to serve it</h2>
        <ul>
          <li>Use seedless watermelon, or pick out the seeds by hand.</li>
          <li>Cut the red flesh into small cubes. Remove the green rind entirely.</li>
          <li>A handful of cubes is plenty for a large dog; a few for a small one.</li>
        </ul>
        <div class="callout">The rind is hard to digest and a known cause of intestinal blockage in dogs. The seeds can cause mild stomach upset or, in quantity, a blockage.</div>

        <h2>When to skip</h2>
        <p>Diabetic dogs should avoid the natural sugar. Stop if your dog gets loose stools after eating it.</p>
        """,
        "faq": [
            ("Can dogs eat watermelon rind?", "No — the rind is tough to digest and can cause a blockage. Feed only the red flesh."),
            ("Can dogs eat watermelon seeds?", "Seedless is best. Swallowed seeds can cause stomach upset or, in large amounts, an obstruction."),
            ("Is watermelon good for overweight dogs?", "Yes — it is very low in calories, so it is a good treat for dogs on a diet, in small amounts."),
        ],
        "related": ["can-dogs-eat-bananas", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
        "sources": [
            ("AKC — Fruits and Vegetables Dogs Can and Can't Eat",
             "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-cheese",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Cheese? In Small Amounts, Sometimes",
        "url": "/dog-nutrition/can-dogs-eat-cheese/",
        "description": "Most dogs can eat a little cheese, but lactose intolerance and fat make moderation the rule. Which cheeses are safer, and what a safe portion looks like.",
        "lede": "Most dogs can eat a small amount of cheese, but many are lactose intolerant and all should keep it occasional because of the fat and salt.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is cheese safe for dogs?</h2>
        <p>Cheese is not toxic, and a thin slice is a handy way to hide a pill or reward a dog. The catch is that many dogs lose the ability to digest lactose as they age, and cheese is high in fat and sodium.</p>

        <h2>How much and which kind</h2>
        <ul>
          <li>Stick to low-sodium, low-fat types: cottage cheese or a small bit of mozzarella are better choices.</li>
          <li>Keep it to a bite or two — not a snack bowl.</li>
          <li>Avoid blue cheeses and anything with added herbs, garlic, or onion.</li>
        </ul>
        <div class="callout">Watch for gas, bloating, or loose stools after cheese. Those are signs of lactose intolerance, and the treat should stop.</div>

        <h2>When to skip</h2>
        <p>Overweight dogs and dogs with pancreatitis should avoid cheese. High-fat cheese can trigger a painful pancreatitis flare.</p>
        """,
        "faq": [
            ("What cheese is safest for dogs?", "Low-fat, low-sodium options like cottage cheese or mozzarella, in small amounts."),
            ("Can cheese give dogs diarrhea?", "Yes — lactose intolerance is common in dogs, and too much fat can upset the gut."),
            ("Can I use cheese to hide my dog's pill?", "A tiny amount is a common, safe trick, as long as your dog tolerates dairy."),
        ],
        "related": ["can-dogs-eat-bananas", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-peanut-butter",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Peanut Butter? Yes — Read the Label First",
        "url": "/dog-nutrition/can-dogs-eat-peanut-butter/",
        "description": "Peanut butter is a favorite dog treat, but xylitol in some brands is deadly. How to read the label, choose a safe jar, and how much of it is safe to give.",
        "lede": "Yes, plain peanut butter is a great dog treat — but only if it contains no xylitol, which is extremely toxic to dogs. Always read the label.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is peanut butter safe for dogs?</h2>
        <p>Plain peanut butter (peanuts, maybe salt) is safe and dogs love it. It is high in fat and calories, so it should stay a small, occasional treat.</p>

        <h2>The one rule that matters: no xylitol</h2>
        <div class="callout warn">Xylitol, a sweetener in some peanut butters and other "sugar-free" foods, causes a rapid, dangerous drop in blood sugar and liver failure in dogs. A small amount can be fatal. Check the ingredients every time — brands change formulas.</div>
        <ul>
          <li>Choose a jar with just peanuts (and salt, if any).</li>
          <li>A teaspoon for a small dog, up to a tablespoon for a large dog, occasionally.</li>
        </ul>

        <h2>When to skip</h2>
        <p>Overweight or pancreatitis-prone dogs should avoid it. And never leave a xylitol product within reach.</p>
        """,
        "faq": [
            ("Is xylitol peanut butter toxic to dogs?", "Yes — xylitol is extremely toxic and can be fatal even in small amounts. Check every label."),
            ("How much peanut butter can a dog have?", "About a teaspoon for small dogs, up to a tablespoon for large dogs, only as an occasional treat."),
            ("Can puppies eat peanut butter?", "A tiny amount of plain, xylitol-free peanut butter is fine, but keep portions very small for puppies."),
        ],
        "related": ["can-dogs-eat-bananas", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
        "sources": [
            ("Pet Poison Helpline — Xylitol",
             "https://www.petpoisonhelpline.com/poison/xylitol/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("AKC — Fruits and Vegetables Dogs Can and Can't Eat",
             "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-carrots",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Carrots? Yes — A Near-Perfect Treat",
        "url": "/dog-nutrition/can-dogs-eat-carrots/",
        "description": "Carrots are one of the healthiest dog snacks around — raw or cooked, low in calories, and good for teeth. How to serve them and just how much is too much.",
        "lede": "Yes, carrots are one of the best treats you can give a dog: low in calories, high in fiber and vitamin A, and a crunchy chew many dogs enjoy.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Are carrots good for dogs?</h2>
        <p>Carrots are a near-ideal dog snack. They are low in calories and fat, provide fiber and beta-carotene, and the raw crunch can help scrub plaque off teeth.</p>

        <h2>How to serve them</h2>
        <ul>
          <li>Raw: washed and cut into sticks or rounds. For small dogs, grate or soften to avoid choking.</li>
          <li>Cooked: steamed or boiled plain — softer and easier to digest.</li>
          <li>A few pieces as a treat; they still count toward the daily 10% treat budget.</li>
        </ul>
        <div class="callout">Cut carrots to a safe size. A whole baby carrot can be a choking hazard for a dog that bolts food.</div>

        <h2>When to skip</h2>
        <p>Carrots are safe for almost every dog. If your dog has never had them, introduce a small piece and watch for any tummy upset.</p>
        """,
        "faq": [
            ("Are raw carrots okay for dogs?", "Yes — raw carrots are safe and the crunch can help clean teeth. Cut them small to prevent choking."),
            ("Do carrots help dog teeth?", "Chewing raw carrots can help reduce plaque, though they are not a replacement for brushing."),
            ("Can diabetic dogs eat carrots?", "Yes, in moderation — carrots are low in sugar and a good low-calorie treat for diabetic dogs."),
        ],
        "related": ["can-dogs-eat-bananas", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
        "sources": [
            ("AKC — Fruits and Vegetables Dogs Can and Can't Eat",
             "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-eggs",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Eggs? Cooked, Plain, and Moderate",
        "url": "/dog-nutrition/can-dogs-eat-eggs/",
        "description": "Cooked eggs are a nutritious, protein-rich food topper for dogs. Why raw eggs are a poor choice, how many a dog can eat per week, and how to serve them.",
        "lede": "Yes, cooked eggs are a healthy, protein-rich addition to a dog's diet. Raw eggs are best avoided because of salmonella risk and a biotin concern.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Are eggs good for dogs?</h2>
        <p>Cooked eggs are packed with protein, fatty acids, and vitamins. Scrambled or boiled plain, they are an easy way to add nutrition for a picky or recovering dog.</p>

        <h2>How to serve them</h2>
        <ul>
          <li>Boil or scramble with no oil, butter, salt, or seasoning.</li>
          <li>One egg a few times a week is plenty for most dogs; adjust by size.</li>
          <li>Let cooked eggs cool before serving.</li>
        </ul>
        <div class="callout">Avoid raw eggs. Raw egg white contains avidin, which can interfere with biotin (a B vitamin) over time, and raw eggs carry a salmonella risk for both dog and handler.</div>

        <h2>When to skip</h2>
        <p>Dogs with pancreatitis or a known egg sensitivity should avoid them. Introduce slowly if eggs are new.</p>
        """,
        "faq": [
            ("Can dogs eat scrambled eggs?", "Yes — plain scrambled (no butter, salt, or oil) is a healthy treat or topper."),
            ("Why not raw eggs for dogs?", "Raw egg white can interfere with biotin, and raw eggs may carry salmonella."),
            ("How many eggs can a dog eat?", "About one egg a few times per week for most dogs, adjusted for their size and diet."),
        ],
        "related": ["can-dogs-eat-chicken", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-chicken",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Chicken? Cooked, Plain, Boneless",
        "url": "/dog-nutrition/can-dogs-eat-chicken/",
        "description": "Plain cooked chicken is a staple protein in dog food and a go-to for upset stomachs. Why bones and seasoning are the danger, and how to serve it safely.",
        "lede": "Yes, plain cooked chicken is one of the safest, most common proteins for dogs. The risks are cooked bones and rich seasoning, not the meat itself.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is chicken good for dogs?</h2>
        <p>Boiled or baked chicken with rice is the classic bland meal for a dog with an upset stomach, and it is a solid everyday protein for most dogs.</p>

        <h2>How to serve it</h2>
        <ul>
          <li>Cook it through with no onion, garlic, salt, or oil.</li>
          <li>Always remove bones — especially cooked bones.</li>
          <li>Shred it and mix with plain rice or your dog's regular food.</li>
        </ul>
        <div class="callout warn">Never give cooked bones. They splinter easily and can pierce the gut or cause a blockage — a genuine emergency. Raw bones carry their own risks and should only be given under guidance.</div>

        <h2>When to skip</h2>
        <p>Some dogs are allergic to chicken. If you see itching, ear infections, or digestive upset after chicken, talk to your vet about an alternative protein.</p>
        """,
        "faq": [
            ("Can dogs eat cooked chicken bones?", "No — cooked bones splinter and can damage the digestive tract. Always remove them."),
            ("Can dogs eat chicken skin?", "Small amounts are fine, but the skin is high in fat and can trigger pancreatitis if fed often."),
            ("Is chicken good for a sick dog?", "Plain boiled chicken with rice is the standard bland meal for mild tummy upset; see a vet if it persists."),
        ],
        "related": ["can-dogs-eat-eggs", "dog-vomiting-causes", "how-much-to-feed-my-dog"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-milk",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Drink Milk? Usually Not Worth It",
        "url": "/dog-nutrition/can-dogs-eat-milk/",
        "description": "Most adult dogs are lactose intolerant, so milk usually causes diarrhea and gas. Why plain yogurt and small amounts of cheese are safer dairy options.",
        "lede": "Most dogs should skip milk. Adult dogs are commonly lactose intolerant, and a bowl of milk more often leads to gas and diarrhea than any benefit.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is milk safe for dogs?</h2>
        <p>A few laps of milk will not harm most dogs, but it is not a good regular drink. As puppies wean, they lose much of the lactase enzyme that digests lactose, so milk sugar ferments in the gut and causes loose stools.</p>

        <h2>How much, if any</h2>
        <ul>
          <li>A small sip now and then is fine for dogs that tolerate it.</li>
          <li>Skip it entirely if your dog gets gas or diarrhea from dairy.</li>
          <li>Plain, unsweetened yogurt or a bit of cheese is often better tolerated than milk.</li>
        </ul>
        <div class="callout">Puppies need their mother's milk or a proper puppy formula — never cow's milk as a substitute, which lacks the right balance and can upset their stomach.</div>

        <h2>When to skip</h2>
        <p>Lactose-intolerant and sensitive dogs should avoid milk. Water remains the best drink for every dog.</p>
        """,
        "faq": [
            ("Why does milk give dogs diarrhea?", "Most adult dogs are lactose intolerant, so the milk sugar ferments and loosens stools."),
            ("Can dogs have yogurt instead?", "Plain, unsweetened yogurt is often better tolerated than milk and adds probiotics."),
            ("Can puppies drink cow's milk?", "No — use a proper puppy milk replacer; cow's milk is unbalanced for puppies."),
        ],
        "related": ["can-dogs-eat-cheese", "can-dogs-eat-bananas", "how-much-to-feed-my-dog"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-strawberries",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Strawberries? Yes — Wash and Limit",
        "url": "/dog-nutrition/can-dogs-eat-strawberries/",
        "description": "Strawberries are a safe, vitamin-rich dog treat most dogs love. Why to keep them occasional, how many to offer, and why you should skip sugary toppings.",
        "lede": "Yes, strawberries are safe for dogs in moderation. They are low in calories and full of vitamin C, but their natural sugar means they should stay an occasional treat.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Are strawberries good for dogs?</h2>
        <p>Fresh strawberries bring vitamin C, fiber, and antioxidants with very few calories — a good sweet treat for dogs watching their weight.</p>

        <h2>How to serve them</h2>
        <ul>
          <li>Wash well and hull them. Slice for small dogs.</li>
          <li>A few berries for a small dog; a small handful for a large one.</li>
          <li>Offer them plain — no syrup, whipped cream, or sugar.</li>
        </ul>
        <div class="callout">Skip strawberry-flavored products and desserts; the added sugar and xylitol risk are not worth it. A mashed berry can also be frozen for a cooling chew.</div>

        <h2>When to skip</h2>
        <p>Diabetic dogs should avoid the extra sugar. Stop if your dog gets an upset stomach after eating them.</p>
        """,
        "faq": [
            ("How many strawberries can a dog eat?", "A few for small dogs, a small handful for large dogs, and only as an occasional treat."),
            ("Can dogs eat frozen strawberries?", "Yes — plain, washed, frozen berries make a cooling summer treat."),
            ("Are strawberry tops safe for dogs?", "The green tops are not toxic, but most dogs prefer the fruit; remove them if your dog is a picky eater."),
        ],
        "related": ["can-dogs-eat-bananas", "can-dogs-eat-watermelon", "foods-toxic-to-dogs"],
        "sources": [
            ("AKC — Fruits and Vegetables Dogs Can and Can't Eat",
             "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-grapes",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Grapes? NO — They Are Toxic",
        "url": "/dog-nutrition/can-dogs-eat-grapes/",
        "description": "Grapes and raisins can cause sudden kidney failure in dogs, even in tiny amounts. Why there is no safe dose, and exactly what to do if yours eats one.",
        "lede": "No — grapes and raisins are toxic to dogs and can cause sudden, severe kidney failure. There is no safe amount, so treat any ingestion as an emergency.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Why grapes are dangerous</h2>
        <p>Grapes and raisins can trigger acute kidney failure in dogs, and the toxic dose varies so wildly that no one can say how many is safe. Some dogs are fine after a few; others collapse after one. Because you cannot predict which dog will react, every exposure is treated as potentially serious.</p>

        <h2>What to do if your dog ate grapes</h2>
        <div class="callout warn">Call your veterinarian or an animal poison control line immediately. Do not wait for symptoms. Faster treatment — inducing vomiting and IV fluids — greatly improves the outcome.</div>
        <ul>
          <li>Note how many and roughly when they were eaten.</li>
          <li>Keep grapes, raisins, and foods made with them (bakery items, trail mix) out of reach.</li>
          <li>Watch for vomiting, lethargy, reduced appetite, and reduced urination in the following days.</li>
        </ul>

        <h2>Watch for these signs</h2>
        <p>Early signs are vomiting and lethargy; later signs of kidney failure include reduced or no urination and weakness. By then the damage is advanced, so act early.</p>
        """,
        "faq": [
            ("How many grapes are toxic to a dog?", "There is no known safe dose. Even one grape has caused kidney failure in some dogs, so any amount is an emergency."),
            ("Are raisins as dangerous as grapes?", "Yes — raisins are dried grapes and just as toxic, and dogs may eat more of them."),
            ("What should I do if my dog ate a grape?", "Call your vet or animal poison control now. Do not wait for symptoms to appear."),
        ],
        "related": ["foods-toxic-to-dogs", "dog-vomiting-causes", "can-dogs-eat-bananas"],
        "sources": [
            ("Pet Poison Helpline — Grapes",
             "https://www.petpoisonhelpline.com/poison/grapes/"),
            ("Pet Poison Helpline — Raisins",
             "https://www.petpoisonhelpline.com/poison/raisins/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
        ],
        "disclaimer": "This article is general information, not veterinary advice. If your dog may have eaten grapes or raisins, contact a veterinarian or emergency clinic right away.",
    },
    {
        "slug": "can-dogs-eat-chocolate",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Chocolate? NO — It Is Toxic",
        "url": "/dog-nutrition/can-dogs-eat-chocolate/",
        "description": "Chocolate contains theobromine, which is poisonous to dogs. Why dark and baking chocolate are worst, the symptoms to watch for, and exactly what to do next.",
        "lede": "No — chocolate is toxic to dogs because it contains theobromine, which they cannot metabolize well. Dark and baking chocolate are the most dangerous.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Why chocolate is dangerous</h2>
        <p>Chocolate contains theobromine and caffeine. Dogs break these down slowly, so they build up and overstimulate the heart and nervous system. The darker and more pure the chocolate, the more theobromine it carries — baking and dark chocolate are far worse than milk chocolate.</p>

        <h2>What to do if your dog eats chocolate</h2>
        <div class="callout warn">Call your veterinarian or an animal poison control line right away. Note the type of chocolate, roughly how much, and your dog's weight — these decide how serious it is.</div>
        <ul>
          <li>Small amounts of milk chocolate may cause only mild upset in a large dog, but any dark or baking chocolate is urgent.</li>
          <li>Keep all chocolate, cocoa powder, and baked goods well out of reach.</li>
        </ul>

        <h2>Watch for these signs</h2>
        <p>Restlessness, panting, a racing heart, vomiting, tremors, and in severe cases seizures. Symptoms can appear within a few hours and escalate, so do not wait.</p>
        """,
        "faq": [
            ("How much chocolate is toxic to a dog?", "It depends on the type and the dog's weight; dark and baking chocolate are dangerous in small amounts. Any ingestion should prompt a vet call."),
            ("Is dark chocolate worse for dogs?", "Yes — darker chocolate has far more theobromine than milk chocolate and is the most toxic."),
            ("What should I do if my dog ate chocolate?", "Call your vet or animal poison control with the type, amount, and your dog's weight as soon as possible."),
        ],
        "related": ["foods-toxic-to-dogs", "dog-vomiting-causes", "can-dogs-eat-grapes"],
        "sources": [
            ("Pet Poison Helpline — Chocolate",
             "https://www.petpoisonhelpline.com/poison/chocolate/"),
            ("Merck Veterinary Manual — Chocolate Toxicosis in Animals",
             "https://www.merckvetmanual.com/toxicology/food-hazards/chocolate-toxicosis-in-animals"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
        ],
        "disclaimer": "This article is general information, not veterinary advice. If your dog may have eaten chocolate, contact a veterinarian or emergency clinic right away.",
    },
    {
        "slug": "can-dogs-eat-avocado",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Avocado? Risky — Best Avoided",
        "url": "/dog-nutrition/can-dogs-eat-avocado/",
        "description": "Avocado flesh is less risky than the skin, pit, and leaves, but the choking hazard and high fat content make it a treat that most dogs are better off skipping.",
        "lede": "Avocado is best avoided. The flesh is the safest part but still high in fat; the pit is a choking hazard and the skin and leaves carry persin, which upsets the gut.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Why avocado is risky</h2>
        <p>Avocado contains persin, a compound concentrated in the skin, pit, and leaves that can cause vomiting and diarrhea. The flesh has far less, but it is still rich in fat, which brings its own problem: too much can trigger pancreatitis.</p>

        <h2>The real hazards</h2>
        <ul>
          <li>The pit is a serious choking and blockage risk if swallowed.</li>
          <li>The skin is hard to digest and can obstruct the gut.</li>
          <li>The high fat content can upset sensitive stomachs or trigger pancreatitis.</li>
        </ul>
        <div class="callout">If your dog grabs a dropped avocado, the main worries are the pit and the fat. Remove any pit and skin, and watch for vomiting, belly pain, or lethargy.</div>

        <h2>When to skip</h2>
        <p>Because safer treats exist, most owners simply avoid avocado. Dogs with pancreatitis or sensitive stomachs should definitely skip it.</p>
        """,
        "faq": [
            ("Is avocado flesh toxic to dogs?", "The flesh is the least risky part but still high in fat; the skin, pit, and leaves are the concern."),
            ("Can the avocado pit hurt my dog?", "Yes — it is a choking and blockage hazard and should never be left where a dog can swallow it."),
            ("Why avoid avocado for dogs?", "Safer, lower-fat treats exist, and the fat content can trigger pancreatitis in sensitive dogs."),
        ],
        "related": ["foods-toxic-to-dogs", "can-dogs-eat-bananas", "how-much-to-feed-my-dog"],
        "sources": [
            ("Pet Poison Helpline — Avocado",
             "https://www.petpoisonhelpline.com/poison/avocado/"),
            ("Merck Veterinary Manual — Avocado Toxicosis in Animals",
             "https://www.merckvetmanual.com/toxicology/food-hazards/avocado-toxicosis-in-animals"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
        ],
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    # ---------------- Cat health & behaviour (batch 2, 2026-10-17) ----------------
    {
        "slug": "cat-hairballs",
        "pillar": "cat",
        "title": "Cat Hairballs — What's Normal and When to Worry",
        "url": "/cat/cat-hairballs/",
        "description": "Fur coming back up is part of how cats work. How often a hairball is normal, what makes them worse, and the signs that turn a hairball into a vet visit.",
        "lede": "A hairball now and then is normal grooming housekeeping. The pattern is what matters — how often, how easily, and whether your cat is otherwise fine.",
        "eyebrow": "CAT CARE",
        "body": """
        <h2>Why hairballs happen</h2>
        <p>Cats groom themselves with barbed tongues that pull loose fur out of the coat — and the fur gets swallowed. Most passes through the gut without trouble; some collects into a compact wet tube that comes back up. Long-haired cats and heavy shedders produce more, simply because they swallow more fur.</p>

        <h2>How often is normal</h2>
        <ul>
          <li>Up to about one hairball every week or two is common, especially in long-haired breeds during a shed.</li>
          <li>Several a week, or a sudden increase, is not normal — it usually means the gut is moving fur through too slowly.</li>
          <li>Effortless vomiting of a formed tube right after eating grass or grooming is typical; straining without producing anything is not.</li>
        </ul>
        <div class="callout warn">Retching with no hairball coming up, refusing food, constipation or no stool, a swollen belly, or low energy are blockage warning signs. A trichobezoar (fur mass) can lodge in the intestine and needs a vet the same day.</div>

        <h2>What actually reduces hairballs</h2>
        <ul>
          <li>Brush regularly — daily for long-haired cats, a few times a week otherwise. Fur you remove is fur they cannot swallow.</li>
          <li>Wipe the coat with a damp cloth or grooming wipe after brushing to catch loose undercoat.</li>
          <li>Add fiber and water: some cats do better on a higher-fiber hairball-control diet, and fountains or wet food keep gut contents moving.</li>
          <li>Malt-based hairball pastes or gels a few times a week can help fur slide through the gut.</li>
          <li>More play, less bored over-grooming — some cats lick themselves for something to do.</li>
        </ul>

        <h2>Watch the other end of the pattern</h2>
        <p>A senior cat that grooms less may develop matted fur — that is worth a check too, since stiff joints make stretching to groom painful. And sudden over-grooming that leads to bald patches is usually stress or skin trouble, not a hairball problem. Hairballs are a plumbing symptom; the coat and the gut tell the story together.</p>
        """,
        "faq": [
            ("How often is it normal for a cat to bring up hairballs?", "Roughly once every one to two weeks is common, more in long-haired cats during shedding season. Several a week or a sudden increase warrants a vet check."),
            ("Can a hairball actually cause a blockage?", "Yes — a compacted fur mass can lodge in the intestine. Repeated retching with nothing produced, appetite loss, constipation, or a tender belly are same-day vet signs."),
            ("Do hairball-control diets and pastes work?", "They can help — added fiber and lubricant pastes move swallowed fur through the gut. Grooming is still the biggest lever, because it stops fur at the source."),
        ],
        "related": ["why-does-my-cat-meow-at-night", "cat-scratching-furniture", "dog-vomiting-causes"],
        "sources": [
            ("International Cat Care — Hairballs in Cats",
             "https://icatcare.org/advice/hairballs-in-cats/"),
            ("International Cat Care — Grooming Your Cat",
             "https://icatcare.org/articles/grooming-your-cat"),
            ("Cornell Feline Health Center",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center"),
        ],
        "checked": "2026-10-17",
        "disclaimer": "Cat health guidance only. Frequent vomiting, retching without a hairball, or a bloated, painful belly need a veterinarian the same day.",
    },
    {
        "slug": "why-does-my-cat-meow-at-night",
        "pillar": "cat",
        "title": "Why Does My Cat Meow at Night — and How to Make It Stop",
        "url": "/cat/why-does-my-cat-meow-at-night/",
        "description": "Cats are wired for dawn and dusk, not for your sleep schedule. The real causes of night-time meowing, the evening routine that works, and when it means illness.",
        "lede": "A cat yelling at your bedroom door at 3 a.m. is not being difficult. The cause is usually energy, hunger, or a habit you accidentally trained — and the fix is a routine, not a punishment.",
        "eyebrow": "CAT CARE",
        "body": """
        <h2>Cats are crepuscular, not nocturnal</h2>
        <p>Cats are most active at dawn and dusk — the hunting hours of their wild ancestors. An indoor cat that slept all day and got no exercise while you were at work is wide awake exactly when you are falling asleep. Some night noise is therefore normal; the goal is to move it, not to erase it.</p>

        <h2>The usual suspects</h2>
        <ul>
          <li>Leftover energy with nowhere to go — especially in kittens and young adults.</li>
          <li>Hunger — a cat fed dinner at 6 p.m. is genuinely starving by morning, and learns that calling works.</li>
          <li>Trained behavior — if meowing has ever gotten food, a door opened, or even a scolding, it was rewarded. Attention of any kind counts.</li>
          <li>Unneutered cats yowl to find mates; outdoor cats visible through the window can trigger territory calling.</li>
        </ul>

        <h2>The evening routine that works</h2>
        <p>Cats run on a natural cycle: hunt, catch, kill, eat, groom, sleep. You can borrow it:</p>
        <ul>
          <li><strong>Play hard before bed</strong> — 10 to 15 minutes with a wand toy, enough to actually tire them, ideally twice in the evening.</li>
          <li><strong>Feed the main meal after play</strong> — a full belly after a "hunt" is the natural signal to sleep.</li>
          <li><strong>Leave quiet enrichment</strong> — a puzzle feeder, a scratching post, a box. Not string or feather toys unsupervised.</li>
          <li><strong>Then hold the line</strong> — if they call at 3 a.m. and you feed them, you have taught them to call louder and longer. Check they are safe, then ignore it. Expect a few worse nights first.</li>
        </ul>
        <div class="callout">An automatic feeder that opens at 5 a.m. breaks the link between <em>you</em> and breakfast — the single most effective fix for food-driven dawn calling.</div>

        <h2>When night meowing means illness</h2>
        <p>A sudden change — a cat that never called at night now yowling loudly — deserves a vet visit before any behavior plan. In cats over about seven, increased night-time vocalizing is a classic sign of an overactive thyroid, high blood pressure, kidney disease, joint pain, or age-related cognitive decline (confusion and changed sleep-wake cycles). These are common in older cats and most are treatable, so do not write it off as "just getting old".</p>

        <h2>What not to do</h2>
        <ul>
          <li>Do not punish — yelling or spraying frightens the cat and still counts as attention, so it reinforces the noise.</li>
          <li>Do not give in "just once" — intermittent rewards are the strongest kind for building a habit.</li>
          <li>Do not assume all meowing is misbehavior — a new, distressed-sounding call in an older cat is information, not nuisance.</li>
        </ul>
        """,
        "faq": [
            ("Why does my cat meow at the bedroom door every night?", "Usually a trained habit — the meowing has produced attention, food, or an open door. Check needs are met, then stop responding, and keep a hard play session and late meal before your bedtime."),
            ("Should I just ignore a cat meowing at night?", "If the behavior is a learned request and the cat is safe, yes — responding rewards it. But a sudden change in a cat that never called before, especially over age seven, needs a vet check first."),
            ("Why is my old cat yowling loudly at night?", "In senior cats, night yowling often signals an overactive thyroid, high blood pressure, kidney disease, or cognitive decline. Most causes are treatable — see the vet, do not dismiss it as old age."),
        ],
        "related": ["cat-hairballs", "cat-litter-training", "cat-spraying-how-to-stop"],
        "sources": [
            ("Cats Protection — Cats at Night",
             "https://www.cats.org.uk/help-and-advice/home-and-environment/cats-at-night"),
            ("ASPCA — Common Cat Behavior Issues",
             "https://www.aspca.org/pet-care/cat-care/common-cat-behavior-issues"),
            ("Merck Veterinary Manual — Behavior of Cats",
             "https://www.merckvetmanual.com/cat-owners/behavior-of-cats"),
        ],
        "checked": "2026-10-17",
        "disclaimer": HEALTH_DISCLAIMER,
    },
]

# ---------------------------------------------------------------------------
# Home
# ---------------------------------------------------------------------------
HOME = {
    "title": "WagWise Pet — Calm, Practical Dog & Cat Care Guides",
    "url": "/",
    "description": "Straightforward dog and cat care answers: training, health symptoms, nutrition, grooming, and honest product picks — written to be useful and calm, not scary.",
    "eyebrow": "DOG & CAT CARE",
    "pillars": ["dog-training", "dog-health", "dog-nutrition", "dog-care", "cat", "best"],
    "featured": [
        "how-to-crate-train-a-puppy",
        "dog-vomiting-causes",
        "foods-toxic-to-dogs",
        "cat-spraying-how-to-stop",
        "best-dog-harness-for-pulling",
        "how-to-trim-dog-nails",
    ],
}

# ---------------------------------------------------------------------------
# Static pages
# ---------------------------------------------------------------------------
ABOUT = {
    "url": "/about/",
    "title": "About WagWise Pet",
    "description": "Why WagWise Pet exists: clear, calm pet care information for everyday dog and cat owners, with cited sources, no fear-mongering, and no false promises.",
    "body": """
    <h1>About WagWise Pet</h1>
    <p>WagWise Pet is an independent pet care resource for everyday dog and cat owners. We write practical guides — training, symptoms, feeding, grooming, and product picks — in plain language, without the fear-mongering you find elsewhere.</p>
    <h2>Our approach</h2>
    <p>Every article is built around a real question a pet owner actually types into search. We lead with the answer, back it with reputable sources, and flag what is urgent versus what can wait. Where a topic touches health, we point you to a veterinarian rather than pretending to be one.</p>
    <h2>Who writes this</h2>
    <p>Content is researched and edited against established veterinary and training references. We are not a clinic; for diagnosis and treatment, your local vet is the authority.</p>
    <h2>How we research a guide</h2>
    <p>Every health or behaviour claim is checked against named public references — the ASPCA, the Merck Veterinary Manual, Cornell Feline Health Center, International Cat Care, the AKC, the AVMA and the American Veterinary Society of Animal Behavior — rather than against other blog posts. You can see the exact list at the bottom of each article, with links out, so you can check us rather than trust us.</p>
    <h2>Editorial standards</h2>
    <ul>
      <li><strong>We do not invent expertise.</strong> No article claims to be written or reviewed by a veterinarian unless it was. We are an editorial team that reads veterinary sources closely and cites them.</li>
      <li><strong>Every guide carries a check date.</strong> The date under the Sources block is the last time the facts were checked against those references — not the day the page was published or reformatted.</li>
      <li><strong>We separate urgent from optional.</strong> Where a symptom needs same-day veterinary care, the guide says so at the point where it matters, not in a vague warning at the end.</li>
      <li><strong>No fear-mongering, no guarantees.</strong> We do not promise outcomes, and we do not stretch a study's finding further than the source does.</li>
    </ul>
    <h2>Corrections</h2>
    <p>If something here is wrong, out of date, or contradicts the source we cited, tell us and we will fix it and say so. Email <a href="mailto:contact@wagwise.org">contact@wagwise.org</a> with the page address and the source that disagrees. Substantive corrections are reflected in the check date on that guide.</p>
    <h2>How we make money</h2>
    <p>Some product pages contain affiliate links. If you buy through them, we may earn a small commission at no extra cost to you. Our picks are based on usefulness, never on commission.</p>
    """,
}

PRIVACY = {
    "url": "/privacy/",
    "title": "Privacy Policy — WagWise Pet",
    "description": "How WagWise Pet handles cookies, analytics, and affiliate links, plus the full veterinary disclaimer that applies to every guide published on this site.",
    "body": """
    <h1>Privacy Policy</h1>
    <h2>Cookies and consent</h2>
    <p>We use essential cookies to keep the site working. Advertising and analytics cookies are optional and are only set if you click \"Accept all\" on the consent banner. You can change your choice anytime via the Cookie settings link in the footer. Rejecting optional cookies does not change how the site works.</p>
    <h2>Data we collect</h2>
    <p>If you enable analytics, we collect anonymous, aggregated usage data (pages visited, approximate region) to improve the site. We do not sell personal data.</p>
    <h2>Affiliate links</h2>
    <p>Some pages link to retailers. If you purchase, we may receive a commission. This does not affect the price you pay or our recommendations.</p>
    <h2>Medical disclaimer</h2>
    <p>All content is general information, not veterinary advice. For diagnosis, treatment, or anything urgent, contact a licensed veterinarian. In an emergency, call your nearest animal clinic.</p>
    """,
}

# ---------------------------------------------------------------------------
# Tool pages (interactive calculators / widgets).
# ---------------------------------------------------------------------------
TOOL = {
    "url": "/tools/dog-age-calculator/",
    "title": "Dog Age Calculator — Dog Years to Human Years",
    "description": "Convert your dog's age to human years by size. A quick, plain-language estimate using the standard veterinary approximation, not the outdated 7x rule.",
    "eyebrow": "TOOLS",
}
