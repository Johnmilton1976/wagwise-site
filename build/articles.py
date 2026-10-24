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
            "can-dogs-eat-blueberries", "can-dogs-eat-pumpkin",
            "can-dogs-eat-sweet-potato", "can-dogs-eat-rice",
            "can-dogs-eat-cucumber", "can-dogs-eat-broccoli",
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
        "description": "Puppy biting is normal teething, not aggression. How to stop puppy biting by redirecting it, teaching bite inhibition, and when the phase should finally end.",
        "lede": "Puppy biting is not aggression — it is teething and play. The fix is to redirect to a toy, reward gentle mouths, and make a brief withdrawal when teeth touch skin.",
        "eyebrow": "DOG TRAINING",
        "body": """
        <h2>Why is my puppy biting?</h2>
        <p>Puppy biting is not aggression — it is teething and play. Puppies explore with their mouths and bite harder than they mean to because they have not yet learned bite inhibition. Littermates teach this by yelping; you can teach it too. Understanding this is the first step to learning how to stop puppy biting without ever raising your voice.</p>

        <h2>How to stop puppy biting — the redirect method</h2>
        <ul>
          <li>When teeth touch skin, say a calm \"ouch\" or just go silent, and offer a toy instead.</li>
          <li>If the puppy takes the toy, praise. If it keeps biting, stand up and turn away for 20-30 seconds — attention is the reward it wants.</li>
          <li>Keep a toy within reach so redirection is instant, not a search mission.</li>
        </ul>
        <div class="callout warn">Do not hit, hold the muzzle, or shout. Those can make a fearless puppy bite harder or a soft one become hand-shy.</div>

        <h2>The reverse timeout</h2>
        <p>The most reliable tool is withdrawal of attention. The instant teeth touch skin, end the interaction: stand up, step away, and stay still for 20-30 seconds. Puppies quickly learn that biting ends the fun. Consistency matters more than any single technique — everyone in the household has to do it the same way.</p>

        <h2>Extra help for teething</h2>
        <p>Cold chew toys from the freezer soothe sore gums. Rotate toys so they stay interesting. A tired puppy bites less — short training games burn energy. Offer appropriate things to chew so the puppy learns what is fair game and what is not.</p>

        <h2>What not to do</h2>
        <ul>
          <li>Do not punish with your hands — it teaches fear, not control.</li>
          <li>Do not let the puppy "win" by getting more play when it bites; that rewards the behavior.</li>
          <li>Do not use physical corrections like muzzle holds or taps.</li>
        </ul>

        <h2>When should puppy biting stop?</h2>
        <p>Biting should fade by 5-6 months as adult teeth come in and bite inhibition sets in. Soft play-mouthing may linger longer, which is normal. Persistent hard biting past that point, or any skin break with a growl, is worth a trainer's eyes.</p>

        <h2>When to get help</h2>
        <p>Most puppy biting resolves with consistency. But reach out to a qualified positive-reinforcement trainer if the biting gets harder or more frequent over time, your puppy growls or snaps from a calm state (not during play), or a bite breaks skin. Early help prevents habits from setting in. For related skills, see our guides to <a href="/dog-training/how-to-leash-train-a-dog/">leash training</a> and <a href="/dog-training/how-to-crate-train-a-puppy/">crate training</a>.</p>
        """,
        "faq": [
            ("At what age do puppies stop biting?", "Most puppies stop hard mouthing by 5 to 6 months, once adult teeth are in and bite inhibition is learned. Soft play-mouthing may linger longer."),
            ("How do I stop my puppy from biting me?", "The reliable fix is redirection plus a reverse timeout: the instant teeth touch skin, say a calm ouch, offer a toy, and if it keeps biting, stand up and step away for 20-30 seconds. Consistency from everyone in the home is what makes it work."),
            ("Why does my puppy bite my ankles when I walk?", "It is herding and chase instinct plus boredom. Stop moving, redirect to a toy, and give more exercise and mental games."),
            ("Is puppy biting a sign of aggression?", "Usually no. In young puppies it is teething and play, not real aggression. The exception is a puppy that growls or snaps from a calm state, which deserves a trainer's assessment."),
            ("Should I use a bitter spray?", "It can help as a backup, but the core fix is redirection and withdrawal of attention. Sprays alone rarely solve the habit."),
            ("How long does the puppy biting phase last?", "Hard mouthing should fade by 5-6 months as adult teeth come in. Gentle play-mouthing may continue but should not hurt."),
            ("What if my puppy breaks skin when biting?", "Clean the wound and watch it. A single playful nip that breaks skin is common, but if bites get harder, more frequent, or come with a growl from a calm state, see a qualified trainer."),
            ("Do puppies grow out of biting?", "Most do, with consistent guidance. Without redirection they can learn that biting is how to get attention, so teaching bite inhibition early matters."),
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
        "experts": [
            "The board-certified behaviourists of the American Veterinary Society of Animal Behavior (AVSAB)",
            "The animal behaviour specialists at the ASPCA",
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
        <p>The flesh is about 92% water, so it is one of the best ways to add hydration on a hot day. A cup of diced watermelon (about 150 g) has roughly 45 calories, a good hit of vitamin A and vitamin C, a little potassium, and almost no fat or sodium. For a dog that turns its nose up at plain water, a few chilled cubes can nudge fluid intake up — useful when you are watching for dehydration during summer walks.</p>

        <h2>Which part of the watermelon can a dog eat?</h2>
        <p>Only the red flesh. The rest of the fruit is where the risk lives:</p>
        <ul>
          <li><b>Rind:</b> tough, fibrous, and hard to digest. It is a known cause of intestinal blockage, especially in smaller dogs that swallow a chunk of it.</li>
          <li><b>Seeds:</b> a few swallowed seeds may only cause mild stomach upset, but in larger amounts they can lodge and obstruct. Seedless watermelon removes the worry entirely.</li>
          <li><b>Flesh:</b> the safe, hydrating part — cut into small cubes.</li>
        </ul>
        <div class="callout">The rind is a bigger hazard than people expect. Even a small piece can cause a blockage, so trim it completely rather than leaving a green rim "for crunch."</div>

        <h2>How much watermelon is safe?</h2>
        <p>Watermelon is a treat, not a meal. A sensible portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe treat amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>2–3 small cubes (about 1 tbsp diced)</td></tr>
          <tr><td>5–15 kg</td><td>A small handful of cubes (2–3 tbsp)</td></tr>
          <tr><td>15–30 kg</td><td>A handful (up to 1/4 cup diced)</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/2 cup diced, occasionally</td></tr>
        </table>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. The rest should come from a complete dog food.</p>

        <h2>How to serve it</h2>
        <ul>
          <li>Use seedless watermelon, or pick out the seeds by hand.</li>
          <li>Cut the flesh into small cubes and remove the green rind entirely.</li>
          <li>For a cooling chew, freeze cubes, or blend flesh with a little water and freeze in an ice tray.</li>
          <li>Wash the outside first — dogs lick the cut surface, so rind dirt matters even though they do not eat it.</li>
        </ul>

        <h2>Can puppies eat watermelon?</h2>
        <p>Yes, in tiny amounts once they are weaned and eating solid food. Puppies have smaller digestive systems, so keep it to a cube or two and watch for loose stools. The same rules apply: flesh only, no rind, no seeds.</p>

        <h2>What if my dog ate too much?</h2>
        <p>A dog that raids a whole watermelon mostly risks a belly ache — bloating, gas, and diarrhea from the sugar and water load. Mild cases pass on their own with water and a bland next meal. Call a vet if there is repeated vomiting, lethargy, a swollen painful belly, or if the dog got into the rind or seeds and may have a blockage. Diabetic dogs should avoid the natural sugar altogether.</p>
        <div class="callout warn">If the dog ate the <b>rind</b> or a lot of <b>seeds</b>, watch closely for blockage signs (straining, repeated vomiting, no stool) and call a vet — that is more urgent than a simple sugar overload.</div>

        <h2>Watermelon vs other fruit treats</h2>
        <p>Watermelon is a strong low-calorie choice, but it is not the only safe one. <a href="/dog-nutrition/can-dogs-eat-bananas/">Banana</a> and <a href="/dog-nutrition/can-dogs-eat-strawberries/">strawberries</a> are also safe in moderation, while <a href="/dog-nutrition/can-dogs-eat-grapes/">grapes and raisins</a> must never be given because they are toxic. For the full rundown of what to avoid, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods list</a>.</p>
        """,
        "faq": [
            ("Can dogs eat watermelon rind?", "No — the rind is tough to digest and can cause a blockage. Feed only the red flesh."),
            ("Can dogs eat watermelon seeds?", "Seedless is best. Swallowed seeds can cause stomach upset or, in large amounts, an obstruction."),
            ("Is watermelon good for overweight dogs?", "Yes — it is very low in calories, so it is a good treat for dogs on a diet, in small amounts."),
            ("Can puppies eat watermelon?", "Yes, a cube or two once weaned and on solid food — flesh only, no rind or seeds, and watch for loose stools."),
            ("How much watermelon can a dog eat?", "Treats should stay under about 10% of daily calories: a few cubes for a small dog, up to half a cup diced for a large one, and only occasionally."),
            ("Can dogs eat frozen watermelon?", "Yes — plain frozen flesh cubes, or a blended ice treat, are a safe cooling summer snack. Never add sugar or syrup."),
            ("Is watermelon safe for diabetic dogs?", "It is best avoided because of the natural sugar; check with your vet before offering any sweet fruit."),
            ("What happens if my dog eats too much watermelon?", "Usually just a sugar-and-water belly ache — bloating, gas, diarrhea — that passes. Call a vet for vomiting, lethargy, a swollen belly, or if the dog ate rind or seeds and may have a blockage."),
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
        "experts": [
            "The canine nutrition specialists at the Cornell Riney Canine Health Center",
            "The veterinarians of the ASPCA Animal Poison Control Center",
        ],
        "checked": "2026-10-24",
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
        "description": "Is milk good for dogs? Usually not — most adult dogs are lactose intolerant, so milk often causes diarrhea and gas. Why plain yogurt and cheese are safer.",
        "lede": "Most dogs should skip milk. Adult dogs are commonly lactose intolerant, and a bowl of milk more often leads to gas and diarrhea than any benefit.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is milk good for dogs?</h2>
        <p>Usually not. Most adult dogs are lactose intolerant, so a bowl of milk more often leads to gas and diarrhea than any real benefit. A few laps will not harm most dogs, but it is not a healthy regular drink — which is why "is milk good for dogs" gets a qualified no rather than a yes.</p>

        <h2>Why does milk upset dogs?</h2>
        <p>As puppies wean, they lose much of the lactase enzyme that digests lactose, the sugar in milk. Without enough lactase, that sugar ferments in the gut and causes loose stools, gas, and sometimes cramping. Some dogs keep enough lactase to tolerate small amounts; many do not.</p>

        <h2>How much milk can a dog have?</h2>
        <ul>
          <li>A small sip now and then is fine for dogs that clearly tolerate it.</li>
          <li>Skip it entirely if your dog gets gas or diarrhea from dairy.</li>
          <li>Plain, unsweetened yogurt or a small piece of cheese is often better tolerated than milk, because these have less lactose and yogurt's live cultures can help.</li>
        </ul>

        <h2>Is milk safe for puppies?</h2>
        <p>No — not cow's milk. Orphaned or supplementary-fed puppies should get a proper puppy milk replacer, not dairy milk from the carton. Cow's milk has the wrong balance of fat, protein, and lactose for a puppy and can cause diarrhea and poor growth. Once weaned, the same lactose intolerance that affects adult dogs applies.</p>
        <div class="callout">Puppies need their mother's milk or a proper puppy formula — never use cow's milk as a substitute, which lacks the right balance and can upset their stomach.</div>

        <h2>Better dairy options: yogurt and cheese</h2>
        <p>If you want to share a dairy treat, these are the safer choices:</p>
        <ul>
          <li><b>Plain, unsweetened yogurt</b> — lower in lactose and adds probiotics. A spoonful is plenty.</li>
          <li><b>Small amounts of cheese</b> — most dogs love it and tolerate it, but it is calorie-dense, so keep it occasional.</li>
          <li><b>Avoid</b> flavored, sweetened, or chocolate dairy products — chocolate is toxic and added sugars are unnecessary.</li>
        </ul>

        <h2>Signs your dog doesn't tolerate milk</h2>
        <p>Watch for loose stools, excess gas, stomach gurgling, or mild cramping within a few hours of drinking milk. If these appear, drop dairy and offer water instead. Persistent diarrhea deserves a vet check.</p>

        <h2>What about almond, oat, or soy milk?</h2>
        <p>These plant milks are not toxic, but they are not a good idea either. Almond milk is low in protein and often sweetened; oat and soy milks can contain added sugars or even xylitol, which is toxic to dogs, so always read the label. None of them offer nutrition a dog actually needs, and plain water remains the better choice. A tiny taste of an unsweetened, xylitol-free milk alternative is unlikely to harm, but there is no reason to make it a habit.</p>

        <h2>Milk vs other treats and drinks</h2>
        <p>Water is the best drink for every dog — no exceptions. For a safe fruit treat in moderation, <a href="/dog-nutrition/can-dogs-eat-bananas/">banana</a> is a better choice than milk. And for the full picture of what to avoid, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods list</a>. If your dog is already vomiting, our <a href="/dog-health/dog-vomiting-causes/">dog vomiting guide</a> explains what is urgent.</p>
        """,
        "faq": [
            ("Is milk good for dogs?", "Usually not. Most adult dogs are lactose intolerant, so milk tends to cause gas and diarrhea rather than provide benefit. Water is the best drink."),
            ("Why does milk give dogs diarrhea?", "Most adult dogs are lactose intolerant — they lose lactase after weaning, so milk sugar ferments in the gut and loosens stools."),
            ("Can dogs have yogurt instead of milk?", "Plain, unsweetened yogurt is often better tolerated than milk and adds probiotics. Keep it to a spoonful."),
            ("Can puppies drink cow's milk?", "No — use a proper puppy milk replacer. Cow's milk is unbalanced for puppies and can cause diarrhea and poor growth."),
            ("How much milk can a dog drink?", "Only a small sip now and then, and only if your dog clearly tolerates dairy. Skip it entirely if it causes gas or diarrhea."),
            ("Is cheese okay for dogs?", "Small amounts of plain cheese are usually fine and many dogs tolerate it, but it is calorie-dense, so keep it occasional."),
            ("What should dogs drink instead of milk?", "Water. Every dog should drink water; milk is not a necessary or healthy regular drink."),
            ("My dog drank milk and seems fine — is it okay to keep giving it?", "Some dogs tolerate small amounts. If there are no digestive signs, an occasional sip is fine, but it should never replace water."),
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
        "experts": [
            "The veterinary nutritionists and clinicians of the Cornell Riney Canine Health Center",
            "The veterinarians of the ASPCA Animal Poison Control Center",
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
        "description": "Can dogs have grapes or raisins? No — they can cause sudden kidney failure in dogs, even in tiny amounts. Why there is no safe dose, and what to do next.",
        "lede": "No — grapes and raisins are toxic to dogs and can cause sudden, severe kidney failure. There is no safe amount, so treat any ingestion as an emergency.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Can dogs eat grapes or raisins?</h2>
        <p>No. Grapes and raisins are toxic to dogs and can cause sudden, sometimes fatal kidney failure — and there is no known safe amount. Some dogs have collapsed after a single grape; others have eaten a handful with no immediate effect. Because no one can predict which dog will react, every ingestion is treated as a potential emergency. This is why the question "can dogs have grapes" gets such a flat no: the risk is real even when the dose looks tiny.</p>

        <h2>How many grapes are toxic to a dog?</h2>
        <p>There is no safe dose, and that is the honest answer rather than a scare tactic. The toxic compound in grapes has never been identified, so veterinarians cannot give you a safe threshold the way they can for chocolate. What is well documented is that toxicity varies enormously between individual dogs, and that raisins are simply dried, concentrated grapes.</p>
        <p>As a practical guide, the smaller the dog, the fewer grapes it takes to cause trouble. A 5 kg (11 lb) dog that eats three or four grapes is in the same danger zone as a 30 kg (66 lb) dog that eats a whole bunch. Treat any amount as worth a phone call to your vet:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Grapes that raise concern</th><th style="text-align:left">What to do</th></tr>
          <tr><td>Up to 5 kg (small/toy breeds)</td><td>1–3 grapes</td><td>Call vet / poison control now</td></tr>
          <tr><td>5–10 kg</td><td>3–5 grapes</td><td>Call vet / poison control now</td></tr>
          <tr><td>10–25 kg</td><td>5–10 grapes</td><td>Call vet; expect monitoring</td></tr>
          <tr><td>25 kg and up</td><td>A small handful or more</td><td>Call vet; large dogs are still at risk</td></tr>
        </table>
        <div class="callout warn"><b>Raisins count for more.</b> Because they are dried, the same weight holds roughly four times the grape material. A small box of raisins (about 40 g) can be as dangerous as a large bunch of fresh grapes.</div>

        <h2>What happens after a dog eats grapes — the timeline</h2>
        <p>Symptoms do not always appear right away, which is exactly why waiting is dangerous. The typical progression looks like this:</p>
        <ul>
          <li><b>0–12 hours:</b> Vomiting and diarrhea are often the first signs, sometimes with reduced appetite and restlessness.</li>
          <li><b>12–24 hours:</b> Lethargy, abdominal pain, and unusual thirst may appear as the kidneys come under stress.</li>
          <li><b>24–72 hours:</b> This is the danger window for kidney failure. Urine output can drop (oliguria) and then stop (anuria). At this stage the damage is severe and much harder to reverse.</li>
        </ul>
        <p>Because the worst harm shows up a day or two later, the time to act is <em>before</em> symptoms — the moment you realise your dog ate grapes.</p>

        <h2>What to do right now if your dog ate grapes</h2>
        <div class="callout warn"><b>Call your veterinarian or an animal poison control line immediately.</b> Do not wait for symptoms. Early treatment — inducing vomiting and starting intravenous fluids — dramatically improves the outcome.</div>
        <ul>
          <li>Note <b>how many</b> grapes or raisins and <b>roughly when</b> they were eaten. This tells the vet how aggressive to be.</li>
          <li>Keep grapes, raisins, and anything made with them (bakery items, trail mix, raisin bread) out of reach going forward.</li>
          <li>Do <b>not</b> try to induce vomiting at home with salt or other remedies — that can cause its own emergencies. Let a professional decide.</li>
          <li>Watch over the next days for vomiting, lethargy, reduced appetite, and especially reduced urination.</li>
        </ul>

        <h2>What will the emergency vet do?</h2>
        <p>Knowing the steps lowers panic, and it is worth understanding why speed matters:</p>
        <ul>
          <li><b>Decontamination:</b> If the ingestion was recent (usually within 1–2 hours) and your dog is stable, the vet may induce vomiting and give activated charcoal to limit absorption.</li>
          <li><b>IV fluids:</b> Aggressive fluid therapy for 48–72 hours is the single most important step. It supports the kidneys and helps flush the toxin.</li>
          <li><b>Monitoring:</b> Blood and urine tests track kidney values (BUN, creatinine) so failure is caught early.</li>
        </ul>
        <p>Most dogs treated early and aggressively recover fully. Delay is what turns a manageable scare into real tragedy.</p>

        <h2>Are grape products also unsafe?</h2>
        <p>Yes — toxicity is not limited to the whole fruit. Watch for:</p>
        <ul>
          <li><b>Raisins and sultanas</b> — more concentrated, and easy for a dog to eat in quantity.</li>
          <li><b>Grape juice and wine</b> — the toxic principle survives processing.</li>
          <li><b>Raisin bread, cookies, and trail mix</b> — common culprits because they sit on counters within reach.</li>
          <li><b>Food a child dropped</b> — grape halves and raisins on the floor are a frequent source of "I didn't know he ate one."</li>
        </ul>

        <h2>Grapes vs raisins vs safer fruit</h2>
        <p>If you want a genuinely safe treat, skip grapes and raisins and reach for options that are safe in moderation — <a href="/dog-nutrition/can-dogs-eat-bananas/">banana</a> or <a href="/dog-nutrition/can-dogs-eat-strawberries/">strawberries</a> are good choices. For the complete rundown of what to avoid, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods list</a>. And if your dog is already vomiting, our guide to <a href="/dog-health/dog-vomiting-causes/">dog vomiting causes</a> explains what is urgent versus what can wait.</p>
        """,
        "faq": [
            ("How many grapes are toxic to a dog?", "There is no known safe dose. Even one grape has caused kidney failure in some dogs, so any amount is treated as an emergency."),
            ("Can dogs have grapes in any amount?", "No. Because the toxic compound is unidentified and tolerance varies between dogs, there is no amount considered safe. Treat any ingestion as potentially serious."),
            ("Are raisins as dangerous as grapes?", "Yes — raisins are dried grapes and just as toxic, and because they are concentrated, a small box can be as dangerous as a large bunch of fresh grapes."),
            ("What should I do if my dog ate a grape?", "Call your vet or animal poison control now. Do not wait for symptoms; early inducing of vomiting and IV fluids greatly improve the outcome."),
            ("How long after eating grapes do symptoms appear?", "Vomiting and diarrhea often start within 12 hours, but the most dangerous kidney damage typically develops 24–72 hours later, which is why you must act before symptoms show."),
            ("My dog ate one grape and seems fine — should I still worry?", "Yes. Effects can be delayed by a day or two, and some dogs show no early signs at all. A single grape has caused failure in small dogs, so a vet call is the safe move."),
            ("Can grape juice or wine hurt dogs?", "Yes. The toxic principle survives processing, so grape juice and wine are also unsafe for dogs."),
            ("Will my dog be okay after eating grapes?", "Most dogs treated early and aggressively — with decontamination and 48–72 hours of IV fluids — recover fully. The outcome depends heavily on how quickly treatment begins."),
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
        "experts": [
            "The Veterinary Toxicology team at Pet Poison Helpline",
            "The veterinarians of the ASPCA Animal Poison Control Center",
        ],
        "disclaimer": "This article is general information, not veterinary advice. If your dog may have eaten grapes or raisins, contact a veterinarian or emergency clinic right away.",
    },
    {
        "slug": "can-dogs-eat-chocolate",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Chocolate? NO — It Is Toxic",
        "url": "/dog-nutrition/can-dogs-eat-chocolate/",
        "description": "Is chocolate bad for dogs? Yes — it contains theobromine, which is poisonous to dogs. Learn why dark and baking chocolate are worst, and what to do next.",
        "lede": "No — chocolate is toxic to dogs because it contains theobromine, which they cannot metabolize well. Dark and baking chocolate are the most dangerous.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is chocolate bad for dogs?</h2>
        <p>Yes. Chocolate is toxic to dogs because it contains theobromine (and caffeine), stimulants their bodies break down far more slowly than ours. The theobromine builds up and over-excites the heart and nervous system. This is why "is chocolate bad for dogs" gets an unqualified yes — and why the type and amount matter so much.</p>

        <h2>Why is chocolate toxic to dogs?</h2>
        <p>Humans metabolise theobromine quickly; dogs do not — it can linger in their system for 17–24 hours or more, so even a moderate amount keeps stimulating them the whole time. The darker and purer the chocolate, the more theobromine it carries, which is why baking and dark chocolate are far more dangerous than milk chocolate.</p>

        <h2>How much chocolate is dangerous?</h2>
        <p>The danger depends on two things: the type of chocolate and your dog's weight. Theobromine content varies roughly like this:</p>
        <table>
          <tr><th style="text-align:left">Type of chocolate</th><th style="text-align:left">Theobromine per ounce (approx.)</th><th style="text-align:left">Risk level</th></tr>
          <tr><td>White chocolate</td><td>~1 mg</td><td>Negligible theobromine (but still fat and sugar)</td></tr>
          <tr><td>Milk chocolate</td><td>~45–60 mg</td><td>Mild risk in small dogs</td></tr>
          <tr><td>Dark chocolate</td><td>~130–160 mg</td><td>Dangerous in small amounts</td></tr>
          <tr><td>Semisweet</td><td>~260 mg</td><td>Dangerous</td></tr>
          <tr><td>Baking / unsweetened</td><td>~390–450 mg</td><td>Very dangerous in tiny amounts</td></tr>
          <tr><td>Cocoa powder (dry)</td><td>~800 mg</td><td>Extremely dangerous</td></tr>
        </table>
        <p>As a rough guide, mild signs begin around <b>20 mg of theobromine per kg of body weight</b>, and severe or life-threatening signs around <b>40–50 mg/kg</b>. For a 10 kg (22 lb) dog, that is mild effects from roughly 3–4 oz of milk chocolate but under half an ounce of baking chocolate; for a 25 kg dog, about 9 oz of milk chocolate or just over 1 oz of baking chocolate.</p>
        <div class="callout warn">When in doubt, assume it is serious. Small dogs, dark chocolate, and any baking chocolate or cocoa powder all move quickly into dangerous territory.</div>

        <h2>What are the symptoms of chocolate poisoning?</h2>
        <p>Signs usually appear within a few hours and can escalate. Watch for:</p>
        <ul>
          <li>Restlessness, panting, and a racing heart.</li>
          <li>Vomiting and diarrhea.</li>
          <li>Tremors, muscle twitching, and in severe cases seizures.</li>
          <li>High body temperature and, without treatment, collapse.</li>
        </ul>

        <h2>What to do if your dog eats chocolate</h2>
        <div class="callout warn"><b>Call your veterinarian or an animal poison control line right away.</b> Note the type of chocolate, roughly how much, and your dog's weight — those three facts decide how serious it is.</div>
        <ul>
          <li>Small amounts of milk chocolate may cause only mild upset in a large dog, but any dark, semisweet, or baking chocolate is urgent.</li>
          <li>Keep all chocolate, cocoa powder, and baked goods well out of reach.</li>
          <li>Do not try to make your dog vomit at home — let a professional assess and act.</li>
        </ul>

        <h2>What will the emergency vet do?</h2>
        <ul>
          <li><b>Decontamination:</b> If the chocolate was eaten recently and your dog is stable, the vet may induce vomiting and give activated charcoal.</li>
          <li><b>Supportive care:</b> IV fluids and medications to control heart rate, tremors, and seizures as needed.</li>
          <li><b>Monitoring:</b> Because theobromine lingers, the vet may keep your dog under observation for many hours.</li>
        </ul>

        <h2>Chocolate vs other toxic foods</h2>
        <p>Chocolate is one of several foods that do not belong near dogs. Grapes and raisins are a different but equally serious risk — see our guides to <a href="/dog-nutrition/can-dogs-eat-grapes/">grapes</a> and our full <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods list</a>. If your dog is already vomiting, our <a href="/dog-health/dog-vomiting-causes/">dog vomiting guide</a> explains what is urgent.</p>
        """,
        "faq": [
            ("Is chocolate bad for dogs?", "Yes. Chocolate contains theobromine, which dogs metabolise slowly, so it builds up and over-stimulates the heart and nervous system."),
            ("How much chocolate is toxic to a dog?", "It depends on the type and your dog's weight. Mild signs start around 20 mg of theobromine per kg of body weight; severe signs around 40–50 mg/kg. Dark, semisweet, baking, and cocoa powder are dangerous in small amounts."),
            ("Is dark chocolate worse for dogs than milk chocolate?", "Yes — dark and baking chocolate carry far more theobromine per ounce than milk chocolate and are the most toxic."),
            ("What are the symptoms of chocolate poisoning in dogs?", "Restlessness, panting, a racing heart, vomiting, diarrhea, tremors, and in severe cases seizures. Signs can appear within a few hours."),
            ("What should I do if my dog ate chocolate?", "Call your vet or animal poison control with the type, amount, and your dog's weight as soon as possible. Do not try to induce vomiting at home."),
            ("How long do chocolate poisoning symptoms last in dogs?", "Theobromine lingers in a dog's system for 17–24 hours or more, so the vet may monitor your dog for many hours even after early treatment."),
            ("Can a little milk chocolate hurt a large dog?", "Often it causes only mild upset, but any amount of dark, semisweet, or baking chocolate is urgent, and small dogs are at risk even from milk chocolate."),
            ("Is white chocolate safe for dogs?", "It has almost no theobromine, but it is still high in fat and sugar and is not a treat we recommend giving dogs."),
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
        "experts": [
            "The Veterinary Toxicology team at Pet Poison Helpline",
            "The veterinarians of the ASPCA Animal Poison Control Center",
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
    # ---------------- Dog nutrition: can dogs eat X (batch 1, 2026-10-24) ----------------
    {
        "slug": "can-dogs-eat-blueberries",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Blueberries? Yes — A Tiny Antioxidant Boost",
        "url": "/dog-nutrition/can-dogs-eat-blueberries/",
        "description": "Blueberries are a safe, low-calorie dog treat rich in antioxidants and vitamin C. How many to offer, why they may help aging dogs, and how to serve them safely.",
        "lede": "Yes — blueberries are one of the safest, healthiest treats you can give a dog. They are low in calories and packed with antioxidants, and most dogs love the burst of sweetness.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Are blueberries good for dogs?</h2>
        <p>Blueberries are one of the safest sweet treats you can hand a dog. A cup has about 84 calories and almost no fat, but it carries vitamin C, vitamin K, fiber, and a heavy load of antioxidants — the pigments that give the berry its deep blue color. Those antioxidants are why blueberries show up in senior-dog diets: research in aging dogs has studied antioxidant-rich foods for supporting memory and learning as dogs get older, though the effect in your own dog is modest, not a cure.</p>

        <h2>Blueberry nutrition at a glance</h2>
        <p>For scale, here is what is in roughly one cup (about 148 g) of blueberries:</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount per cup</th></tr>
          <tr><td>Calories</td><td>~84 kcal</td></tr>
          <tr><td>Fiber</td><td>3.6 g</td></tr>
          <tr><td>Vitamin C</td><td>14 mg (about 16% of a person's daily value)</td></tr>
          <tr><td>Vitamin K</td><td>29 mcg (about 24% of a person's daily value)</td></tr>
          <tr><td>Sugar (natural)</td><td>~15 g</td></tr>
        </table>
        <p>These are human nutrition figures, but they show why a few berries are a light, low-fat reward rather than a calorie bomb.</p>

        <h2>How many blueberries can a dog eat?</h2>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. A sensible portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe amount</th></tr>
          <tr><td>Under 5 kg</td><td>2–3 berries, mashed</td></tr>
          <tr><td>5–15 kg</td><td>A small handful (5–8 berries)</td></tr>
          <tr><td>15–30 kg</td><td>Up to 10–15 berries</td></tr>
          <tr><td>30 kg and up</td><td>A generous handful, occasionally</td></tr>
        </table>

        <h2>How to serve them</h2>
        <ul>
          <li>Wash well to remove pesticide residue, then serve fresh or frozen.</li>
          <li>Mash or cut berries for small dogs and puppies — a whole berry can be a choking hazard for a dog that bolts food.</li>
          <li>Mix a few into meals, use them as training rewards, or freeze them for a cooling chew.</li>
          <li>Keep it to plain berries. Skip blueberry muffins, yogurt coatings, and anything sweetened — and never anything with xylitol.</li>
        </ul>
        <div class="callout">Frozen blueberries make a great summer treat, but count them toward the daily treat budget. A dog that gets a lot of treats still needs most calories from a complete dog food.</div>

        <h2>Can puppies eat blueberries?</h2>
        <p>Yes — a mashed berry or two is fine once a puppy is weaned and eating solid food. Their tiny tummies mean keep it to a bite, and watch for any loose stools.</p>

        <h2>Are there any risks?</h2>
        <p>Blueberries are not toxic, and serious reactions are rare. The real watch-items are choking in small dogs (solve by mashing) and the natural sugar, which means diabetic dogs should keep portions tiny and check with a vet. The bigger danger is the vehicle: baked goods, flavored snacks, and "sugar-free" products can carry fat, sugar, or xylitol, none of which belong in a dog's bowl.</p>

        <h2>What if my dog ate a whole pint?</h2>
        <p>A dog that raids a container of blueberries mostly risks a sugary belly ache — gas, loose stools, maybe a briefly upset stomach. That usually passes. Call a vet if there is repeated vomiting, lethargy, or if the berries came with something else (chocolate, xylitol sweetener). Unlike <a href="/dog-nutrition/can-dogs-eat-grapes/">grapes and raisins</a>, blueberries are not a poisoning emergency.</p>

        <h2>Blueberries vs other fruit treats</h2>
        <p>Blueberries sit alongside <a href="/dog-nutrition/can-dogs-eat-bananas/">banana</a> and <a href="/dog-nutrition/can-dogs-eat-strawberries/">strawberries</a> as safe, low-calorie options, while <a href="/dog-nutrition/can-dogs-eat-grapes/">grapes and raisins</a> must never be given because they are toxic. For the full list of what to avoid, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>. To keep treats in check, our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> explains the 10% rule.</p>
        """,
        "faq": [
            ("Can dogs eat blueberry skin?", "Yes — the skin is where most of the antioxidants are, and it is safe. Just wash the berries first."),
            ("Can puppies have blueberries?", "Yes, a mashed berry or two once weaned and on solid food; keep portions tiny and watch for loose stools."),
            ("How many blueberries can a dog eat?", "A few for small dogs, up to a generous handful for large dogs, and only as a treat below 10% of daily calories."),
            ("Are frozen blueberries OK for dogs?", "Yes — plain frozen berries are a safe cooling treat. Avoid anything sweetened or with xylitol."),
            ("Are blueberries good for senior dogs?", "They are rich in antioxidants that studies have linked to supporting aging dog cognition, though the effect is modest, not a treatment."),
            ("Can diabetic dogs eat blueberries?", "Small amounts may be fine, but the natural sugar adds up — check with your vet before making them a regular treat."),
            ("Can dogs eat blueberry muffins?", "No — muffins bring sugar, fat, and sometimes xylitol or grape products. Stick to plain berries."),
            ("What if my dog ate too many blueberries?", "Usually just a sugary stomach upset that passes. Call a vet for repeated vomiting or lethargy, or if other ingredients were involved."),
        ],
        "related": ["can-dogs-eat-strawberries", "can-dogs-eat-bananas", "foods-toxic-to-dogs"],
        "sources": [
            ("AKC — Fruits and Vegetables Dogs Can and Can't Eat",
             "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The canine nutrition specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-pumpkin",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Pumpkin? Yes — Plain, Cooked, and Helpful",
        "url": "/dog-nutrition/can-dogs-eat-pumpkin/",
        "description": "Plain pumpkin is a fiber-rich dog superfood vets recommend for diarrhea and constipation. Why pie filling is dangerous, and exactly how much to add to meals.",
        "lede": "Yes — plain cooked pumpkin (never the sugary pie filling) is one of the most useful foods to add to a dog's bowl. Its fiber helps firm up loose stool and ease mild constipation.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is pumpkin good for dogs?</h2>
        <p>Plain pumpkin is one of the few "people foods" vets routinely suggest for dogs. It is low in calories and rich in soluble fiber, which soaks up excess water in the gut (helping firm up loose stool) and adds gentle bulk (helping mild constipation). That two-way effect is why a spoonful of plain pumpkin is a common first step for a dog with a slightly off tummy — though it is a helper, not a cure for anything serious.</p>

        <h2>Pumpkin nutrition at a glance</h2>
        <p>For scale, here is what is in about one cup of cooked pumpkin (245 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount per cup</th></tr>
          <tr><td>Calories</td><td>~49 kcal</td></tr>
          <tr><td>Protein</td><td>1.8 g</td></tr>
          <tr><td>Fiber</td><td>2.7 g</td></tr>
          <tr><td>Vitamin A</td><td>About 245% of a person's daily value</td></tr>
          <tr><td>Potassium</td><td>Notable amount</td></tr>
        </table>
        <p>Vitamin A is the headline here — pumpkins are among the richest natural sources — but a balanced dog food already covers a dog's needs, so pumpkin is a topper, not a vitamin fix.</p>

        <h2>How much pumpkin for a dog?</h2>
        <p>Start small and build up. A useful daily amount mixed into meals:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Plain pumpkin per day</th></tr>
          <tr><td>Under 5 kg</td><td>1/2–1 teaspoon</td></tr>
          <tr><td>5–15 kg</td><td>1–2 teaspoons</td></tr>
          <tr><td>15–30 kg</td><td>1–2 tablespoons</td></tr>
          <tr><td>30 kg and up</td><td>2–3 tablespoons</td></tr>
        </table>
        <div class="callout">Too much fiber backfires — pile on the pumpkin and you can trade loose stool for gas, bloating, or the other extreme. A little goes a long way.</div>

        <h2>Plain pumpkin vs pumpkin pie filling</h2>
        <div class="callout warn">Never use pumpkin pie filling. It is sweetened and spiced, and the spice mix often includes nutmeg, which contains myristicin and is toxic to dogs. Only ever use 100% plain pumpkin with nothing added.</div>
        <ul>
          <li>Buy canned "100% pumpkin" (not "pumpkin pie mix") and read the label — the only ingredient should be pumpkin.</li>
          <li>Or cook fresh pumpkin plain: peel, remove seeds and stringy bits, steam or bake with no salt, sugar, or butter.</li>
        </ul>

        <h2>Canned or fresh?</h2>
        <p>Both are fine as long as they are plain. Canned 100% pumpkin is convenient and consistent; fresh cooked pumpkin works too. The deciding factor is the label — if it lists sugar, spices, or "pie," it stays in the human pantry.</p>

        <h2>How to serve it</h2>
        <ul>
          <li>Stir the measured amount into your dog's regular food.</li>
          <li>Introduce gradually over a few days so the gut adjusts.</li>
          <li>For a constipated dog, the same small amount helps add bulk — but if there is no stool for more than a day or two, or any vomiting, see a vet.</li>
        </ul>

        <h2>What about pumpkin seeds?</h2>
        <p>Plain, roasted, unsalted pumpkin seeds are not toxic and some owners feed a few ground-up seeds. They contain compounds studied for gently loosening some intestinal parasites, but that is not a substitute for proper veterinary deworming. Keep seeds plain — no salt, no oil, no spice — and only a small sprinkle.</p>

        <h2>Can puppies eat pumpkin?</h2>
        <p>Yes, a tiny amount of plain pumpkin once a puppy is weaned and eating solid food can help with mild tummy upset. Keep portions very small and watch the stool.</p>

        <h2>What if my dog ate pumpkin pie filling?</h2>
        <p>A small lick is unlikely to cause more than a stomach upset, but pie filling's nutmeg is the concern. A large amount, or any signs like disorientation, rapid heartbeat, tremors, or vomiting, means call a vet or poison control. Plain pumpkin itself is the safe choice; the spiced version is the risk.</p>

        <h2>When pumpkin isn't enough</h2>
        <p>Pumpkin is for mild, short-lived gut wobbles. Persistent diarrhea, blood in stool, repeated vomiting, lethargy, or a painful belly are not "add pumpkin" situations — they need a veterinarian. If your dog is already vomiting, our <a href="/dog-health/dog-vomiting-causes/">vomiting guide</a> explains what is urgent. For the broader picture of safe and unsafe foods, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods list</a>.</p>
        """,
        "faq": [
            ("Can dogs eat canned pumpkin?", "Yes — as long as it is 100% plain pumpkin with no added sugar or spices. Avoid pumpkin pie filling."),
            ("Is pumpkin pie filling safe for dogs?", "No — it is sweetened and spiced, and the nutmeg it often contains is toxic to dogs."),
            ("How much pumpkin for dog diarrhea?", "A small daily amount (1/2 tsp for tiny dogs up to 2–3 tbsp for large) can help firm stool, but see a vet if diarrhea persists beyond a day or two."),
            ("Can pumpkin help a constipated dog?", "Yes — its fiber adds bulk, but introduce it gradually and consult a vet if there is no stool for more than a day or two."),
            ("Can puppies eat pumpkin?", "Yes, a tiny amount of plain pumpkin once weaned; keep portions very small and watch the stool."),
            ("Are pumpkin seeds OK for dogs?", "Plain, roasted, unsalted seeds are not toxic in small amounts, but they are not a replacement for veterinary deworming."),
            ("How often can I give my dog pumpkin?", "Small amounts can be added daily as a topper, but keep total treats under about 10% of daily calories."),
            ("Can diabetic dogs eat pumpkin?", "In moderation it can fit a diabetic plan because it is low in calories, but confirm portions with your vet."),
        ],
        "related": ["foods-toxic-to-dogs", "can-dogs-eat-chicken", "how-much-to-feed-my-dog"],
        "sources": [
            ("AKC — Fruits and Vegetables Dogs Can and Can't Eat",
             "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
        ],
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The canine nutrition specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    # ---------------- Dog nutrition: can dogs eat X (batch 2, 2026-10-24) ----------------
    {
        "slug": "can-dogs-eat-sweet-potato",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Sweet Potato? Yes — Cooked, Plain",
        "url": "/dog-nutrition/can-dogs-eat-sweet-potato/",
        "description": "Can dogs eat sweet potato? Yes — cooked, plain, and packed with fiber and vitamin A. Why you should skip the skin and spices, and how much to feed by weight.",
        "lede": "Yes — plain cooked sweet potato is one of the better carbohydrate treats you can share. It is packed with fiber and vitamin A, but only once it is cooked and freed of skin, salt, and spices.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is sweet potato good for dogs?</h2>
        <p>Plain cooked sweet potato is a genuinely useful carb to share. A serving brings beta-carotene (the plant form of vitamin A), fiber, vitamin C, vitamin B6, and potassium, with almost no fat. That nutrient mix is why sweet potato shows up as the carbohydrate in many sensitive-stomach and limited-ingredient dog foods. It is a step up from plain white potato in nutritional density — though, like any carb, it belongs in the treat budget, not as a free-for-all.</p>

        <h2>Sweet potato nutrition at a glance</h2>
        <p>For scale, here is roughly what is in one cup of cooked, mashed sweet potato (about 200 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount per cup</th></tr>
          <tr><td>Calories</td><td>~180 kcal</td></tr>
          <tr><td>Fiber</td><td>6.6 g</td></tr>
          <tr><td>Vitamin A</td><td>About 214% of a person's daily value</td></tr>
          <tr><td>Vitamin C</td><td>~24% of a person's daily value</td></tr>
          <tr><td>Potassium</td><td>Notable amount</td></tr>
        </table>
        <p>Vitamin A is the headline — sweet potato is one of the richest natural sources — but a balanced dog food already covers a dog's needs, so think of sweet potato as a topper, not a vitamin fix.</p>

        <h2>How much sweet potato for a dog?</h2>
        <p>Sweet potato is more calorie-dense than people expect, so keep it occasional. A sensible portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe amount (cooked)</th></tr>
          <tr><td>Under 5 kg</td><td>1–2 teaspoons mashed</td></tr>
          <tr><td>5–15 kg</td><td>1–2 tablespoons</td></tr>
          <tr><td>15–30 kg</td><td>2–3 tablespoons</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/4 cup, occasionally</td></tr>
        </table>
        <div class="callout">Sweet potato is not a low-calorie treat despite the "vegetable" label — a cup is around 180 calories. Count it toward the daily treat budget so it does not crowd out balanced food.</div>

        <h2>How to serve it</h2>
        <ul>
          <li>Steam or bake plain, with no salt, butter, oil, or spices.</li>
          <li>Mash it or cut it into small soft cubes for easy eating.</li>
          <li>If keeping the skin on, scrub it very well; many owners simply peel it to be safe.</li>
          <li>Skip sweet potato fries, sweet potato pie, and candied yams — the oil, sugar, and spices are the problem, not the vegetable.</li>
        </ul>

        <h2>Never give raw sweet potato</h2>
        <p>Raw sweet potato is hard to digest and a choking and blockage hazard, especially for a dog that gulps food. It must be fully cooked before it reaches the bowl.</p>

        <h2>Can puppies eat sweet potato?</h2>
        <p>Yes — a small amount of plain cooked sweet potato is fine once a puppy is weaned and eating solid food. Their smaller digestive systems mean keep it to a spoonful and watch the stool.</p>

        <h2>Sweet potato vs white potato</h2>
        <p>Both are safe once cooked, but they are not equal. Sweet potato wins on fiber and vitamin A. White potato must be cooked too — raw or green potatoes contain solanine, a compound that is toxic to dogs, so never offer those. For the full rundown of what to avoid, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods list</a>. If you want a gentle gut soother instead, <a href="/dog-nutrition/can-dogs-eat-pumpkin/">plain pumpkin</a> does a similar job with even less risk.</p>

        <h2>Are there risks?</h2>
        <p>Sweet potato is healthy for most dogs, but three watch-items apply: the natural sugar means diabetic dogs should keep portions tiny and check with a vet; the carb load means overweight or pancreatitis-prone dogs should limit it; and the high fiber means a large serving in one sitting can cause gas or diarrhea. The leafy tops and vines should not be fed.</p>

        <h2>What if my dog ate too much?</h2>
        <p>A dog that overloads on sweet potato mostly risks gas, bloating, and loose stools from the fiber and starch — usually mild and self-limiting with water and a bland next meal. Call a vet if there is repeated vomiting, a painful swollen belly, no stool, or signs of pancreatitis (hunched posture, appetite loss). To keep treats in check, our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> explains the 10% rule.</p>
        """,
        "faq": [
            ("Can dogs eat sweet potato skin?", "Scrubbed and fully cooked skin is not toxic, but it is harder to digest — many owners peel it. The key is that the sweet potato is cooked, never raw."),
            ("Can dogs eat raw sweet potato?", "No — raw sweet potato is hard to digest and a choking or blockage risk. Always cook it first."),
            ("How much sweet potato can a dog eat?", "A teaspoon or two for small dogs up to about 1/4 cup for large dogs, only as an occasional treat below 10% of daily calories."),
            ("Is sweet potato good for diabetic dogs?", "It is naturally high in sugar, so portions should be tiny and cleared with your vet before it becomes a regular treat."),
            ("Can puppies eat sweet potato?", "Yes, a small amount of plain cooked sweet potato once weaned; keep portions tiny and watch for loose stools."),
            ("Is sweet potato or white potato better for dogs?", "Sweet potato is more nutritious (more fiber and vitamin A). White potato must be cooked too, because raw or green potato contains solanine, which is toxic."),
            ("Can dogs eat sweet potato fries?", "No — frying adds fat and the salt and spices are unnecessary. Only plain cooked sweet potato belongs in the bowl."),
            ("What if my dog ate too much sweet potato?", "Usually just gas and diarrhea that pass. Call a vet for repeated vomiting, a painful belly, no stool, or signs of pancreatitis."),
        ],
        "related": ["can-dogs-eat-pumpkin", "can-dogs-eat-chicken", "how-much-to-feed-my-dog"],
        "sources": [
            ("AKC — Fruits and Vegetables Dogs Can and Can't Eat",
             "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The canine nutrition specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-rice",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Rice? Yes — Plain White Rice for Upset Tummies",
        "url": "/dog-nutrition/can-dogs-eat-rice/",
        "description": "Plain white rice is the classic bland meal for a dog with an upset tummy. Why unseasoned matters, how it pairs with chicken, and how much is safe. Stick to plain.",
        "lede": "Yes — plain cooked white rice is one of the safest, most digestible foods for dogs, and it is the backbone of the standard bland diet vets recommend for mild tummy upset.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is rice good for dogs?</h2>
        <p>Plain white rice is about as gentle as food gets. It is low in fiber and fat and easy to digest, which is exactly why vets point to boiled white rice with plain boiled chicken as the standard bland diet for a dog with mild diarrhea or a sensitive stomach. It is not a nutrient powerhouse, but it gives a recovering gut an easy source of energy while things settle.</p>

        <h2>White rice vs brown rice</h2>
        <p>White rice is lower in fiber and the easier choice during active tummy trouble. Brown rice keeps more fiber and nutrients, so it can suit a healthy dog as an everyday carb — but that extra fiber can be too much for a gut that is already upset. Rule of thumb: white rice for an upset stomach, brown rice for a healthy dog's regular meals.</p>

        <h2>Rice nutrition at a glance</h2>
        <p>For scale, here is roughly what is in one cup of cooked white rice (about 158 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount per cup</th></tr>
          <tr><td>Calories</td><td>~205 kcal</td></tr>
          <tr><td>Fat</td><td>0.4 g</td></tr>
          <tr><td>Carbohydrate</td><td>~45 g</td></tr>
          <tr><td>Fiber</td><td>0.6 g</td></tr>
          <tr><td>Protein</td><td>~4 g</td></tr>
        </table>
        <p>Low fat and low fiber are the features that make it a gut soother — not a nutrition supplement.</p>

        <h2>How much rice for a dog?</h2>
        <p>As a bland meal, a useful amount by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Plain cooked rice</th></tr>
          <tr><td>Under 5 kg</td><td>1–2 tablespoons</td></tr>
          <tr><td>5–15 kg</td><td>1/4–1/3 cup</td></tr>
          <tr><td>15–30 kg</td><td>1/2 cup</td></tr>
          <tr><td>30 kg and up</td><td>1/2–1 cup, per vet guidance</td></tr>
        </table>
        <div class="callout">Rice alone is not a complete diet. It is a short-term soother or a small part of balanced meals — a dog cannot live on plain rice long term.</div>

        <h2>How to serve it</h2>
        <ul>
          <li>Boil plain with no salt, oil, butter, or seasoning.</li>
          <li>For an upset stomach, mix with <a href="/dog-nutrition/can-dogs-eat-chicken/">plain boiled chicken</a> (no skin, no bones, no seasoning) — the classic bland combo.</li>
          <li>Let it cool before serving.</li>
        </ul>

        <h2>The real danger: table scraps and seasonings</h2>
        <div class="callout warn">Never feed a dog seasoned or leftover rice. Human rice often contains onion or garlic — both are toxic to dogs and can damage red blood cells — plus salt and oil a dog does not need. Only plain, unseasoned rice is safe.</div>

        <h2>Can puppies eat rice?</h2>
        <p>Yes — plain white rice is a common, easily digested bland meal for puppies with mild tummy upset. Keep portions small for their size.</p>

        <h2>Are there risks?</h2>
        <p>Plain rice is low-risk, but a few points matter: white rice spikes blood sugar quickly, so diabetic dogs need smaller portions (a vet may prefer brown rice or a different carb); long-term rice-only feeding is nutritionally incomplete; and any rice with onion, garlic, salt, or oil is off the menu. For the full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</p>

        <h2>When rice isn't enough</h2>
        <p>Rice is for short-lived, mild gut wobbles. Persistent vomiting or diarrhea, blood in stool, lethargy, or a painful belly are not "feed more rice" situations — they need a veterinarian. If your dog is already vomiting, our <a href="/dog-health/dog-vomiting-causes/">vomiting guide</a> explains what is urgent, and our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers portion basics.</p>
        """,
        "faq": [
            ("Can dogs eat white rice every day?", "Short-term, as a bland diet, yes. Long term, rice alone is not complete — most calories should come from balanced dog food."),
            ("Is brown rice better than white rice for dogs?", "Brown rice has more fiber and nutrients but is harder to digest; white rice is the better choice for an upset stomach, brown for a healthy dog's regular meals."),
            ("Can dogs eat rice with chicken?", "Yes — plain boiled chicken with plain white rice is the standard bland meal vets recommend for mild tummy upset."),
            ("Can dogs eat fried rice or leftovers?", "No — leftover rice often contains onion, garlic, salt, or oil, and onion and garlic are toxic to dogs. Only plain unseasoned rice is safe."),
            ("How much rice for a dog with diarrhea?", "Small amounts of plain white rice with boiled chicken can help, but see a vet if diarrhea lasts more than a day or two."),
            ("Can puppies eat rice?", "Yes — plain white rice is a gentle, easily digested bland meal for puppies with mild stomach upset."),
            ("Can diabetic dogs eat rice?", "White rice raises blood sugar quickly, so portions should be small and cleared with your vet, who may suggest brown rice or another carb."),
            ("Can dogs eat plain rice cakes?", "A plain, unsalted rice cake is not toxic and can be an occasional low-fat chew, but it adds little nutrition — keep it rare and unseasoned."),
        ],
        "related": ["can-dogs-eat-chicken", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The canine nutrition specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-cucumber",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Cucumber? Yes — a Low-Calorie Crunch",
        "url": "/dog-nutrition/can-dogs-eat-cucumber/",
        "description": "Cucumber is a safe, low-calorie, hydrating crunch that most dogs love. Peel it first, skip the pickles, and learn exactly how much to feed by body weight.",
        "lede": "Yes — cucumber is a safe, crunchy, near-zero-calorie treat that is mostly water, so it is a great low-fat option for dogs, including those watching their weight. Peel it, and skip the pickles.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is cucumber good for dogs?</h2>
        <p>Cucumber is about 96% water and very low in calories — roughly 8 calories in a half-cup of slices. That makes it one of the lightest treats you can offer, especially useful for overweight dogs or as a cooling snack on a warm day. It brings a little vitamin K, vitamin C, and potassium, but the real selling point is hydration and crunch with almost no fat or sugar.</p>

        <h2>Which part of the cucumber can a dog eat?</h2>
        <p>The flesh is the safe part. A few cautions on the rest:</p>
        <ul>
          <li><b>Peel:</b> the skin is where pesticide residue concentrates, and it can be a choking or gut irritant for small dogs. Peel it, especially if the cucumber is not organic.</li>
          <li><b>Seeds:</b> a few seeds are harmless, but they add bulk and can upset a sensitive stomach, so scoop them out for toy breeds.</li>
          <li><b>Flesh:</b> the safe, hydrating part — slice thin or into small cubes.</li>
        </ul>
        <div class="callout">Wash the whole cucumber before cutting, even though you peel it — dogs lick the cut surface, so surface dirt and wax matter.</div>

        <h2>Cucumber nutrition at a glance</h2>
        <p>For scale, here is roughly what is in half a cup of sliced cucumber (about 52 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount</th></tr>
          <tr><td>Calories</td><td>~8 kcal</td></tr>
          <tr><td>Water</td><td>~96%</td></tr>
          <tr><td>Carbohydrate</td><td>~1.9 g</td></tr>
          <tr><td>Fiber</td><td>~0.3 g</td></tr>
          <tr><td>Vitamin K</td><td>small amount</td></tr>
          <tr><td>Vitamin C</td><td>small amount</td></tr>
        </table>
        <p>Low calorie and high water are the features that make it a diet-friendly crunch, not a nutrition supplement.</p>

        <h2>How much cucumber is safe?</h2>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. A sensible portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe treat amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>2–3 thin slices (about 1 tbsp diced)</td></tr>
          <tr><td>5–15 kg</td><td>A small handful of slices (2–3 tbsp)</td></tr>
          <tr><td>15–30 kg</td><td>Up to 1/4 cup sliced</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/2 cup sliced, occasionally</td></tr>
        </table>

        <h2>How to serve it</h2>
        <ul>
          <li>Peel, then slice thin or cut into small cubes.</li>
          <li>Remove seeds for very small dogs.</li>
          <li>For a cooling chew, freeze thin slices — a safe summer ice treat.</li>
          <li>Offer plain. No salt, oil, dressing, or dip.</li>
        </ul>

        <h2>Can puppies eat cucumber?</h2>
        <p>Yes, in small amounts once they are weaned and eating solid food. Puppies have smaller tummies, so keep it to a slice or two and watch for loose stools.</p>

        <h2>The real danger: pickles and seasonings</h2>
        <div class="callout warn">Never feed a dog pickles, cucumber salad, or seasoned cucumber. Pickles are loaded with salt and often contain garlic or onion — both toxic to dogs — plus vinegar and spices a dog does not need. Only plain, unseasoned cucumber is safe.</div>

        <h2>What if my dog ate a pickle?</h2>
        <p>A small bite of a plain dill pickle is unlikely to be dangerous beyond extra salt, but if it contained garlic or onion, or the dog ate a lot, call your vet or a poison helpline. Watch for vomiting, diarrhea, lethargy, or excessive thirst. For the full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</p>

        <h2>Cucumber vs other crunchy treats</h2>
        <p>Cucumber is a lighter choice than many fruits. <a href="/dog-nutrition/can-dogs-eat-watermelon/">Watermelon</a> is another safe, hydrating option (flesh only), while <a href="/dog-nutrition/can-dogs-eat-grapes/">grapes and raisins</a> must never be given because they are toxic. Keep treats small and see our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> for portion basics.</p>
        """,
        "faq": [
            ("Can dogs eat cucumber skin?", "It is safest to peel it — the skin holds pesticide residue and can irritate a small dog's gut. Peel, especially if not organic."),
            ("Is cucumber good for overweight dogs?", "Yes — at about 8 calories per half-cup, it is one of the lightest treats you can give a dog watching its weight."),
            ("Can dogs eat pickles?", "No — pickles are high in salt and often contain garlic or onion, both toxic to dogs. Only plain cucumber is safe."),
            ("Can puppies eat cucumber?", "Yes, a slice or two once weaned and on solid food — peeled, seeded for tiny breeds, and watch for loose stools."),
            ("How much cucumber can a dog eat?", "Keep treats under about 10% of daily calories: a few slices for a small dog, up to half a cup for a large one, and only occasionally."),
            ("Can dogs eat frozen cucumber?", "Yes — plain frozen thin slices are a safe cooling summer snack. Never add salt, sugar, or syrup."),
            ("Can dogs eat cucumber seeds?", "A few seeds are harmless, but scoop them out for toy breeds to avoid an upset stomach."),
            ("What if my dog ate a pickle?", "A small plain dill bite is usually just extra salt; if it had garlic or onion, or the dog ate a lot, call your vet and watch for vomiting or lethargy."),
        ],
        "related": ["can-dogs-eat-watermelon", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The canine nutrition specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "disclaimer": "Nutrition information only; not a substitute for veterinary dietary advice, especially for dogs with health conditions.",
    },
    {
        "slug": "can-dogs-eat-broccoli",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Broccoli? Yes — in Small Amounts",
        "url": "/dog-nutrition/can-dogs-eat-broccoli/",
        "description": "Broccoli is a safe, nutrient-rich vegetable for dogs, but only in small amounts. Why too much can upset the gut, and how to serve it plain and cooked.",
        "lede": "Yes — broccoli is safe and genuinely healthy for dogs in small amounts. The catch is that too much can irritate the stomach and, in large doses, affect the thyroid, so portion control is the whole game.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is broccoli safe for dogs?</h2>
        <p>Both the florets and the stalk are non-toxic and packed with good things — vitamin C, vitamin K, fiber, and antioxidants. The issue is quantity. Broccoli contains isothiocyanates, compounds that in large amounts can cause mild to severe gastric irritation in dogs. The widely cited rule of thumb is that broccoli (and any treat) should make up no more than about 10% of daily calories, and some sources note the isothiocyanate risk rises sharply above that.</p>

        <h2>Broccoli nutrition at a glance</h2>
        <p>For scale, here is roughly what is in half a cup of chopped broccoli (about 45 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount</th></tr>
          <tr><td>Calories</td><td>~15 kcal</td></tr>
          <tr><td>Carbohydrate</td><td>~3 g</td></tr>
          <tr><td>Fiber</td><td>~1.5 g</td></tr>
          <tr><td>Vitamin C</td><td>good source</td></tr>
          <tr><td>Vitamin K</td><td>good source</td></tr>
          <tr><td>Protein</td><td>~1.5 g</td></tr>
        </table>
        <p>Low calorie and high in vitamins — a genuinely healthy bite when the portion is small.</p>

        <h2>How much broccoli is safe?</h2>
        <p>Keep broccoli to about 10% of daily calories or less. A practical portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe broccoli amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>1–2 small florets (about 1 tbsp chopped)</td></tr>
          <tr><td>5–15 kg</td><td>A few small florets (1–2 tbsp)</td></tr>
          <tr><td>15–30 kg</td><td>Up to 1/4 cup chopped</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/2 cup chopped, occasionally</td></tr>
        </table>
        <div class="callout">The 10% rule is the line. Push much beyond it and the isothiocyanates can cause drooling, gas, and an upset stomach — and very large amounts are a real concern for the thyroid.</div>

        <h2>Raw vs cooked</h2>
        <p>Both work. Lightly steamed broccoli is easier to digest and softer on the gut; raw florets give a satisfying crunch but are tougher to break down. Either way, cut into small pieces so a dog cannot choke, especially on the stalk.</p>

        <h2>How to serve it</h2>
        <ul>
          <li>Plain, with no butter, oil, salt, cheese sauce, or seasoning.</li>
          <li>Steam or boil briefly, or offer raw florets in small pieces.</li>
          <li>Chop the stalk fine — it is the most common choking hazard.</li>
          <li>Let it cool before serving.</li>
        </ul>

        <h2>Can puppies eat broccoli?</h2>
        <p>Yes, in tiny amounts once weaned and on solid food. Puppies have sensitive tummies, so a floret or two and watch for gas or loose stools.</p>

        <h2>What to avoid</h2>
        <div class="callout warn">Never serve broccoli with garlic, onion, butter, or cheese sauce — garlic and onion are toxic to dogs, and the fats add needless calories and gut risk. Only plain broccoli is safe. For the full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</div>

        <h2>When broccoli isn't enough</h2>
        <p>Broccoli is a small, healthy extra — not a meal and not a fix for a sick dog. Persistent vomiting or diarrhea, lethargy, or a painful belly need a veterinarian, not more vegetables. Our <a href="/dog-health/dog-vomiting-causes/">vomiting guide</a> explains what is urgent, and our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers portion basics.</p>
        """,
        "faq": [
            ("Can dogs eat broccoli raw or cooked?", "Both are safe. Lightly steamed is easier to digest; raw florets are a safe crunch. Cut small to avoid choking."),
            ("Why is too much broccoli bad for dogs?", "Large amounts of isothiocyanates in broccoli can irritate the gut and, in big doses, affect the thyroid, so keep it under about 10% of daily calories."),
            ("Can dogs eat broccoli stalks?", "Yes, but chop them finely — the stalk is the main choking hazard. The florets are the easiest part to serve."),
            ("Can puppies eat broccoli?", "Yes, a floret or two once weaned and on solid food — watch for gas or loose stools."),
            ("How much broccoli can a dog eat?", "Keep it to about 10% of daily calories: a couple of small florets for a small dog, up to half a cup chopped for a large one."),
            ("Can dogs eat broccoli with cheese or butter?", "No — cheese sauce and butter add fat a dog does not need, and never add garlic or onion, which are toxic. Only plain broccoli is safe."),
            ("Is broccoli good for overweight dogs?", "Yes — at about 15 calories per half-cup and high in fiber, it is a filling, low-calorie treat in small amounts."),
            ("What if my dog ate a lot of broccoli?", "Mild cases cause gas and an upset stomach that pass. Call a vet for repeated vomiting, lethargy, or if a large amount was eaten, since very high doses concern the thyroid."),
        ],
        "related": ["foods-toxic-to-dogs", "how-much-to-feed-my-dog", "can-dogs-eat-carrots"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The canine nutrition specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
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
        "can-dogs-eat-grapes",
        "can-dogs-eat-chocolate",
        "can-dogs-eat-milk",
        "foods-toxic-to-dogs",
        "how-to-stop-puppy-biting",
        "dog-vomiting-causes",
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
    <p>We have written out our full research, review, and correction process on the <a href="/about/editorial-standards/">Editorial &amp; Medical Review Standards</a> page — including our no-fabricated-credentials rule and the exact sources we cite.</p>
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

CONTACT = {
    "url": "/contact/",
    "title": "Contact WagWise Pet",
    "description": "Reach the WagWise Pet team at contact@wagwise.org for corrections, feedback, or guide suggestions about dog and cat care. We reply within two business days.",
    "body": """
    <h1>Contact WagWise Pet</h1>
    <p>The fastest way to reach us is email: <a href="mailto:contact@wagwise.org">contact@wagwise.org</a>. We read everything and reply within two business days, usually sooner.</p>
    <h2>What to write to us about</h2>
    <ul>
      <li><strong>Corrections.</strong> If a guide contradicts the source it cites, or a rate has changed, tell us. Substantive corrections are reflected in the check date on that guide.</li>
      <li><strong>Guide requests.</strong> Tell us the question you could not find an answer to. Most of our topics started as reader questions.</li>
      <li><strong>Feedback.</strong> If a guide was unclear, too long, or missed the point, that is exactly what we want to hear.</li>
    </ul>
    <h2>What we cannot do</h2>
    <p>We are writers, not veterinarians. We cannot diagnose your pet, review X-rays, or advise on medication — for anything urgent or medical, please contact a licensed vet. Everything on this site is general information, not veterinary advice.</p>
    <h2>For product and partnership enquiries</h2>
    <p>Use the same address. We test what we recommend and say so when a link is an affiliate link; we do not publish paid placements disguised as guides.</p>
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

EDITORIAL = {
    "url": "/about/editorial-standards/",
    "title": "Editorial & Medical Review Standards — WagWise Pet",
    "description": "How WagWise Pet researches, reviews, and corrects every dog and cat care guide — including our no-fabricated-credentials rule and the veterinary sources we cite.",
    "body": """
    <h1>Editorial &amp; Medical Review Standards</h1>
    <p>WagWise Pet is an independent pet care resource written for everyday dog and cat owners. Because most of what we publish touches health or behaviour, we hold it to a clear standard. This page explains exactly how a guide is built, who stands behind it, and what we will not do.</p>

    <h2>Who writes and reviews WagWise</h2>
    <p>Guides are researched and written by the WagWise editorial team — a group of writers who specialise in reading and summarising veterinary and training literature in plain language. <strong>We do not invent individual authors or reviewers.</strong> No article on this site claims to be written or reviewed by a named veterinarian unless a real, verifiable veterinarian did so. Where a topic is medical, we point you to a licensed vet rather than pretending to be one. Our authority comes from the sources we cite, not from a borrowed white coat.</p>

    <h2>Expert citations, not borrowed authority</h2>
    <p>Because our topics are medical, we cite the <em>named</em> veterinary experts and specialist teams behind the guidance we summarise — for example the Veterinary Toxicology team at Pet Poison Helpline, or the veterinarians at the ASPCA Animal Poison Control Center. These appear in two places on every relevant article:</p>
    <ul>
      <li>The <strong>Sources</strong> block lists the public references, each linked so you can read them yourself.</li>
      <li>The <strong>Expert sources</strong> block names the veterinary experts and teams whose published work underpins the article.</li>
    </ul>
    <p>This is honest attribution: we are summarising experts' published guidance, and we say so by name. It is <strong>not</strong> the same as claiming those experts reviewed or approved this specific article — we never do that unless they actually did. The distinction matters: a fabricated "reviewed by Dr. X" line would be deceptive and would be penalised by search engines, whereas transparent citation of real experts strengthens trust without lying.</p>

    <h2>How we research a guide</h2>
    <p>Every health or behaviour claim is checked against named, public reference organisations rather than against other blogs. The core sources we draw on include:</p>
    <ul>
      <li>The American Kennel Club (AKC) — expert advice library</li>
      <li>The American Veterinary Medical Association (AVMA)</li>
      <li>The ASPCA — animal poison control and behaviour guidance</li>
      <li>The Merck Veterinary Manual</li>
      <li>Cornell Feline Health Center</li>
      <li>International Cat Care</li>
      <li>The American Veterinary Society of Animal Behavior (AVSAB)</li>
    </ul>
    <p>You can see the exact sources for any guide at the bottom of that article, with links out, so you can check us rather than trust us.</p>

    <h2>The check-date system</h2>
    <p>Every guide carries a "checked" date under its Sources block. That date is the last time the facts were compared against those references — not the day the page was first published or reformatted. When a source updates (a fee change, a revised guideline, new research), we revisit the guide and move the check date forward. Substantive corrections are reflected in that date too.</p>

    <h2>We separate urgent from optional</h2>
    <p>Where a symptom needs same-day veterinary care, the guide says so at the point where it matters — not in a vague warning at the end. We would rather tell you to call a vet than risk you waiting on a blog post.</p>

    <h2>No fear-mongering, no guarantees</h2>
    <p>We do not promise outcomes, and we do not stretch a study's finding further than the source does. Pet health content earns trust by being calm and accurate, not by being alarming.</p>

    <h2>Corrections policy</h2>
    <p>If something here is wrong, out of date, or contradicts the source we cited, tell us at <a href="mailto:contact@wagwise.org">contact@wagwise.org</a> with the page address and the source that disagrees. We fix it, move the check date, and note the change. We would rather be correct than defensive.</p>

    <h2>How we make money</h2>
    <p>Some product pages contain affiliate links. If you buy through them, we may earn a small commission at no extra cost to you. Our picks are based on usefulness, never on commission, and we label affiliate links as such.</p>

    <h2>WagWise is not a veterinary practice</h2>
    <p>This site is general information, not veterinary advice, diagnosis, or treatment. For anything urgent, medical, or about your specific pet, contact a licensed veterinarian or your nearest animal clinic. In an emergency, do not wait for a website.</p>
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
