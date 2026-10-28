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
            "can-dogs-eat-green-beans", "can-dogs-eat-pineapple",
            "can-dogs-eat-mango", "can-dogs-eat-potato",
            "can-dogs-eat-spinach", "can-dogs-eat-tomato",
            "can-dogs-eat-bread", "can-dogs-eat-popcorn",
            "can-dogs-eat-honey", "can-dogs-eat-yogurt",
            "can-dogs-eat-salmon", "can-dogs-eat-shrimp",
            "can-dogs-eat-peas", "can-dogs-eat-corn",
            "can-dogs-eat-onion", "can-dogs-eat-garlic",
            "can-dogs-eat-macadamia-nuts", "can-dogs-eat-cherries",
            "can-dogs-eat-peaches", "can-dogs-eat-plums",
            "can-dogs-eat-xylitol", "can-dogs-eat-alcohol",
            "can-dogs-eat-caffeine", "can-dogs-eat-raw-dough",
            "can-dogs-eat-almonds", "can-dogs-eat-walnuts",
            "can-dogs-eat-ham", "can-dogs-eat-ice-cream",
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
        <h2>The four tiers, in one table</h2>
        <p>Most "toxic food" lists are a flat alphabetical dump, which is not how an owner needs the information at 10pm. What matters is how fast you have to act. These four tiers sort the same foods by the decision they trigger, and every item links to a full write-up with doses and symptoms.</p>
        <table>
          <tr><th style="text-align:left">Tier</th><th style="text-align:left">Foods</th><th style="text-align:left">What it means</th></tr>
          <tr><td><b>1. Never — call the vet</b></td><td>Chocolate, grapes and raisins, onions, garlic, xylitol, alcohol, caffeine, macadamia nuts, raw yeast dough</td><td>Any amount in a small dog is a phone call at minimum. Several are emergencies regardless of dose.</td></tr>
          <tr><td><b>2. High risk — depends on dose</b></td><td>Avocado, cherry and peach and plum stones, walnuts, potato (raw or green), tomato leaves, salt, cooked bones</td><td>Often survivable, sometimes not. The dose and the size of the dog decide it.</td></tr>
          <tr><td><b>3. Caution — small amounts only</b></td><td>Milk, cheese, ice cream, ham, honey, bread, popcorn, corn on the cob, almonds, spinach, salmon, shrimp, eggs</td><td>Not poisonous, but fat, salt, lactose or a physical hazard. Measure rather than guess.</td></tr>
          <tr><td><b>4. Safe in moderation</b></td><td>Apples, bananas, blueberries, strawberries, watermelon, pumpkin, sweet potato, rice, cucumber, broccoli, green beans, pineapple, mango, peas, carrots, plain yoghurt, plain peanut butter, cooked chicken</td><td>Fine as treats, inside the 10% calorie budget, prepared correctly.</td></tr>
        </table>

        <h2>Tier 1 in detail — the ones that actually kill</h2>
        <p><b>Chocolate.</b> The toxin is theobromine and the dose is everything. Roughly: white chocolate 0.25 mg per gram, milk chocolate 2.4, dark chocolate 5 to 6, unsweetened baking chocolate 16 to 26, cocoa powder around 26 mg per gram. Signs start at about 20 mg per kg of body weight, heart rhythm problems appear around 40 to 50, and seizures above 60. A 10 kg dog eating 100 g of dark chocolate takes in roughly 550 mg — 55 mg per kg, squarely in the cardiac range. The same weight of milk chocolate lands at 24 mg per kg: upset stomach territory, not emergency territory. That gap is why "how much chocolate" has no single answer, and why the calculator matters more than the rule.</p>
        <p><b>Grapes and raisins.</b> No known safe dose. The mechanism is still unidentified, and individual dogs vary enormously — some eat a handful with no effect, others go into kidney failure from a few. Because the sensitivity cannot be predicted, any ingestion is treated as serious. Raisins are worse by weight, since drying concentrates whatever the toxin is.</p>
        <p><b>Xylitol.</b> A sugar alcohol in sugar-free gum, some mints, some peanut butters and an increasing number of "no added sugar" products. About 0.1 g per kg causes dangerous hypoglycaemia within 30 minutes; around 0.5 g per kg brings liver injury into play. For a 10 kg dog, that first threshold is one gram — less than a single stick of gum.</p>
        <p><b>Onions and garlic.</b> Both damage red blood cells; garlic is the more concentrated of the two. A single large ingestion causes haemolytic anaemia, but repeated small amounts in leftovers do the same thing slowly, which is how it is usually missed. Signs can take days to appear — pale gums, weakness, dark urine.</p>
        <p><b>Alcohol and raw dough.</b> Ethanol is ethanol whatever the source. Bread dough is a double problem: it rises in the warm stomach and distends it, and it ferments into alcohol while it sits there. A dog that ate dough is both bloated and drunk.</p>

        <h2>The dose that matters: a reference table</h2>
        <table>
          <tr><th style="text-align:left">Substance</th><th style="text-align:left">Threshold for concern</th><th style="text-align:left">First signs</th></tr>
          <tr><td>Chocolate (theobromine)</td><td>20 mg/kg mild, 40–50 mg/kg cardiac, 60+ seizures</td><td>Vomiting, restlessness, racing heart</td></tr>
          <tr><td>Xylitol</td><td>0.1 g/kg hypoglycaemia, 0.5 g/kg liver</td><td>Wobbling, weakness, collapse within 30 min</td></tr>
          <tr><td>Grapes and raisins</td><td>No known safe dose</td><td>Vomiting, then lethargy 12–24 h later</td></tr>
          <tr><td>Onion and garlic</td><td>Large single dose, or repeated small amounts</td><td>Pale gums, weakness, dark urine after 2–5 days</td></tr>
          <tr><td>Alcohol</td><td>Roughly 5.5 g/kg is life-threatening</td><td>Wobbling, vomiting, low body temperature</td></tr>
          <tr><td>Caffeine</td><td>20 mg/kg signs, 140 mg/kg severe</td><td>Restlessness, panting, tremors</td></tr>
          <tr><td>Macadamia nuts</td><td>Around 2 g/kg</td><td>Hind-leg weakness, tremors, fever</td></tr>
        </table>

        <h2>The eight symptoms that mean poisoning</h2>
        <p>Poisoning does not announce itself with one clean sign. The pattern to watch for is a dog that was normal an hour ago and is now some combination of: vomiting, drooling more than usual, tremors or twitching, wobbling or unable to stand, panting at rest, a racing or irregular heartbeat, gums that are pale or brick-red, and collapse. Seizures and bloody diarrhoea are late signs, not early ones.</p>
        <p>Two behavioural signals are easy to dismiss and worth taking seriously: a dog that has suddenly gone very quiet and hidden, and a dog that is pressing its head against a wall or the back of the sofa. Both suggest something neurological rather than a stomach upset.</p>

        <h2>The first ten minutes</h2>
        <p><b>1. Remove access.</b> Move the dog away from the source, then secure the packaging. You will need it.</p>
        <p><b>2. Work out what and how much.</b> The three numbers every vet or poison line will ask for: what was eaten, how much, and the dog's weight. The wrapper gives you the first two, and the cocoa percentage if it is chocolate.</p>
        <p><b>3. Call before you act.</b> Your vet, the practice's emergency number, or a pet poison service. Describe the numbers and the time it happened.</p>
        <p><b>4. Note the time.</b> Everything in toxicology is time-dependent — what can be done at 30 minutes cannot be done at three hours.</p>
        <div class="callout warn"><b>Do not induce vomiting unless a vet tells you to.</b> It is wrong for caustic substances, wrong for a dog that is already wobbly, and it carries a real risk of aspiration pneumonia. The old advice to force salt water or hydrogen peroxide down a dog's throat causes more harm than the chocolate does.</div>

        <h2>What not to do</h2>
        <p><b>Do not give milk.</b> It does not dilute a toxin, and it adds a lactose problem to an existing one.</p>
        <p><b>Do not wait for symptoms.</b> With xylitol and grapes in particular, the window where treatment is simple closes before the dog looks unwell. A dog that seems fine at 20 minutes is the normal presentation, not evidence that nothing happened.</p>
        <p><b>Do not "dilute" with a big meal.</b> Food in the stomach can delay absorption, but it also makes induced vomiting harder and can complicate anaesthesia if the dog needs it.</p>
        <p><b>Do not rely on the internet instead of a professional.</b> Use a page like this one to decide how urgent it is, then call.</p>

        <h2>Not food, but in the same category</h2>
        <p>The most common pet poisonings are not food at all. Human medication — ibuprofen, paracetamol, antidepressants, ADHD medication — is the leading category, and a single tablet can be enough for a small dog. Then antifreeze, which is sweet and lethal in tiny volumes; rodenticide, which causes internal bleeding days later; slug pellets; nicotine and cannabis edibles; and lilies, which cause kidney failure in cats from pollen alone. Grapes and chocolate get the headlines, but the medicine cabinet and the garage do more damage.</p>

        <h2>Safe swaps that keep the begging quiet</h2>
        <p>A dog that is used to getting something from your plate does not need the plate. Plain cooked chicken, a carrot, a green bean, a slice of cucumber, or a piece of apple with the core removed all satisfy the same ritual. Keep a small box of dog-safe treats where the human snacks live, so the thing you reach for is already the right thing.</p>
        <p>If you want the detail behind any item above, each food has its own page in this section with the safe amount by body weight and the preparation that matters — see <a href="/dog-nutrition/can-dogs-eat-chocolate/">chocolate</a>, <a href="/dog-nutrition/can-dogs-eat-grapes/">grapes</a>, <a href="/dog-nutrition/can-dogs-eat-xylitol/">xylitol</a>, <a href="/dog-nutrition/can-dogs-eat-onion/">onion</a> and <a href="/dog-nutrition/can-dogs-eat-macadamia-nuts/">macadamia nuts</a> for the five that send most dogs to the vet.</p>

        <h2>Keeping it from happening again</h2>
        <p>Most repeat incidents come from the same three places: a bag left within reach, a child sharing food, and a counter surfer. Move chocolate and raisins into a closed cupboard rather than a low shelf, keep gum and mints out of bags on the floor, and teach a reliable "leave it" — it is the one cue that pays for itself in this exact situation. If your dog is a counter surfer, nothing on the worktop is safe; treat the kitchen as a room with a lid.</p>
        """,
        "faq": [
            ("How much chocolate is toxic to a dog?", "Around 20 mg of theobromine per kg of body weight brings the first signs, 40 to 50 mg/kg causes heart rhythm problems, and above 60 mg/kg seizures are possible. A 10 kg dog reaches the cardiac range at roughly 100 g of dark chocolate, but would need far more milk chocolate to get there."),
            ("Are grapes really that dangerous?", "Yes. There is no known safe dose and sensitivity varies between dogs, so a handful of grapes or raisins can cause acute kidney failure in one dog and nothing in another. Any ingestion is treated as serious."),
            ("Is xylitol in peanut butter?", "In some brands. It appears on labels as xylitol, birch sugar, birch bark sugar or wood sugar, and it is most common in reduced-fat and no-added-sugar products. Read the ingredient list every time, because recipes change."),
            ("How long after eating poison do symptoms show?", "It depends on the substance. Xylitol can collapse a dog within 30 minutes; chocolate signs usually appear in 4 to 12 hours; onion and garlic damage shows up 2 to 5 days later; kidney failure from grapes can take 24 to 72 hours. A dog that looks fine early on has not necessarily escaped it."),
            ("Should I make my dog vomit?", "Only if a vet or poison service tells you to. It is dangerous with caustic substances, unsafe in a dog that is already wobbly or unconscious, and carries a risk of aspiration pneumonia. Never use salt water or hydrogen peroxide on your own."),
            ("My dog ate a small amount of onion — is that an emergency?", "A single small piece in a medium or large dog is unlikely to cause a crisis, but repeated small amounts in leftovers cause the same anaemia slowly. Call your vet with the amount and the dog's weight, and watch for pale gums and weakness over the following days."),
            ("What foods are safe to share with a dog?", "Plain cooked chicken, carrot, green beans, cucumber, apple without the core, blueberries, watermelon without seeds, plain cooked rice, and plain unsweetened yoghurt in small amounts. All of them count toward the 10% of daily calories that treats are allowed."),
            ("Is peanut butter safe if it is organic?", "Organic says nothing about xylitol. The risk is the sweetener, not the farming method, so read the ingredient list on organic jars exactly as you would on any other."),
        ],
        "related": ["can-dogs-eat-chocolate", "can-dogs-eat-grapes", "can-dogs-eat-xylitol"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Pet Poison Helpline — Xylitol",
             "https://www.petpoisonhelpline.com/poison/xylitol/"),
            ("Pet Poison Helpline — Grapes",
             "https://www.petpoisonhelpline.com/poison/grapes/"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The Veterinary Toxicology team at Pet Poison Helpline",
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
        <p>Plain peanut butter — peanuts, maybe a little salt — is safe for dogs and almost universally loved. It is high in fat and calories, so it belongs in the treat column, not the food bowl: a couple of teaspoons a day is plenty for most dogs.</p>
        <p>The complication is not the peanut. It is what else ends up in the jar. A growing number of peanut butter products, especially the ones marketed as healthier for people, are sweetened with xylitol — a sugar alcohol that is safe for humans and devastating for dogs. <b>That single ingredient is the reason this page exists.</b></p>

        <h2>The one ingredient that makes peanut butter deadly: xylitol</h2>
        <p>Xylitol is a sugar substitute found in sugar-free gum, some mints, certain baked goods, and an increasing number of nut butters. In people it barely moves blood sugar. In dogs it triggers a rapid insulin release that can crash their blood glucose within 30 minutes, and at higher doses it causes liver failure.</p>
        <p>The dose thresholds vets work with: <b>about 0.1 g of xylitol per kg of body weight</b> is enough to cause dangerous hypoglycaemia, and roughly <b>0.5 g per kg</b> is where liver injury becomes a real risk. For a 10 kg dog, 0.1 g per kg is one gram of xylitol — less than the amount in a single stick of sugar-free gum. Some peanut butter products contain several grams per serving.</p>
        <div class="callout warn"><b>There is no safe amount to "test".</b> If a jar lists xylitol, it does not become safe by giving a smaller spoon. A dog that has eaten any of it needs a vet call, not a smaller portion.</div>

        <h2>How to read a peanut butter label in 30 seconds</h2>
        <p>You do not need to understand the whole ingredient list. You need to scan for one family of words and stop if you see any of them. Xylitol is allowed to appear under several names, and manufacturers are not required to put it in bold.</p>
        <table>
          <tr><th style="text-align:left">Stop — do not feed</th><th style="text-align:left">Fine for most dogs</th><th style="text-align:left">Fine, but count the calories</th></tr>
          <tr><td>xylitol</td><td>peanuts</td><td>sugar</td></tr>
          <tr><td>birch sugar</td><td>salt</td><td>molasses</td></tr>
          <tr><td>birch bark sugar</td><td>peanut oil</td><td>palm oil</td></tr>
          <tr><td>wood sugar</td><td>—</td><td>hydrogenated vegetable oil</td></tr>
          <tr><td>xylite</td><td>—</td><td>honey</td></tr>
        </table>
        <p>If the label says "sugar alcohol" without naming which one, treat it as a no. If the packaging advertises "no sugar added" but the ingredient list includes anything ending in <i>-ol</i>, that is the xylitol hiding in plain sight.</p>

        <h2>Why "no sugar added" and "low fat" jars are the riskiest</h2>
        <p>This is the part that catches people out. The plain, cheap, own-brand jar is usually the safest one on the shelf, because it is just peanuts and salt. The premium products — reduced-fat, no-added-sugar, "natural sweetness" — are exactly the ones where a manufacturer needs to replace sweetness and bulk, and xylitol is a cheap way to do both.</p>
        <p>Powdered peanut butter is a separate case. It is lower in fat and calories because the oil has been pressed out, but the ingredient list still has to be read the same way, and some brands add sweeteners to compensate for the missing fat. Crunchy versus smooth makes no difference to safety — it is the same product with pieces left in.</p>

        <h2>How much peanut butter can a dog have?</h2>
        <p>The standard veterinary rule is that treats should stay under <b>10% of a dog's daily calorie intake</b>. Peanut butter runs about 588 kcal per 100 g, or roughly 32 kcal per level teaspoon, so the ceiling arrives faster than most owners expect — a large dog's whole treat budget can disappear into three or four spoons.</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Approx. daily calories</th><th style="text-align:left">Treat budget (10%)</th><th style="text-align:left">Peanut butter ceiling per day</th></tr>
          <tr><td>5 kg</td><td>370 kcal</td><td>37 kcal</td><td>1 teaspoon (about 6 g)</td></tr>
          <tr><td>10 kg</td><td>630 kcal</td><td>63 kcal</td><td>2 teaspoons (about 11 g)</td></tr>
          <tr><td>20 kg</td><td>1,060 kcal</td><td>106 kcal</td><td>3.5 teaspoons (about 18 g)</td></tr>
          <tr><td>30 kg</td><td>1,440 kcal</td><td>144 kcal</td><td>5 teaspoons (about 25 g)</td></tr>
          <tr><td>40 kg</td><td>1,780 kcal</td><td>178 kcal</td><td>6 teaspoons (about 30 g)</td></tr>
        </table>
        <p>These are maintenance estimates for a healthy, neutered adult dog at ideal weight. Puppies, working dogs and intact dogs need more; a dog on a weight-loss plan needs less, and for those dogs peanut butter should be measured rather than spooned.</p>

        <h2>Salt, sugar and palm oil: what actually matters</h2>
        <p><b>Salt.</b> A salted peanut butter is fine for a healthy dog at treat-sized amounts. It matters for dogs with heart disease, kidney disease or hypertension, where total sodium is being managed — for those dogs, buy unsalted.</p>
        <p><b>Sugar and palm oil.</b> Neither is toxic. Both add calories a dog does not need, and a high-fat meal is one of the recognised triggers for pancreatitis. A dog with a history of pancreatitis, or one that has had a high-fat treat followed by vomiting and a hunched posture, should not be given peanut butter at all without asking the vet first.</p>
        <p><b>Hydrogenated vegetable oil.</b> Common in cheaper brands to stop separation. Not poisonous, but it is the ingredient that pushes the fat content up, so check the number rather than the name.</p>

        <h2>Five ways to use peanut butter that actually help</h2>
        <p>Peanut butter earns its place less as a treat and more as a delivery mechanism. These are the uses that hold up:</p>
        <p><b>1. Frozen in a rubber toy.</b> Fill, freeze overnight, hand it over. A frozen stuffed toy lasts 20 to 40 minutes instead of three, which is the difference between a distraction and a snack.</p>
        <p><b>2. Pill delivery.</b> A teaspoon hides most tablets and the smell covers the taste. Ask the vet first if the medication is time-critical — a dog that licks the peanut butter off and leaves the pill has not been medicated.</p>
        <p><b>3. Nail trims and vet visits.</b> A silicone lick mat smeared with peanut butter and stuck to the wall keeps a dog's head occupied while the nails are done. This works better than a bowl because the dog cannot walk away with it.</p>
        <p><b>4. Counter-conditioning.</b> A small amount given at the exact moment a dog hears the doorbell or the hoover changes the association. Keep the portion tiny — this is repetition work, not feeding.</p>
        <p><b>5. Senior dogs with low appetite.</b> A little warm peanut butter stirred into food can restart interest in a dog that has gone off its bowl. If a dog stops eating for more than 24 hours, that is a vet question rather than a palatability question.</p>

        <h2>When peanut butter is the wrong choice</h2>
        <p>Skip it, or ask the vet first, if the dog has a history of pancreatitis or high blood fat, is overweight and on a measured diet, has kidney or heart disease where sodium is restricted, or is scheduled for surgery (fat delays gastric emptying, which matters for anaesthesia).</p>
        <p>Peanut allergy in dogs is rare but real. Signs are itching, hives, facial swelling and, in severe cases, breathing difficulty, usually within minutes to a couple of hours of eating. A dog that reacts to peanuts should also avoid other peanut products, and the reaction should be noted in its records.</p>

        <h2>If your dog ate peanut butter with xylitol</h2>
        <p>Do not wait for symptoms. Xylitol acts fast, and a dog that looks fine at 15 minutes can be seizing at 45. Call your vet or a pet poison service immediately and have the jar in your hand — the amount eaten, the dog's weight and the xylitol content per serving are the three numbers they will ask for.</p>
        <table>
          <tr><th style="text-align:left">Time after eating</th><th style="text-align:left">What can happen</th><th style="text-align:left">What to do</th></tr>
          <tr><td>0–30 minutes</td><td>Often nothing visible yet</td><td>Call the vet or poison service now; do not wait for signs</td></tr>
          <tr><td>30–60 minutes</td><td>Vomiting, weakness, wobbling, collapse</td><td>Emergency visit; blood glucose checked</td></tr>
          <tr><td>1–12 hours</td><td>Severe hypoglycaemia, seizures</td><td>IV glucose and monitoring</td></tr>
          <tr><td>12–72 hours</td><td>Liver enzyme rise at higher doses</td><td>Liver values rechecked; supportive care</td></tr>
        </table>
        <p>Never induce vomiting unless a vet tells you to. With xylitol the risk of aspiration is real, and the treatment that matters is blood glucose, not an empty stomach.</p>
        """,
        "faq": [
            ("How much peanut butter is too much for a dog?", "For a healthy 10 kg dog, about two level teaspoons a day is the ceiling — treats should stay under 10% of daily calories, and peanut butter is roughly 32 kcal per teaspoon. Anything beyond that is weight gain with no nutritional benefit."),
            ("Can dogs eat peanut butter every day?", "Yes, in small measured amounts, as long as the jar contains no xylitol. Daily use is fine for most healthy dogs but adds up fast, so weigh it into the treat budget rather than adding it on top."),
            ("Is crunchy peanut butter safe for dogs?", "Yes. Crunchy and smooth are the same product with peanut pieces left in. Read the ingredient list the same way — the risk is xylitol and other sweeteners, not the texture."),
            ("What if my dog ate peanut butter with xylitol?", "Call your vet or a pet poison service immediately, even if the dog seems normal. Hypoglycaemia can start within 30 minutes, and roughly 0.1 g of xylitol per kg of body weight is enough to cause it."),
            ("Can puppies have peanut butter?", "In tiny amounts, yes, provided it is plain and xylitol-free. Puppies need proportionally more calories but very little fat, so keep it to a smear rather than a spoon and count it in their daily food."),
            ("Is peanut butter good for hiding pills?", "It is one of the better options — thick enough to coat a tablet and strong enough in smell to mask it. Confirm with your vet that the drug can be given with food, and watch that the pill actually goes down."),
            ("Can dogs be allergic to peanut butter?", "Rarely, yes. Signs include itching, hives, facial swelling and breathing difficulty, usually within minutes to two hours. Stop feeding it and have the reaction recorded by your vet."),
            ("Does peanut butter help a dog's dry skin?", "Not really. The fat in peanut butter is mostly omega-6, which can push inflammation the wrong way when fed in excess. Skin and coat support comes from omega-3s and a balanced diet, not from peanut butter."),
        ],
        "sources": [
            ("Pet Poison Helpline — Xylitol",
             "https://www.petpoisonhelpline.com/poison/xylitol/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("WSAVA Global Nutrition Guidelines",
             "https://wsava.org/global-guidelines/global-nutrition-guidelines/"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "experts": [
            "The Veterinary Toxicology team at Pet Poison Helpline",
            "The veterinarians of the ASPCA Animal Poison Control Center",
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
        <p>Fresh strawberries bring vitamin C, fiber, and antioxidants with very few calories — around 32 kcal per 100 g — which makes them one of the better sweet treats for a dog that is watching its weight. A dog that will not touch a carrot will often take a strawberry.</p>
        <p>They are not, however, a food. Strawberries supply almost no protein, no fat and no calcium, and a dog's diet has to be built on a complete food. Think of them as a treat that happens to be healthier than most, not as something to add to the bowl for nutrition's sake.</p>

        <h2>How many strawberries can a dog have?</h2>
        <p>Because strawberries are so low in calories, the limit is not really about calories — it is about sugar load and about how much fiber a small gut can handle at once. Too many in one sitting produces loose stool, which is the most common complaint owners report.</p>
        <table>
          <tr><th style="text-align:left">Dog size</th><th style="text-align:left">Berries per day</th><th style="text-align:left">Preparation</th></tr>
          <tr><td>Toy breeds (under 5 kg)</td><td>1–2</td><td>Cut into quarters; a whole berry is a choking shape for a small throat</td></tr>
          <tr><td>Small (5–10 kg)</td><td>2–3</td><td>Halved</td></tr>
          <tr><td>Medium (10–25 kg)</td><td>3–5</td><td>Halved or whole</td></tr>
          <tr><td>Large (25 kg and up)</td><td>5–8</td><td>Whole is fine</td></tr>
        </table>
        <div class="callout"><b>The 10% rule still applies.</b> Treats should stay under a tenth of a dog's daily calories. Strawberries rarely threaten that ceiling, but the cream, the jam and the peanut butter they are often served with do.</div>

        <h2>Wash them properly — strawberries are a high-residue crop</h2>
        <p>Strawberries are grown close to the ground, picked by hand and eaten with the skin on, which is why they consistently appear near the top of pesticide-residue monitoring lists. That residue sits on the outside, exactly the part the dog eats.</p>
        <p>The method that works: rinse under running water for about 15 seconds, rub gently, and <b>do not hull them until after washing</b>. Pulling the green top off first opens a channel into the flesh and the berry takes up water, which dulls flavour and does nothing for cleanliness. Soaking in a bowl of water is less effective than running water, and soap or vinegar soaks are not recommended for anything a dog will eat.</p>
        <p>Organic berries reduce the concern but still need rinsing — soil and handling are the other reason to wash.</p>

        <h2>What about the green tops and leaves?</h2>
        <p>The calyx — the green leafy top — is not toxic to dogs. It is also not worth feeding: it is tough, bitter, and it is where residue and grit collect. Hull the berry and throw the top away.</p>
        <p>One genuine caution belongs here. Wild berries picked on a walk are a different matter from shop-bought ones. Unfamiliar red berries in a hedge or park may be a non-toxic lookalike, or may not be — and the bigger risk is a park hedge that has been sprayed. Keep foraging dogs away from unidentified fruit, and if you think a dog has eaten something unknown, call a vet rather than waiting for symptoms.</p>

        <h2>Fresh, frozen or dried: which is safe?</h2>
        <p><b>Fresh.</b> The default. Wash, hull, cut to size, serve plain.</p>
        <p><b>Frozen.</b> Plain frozen berries are fine and keep most of the vitamin C. They make a good cooling chew in summer, but serve them one or two at a time — a dog that swallows a frozen whole berry too fast can gulp air and vomit. Letting them soften for a couple of minutes is the safer version for small dogs.</p>
        <p><b>Dried.</b> This is where it goes wrong. Drying concentrates the sugar several-fold and the pieces are small enough to be eaten by the handful. Dried fruit also clings to teeth. If you feed dried strawberries at all, treat three dried pieces as equal to one fresh berry.</p>
        <p><b>Flavoured, jam, yoghurt, ice cream.</b> No. These carry added sugar, and some sugar-free products are sweetened with xylitol, which is severely toxic to dogs even in small amounts. Strawberry-flavoured dog chews are a separate category — read the label rather than assuming the flavour is real fruit.</p>

        <h2>When strawberries are the wrong choice</h2>
        <p><b>Diabetic dogs.</b> Strawberries are lower in sugar than most fruit — roughly 5 g per 100 g, about half that of an apple — but they are still sugar, and a dog on insulin needs the carbohydrate counted rather than guessed. Ask the vet for an allowance.</p>
        <p><b>Dogs with a sensitive gut.</b> Fiber and seeds can loosen stool. Introduce one berry, wait a day, then increase.</p>
        <p><b>Dogs that have just had surgery or anaesthesia.</b> Fruit is not the issue; the point is that any change to the diet during recovery muddies the picture if something goes wrong. Keep it boring for a few days.</p>
        <p><b>Dogs with a history of pancreatitis.</b> Strawberries themselves are low in fat, so they are not the trigger — but the whipped cream and the peanut butter dip that usually accompany them are.</p>

        <h2>Three ways to serve them that dogs actually use</h2>
        <p><b>1. Frozen strawberry and yoghurt bites.</b> Mash plain berries into a spoon of plain unsweetened yoghurt, freeze in an ice-cube tray. A cooling chew that lasts minutes instead of seconds.</p>
        <p><b>2. Mashed over food.</b> For a dog that has gone off its bowl, a mashed berry stirred through the top adds smell without adding much. Do not replace the meal — just scent it.</p>
        <p><b>3. Training treat for a soft mouth.</b> Halved berries are low-value enough to be repeated ten times in a session without wrecking the calorie budget, which makes them useful for puppies still learning to take treats gently.</p>

        <h2>What to watch for afterwards</h2>
        <p>The usual reaction to too many berries is loose stool within 12 to 24 hours, sometimes with visible seeds. It settles on its own once the berries stop. Vomiting, abdominal pain, or a dog that goes off its food are not normal responses to a strawberry and point to something else — call the vet.</p>
        <p>True strawberry allergy in dogs is uncommon. If you see itching, hives, facial swelling, or breathing difficulty within a couple of hours of eating, stop feeding them and have it recorded.</p>
        """,
        "faq": [
            ("How many strawberries can a dog eat?", "One to two for a toy breed, two to three for a small dog, three to five for a medium dog, and five to eight for a large dog, per day. Cut them small for small mouths — a whole berry is a choking shape for a toy breed."),
            ("Can dogs eat frozen strawberries?", "Yes, plain frozen berries are safe and keep most of their vitamin C. Serve one or two at a time and let them soften slightly for small dogs, since a frozen whole berry can be swallowed too fast."),
            ("Are strawberry tops safe for dogs?", "The green tops are not toxic, but they are tough, bitter and collect grit and residue. Hull the berry and discard the top rather than feeding it."),
            ("Can dogs eat dried strawberries?", "Only in very small amounts. Drying concentrates the sugar several-fold and makes the pieces easy to eat by the handful. Treat three dried pieces as roughly equal to one fresh berry."),
            ("Can a diabetic dog eat strawberries?", "Only with a vet's allowance. At about 5 g of sugar per 100 g they are lower than most fruit — roughly half an apple — but a dog on insulin needs carbohydrate counted rather than estimated."),
            ("Do I need to wash strawberries before giving them to my dog?", "Yes, every time. Rinse under running water for about 15 seconds and rub gently, and do not pull the green top off until after washing — hulling first lets the berry take up water."),
            ("Can puppies eat strawberries?", "Yes, in very small amounts once they are on solid food. One halved berry is plenty for a puppy, and it should not displace any of their growth diet."),
            ("Can I put strawberries in my dog's food bowl?", "A mashed berry on top of the usual food is fine as a scent topper for a fussy eater. Do not use fruit to bulk out a meal — the bowl still has to be a complete diet."),
        ],
        "related": ["can-dogs-eat-bananas", "can-dogs-eat-watermelon", "foods-toxic-to-dogs"],
        "sources": [
            ("AKC — Fruits and Vegetables Dogs Can and Can't Eat",
             "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("USDA FoodData Central — Nutrient values",
             "https://fdc.nal.usda.gov/"),
            ("Pet Poison Helpline — Xylitol",
             "https://www.petpoisonhelpline.com/poison/xylitol/"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The nutrition team at the American Kennel Club",
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
    {
        "slug": "can-dogs-eat-green-beans",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Green Beans? Yes — a Low-Cal Diet Staple",
        "url": "/dog-nutrition/can-dogs-eat-green-beans/",
        "description": "Green beans are a safe, low-calorie, high-fiber snack dogs can eat raw or cooked. Why to skip the butter and canned versions, and how much to feed by weight.",
        "lede": "Yes — plain green beans are a safe, low-calorie, high-fiber snack dogs can eat raw or cooked. They are a common diet food for overweight dogs, as long as they stay plain.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Are green beans good for dogs?</h2>
        <p>Plain green beans are about as healthy a treat as it gets: roughly 31 calories per cooked cup, with fiber, vitamin C, vitamin K, and manganese, and almost no fat. That makes them a go-to snack for dogs on a weight-management plan — many vets suggest them as a low-calorie swap for biscuits. The beans themselves are non-toxic; the problems come only from how they are prepared.</p>

        <h2>Raw vs cooked</h2>
        <p>Both raw and cooked are safe, but a whole raw green bean is a choking hazard, especially for small dogs that gulp food. Snap or cut them into bite-size pieces, and light steaming makes them easier to digest. Avoid frozen-for-cooking beans with added sauce.</p>
        <div class="callout">Cut beans to match your dog's mouth. A full-length raw bean is the classic "went down the wrong way" item in the ER — short pieces only.</div>

        <h2>Green bean nutrition at a glance</h2>
        <p>For scale, here is roughly what is in one cup of cooked green beans (about 125 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount</th></tr>
          <tr><td>Calories</td><td>~31 kcal</td></tr>
          <tr><td>Carbohydrate</td><td>~7 g</td></tr>
          <tr><td>Fiber</td><td>~3.6 g</td></tr>
          <tr><td>Vitamin C</td><td>good source</td></tr>
          <tr><td>Vitamin K</td><td>good source</td></tr>
          <tr><td>Protein</td><td>~1.8 g</td></tr>
        </table>
        <p>Low calorie and high fiber are what make them a filling, diet-friendly bite.</p>

        <h2>How much green beans is safe?</h2>
        <p>Treats should stay under about 10% of daily calories. A sensible portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe treat amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>2–3 cut pieces (about 1 tbsp)</td></tr>
          <tr><td>5–15 kg</td><td>A small handful of pieces (2–3 tbsp)</td></tr>
          <tr><td>15–30 kg</td><td>Up to 1/4 cup cut pieces</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/2 cup cut pieces, occasionally</td></tr>
        </table>

        <h2>How to serve it</h2>
        <ul>
          <li>Plain, with no salt, butter, oil, or seasoning.</li>
          <li>Raw (cut small) or lightly steamed — both are fine.</li>
          <li>Let cooked beans cool before serving.</li>
        </ul>

        <h2>Can puppies eat green beans?</h2>
        <p>Yes, in small cut pieces once weaned and on solid food. Puppies have small airways, so keep the pieces tiny and watch them chew.</p>

        <h2>The real danger: butter, salt, and canned beans</h2>
        <div class="callout warn">Never feed green beans with butter, garlic, or onion, and skip canned green beans packed in salt. Garlic and onion are toxic to dogs, and the extra sodium and fat add real risk. Only plain beans are safe. For the full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</div>

        <h2>What if my dog ate too many?</h2>
        <p>A dog that raids a bag of plain beans mostly risks gas and a mild tummy ache that passes. Call a vet if there was butter, garlic, or onion involved, or if the dog is vomiting, lethargic, or shows signs of a blockage from swallowing whole beans. Our <a href="/dog-health/dog-vomiting-causes/">vomiting guide</a> explains what is urgent, and our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers portion basics.</p>
        """,
        "faq": [
            ("Can dogs eat raw green beans?", "Yes, but cut them into small pieces first — a whole raw bean is a choking hazard, especially for small dogs."),
            ("Are green beans good for overweight dogs?", "Yes — at about 31 calories per cooked cup and high in fiber, they are a classic low-calorie treat for dogs on a diet."),
            ("Can dogs eat canned green beans?", "Only plain, no-salt canned beans, and even then rinse them. Regular canned beans are too high in sodium; avoid any with added sauce."),
            ("Can dogs eat green beans with butter or garlic?", "No — butter adds fat a dog does not need, and garlic is toxic to dogs. Only plain beans are safe."),
            ("How much green beans can a dog eat?", "Keep treats under about 10% of daily calories: a few cut pieces for a small dog, up to half a cup for a large one."),
            ("Can puppies eat green beans?", "Yes, in tiny cut pieces once weaned and on solid food — keep them small to avoid choking."),
            ("Can dogs eat frozen green beans?", "Yes — plain frozen (no sauce) beans, thawed or lightly cooked, are fine. Cut them small."),
            ("What if my dog ate too many green beans?", "Plain beans usually cause just gas and a mild stomach ache. Call a vet if butter, garlic, or onion was involved, or for vomiting or lethargy."),
        ],
        "related": ["can-dogs-eat-broccoli", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
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
        "slug": "can-dogs-eat-pineapple",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Pineapple? Yes — in Small Pieces",
        "url": "/dog-nutrition/can-dogs-eat-pineapple/",
        "description": "Fresh pineapple is a safe, vitamin-C-rich dog treat served in small pieces. Why to skip canned syrup and the skin, and exactly how much to feed by body weight.",
        "lede": "Yes — fresh pineapple is a safe, vitamin-C-rich treat in small amounts. The flesh only, cut into small pieces; skip the tough core, skin, and the sugary canned version.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is pineapple safe for dogs?</h2>
        <p>The fresh flesh is non-toxic and genuinely good for dogs in small amounts — it brings vitamin C, manganese, and a little fiber, plus water for hydration. The catch is the natural sugar: a few small pieces is a nice treat, but a lot can loosen stools or spike blood sugar. Pineapple also contains bromelain, an enzyme that can mildly irritate the mouth or gut if a dog eats a large amount.</p>

        <h2>Pineapple nutrition at a glance</h2>
        <p>For scale, here is roughly what is in half a cup of fresh pineapple chunks (about 80 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount</th></tr>
          <tr><td>Calories</td><td>~42 kcal</td></tr>
          <tr><td>Carbohydrate</td><td>~11 g</td></tr>
          <tr><td>Sugar (natural)</td><td>~8 g</td></tr>
          <tr><td>Fiber</td><td>~1.4 g</td></tr>
          <tr><td>Vitamin C</td><td>good source</td></tr>
          <tr><td>Manganese</td><td>good source</td></tr>
        </table>
        <p>Nutrient-dense, but the natural sugar is why portion size matters.</p>

        <h2>How much pineapple is safe?</h2>
        <p>Treats should stay under about 10% of daily calories. A sensible portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe treat amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>1–2 small cubes (about 1 tbsp)</td></tr>
          <tr><td>5–15 kg</td><td>A few small cubes (2–3 tbsp)</td></tr>
          <tr><td>15–30 kg</td><td>Up to 1/4 cup chunks</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/2 cup chunks, occasionally</td></tr>
        </table>

        <h2>Fresh vs canned vs the core and skin</h2>
        <ul>
          <li><b>Fresh flesh:</b> the safe part — cut into small cubes.</li>
          <li><b>Canned pineapple:</b> usually packed in heavy syrup. Skip it; the added sugar is far too much for a dog. If you must, use fruit-only canned in its own juice and rinse it.</li>
          <li><b>Core and skin:</b> the tough core is a choking and blockage risk, and the spiky skin is indigestible. Cut both away.</li>
        </ul>
        <div class="callout">The core is the part people forget — it is woody and can lodge. Trim it completely and serve only soft flesh cubes.</div>

        <h2>How to serve it</h2>
        <ul>
          <li>Peel, remove the core, and cut flesh into small cubes.</li>
          <li>Offer plain, fresh or frozen (a cooling bite).</li>
          <li>For a fun chew, freeze cubes — no sugar or syrup ever.</li>
        </ul>

        <h2>Can puppies eat pineapple?</h2>
        <p>Yes, in tiny amounts once weaned and on solid food. The sugar and acidity mean keep it to a cube or two and watch for loose stools.</p>

        <h2>The danger: sugar and canned syrup</h2>
        <div class="callout warn">Avoid canned pineapple in syrup and any dried pineapple with added sugar — both pile on sugar a dog does not need and can prompt diarrhea or weight gain. Diabetic dogs should skip pineapple or get a vet's OK first. For the full list of risky foods, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</div>

        <h2>What if my dog ate too much?</h2>
        <p>A dog that eats a lot of fresh pineapple mostly risks an upset, loose-stool belly from the sugar and bromelain. It usually passes with water and a bland next meal. Call a vet for repeated vomiting, lethargy, or if the dog got into the core or skin and may have a blockage. Our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers portion basics.</p>
        """,
        "faq": [
            ("Can dogs eat fresh pineapple?", "Yes — the fresh flesh is safe and vitamin-C-rich in small amounts. Cut into small cubes and skip the core and skin."),
            ("Can dogs eat canned pineapple?", "Avoid the syrup-packed kind; the added sugar is too much. If canned, use fruit in its own juice, rinse it, and keep it tiny."),
            ("Is pineapple good for dogs?", "In small amounts it adds vitamin C, manganese, and fiber, but the natural sugar means it should stay an occasional treat."),
            ("Can puppies eat pineapple?", "Yes, a cube or two once weaned and on solid food — watch for loose stools from the sugar and acidity."),
            ("How much pineapple can a dog eat?", "Keep treats under about 10% of daily calories: a couple of cubes for a small dog, up to half a cup for a large one."),
            ("Can dogs eat pineapple core or skin?", "No — the core is a choking and blockage risk and the skin is indigestible. Serve only soft flesh."),
            ("Can diabetic dogs eat pineapple?", "It is best avoided because of the natural sugar, or cleared with your vet first."),
            ("What if my dog ate too much pineapple?", "Usually just a loose-stool belly that passes; call a vet for vomiting, lethargy, or if the core or skin was eaten."),
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
        "slug": "can-dogs-eat-mango",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Mango? Yes — Peeled, Pitted, Small",
        "url": "/dog-nutrition/can-dogs-eat-mango/",
        "description": "Fresh mango flesh is a safe, vitamin-rich dog treat in small pieces. Why to peel it, remove the pit, and skip canned syrup, plus how much to feed by weight.",
        "lede": "Yes — fresh mango flesh is a safe, vitamin-rich treat in small pieces. Peel it, remove the pit, and skip the skin; the pit is a choking hazard and the skin is hard to digest.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is mango safe for dogs?</h2>
        <p>The fresh flesh is non-toxic and a genuine nutrient win in small amounts — vitamin C, vitamin A, and fiber, plus water for hydration. The watch-items are the natural sugar (keep it occasional) and the inedible parts: the skin and the large central pit. Dogs should get only soft flesh, cut small.</p>

        <h2>Mango nutrition at a glance</h2>
        <p>For scale, here is roughly what is in half a cup of fresh mango cubes (about 83 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount</th></tr>
          <tr><td>Calories</td><td>~50 kcal</td></tr>
          <tr><td>Carbohydrate</td><td>~12 g</td></tr>
          <tr><td>Sugar (natural)</td><td>~11 g</td></tr>
          <tr><td>Fiber</td><td>~1.4 g</td></tr>
          <tr><td>Vitamin C</td><td>good source</td></tr>
          <tr><td>Vitamin A</td><td>good source</td></tr>
        </table>
        <p>Nutrient-dense, but the sugar is why portion size matters.</p>

        <h2>How much mango is safe?</h2>
        <p>Treats should stay under about 10% of daily calories. A sensible portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe treat amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>1–2 small cubes (about 1 tbsp)</td></tr>
          <tr><td>5–15 kg</td><td>A few small cubes (2–3 tbsp)</td></tr>
          <tr><td>15–30 kg</td><td>Up to 1/4 cup cubes</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/2 cup cubes, occasionally</td></tr>
        </table>

        <h2>The pit and the skin</h2>
        <div class="callout warn">The pit is a serious choking and blockage hazard — never let a dog gnaw a mango half. The skin is tough, waxy, and hard to digest, and may carry pesticide residue, so peel it completely. Feed only peeled flesh, pit removed.</div>

        <h2>How to serve it</h2>
        <ul>
          <li>Peel, cut the flesh off the pit, and cube small.</li>
          <li>Offer plain, fresh or frozen (a cooling bite).</li>
          <li>No sugar, syrup, or whipped topping ever.</li>
        </ul>

        <h2>Can puppies eat mango?</h2>
        <p>Yes, in tiny amounts once weaned and on solid food. The sugar and fiber mean keep it to a cube or two and watch for loose stools.</p>

        <h2>The danger: sugar and canned mango</h2>
        <div class="callout warn">Avoid canned mango in syrup and dried mango with added sugar — both pile on sugar a dog does not need. Diabetic dogs should skip mango or get a vet's OK first. For the full list of risky foods, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</div>

        <h2>What if my dog ate the pit or too much?</h2>
        <p>A lot of flesh mostly causes a loose-stool belly that passes. But if the dog swallowed the pit, call a vet right away — pits are a real blockage risk, especially in small dogs. Also call for vomiting, lethargy, or straining. Our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers portion basics.</p>
        """,
        "faq": [
            ("Can dogs eat mango flesh?", "Yes — peeled, pitted, and cut small, fresh mango flesh is a safe vitamin-rich treat in moderation."),
            ("Can dogs eat mango skin?", "No — the skin is tough, waxy, and hard to digest, and may hold pesticide residue. Peel it completely."),
            ("Can dogs eat mango pit?", "No — the pit is a choking and blockage hazard. Never give a dog a mango half; remove the pit first."),
            ("Can puppies eat mango?", "Yes, a cube or two once weaned and on solid food — watch for loose stools from the sugar."),
            ("How much mango can a dog eat?", "Keep treats under about 10% of daily calories: a couple of cubes for a small dog, up to half a cup for a large one."),
            ("Can dogs eat canned or dried mango?", "Avoid syrup-packed canned and sugar-added dried mango; the added sugar is too much. Fresh is best."),
            ("Can diabetic dogs eat mango?", "It is best avoided because of the natural sugar, or cleared with your vet first."),
            ("What if my dog ate a mango pit?", "Call a vet promptly — pits are a real blockage risk, especially in small dogs. Watch for vomiting or straining."),
        ],
        "related": ["can-dogs-eat-pineapple", "can-dogs-eat-watermelon", "foods-toxic-to-dogs"],
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
        "slug": "can-dogs-eat-potato",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Potato? Cooked Only, Never Raw",
        "url": "/dog-nutrition/can-dogs-eat-potato/",
        "description": "Plain cooked potato is safe for dogs, but raw potato is toxic and fried or buttered versions are off the menu. Why, and how much to feed by body weight.",
        "lede": "Yes — fully cooked potato is safe for dogs, but raw potato is toxic and fried or buttered potato is off the menu. Plain, boiled or baked, and never green or sprouted.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is potato safe for dogs?</h2>
        <p>A plain, fully cooked potato is safe and easy to digest — it is mostly starch, with some vitamin C, vitamin B6, and potassium. The danger is in the preparation and the state of the potato: raw potatoes and green or sprouted potatoes contain solanine, a compound that is toxic to dogs, and fried or loaded potatoes add fat and salt a dog does not need.</p>

        <h2>Raw vs cooked — the solanine risk</h2>
        <div class="callout warn">Raw potatoes, and any potato that is green or sprouting, contain solanine, which can cause vomiting, diarrhea, confusion, and in large amounts serious poisoning. Cook thoroughly, and never feed raw potato or green/sprouted parts. The same goes for raw potato skins in quantity.</div>

        <h2>Potato nutrition at a glance</h2>
        <p>For scale, here is roughly what is in one cup of plain boiled potato (about 150 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount</th></tr>
          <tr><td>Calories</td><td>~135 kcal</td></tr>
          <tr><td>Carbohydrate</td><td>~31 g</td></tr>
          <tr><td>Fiber</td><td>~2.4 g</td></tr>
          <tr><td>Vitamin C</td><td>some</td></tr>
          <tr><td>Vitamin B6</td><td>some</td></tr>
          <tr><td>Potassium</td><td>good source</td></tr>
        </table>
        <p>A filling carb, not a nutrient powerhouse — keep portions modest.</p>

        <h2>How much potato is safe?</h2>
        <p>As an occasional plain side, a sensible portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Plain cooked potato</th></tr>
          <tr><td>Under 5 kg</td><td>1–2 tablespoons mashed</td></tr>
          <tr><td>5–15 kg</td><td>1/4–1/3 cup</td></tr>
          <tr><td>15–30 kg</td><td>1/2 cup</td></tr>
          <tr><td>30 kg and up</td><td>1/2–1 cup, occasionally</td></tr>
        </table>
        <div class="callout">Potato is calorie-dense. For a dog watching its weight, <a href="/dog-nutrition/can-dogs-eat-sweet-potato/">sweet potato</a> or a low-cal veggie is often a better swap.</div>

        <h2>How to serve it</h2>
        <ul>
          <li>Boil or bake plain, with no salt, butter, oil, or seasoning.</li>
          <li>Mash or cube small so a dog cannot choke.</li>
          <li>Skip the skin if it is thick or you are unsure it is fully cooked.</li>
        </ul>

        <h2>Can puppies eat potato?</h2>
        <p>Yes, plain cooked potato in small amounts once weaned and on solid food. Never raw, green, or sprouted.</p>

        <h2>The danger: fries, butter, and green potatoes</h2>
        <div class="callout warn">French fries, chips, and buttered or seasoned potato are off the menu — the fat, salt, and often garlic or onion are bad for dogs, and onion and garlic are toxic. And never feed raw or green/sprouted potato (solanine). For the full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</div>

        <h2>When potato isn't enough</h2>
        <p>Plain potato is a small occasional carb, not a meal and not a remedy for a sick dog. Persistent vomiting or diarrhea, lethargy, or a painful belly need a veterinarian, not more food. Our <a href="/dog-health/dog-vomiting-causes/">vomiting guide</a> explains what is urgent, and our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers portion basics.</p>
        """,
        "faq": [
            ("Can dogs eat cooked potato?", "Yes — plain boiled or baked potato, with no salt, butter, or seasoning, is safe in moderation."),
            ("Can dogs eat raw potato?", "No — raw potato contains solanine, which is toxic to dogs. Cook it thoroughly."),
            ("Why are green or sprouted potatoes dangerous?", "They contain higher solanine levels and can poison a dog; never feed green, sprouting, or raw potato."),
            ("Can dogs eat fries or chips?", "No — fries and chips are loaded with fat and salt, and often garlic or onion, which are toxic. Only plain cooked potato is safe."),
            ("How much potato can a dog eat?", "Keep it occasional: a tablespoon or two for a small dog, up to a cup for a large one, plain and cooked."),
            ("Can puppies eat potato?", "Yes, plain cooked potato in small amounts once weaned — never raw, green, or sprouted."),
            ("Is potato or sweet potato better for dogs?", "Both are safe cooked; sweet potato is a bit more nutrient-rich, while potato is more calorie-dense. See our sweet potato guide."),
            ("What if my dog ate raw or green potato?", "Call a vet or poison helpline, especially for vomiting, diarrhea, confusion, or weakness — solanine poisoning needs prompt care."),
        ],
        "related": ["can-dogs-eat-sweet-potato", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
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
        "slug": "can-dogs-eat-spinach",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Spinach? Yes — in Small Amounts",
        "url": "/dog-nutrition/can-dogs-eat-spinach/",
        "description": "Plain spinach is safe for dogs in small amounts — nutrient-rich but high in oxalates, so keep it occasional. Why cooked is easier, and how much to feed by weight.",
        "lede": "Yes — plain spinach is safe for dogs in small amounts. It is nutrient-rich, but the natural oxalates mean it should stay an occasional treat, not a daily heap.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is spinach safe for dogs?</h2>
        <p>Plain spinach is non-toxic and genuinely nutritious — vitamin K, vitamin A, vitamin C, folate, iron, and fiber. The catch is oxalic acid (oxalates), which in large amounts can bind calcium and, over time, stress the kidneys, especially in dogs with existing kidney issues. The widely cited rule is the same as for any treat: keep spinach to a small, occasional amount and it is fine for healthy dogs.</p>

        <h2>Spinach nutrition at a glance</h2>
        <p>For scale, here is roughly what is in one cup of cooked spinach (about 180 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount</th></tr>
          <tr><td>Calories</td><td>~41 kcal</td></tr>
          <tr><td>Carbohydrate</td><td>~6.8 g</td></tr>
          <tr><td>Fiber</td><td>~4.3 g</td></tr>
          <tr><td>Vitamin K</td><td>excellent source</td></tr>
          <tr><td>Vitamin A</td><td>good source</td></tr>
          <tr><td>Iron</td><td>some</td></tr>
        </table>
        <p>Nutrient-dense, which is exactly why the oxalate caution applies — more is not better here.</p>

        <h2>The oxalate caveat</h2>
        <div class="callout">Spinach is high in oxalates. For a healthy dog, small occasional servings are fine, but dogs with kidney disease or a history of calcium oxalate stones should avoid it or get a vet's OK first. Keep portions small.</div>

        <h2>How much spinach is safe?</h2>
        <p>Treats should stay under about 10% of daily calories. A sensible portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe treat amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>A few small leaves or 1 tbsp cooked</td></tr>
          <tr><td>5–15 kg</td><td>1–2 tbsp cooked, chopped</td></tr>
          <tr><td>15–30 kg</td><td>Up to 1/4 cup cooked</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/3 cup cooked, occasionally</td></tr>
        </table>

        <h2>Raw vs cooked</h2>
        <p>Lightly cooked (steamed or boiled, no seasoning) is easier to digest and softer on the gut than a wad of raw leaves. Either way, chop fine so it is not a choking clump.</p>

        <h2>How to serve it</h2>
        <ul>
          <li>Plain, with no butter, oil, salt, garlic, or onion.</li>
          <li>Steam or boil briefly, then chop small.</li>
          <li>Let it cool before serving.</li>
        </ul>

        <h2>Can puppies eat spinach?</h2>
        <p>Yes, in tiny amounts once weaned and on solid food. Puppies have small kidneys too, so keep it a leaf or two and watch for any tummy upset.</p>

        <h2>What to avoid</h2>
        <div class="callout warn">Never serve spinach with butter, cream, garlic, or onion — garlic and onion are toxic to dogs, and the fats add needless calories. Only plain spinach is safe. For the full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</div>

        <h2>When spinach isn't the answer</h2>
        <p>Spinach is a small, healthy extra — not a meal and not a fix for a sick dog. Persistent vomiting or diarrhea, lethargy, or a painful belly need a veterinarian. Our <a href="/dog-health/dog-vomiting-causes/">vomiting guide</a> explains what is urgent, and our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers portion basics.</p>
        """,
        "faq": [
            ("Can dogs eat spinach?", "Yes — plain spinach is safe in small, occasional amounts for healthy dogs. It is nutrient-rich but high in oxalates."),
            ("Why is too much spinach bad for dogs?", "Spinach is high in oxalates, which can bind calcium and stress the kidneys in large amounts, especially in dogs with kidney issues."),
            ("Can dogs with kidney disease eat spinach?", "It is best avoided or cleared with a vet first, because the oxalates can worsen kidney and stone problems."),
            ("Is cooked or raw spinach better for dogs?", "Lightly cooked (steamed or boiled, plain) is easier to digest; chop either fine to avoid a choking clump."),
            ("How much spinach can a dog eat?", "Keep it occasional: a tablespoon or two for a small dog, up to a third of a cup cooked for a large one."),
            ("Can puppies eat spinach?", "Yes, a leaf or two once weaned and on solid food — watch for any tummy upset."),
            ("Can dogs eat spinach with butter or garlic?", "No — butter adds fat a dog does not need, and garlic is toxic. Only plain spinach is safe."),
            ("What if my dog ate a lot of spinach?", "A healthy dog may just get an upset stomach; call a vet if there is vomiting, lethargy, or if the dog has kidney disease."),
        ],
        "related": ["can-dogs-eat-broccoli", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
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
        "slug": "can-dogs-eat-tomato",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Tomatoes? Ripe Flesh, No Leaves",
        "url": "/dog-nutrition/can-dogs-eat-tomato/",
        "description": "Ripe tomato flesh is safe for dogs in small amounts, but green tomatoes and the stems and leaves are toxic. Why to skip sauces, and how much to feed by weight.",
        "lede": "Yes — ripe red tomato flesh is safe in small amounts, but the green parts, stems, and leaves contain solanine and are toxic. Skip sauces and seasoned tomato.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is tomato safe for dogs?</h2>
        <p>The ripe, red flesh of a tomato is non-toxic and can be a low-calorie treat — it brings vitamin C, potassium, and lycopene, an antioxidant. The problem is everything else on the plant: unripe (green) tomatoes and the stems, leaves, and vines contain solanine, the same toxin found in green potatoes, and that is genuinely dangerous to dogs.</p>

        <h2>Tomato nutrition at a glance</h2>
        <p>For scale, here is roughly what is in half a cup of chopped ripe tomato (about 90 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Amount</th></tr>
          <tr><td>Calories</td><td>~16 kcal</td></tr>
          <tr><td>Carbohydrate</td><td>~3.5 g</td></tr>
          <tr><td>Fiber</td><td>~1 g</td></tr>
          <tr><td>Vitamin C</td><td>good source</td></tr>
          <tr><td>Potassium</td><td>some</td></tr>
          <tr><td>Lycopene</td><td>present</td></tr>
        </table>
        <p>Low calorie and antioxidant-rich — a light, safe bite when ripe and plain.</p>

        <h2>The danger: green tomatoes and the plant</h2>
        <div class="callout warn">Green (unripe) tomatoes and every green part of the plant — stems, leaves, and vines — contain solanine and are toxic to dogs. Keep dogs out of the garden and the compost of tomato plants, and never let them chew a leafy tomato stem.</div>

        <h2>How much tomato is safe?</h2>
        <p>Treats should stay under about 10% of daily calories. A sensible portion by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe treat amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>1–2 small cubes (about 1 tbsp)</td></tr>
          <tr><td>5–15 kg</td><td>A few cubes (2–3 tbsp)</td></tr>
          <tr><td>15–30 kg</td><td>Up to 1/4 cup chopped</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/2 cup chopped, occasionally</td></tr>
        </table>

        <h2>How to serve it</h2>
        <ul>
          <li>Use only ripe, red tomatoes — no green ones.</li>
          <li>Wash, remove the stem and leaves completely, and cube small.</li>
          <li>Offer plain, fresh or a little cooked — no salt, oil, or seasoning.</li>
        </ul>

        <h2>Can puppies eat tomato?</h2>
        <p>Yes, ripe flesh in tiny amounts once weaned and on solid food. Puppies are smaller and more sensitive, so keep it to a cube or two and watch for loose stools.</p>

        <h2>The danger: sauce, ketchup, and seasonings</h2>
        <div class="callout warn">Tomato sauce, ketchup, and soup are off the menu — they are loaded with salt, sugar, and often garlic or onion, which are toxic to dogs. Only plain ripe tomato flesh is safe. For the full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</div>

        <h2>What if my dog ate a tomato leaf or green tomato?</h2>
        <p>Call a vet or poison helpline promptly if the dog ate stems, leaves, vines, or a green tomato — solanine poisoning can cause drooling, vomiting, diarrhea, confusion, and weakness. A few bites of ripe red flesh is usually just a mild tummy upset that passes. Our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers portion basics.</p>
        """,
        "faq": [
            ("Can dogs eat ripe tomatoes?", "Yes — ripe red tomato flesh is safe in small amounts, plain and without stems or leaves."),
            ("Can dogs eat tomato leaves or stems?", "No — the green parts of the plant contain solanine and are toxic. Keep dogs away from tomato plants and their trimmings."),
            ("Can dogs eat green (unripe) tomatoes?", "No — unripe tomatoes also contain solanine and can poison a dog. Only fully ripe red flesh is safe."),
            ("Can dogs eat tomato sauce or ketchup?", "No — sauces and ketchup are high in salt and sugar and often contain garlic or onion, which are toxic. Only plain ripe tomato is safe."),
            ("How much tomato can a dog eat?", "Keep treats under about 10% of daily calories: a couple of cubes for a small dog, up to half a cup for a large one."),
            ("Can puppies eat tomato?", "Yes, a cube or two of ripe flesh once weaned and on solid food — watch for loose stools."),
            ("Is tomato good for dogs?", "In small amounts, ripe tomato adds vitamin C, potassium, and lycopene, but it should stay an occasional low-cal treat."),
            ("What if my dog ate a tomato leaf or green tomato?", "Call a vet or poison helpline promptly — solanine poisoning needs quick care. Watch for vomiting, drooling, or weakness."),
        ],
        "related": ["foods-toxic-to-dogs", "how-much-to-feed-my-dog", "can-dogs-eat-potato"],
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
        "slug": "can-dogs-eat-bread",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Bread? Yes — Plain, but Empty Calories",
        "url": "/dog-nutrition/can-dogs-eat-bread/",
        "description": "Plain bread is safe for dogs in tiny amounts, but it adds little nutrition and raw dough is dangerous. Why plain wins, how much, and the yeast risk to avoid.",
        "lede": "Yes — a small piece of plain, fully baked bread is not toxic to dogs, but it is mostly empty calories. The one real emergency is raw dough, which can bloat the stomach and ferment into alcohol.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is bread safe for dogs?</h2>
        <p>A small bite of plain bread — white or brown, fully baked — is not toxic to dogs and will not hurt them. But bread is mostly starch with very little real nutrition for a carnivore, so it is empty calories: nice as a rare nibble, never a meal. Most dogs like it, but it earns its place only as an occasional treat, not a food group.</p>

        <h2>The real danger: raw dough</h2>
        <div class="callout warn">Raw bread or pizza dough is a genuine emergency. Live yeast keeps fermenting in a dog's warm stomach, so the dough expands and can bloat the stomach — a life-threatening condition. On top of that, the yeast produces alcohol, causing alcohol poisoning. A dog that ate raw dough needs a veterinarian immediately; do not wait for symptoms.</div>

        <h2>Bread nutrition at a glance</h2>
        <p>For scale, here is roughly what is in one slice of plain white bread (about 25 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Per slice</th></tr>
          <tr><td>Calories</td><td>~70 kcal</td></tr>
          <tr><td>Carbohydrate</td><td>~13 g</td></tr>
          <tr><td>Protein</td><td>~2.3 g</td></tr>
          <tr><td>Fat</td><td>~0.8 g</td></tr>
          <tr><td>Fiber</td><td>~0.6 g</td></tr>
        </table>
        <p>Low in protein and fat, high in starch — that is why bread is an occasional treat, not a nutrition source for dogs.</p>

        <h2>How much bread is safe?</h2>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. A sensible occasional amount by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe occasional piece</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>A thumbnail-sized crumb (1–2 small bites)</td></tr>
          <tr><td>5–15 kg</td><td>Up to 1/4 slice</td></tr>
          <tr><td>15–30 kg</td><td>Up to 1/2 slice</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/2–1 slice, occasionally</td></tr>
        </table>

        <h2>How to serve bread safely</h2>
        <ul>
          <li>Plain, fully baked, with nothing added — no butter, no salt, no garlic, no raisins.</li>
          <li>Tear into small pieces to avoid gulping a big dry chunk.</li>
          <li>Keep it rare; it is filler, not food.</li>
        </ul>

        <h2>Breads to never feed a dog</h2>
        <ul>
          <li><b>Raisin bread:</b> raisins (and grapes) are toxic to dogs and can cause kidney failure.</li>
          <li><b>Garlic or onion bread:</b> both damage a dog's red blood cells and are toxic.</li>
          <li><b>Anything with xylitol:</b> the artificial sweetener is highly toxic to dogs.</li>
          <li><b>Moldy bread:</b> some molds produce tremorgenic mycotoxins that can cause seizures.</li>
        </ul>

        <h2>Can puppies eat bread?</h2>
        <p>A tiny piece of plain bread is not toxic to puppies, but their calories are better spent on complete puppy food. Skip it unless you are using a crumb to hide a pill — and ask your vet first.</p>

        <h2>When bread isn't the answer</h2>
        <p>Bread does not settle a dog's stomach the way plain <a href="/dog-nutrition/can-dogs-eat-rice/">white rice</a> can, and it adds nothing a balanced diet lacks. If your dog has vomiting or diarrhea, see our <a href="/dog-health/dog-vomiting-causes/">vomiting guide</a> and our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a>, and call your vet rather than reaching for the loaf. For a full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</p>
        """,
        "faq": [
            ("Can dogs eat plain bread?", "Yes — a small piece of plain, fully baked white or brown bread is not toxic, but it is mostly empty calories and should stay an occasional treat."),
            ("Why is raw bread dough dangerous?", "Live yeast keeps fermenting in the stomach, expanding and risking bloat, while also producing alcohol and causing alcohol poisoning — a veterinary emergency."),
            ("Can dogs eat bread with butter or salt?", "Plain is best; butter adds fat a dog does not need and too much salt is harmful. A tiny buttered scrape will not hurt, but skip it when you can."),
            ("Is raisin bread safe for dogs?", "No — raisins and grapes are toxic to dogs and can cause kidney failure, so raisin bread must stay out of reach."),
            ("Can dogs eat garlic or onion bread?", "No — garlic and onion damage a dog's red blood cells and are toxic, so any savory or seasoned bread is off the menu."),
            ("Can puppies eat bread?", "A tiny piece of plain bread is not toxic to puppies, but their calories are better spent on complete puppy food; skip it unless hiding a pill with vet approval."),
            ("Does bread help a dog's upset stomach?", "Not really — plain white rice is the better bland soother. Bread is filler and adds nothing a balanced diet lacks."),
            ("What if my dog ate raw dough?", "Call a veterinarian immediately. Raw dough can bloat the stomach and ferment into alcohol; do not wait for symptoms to appear."),
        ],
        "related": ["can-dogs-eat-rice", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
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
        "slug": "can-dogs-eat-popcorn",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Popcorn? Yes — Air-Popped and Plain",
        "url": "/dog-nutrition/can-dogs-eat-popcorn/",
        "description": "Plain air-popped popcorn is a safe, low-calorie dog treat, but buttered, salted, or unpopped kernels are not. How to serve it plain and how much to offer safely.",
        "lede": "Yes — plain air-popped popcorn is a light, low-calorie treat many dogs love, but buttered and salted popcorn is not, and unpopped kernels are a choking and teeth risk. Plain and fully popped is the rule.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is popcorn safe for dogs?</h2>
        <p>Plain, air-popped popcorn with nothing added is safe for dogs and is a genuinely light snack — it is low in calories and brings a little fiber and a few minerals like magnesium and phosphorus. The problems come from how people usually eat it: drenched in butter and salt, or with unpopped hard kernels mixed in.</p>

        <h2>The real risks in a bowl of popcorn</h2>
        <ul>
          <li><b>Unpopped kernels:</b> hard, round, and a choking hazard, plus they can crack or break teeth. Pick them out before sharing.</li>
          <li><b>Butter and salt:</b> too much salt is harmful to dogs and butter adds fat they do not need; heavily buttered popcorn is best avoided.</li>
          <li><b>Coatings:</b> caramel, chocolate, or anything sugar-free may contain xylitol, which is highly toxic to dogs.</li>
        </ul>
        <div class="callout warn">Never give a dog popcorn with butter, salt, caramel, chocolate, or any sugar-free topping — and always remove the unpopped kernels first.</div>

        <h2>Popcorn nutrition at a glance</h2>
        <p>For scale, here is roughly what is in one cup of air-popped popcorn (about 8 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Per cup</th></tr>
          <tr><td>Calories</td><td>~31 kcal</td></tr>
          <tr><td>Carbohydrate</td><td>~6 g</td></tr>
          <tr><td>Fiber</td><td>~1.2 g</td></tr>
          <tr><td>Protein</td><td>~1 g</td></tr>
          <tr><td>Fat</td><td>~0.4 g</td></tr>
        </table>
        <p>Low calorie, light fiber — that is why plain popcorn is a reasonable occasional treat, not a daily snack.</p>

        <h2>How much popcorn is safe?</h2>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. A sensible occasional amount by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe occasional amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>A few plain pieces (1–2 tbsp)</td></tr>
          <tr><td>5–15 kg</td><td>Up to 1/4 cup</td></tr>
          <tr><td>15–30 kg</td><td>Up to 1/2 cup</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/2–1 cup, occasionally</td></tr>
        </table>

        <h2>How to serve popcorn safely</h2>
        <ul>
          <li>Air-pop it with no oil, butter, salt, or sugar.</li>
          <li>Remove every unpopped kernel by hand.</li>
          <li>Let it cool — fresh popcorn can be hot enough to burn a dog's mouth.</li>
        </ul>

        <h2>Can puppies eat popcorn?</h2>
        <p>Plain air-popped popcorn is not toxic to puppies, but the choking risk from kernels is higher for small dogs, so it is safer to skip it for puppies and stick to their complete food.</p>

        <h2>When popcorn isn't worth it</h2>
        <p>Popcorn is a fun, low-calorie nibble, not a nutrition source. If your dog has a sensitive stomach, plain <a href="/dog-nutrition/can-dogs-eat-rice/">white rice</a> or <a href="/dog-nutrition/can-dogs-eat-cucumber/">cucumber</a> are gentler choices, and our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers portion basics. For a full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</p>
        """,
        "faq": [
            ("Can dogs eat plain popcorn?", "Yes — plain air-popped popcorn with no butter, salt, or sugar is a safe, low-calorie treat for most dogs."),
            ("Why are unpopped kernels dangerous?", "They are a choking hazard and can crack or break teeth, so pick them all out before sharing popcorn with a dog."),
            ("Can dogs eat buttered or salted popcorn?", "Butter adds fat a dog does not need and too much salt is harmful, so plain air-popped popcorn is the only safe choice."),
            ("Is caramel or chocolate popcorn safe?", "No — caramel and chocolate coatings add sugar and, if sugar-free, may contain xylitol, which is highly toxic to dogs."),
            ("How much popcorn can a dog have?", "Keep it under about 10% of daily calories: a few pieces for toy dogs, up to a cup for large dogs, only occasionally."),
            ("Can puppies eat popcorn?", "Plain air-popped popcorn is not toxic, but the kernel choking risk is higher for small puppies, so it is safer to skip."),
            ("Is popcorn good for dogs?", "It is a light, low-calorie nibble with a little fiber, but it is a treat, not a nutrition source — keep it occasional."),
            ("What if my dog ate buttered popcorn?", "A small amount will likely be fine, but large amounts of fat and salt can upset the stomach; watch for vomiting and call your vet if it persists."),
        ],
        "related": ["can-dogs-eat-rice", "can-dogs-eat-cucumber", "foods-toxic-to-dogs"],
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
        "slug": "can-dogs-eat-honey",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Honey? Yes — in Tiny Amounts",
        "url": "/dog-nutrition/can-dogs-eat-honey/",
        "description": "Plain honey is safe for dogs in tiny amounts, but it is sugar with few real benefits. Why puppies and diabetic dogs should skip it, and exactly how much is safe.",
        "lede": "Yes — a lick of plain honey is not toxic to dogs, but it is essentially sugar, so it belongs in the 'tiny treat' category. The two dogs who should skip it entirely are puppies under a year and diabetic dogs.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is honey safe for dogs?</h2>
        <p>Plain honey is not toxic to dogs, and a small dab now and then will not hurt a healthy adult dog. But honey is mostly sugar — about 17 g in a single tablespoon — so it is a treat, not a health food. Any 'immune boost' or 'allergy cure' claims you see online are not backed by veterinary evidence; think of honey as a sweet occasional nibble, nothing more.</p>

        <h2>The two dogs who should skip honey</h2>
        <div class="callout warn">Two groups should not eat honey. Puppies under about 12 months: their gut is not mature enough to handle the <i>Clostridium botulinum</i> spores honey can contain, which can cause infant botulism. And diabetic dogs: honey spikes blood sugar fast. For both, honey is off the menu.</div>

        <h2>Honey nutrition at a glance</h2>
        <p>For scale, here is roughly what is in one tablespoon of honey (about 21 g):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Per tablespoon</th></tr>
          <tr><td>Calories</td><td>~64 kcal</td></tr>
          <tr><td>Sugar</td><td>~17 g</td></tr>
          <tr><td>Protein</td><td>~0.1 g</td></tr>
          <tr><td>Fat</td><td>~0 g</td></tr>
        </table>
        <p>Almost pure sugar is why honey is a rare treat, not a daily drizzle — the calories add up fast for a small dog.</p>

        <h2>How much honey is safe?</h2>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. A sensible occasional amount by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe occasional amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>A dab (1/4 teaspoon or less)</td></tr>
          <tr><td>5–15 kg</td><td>Up to 1/2 teaspoon</td></tr>
          <tr><td>15–30 kg</td><td>Up to 1 teaspoon</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1–2 teaspoons, occasionally</td></tr>
        </table>

        <h2>How to serve honey</h2>
        <ul>
          <li>Plain, with nothing added — no sweeteners, no mix-ins.</li>
          <li>A tiny dab can help a pill go down if your dog is a fussy taker (check with your vet first).</li>
          <li>Raw honey carries the same puppy caution, so keep it away from young dogs.</li>
        </ul>

        <h2>Are there risks?</h2>
        <p>Beyond sugar weight gain and tooth decay from regular use, the only real danger is the puppy botulism risk above and any honey blended with artificial sweeteners — which can include xylitol, highly toxic to dogs. Plain honey only, and never for puppies or diabetic dogs. For the full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</p>

        <h2>Can puppies eat honey?</h2>
        <p>No — not under about 12 months. Their immature digestive system cannot be trusted with <i>C. botulinum</i> spores. Wait until adulthood, and even then keep it to a rare dab.</p>

        <h2>When honey isn't the answer</h2>
        <p>Honey will not cure allergies or coat conditions, and it is not a substitute for balanced food. If your dog has persistent skin, weight, or gut issues, our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> and a chat with your vet beat a honey jar every time. Plain <a href="/dog-nutrition/can-dogs-eat-pumpkin/">pumpkin</a> is a far better everyday topper for most dogs.</p>
        """,
        "faq": [
            ("Can dogs eat honey?", "Yes — plain honey is not toxic and a tiny amount is fine for a healthy adult dog, but it is mostly sugar, so keep it a rare treat."),
            ("Why can't puppies eat honey?", "Puppies under about 12 months have immature guts that cannot handle Clostridium botulinum spores honey can contain, risking infant botulism."),
            ("Can diabetic dogs eat honey?", "No — honey spikes blood sugar quickly, so diabetic dogs should avoid it entirely."),
            ("Is honey good for dogs' allergies?", "No proven veterinary benefit — honey is sugar, not a cure; any allergy claims are unsubstantiated."),
            ("How much honey can a dog have?", "Keep it tiny: a dab for toy dogs, up to a teaspoon or two for large dogs, only occasionally, under 10% of daily calories."),
            ("Can honey help my dog take a pill?", "A tiny dab can help a fussy dog swallow a pill, but check with your vet first and use plain honey only."),
            ("Is raw honey safe for dogs?", "For adult dogs yes, but it carries the same puppy botulism caution, so keep raw honey away from young dogs."),
            ("What if honey has sweeteners added?", "Avoid any honey with added sweeteners, which can include xylitol — highly toxic to dogs. Plain honey only."),
        ],
        "related": ["can-dogs-eat-pumpkin", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
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
        "slug": "can-dogs-eat-yogurt",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Yogurt? Yes — Plain and Unsweetened",
        "url": "/dog-nutrition/can-dogs-eat-yogurt/",
        "description": "Plain unsweetened yogurt is a safe probiotic treat for many dogs, but lactose intolerance and xylitol are the catches. How to choose it and how much to feed.",
        "lede": "Yes — plain, unsweetened yogurt is a safe, gut-friendly treat for many dogs, thanks to lower lactose than milk and live cultures. The catches are lactose intolerance and, above all, any yogurt sweetened with xylitol.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is yogurt safe for dogs?</h2>
        <p>Plain, unsweetened yogurt is not toxic to dogs and is a reasonable occasional treat. Because the live cultures break down much of the lactose, yogurt is easier on the gut than plain milk, and it brings a little protein and calcium plus probiotics. But many dogs are still at least mildly lactose intolerant, so start with a small amount and watch the results.</p>

        <h2>How to choose the right yogurt</h2>
        <ul>
          <li><b>Plain:</b> no added sugar, no fruit, no flavoring.</li>
          <li><b>Unsweetened:</b> never any product with xylitol or other artificial sweeteners — xylitol is highly toxic to dogs.</li>
          <li><b>Greek is best:</b> strained yogurt is thicker and even lower in lactose, so it suits more dogs.</li>
          <li><b>Avoid:</b> flavored, 'light', or diet yogurts — they are the ones most likely to hide xylitol or sugar alcohols.</li>
        </ul>
        <div class="callout warn">The single most important rule: the yogurt must contain no xylitol. Check the label every time, because a 'sugar-free' yogurt can be deadly for a dog.</div>

        <h2>Yogurt nutrition at a glance</h2>
        <p>For scale, here is roughly what is in 100 g of plain low-fat yogurt:</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Per 100 g</th></tr>
          <tr><td>Calories</td><td>~59 kcal</td></tr>
          <tr><td>Protein</td><td>~10 g</td></tr>
          <tr><td>Fat</td><td>~1.5 g</td></tr>
          <tr><td>Sugar (natural)</td><td>~3–4 g</td></tr>
          <tr><td>Calcium</td><td>~110 mg</td></tr>
        </table>
        <p>Modest protein and calcium with low natural sugar make plain yogurt a decent occasional topper — once you rule out sweetener and lactose issues.</p>

        <h2>How much yogurt is safe?</h2>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. A sensible occasional amount by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe occasional amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>1 teaspoon</td></tr>
          <tr><td>5–15 kg</td><td>1–2 tablespoons</td></tr>
          <tr><td>15–30 kg</td><td>2–4 tablespoons</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/4 cup, occasionally</td></tr>
        </table>

        <h2>How to serve yogurt</h2>
        <ul>
          <li>Offer a plain spoonful, or freeze dollops for a cool treat.</li>
          <li>Use it to hide a pill for a fussy taker (vet approval first).</li>
          <li>Stick to plain — no granola, no honey drizzle, no fruit mix-ins.</li>
        </ul>

        <h2>Are there risks?</h2>
        <p>The two real catches: xylitol-sweetened yogurt is an emergency, and lactose-intolerant dogs may get gas or diarrhea. If your dog reacts badly, stop and switch to a non-dairy option. For the full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>. Note that <a href="/dog-nutrition/can-dogs-eat-milk/">milk</a> is higher in lactose, so yogurt is usually the gentler dairy choice.</p>

        <h2>Can puppies eat yogurt?</h2>
        <p>A small amount of plain yogurt is not toxic to puppies, but their guts are sensitive, so keep portions tiny and watch for loose stools. Plain pumpkin or a vet-recommended puppy food is a safer everyday choice.</p>

        <h2>When yogurt isn't the answer</h2>
        <p>Yogurt is a fun occasional topper, not a probiotic cure. If your dog has ongoing digestive trouble, our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> and a vet visit beat a yogurt tub. Persistent diarrhea, vomiting, or bloating needs a professional, not dairy.</p>
        """,
        "faq": [
            ("Can dogs eat plain yogurt?", "Yes — plain, unsweetened yogurt is a safe occasional treat for many dogs and is easier to digest than milk thanks to lower lactose and live cultures."),
            ("Is Greek yogurt better for dogs?", "Greek yogurt is strained and even lower in lactose, so it suits more dogs; just keep it plain and unsweetened."),
            ("Why must yogurt have no xylitol?", "Xylitol is highly toxic to dogs and can cause a fatal blood-sugar crash; always check the label and avoid any 'sugar-free' yogurt."),
            ("Can lactose-intolerant dogs eat yogurt?", "Many can tolerate small amounts because cultures lower the lactose, but some still get gas or diarrhea — start tiny and watch."),
            ("How much yogurt can a dog have?", "Keep it under 10% of daily calories: a teaspoon for toy dogs, up to 1/4 cup for large dogs, only occasionally."),
            ("Can dogs eat flavored or fruit yogurt?", "No — flavored and 'light' yogurts often hide sugar or xylitol; stick to plain, unsweetened yogurt only."),
            ("Can puppies eat yogurt?", "A small amount of plain yogurt is not toxic, but puppy guts are sensitive, so keep portions tiny and watch for loose stools."),
            ("Is yogurt a probiotic cure for dogs?", "No — it is a fun occasional topper, not a treatment; ongoing gut issues need a vet, not a yogurt tub."),
        ],
        "related": ["can-dogs-eat-milk", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
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
        "slug": "can-dogs-eat-salmon",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Salmon? Yes — Cooked, Never Raw",
        "url": "/dog-nutrition/can-dogs-eat-salmon/",
        "description": "Cooked salmon is a safe, omega-3-rich dog food, but raw salmon can carry a deadly parasite. Why to cook it plainly, debone it, and skip salt and seasoning.",
        "lede": "Yes — cooked salmon is one of the best fish you can offer a dog, packed with omega-3s and lean protein. The one hard rule: never feed it raw, because raw salmon can carry a parasite that is fatal to dogs.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is salmon good for dogs?</h2>
        <p>Fully cooked salmon is excellent for dogs. It is a rich source of omega-3 fatty acids, which support skin, coat, and joint health, plus high-quality lean protein. Many premium dog foods use salmon as the headline ingredient for good reason. The benefits are real — as long as it is cooked and plainly prepared.</p>

        <h2>The danger: raw salmon</h2>
        <div class="callout warn">Never feed a dog raw salmon (or raw trout). In parts of the Pacific Northwest, wild salmon can carry a parasite, <i>Nanophyetus salmincola</i>, that harbors a bacterium causing salmon poisoning disease — fatal to dogs if untreated, though it does not affect people. Cooking kills both the parasite and the bacterium. Raw fish elsewhere also risks ordinary parasites and bacteria, so cook it every time.</div>

        <h2>Salmon nutrition at a glance</h2>
        <p>For scale, here is roughly what is in 100 g of cooked salmon (about one small fillet piece):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Per 100 g cooked</th></tr>
          <tr><td>Calories</td><td>~208 kcal</td></tr>
          <tr><td>Protein</td><td>~20 g</td></tr>
          <tr><td>Fat</td><td>~13 g</td></tr>
          <tr><td>Omega-3</td><td>~1.5–2.5 g</td></tr>
        </table>
        <p>High protein and omega-3 with moderate fat are why cooked salmon is a standout topper, not just a treat.</p>

        <h2>How much salmon is safe?</h2>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. A sensible occasional amount by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe occasional amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>1–2 small flakes (1 tablespoon)</td></tr>
          <tr><td>5–15 kg</td><td>2–3 tablespoons</td></tr>
          <tr><td>15–30 kg</td><td>1/4 cup flaked</td></tr>
          <tr><td>30 kg and up</td><td>1/4–1/2 cup, occasionally</td></tr>
        </table>

        <h2>How to serve salmon</h2>
        <ul>
          <li>Always cook it through — baked, steamed, or poached. No raw.</li>
          <li>Remove every bone; even small pin bones can choke or splinter.</li>
          <li>No salt, oil, garlic, onion, or seasoning — plain is the rule.</li>
          <li>Skip smoked salmon: it is far too salty for a dog.</li>
        </ul>

        <h2>Can puppies eat salmon?</h2>
        <p>Yes — cooked, deboned, plain salmon is a healthy protein for puppies in small amounts. It is gentler than many meats and supports growing coats and brains.</p>

        <h2>Are there risks?</h2>
        <p>Beyond raw salmon, the catches are bones and rich skin (high fat can trigger pancreatitis in sensitive dogs), plus any salmon prepared with garlic, onion, salt, or oil. Canned salmon is acceptable if it is in water with no salt added and bones removed. For more safe proteins, see our <a href="/dog-nutrition/can-dogs-eat-chicken/">chicken guide</a> and <a href="/dog-nutrition/can-dogs-eat-shrimp/">shrimp guide</a>.</p>

        <h2>When salmon isn't the answer</h2>
        <p>Salmon is a healthy occasional protein, not an everyday staple, and it does not replace balanced dog food. Dogs with pancreatitis or fish allergies should skip it. If your dog shows vomiting, diarrhea, or lethargy after eating fish, our <a href="/dog-health/dog-vomiting-causes/">vomiting guide</a> explains what is urgent, and a vet visit beats another fillet.</p>
        """,
        "faq": [
            ("Can dogs eat salmon?", "Yes — cooked, deboned, plain salmon is a healthy, omega-3-rich protein for dogs; it is a common premium dog-food ingredient."),
            ("Why can't dogs eat raw salmon?", "Raw salmon can carry a parasite that causes salmon poisoning disease, fatal to dogs if untreated; cooking kills it. Raw fish also risks other parasites and bacteria."),
            ("Is salmon good for a dog's coat and skin?", "Yes — the omega-3s in cooked salmon support skin, coat, and joint health, which is why salmon leads many quality dog foods."),
            ("How much salmon can a dog eat?", "Keep it occasional, under about 10% of daily calories: a tablespoon for toy dogs, up to 1/2 cup for large dogs."),
            ("Can dogs eat smoked or canned salmon?", "Smoked salmon is too salty; canned is OK only if packed in water with no salt and bones removed."),
            ("Can puppies eat salmon?", "Yes — cooked, deboned, plain salmon is a healthy protein for puppies in small amounts."),
            ("Can dogs eat salmon skin?", "It is fatty and can trigger pancreatitis in sensitive dogs, so it is best removed; plain cooked flesh is the safer choice."),
            ("What if my dog ate raw salmon?", "Contact a veterinarian promptly — raw salmon can cause salmon poisoning disease, which is serious but treatable if caught early."),
        ],
        "related": ["can-dogs-eat-chicken", "can-dogs-eat-shrimp", "foods-toxic-to-dogs"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Salmon Poisoning Disease",
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
        "slug": "can-dogs-eat-shrimp",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Shrimp? Yes — Cooked and Peeled",
        "url": "/dog-nutrition/can-dogs-eat-shrimp/",
        "description": "Cooked, peeled shrimp is a safe, low-fat, high-protein dog treat, but raw shrimp and shells are the real risks. How to serve it plain and how much is safe.",
        "lede": "Yes — cooked, peeled shrimp is a lean, protein-rich treat many dogs love. The rules are simple: cook it, peel it, and skip the garlic butter and frying that make shrimp dangerous.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Is shrimp safe for dogs?</h2>
        <p>Plain cooked shrimp is safe for dogs and is a genuinely lean protein — high in protein, very low in fat, and a useful source of vitamin B12 and selenium. For a dog watching its weight, shrimp is a better treat than most cheese or meat scraps. The problems come from how people usually eat it: raw, shell-on, or drowned in garlic butter.</p>

        <h2>The risks in a plate of shrimp</h2>
        <ul>
          <li><b>Raw shrimp:</b> can carry bacteria and is harder to digest; cook it through.</li>
          <li><b>Shells and tails:</b> sharp and a choking or gut-blocking hazard — always peel and remove the tail.</li>
          <li><b>Devein:</b> the dark intestinal tract is best removed for cleanliness.</li>
          <li><b>Garlic butter and frying:</b> butter adds fat a dog does not need and garlic is toxic; fried, breaded shrimp is off the menu.</li>
        </ul>
        <div class="callout warn">Never feed a dog raw shrimp, shells, tails, or anything cooked with garlic, onion, butter, or heavy oil. Plain boiled or steamed shrimp, peeled, is the only safe way.</div>

        <h2>Shrimp nutrition at a glance</h2>
        <p>For scale, here is roughly what is in 100 g of cooked shrimp (about 4–5 medium shrimp):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Per 100 g cooked</th></tr>
          <tr><td>Calories</td><td>~99 kcal</td></tr>
          <tr><td>Protein</td><td>~24 g</td></tr>
          <tr><td>Fat</td><td>~0.3 g</td></tr>
          <tr><td>Cholesterol</td><td>~189 mg</td></tr>
        </table>
        <p>Very high protein, very low fat — that is why shrimp is a great lean treat, in moderation.</p>

        <h2>How much shrimp is safe?</h2>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. A sensible occasional amount by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe occasional amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>1 small shrimp, chopped</td></tr>
          <tr><td>5–15 kg</td><td>2–3 small shrimp</td></tr>
          <tr><td>15–30 kg</td><td>4–5 medium shrimp</td></tr>
          <tr><td>30 kg and up</td><td>Up to 6–7 medium shrimp, occasionally</td></tr>
        </table>

        <h2>How to serve shrimp</h2>
        <ul>
          <li>Boil or steam plain, with no salt, butter, or seasoning.</li>
          <li>Peel completely and remove the tail and vein.</li>
          <li>Chop for small dogs so nothing is a choking lump.</li>
        </ul>

        <h2>Can puppies eat shrimp?</h2>
        <p>Cooked, peeled shrimp is not toxic to puppies, but the choking risk from shells is higher for small mouths, so keep portions tiny and always chop and peel thoroughly.</p>

        <h2>Are there risks?</h2>
        <p>The main risks are shells, raw shrimp, and garlic-butter or fried preparation. Shrimp is also a shellfish, so a small number of dogs are allergic — introduce one piece and watch for itching, swelling, or digestive upset. For another lean protein, see our <a href="/dog-nutrition/can-dogs-eat-salmon/">salmon guide</a>; for a full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</p>

        <h2>When shrimp isn't the answer</h2>
        <p>Shrimp is a fun, lean occasional treat, not a nutrition source or a meal. Dogs with shellfish allergy or pancreatitis should skip it. If your dog shows signs of an allergic reaction — face swelling, hives, trouble breathing — that is an emergency; call your vet. Otherwise, our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers everyday portions.</p>
        """,
        "faq": [
            ("Can dogs eat shrimp?", "Yes — cooked, peeled shrimp is a safe, lean, high-protein treat for most dogs; it is low in fat and a good source of vitamin B12."),
            ("Why must shrimp be cooked and peeled?", "Raw shrimp can carry bacteria, and shells or tails are a choking and gut-blocking hazard, so always cook and peel it completely."),
            ("Can dogs eat shrimp with garlic butter?", "No — garlic is toxic to dogs and butter adds unneeded fat; only plain boiled or steamed shrimp is safe."),
            ("How much shrimp can a dog have?", "Keep it occasional, under about 10% of daily calories: one small shrimp for toy dogs, up to 6–7 for large dogs."),
            ("Can puppies eat shrimp?", "Cooked, peeled shrimp is not toxic, but the shell choking risk is higher for small puppies, so keep portions tiny and chop finely."),
            ("Can dogs be allergic to shrimp?", "Yes — shellfish allergy is possible; introduce one piece and watch for itching, swelling, or digestive upset."),
            ("Is fried or breaded shrimp safe?", "No — the frying, breading, and seasonings add fat and often garlic or onion, so skip it entirely."),
            ("What if my dog ate raw shrimp?", "Watch for vomiting or diarrhea; if symptoms appear or your dog seems unwell, contact your vet. Cooked shrimp only going forward."),
        ],
        "related": ["can-dogs-eat-salmon", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
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
        "slug": "can-dogs-eat-peas",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Peas? Yes — a Healthy, Low-Fat Veggie",
        "url": "/dog-nutrition/can-dogs-eat-peas/",
        "description": "Plain peas are a safe, low-fat, fiber-rich veggie for dogs, but canned peas are too salty and the pods can choke. How to serve them and how much is safe.",
        "lede": "Yes — plain peas are a safe, low-calorie, fiber-rich vegetable that many dogs enjoy, and they show up in plenty of quality dog foods. The catches are canned peas (too much salt) and whole pods, which can choke a small dog.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Are peas good for dogs?</h2>
        <p>Green peas are a healthy, low-fat treat for dogs. They bring fiber, a surprising amount of plant protein, and vitamins like K and C plus thiamin. Because they are low in calories, they are a good crunchy option for dogs watching their weight — and they are a common, well-tolerated ingredient in premium dog foods.</p>

        <h2>The catches: canned peas and pods</h2>
        <ul>
          <li><b>Canned peas:</b> almost always packed in salt, so the sodium is too high for a dog. Use fresh or frozen instead.</li>
          <li><b>Pods and strings:</b> snow or sugar-snap pea pods can be a choking or gut hazard for small dogs — shell them or cut into tiny pieces.</li>
          <li><b>Raw garden peas:</b> fine in small amounts, though cooking or thawing makes them easier to digest.</li>
        </ul>
        <div class="callout">Frozen peas straight from the bag, thawed, are one of the easiest safe veggies — no salt, no prep beyond a rinse.</div>

        <h2>Peas nutrition at a glance</h2>
        <p>For scale, here is roughly what is in 100 g of cooked green peas (about half a cup):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Per 100 g cooked</th></tr>
          <tr><td>Calories</td><td>~81 kcal</td></tr>
          <tr><td>Protein</td><td>~5 g</td></tr>
          <tr><td>Carbohydrate</td><td>~14 g</td></tr>
          <tr><td>Fiber</td><td>~5 g</td></tr>
          <tr><td>Vitamin C</td><td>small amount</td></tr>
        </table>
        <p>Low calorie, decent fiber and protein are why peas are a smart light treat, not a nutrition gap-filler.</p>

        <h2>How much peas is safe?</h2>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. A sensible occasional amount by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe occasional amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>1 tablespoon, mashed or whole</td></tr>
          <tr><td>5–15 kg</td><td>2–3 tablespoons</td></tr>
          <tr><td>15–30 kg</td><td>1/4 cup</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/3 cup, occasionally</td></tr>
        </table>

        <h2>How to serve peas</h2>
        <ul>
          <li>Fresh cooked or thawed frozen, plain — no salt, butter, or oil.</li>
          <li>Shell snow/sugar-snap peas and cut pods small for toy breeds.</li>
          <li>Mash for very small dogs so nothing is a choking lump.</li>
        </ul>

        <h2>Can puppies eat peas?</h2>
        <p>Yes — plain peas are not toxic to puppies and make a low-calorie training treat, but keep portions tiny and mash them for small breeds.</p>

        <h2>Are there risks?</h2>
        <p>Peas are low-risk, but they can cause gas in some dogs, and canned peas are too salty. A small number of dogs with kidney issues are sometimes advised to limit certain legumes, so check with your vet if that applies. For another gentle veggie, see our <a href="/dog-nutrition/can-dogs-eat-green-beans/">green beans guide</a>; for the full list of dangerous additions, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</p>

        <h2>When peas aren't the answer</h2>
        <p>Peas are a fun, healthy occasional veggie, not a meal. If your dog has persistent gas, bloating, or kidney concerns, our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> and a vet visit beat a bag of frozen peas. Persistent vomiting or a painful belly needs a professional, not more vegetables.</p>
        """,
        "faq": [
            ("Can dogs eat peas?", "Yes — plain green peas are a safe, low-fat, fiber-rich treat for most dogs and are a common ingredient in quality dog foods."),
            ("Can dogs eat canned peas?", "Avoid them — canned peas are packed in too much salt for a dog; use fresh or frozen peas instead."),
            ("Can dogs eat pea pods?", "Snow or sugar-snap pods can choke small dogs, so shell them or cut tiny; the peas inside are the safe part."),
            ("Are frozen peas safe for dogs?", "Yes — thawed frozen peas are one of the easiest safe veggies, with no salt and minimal prep."),
            ("How much peas can a dog have?", "Keep it occasional, under about 10% of daily calories: a tablespoon for toy dogs, up to 1/3 cup for large dogs."),
            ("Can puppies eat peas?", "Yes — plain peas are not toxic and make a low-calorie training treat, but keep portions tiny and mash for small breeds."),
            ("Do peas cause gas in dogs?", "Some dogs get gassy from peas; start small and watch, and limit them if your dog is prone to flatulence."),
            ("Are peas bad for dogs with kidney issues?", "A vet may advise limiting certain legumes for some kidney conditions, so check with your vet if that applies."),
        ],
        "related": ["can-dogs-eat-green-beans", "can-dogs-eat-cucumber", "foods-toxic-to-dogs"],
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
        "slug": "can-dogs-eat-corn",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Corn? Yes — the Kernels, Not the Cob",
        "url": "/dog-nutrition/can-dogs-eat-corn/",
        "description": "Plain cooked corn kernels are safe for dogs, but the cob is a dangerous choking and blockage risk. Why to skip butter and never let a dog chew the cob.",
        "lede": "Yes — plain cooked corn kernels are safe and show up in many dog foods, but the corn cob is a serious hazard: it does not digest and can block a dog's intestine, often needing surgery. Kernels yes, cob never.",
        "eyebrow": "DOG NUTRITION",
        "body": """
        <h2>Are corn kernels safe for dogs?</h2>
        <p>Plain cooked corn kernels are safe for dogs and are a common, well-tolerated carbohydrate in dog food. They offer some fiber and a little protein. The grain itself is not the problem — the cob is.</p>

        <h2>The cob is the real danger</h2>
        <div class="callout warn">Never let a dog chew or eat a corn cob. A cob does not break down in a dog's digestive tract and can cause a life-threatening intestinal blockage that often requires surgery. Dogs love to gulp them whole, so keep cobs in the trash, not the bowl.</div>

        <h2>Corn nutrition at a glance</h2>
        <p>For scale, here is roughly what is in 100 g of cooked corn kernels (about half a cup):</p>
        <table>
          <tr><th style="text-align:left">Nutrient</th><th style="text-align:left">Per 100 g cooked</th></tr>
          <tr><td>Calories</td><td>~96 kcal</td></tr>
          <tr><td>Carbohydrate</td><td>~21 g</td></tr>
          <tr><td>Fiber</td><td>~2.4 g</td></tr>
          <tr><td>Protein</td><td>~3.4 g</td></tr>
        </table>
        <p>Mostly carbohydrate with a little fiber — corn is an energy treat, not a nutrition powerhouse, so keep it small.</p>

        <h2>How much corn is safe?</h2>
        <p>Treats of any kind should stay under about 10% of a dog's daily calories. A sensible occasional amount by body weight:</p>
        <table>
          <tr><th style="text-align:left">Dog weight</th><th style="text-align:left">Safe occasional amount</th></tr>
          <tr><td>Under 5 kg (toy / small)</td><td>1–2 tablespoons kernels</td></tr>
          <tr><td>5–15 kg</td><td>2–3 tablespoons</td></tr>
          <tr><td>15–30 kg</td><td>1/4 cup kernels</td></tr>
          <tr><td>30 kg and up</td><td>Up to 1/3 cup, occasionally</td></tr>
        </table>

        <h2>How to serve corn</h2>
        <ul>
          <li>Cut the kernels off the cob first — never hand over the cob.</li>
          <li>Plain, cooked, with no butter, salt, or oil.</li>
          <li>Canned corn is fine only if it is no-salt-added; rinse it to cut sodium further.</li>
        </ul>

        <h2>Can puppies eat corn?</h2>
        <p>Plain cooked kernels (off the cob) are not toxic to puppies, but keep portions tiny and always remove every bit of cob.</p>

        <h2>Are there risks?</h2>
        <p>The cob is the headline risk; beyond that, buttered or salted corn adds fat and sodium a dog does not need, and raw corn is harder to digest. Corn is also a common allergen, though true corn allergy in dogs is uncommon. For another plain-carb treat, see our <a href="/dog-nutrition/can-dogs-eat-rice/">rice guide</a>; for the full list of dangerous items, see our <a href="/dog-nutrition/foods-toxic-to-dogs/">toxic foods guide</a>.</p>

        <h2>When corn isn't the answer</h2>
        <p>Corn kernels are a small occasional treat, and the cob is never food. If your dog has vomiting, abdominal pain, or straining to poop after getting near a cob, that is an emergency — call your vet. Otherwise, our <a href="/dog-nutrition/how-much-to-feed-my-dog/">feeding guide</a> covers everyday portions.</p>
        """,
        "faq": [
            ("Can dogs eat corn?", "Yes — plain cooked corn kernels are safe and common in dog food; the problem is the cob, not the kernels."),
            ("Why is the corn cob dangerous?", "A cob does not digest and can block a dog's intestine, often requiring surgery — never let a dog chew or eat a cob."),
            ("Can dogs eat corn with butter or salt?", "Plain is best; butter adds fat and salt is harmful, so serve kernels with nothing added."),
            ("Can dogs eat canned corn?", "Yes only if it is no-salt-added; rinse it to cut sodium further, and never the cob."),
            ("How much corn can a dog have?", "Keep it occasional, under about 10% of daily calories: a tablespoon or two for small dogs, up to 1/3 cup for large dogs."),
            ("Can puppies eat corn?", "Plain cooked kernels off the cob are not toxic, but keep portions tiny and remove all cob completely."),
            ("Can dogs be allergic to corn?", "Corn allergy is uncommon but possible; if you see itching or digestive upset, stop and ask your vet."),
            ("What if my dog ate a corn cob?", "Call a veterinarian promptly — a swallowed cob can block the intestine and often needs surgery; do not wait for symptoms."),
        ],
        "related": ["can-dogs-eat-rice", "foods-toxic-to-dogs", "how-much-to-feed-my-dog"],
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
        "slug": "can-dogs-eat-onion",
        "url": "/dog-nutrition/can-dogs-eat-onion/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Onion? No — Even a Little Is Toxic",
        "description": "Onion is toxic to dogs in any form — raw, cooked, powdered, or in broth. It damages red blood cells and can cause fatal anemia. Learn the risks and next steps.",
        "lede": "No — onion is toxic to dogs in every form, with no safe dose. Its sulfur compounds destroy red blood cells and cause hemolytic anemia, often days after eating. Onion powder hiding in sauces and broths is the most common source.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>no</strong>. Onion is one of the most dangerous everyday
        foods for dogs. Unlike many "people foods" that are safe in moderation, onion has
        <strong>no safe dose</strong> — and the toxic compound survives cooking, frying, and
        even dehydration into powder.</p>

        <h2>Why onion is toxic to dogs</h2>
        <p>Onions belong to the <em>Allium</em> family (along with garlic, leeks, chives, and
        shallots). They contain sulfur compounds called <strong>organosulfides</strong> that,
        once absorbed, damage a dog's red blood cells. The cells become fragile and burst
        (a process called <em>hemolysis</em>), leading to <strong>hemolytic anemia</strong> —
        too few healthy red blood cells to carry oxygen.</p>
        <p>The damage is not instant. Symptoms can appear within a day, but often take
        <strong>2–4 days</strong> to show up, which is why owners frequently don't connect the
        illness to the food their dog ate days earlier.</p>

        <h2>Every form is dangerous</h2>
        <ul>
          <li><strong>Raw onion</strong> — whole, chopped, or in salads.</li>
          <li><strong>Cooked onion</strong> — sautéed, roasted, in soups or stews.</li>
          <li><strong>Onion powder</strong> — the sneakiest form; it is concentrated and hides in
            spice blends, gravy mixes, bouillon, and many packaged sauces.</li>
          <li><strong>Caramelized or fried onion</strong> — still toxic, just tastier to dogs.</li>
          <li><strong>Leftover scraps and table scraps</strong> — a single discarded slice can
            sicken a small dog.</li>
        </ul>
        <p>Cats are even more sensitive than dogs, but this page focuses on dogs.</p>

        <h2>How much onion is too much?</h2>
        <p>Veterinary toxicology references place the concerning dose around
        <strong>15–30 g of onion per kg of body weight</strong> (roughly 0.5–1 oz per 2.2 lb).
        That sounds like a lot — but onion powder is far more concentrated, and small dogs
        reach the danger zone with just a teaspoon of powder or a few bites of a sauced dish.</p>
        <table class="dose">
          <thead><tr><th>Dog weight</th><th>Rough toxic amount (fresh)</th><th>Safe amount</th></tr></thead>
          <tbody>
            <tr><td>5 kg (11 lb)</td><td>~75–150 g (half a small onion)</td><td><strong>0 — none</strong></td></tr>
            <tr><td>10 kg (22 lb)</td><td>~150–300 g</td><td><strong>0 — none</strong></td></tr>
            <tr><td>20 kg (44 lb)</td><td>~300–600 g</td><td><strong>0 — none</strong></td></tr>
            <tr><td>30 kg (66 lb)</td><td>~450 g–900 g</td><td><strong>0 — none</strong></td></tr>
          </tbody>
        </table>
        <p class="note">Because powdered and cooked forms are concentrated and easy to
        over-serve, treat the safe amount as <strong>zero</strong> for every dog, of every size.</p>

        <h2>Signs of onion poisoning</h2>
        <p>Watch for these over the 2–4 days after exposure:</p>
        <ul>
          <li>Lethargy, weakness, or reluctance to move</li>
          <li>Pale or yellowish gums (signs of anemia)</li>
          <li>Rapid breathing or elevated heart rate</li>
          <li>Red or brown urine (broken red cells are being cleared)</li>
          <li>Vomiting, diarrhea, loss of appetite</li>
          <li>Collapse in severe cases</li>
        </ul>

        <h2>What to do if your dog ate onion</h2>
        <ol>
          <li><strong>Note what and how much</strong> — fresh, cooked, or powder, and roughly
            how many grams.</li>
          <li><strong>Call your veterinarian or an animal poison hotline immediately.</strong>
            Do not wait for symptoms; early treatment (induced vomiting, activated charcoal,
            IV fluids, and blood monitoring) works far better than waiting.</li>
          <li><strong>Bring the packaging</strong> if it was a packaged or powdered product so
            the clinic can assess concentration.</li>
          <li><strong>Do not induce vomiting at home</strong> unless a professional tells you to —
            it is unsafe in some situations.</li>
        </ol>

        <h2>Onion vs. garlic: the Allium family</h2>
        <p>Garlic is onion's close relative and causes the <a href="/dog-nutrition/can-dogs-eat-garlic/">
        same type of poisoning</a>, though its toxic threshold is higher. Both are unsafe,
        and "a little bit" is never a safe bet. See our pages on
        <a href="/dog-nutrition/can-dogs-eat-grapes/">grapes</a> and
        <a href="/dog-nutrition/can-dogs-eat-chocolate/">chocolate</a> for other common
        kitchen dangers.</p>
        """,
        "faq": [
            ("Can dogs eat cooked onion?", "No. Cooking does not destroy the organosulfides; cooked, fried, or caramelized onion is just as toxic as raw."),
            ("Is onion powder dangerous too?", "Yes — and it is the most common culprit. Powder is concentrated and hides in seasonings, gravy, and sauces; a small amount can equal a large amount of fresh onion."),
            ("My dog ate a tiny bit of onion. Will it be okay?", "Maybe, but don't gamble. Small dogs and powdered forms are highest risk. Call your vet with the estimated amount and follow their advice."),
            ("How long until symptoms appear?", "Typically 2–4 days, sometimes within 24 hours. The delay is why prompt veterinary contact matters even when your dog seems fine."),
            ("Can onion kill a dog?", "Yes — severe hemolytic anemia can be fatal without treatment. The risk is highest in small dogs and with concentrated powdered forms."),
            ("Are onion-flavored chips or snacks safe?", "No. They contain onion powder or extract plus salt and fat, making them doubly unsuitable."),
            ("What about leeks, chives, and shallots?", "All Allium family members are toxic to dogs and should be avoided entirely."),
            ("Can I give my dog bone broth with onion?", "No. Many broths and bouillon cubes contain onion. Use only plain, onion-free broth, or check the label carefully."),
        ],
        "related": ["can-dogs-eat-garlic", "can-dogs-eat-grapes", "can-dogs-eat-chocolate", "foods-toxic-to-dogs"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has eaten onion, contact your veterinarian or a pet poison hotline right away.",
    },
    {
        "slug": "can-dogs-eat-garlic",
        "url": "/dog-nutrition/can-dogs-eat-garlic/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Garlic? No — It's Still Allium Toxicity",
        "description": "Garlic, like onion, destroys a dog's red blood cells — the safe dose is effectively zero, especially for small breeds. Skip the folk remedies and flea myths.",
        "lede": "No — garlic is in the same Allium family as onion and causes the same red-blood-cell damage. The 'garlic for fleas' folk remedy is unsafe and unsupported, and even powdered garlic in spice rubs can harm a small dog.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>no</strong>. Garlic sits in the same <em>Allium</em> family as
        onion, leeks, and chives, and it causes the <strong>same red-blood-cell damage</strong>
        (hemolytic anemia). A popular myth claims garlic is a safe natural flea remedy or a
        healthy dog supplement — <strong>neither is supported by veterinary evidence</strong>, and
        feeding it is a real poisoning risk.</p>

        <h2>Why garlic is dangerous for dogs</h2>
        <p>Like onion, garlic contains organosulfides that rupture red blood cells after they
        are absorbed. The result is hemolytic anemia: the body can no longer carry enough
        oxygen, and in serious cases the damage is life-threatening.</p>
        <p>Garlic's toxic threshold is <strong>higher than onion's</strong> — roughly 5 times less
        potent gram-for-gram — but that does <em>not</em> make it safe. Powdered garlic is
        concentrated, and a small dog can cross the danger line with a fraction of a clove or a
        pinch of garlic powder.</p>

        <h2>Garlic powder is the hidden hazard</h2>
        <ul>
          <li><strong>Garlic powder and granules</strong> — common in spice rubs, bread,
            dressing mixes, and pet "treats" marketed with garlic.</li>
          <li><strong>Garlic bread, knots, and naan</strong> — butter, salt, and garlic together.</li>
          <li><strong>Chinese, Korean, and Thai dishes</strong> — garlic is a base aromatic in
            many takeout meals dogs are tempted by.</li>
          <li><strong>Homemade "flea" pastes</strong> — a folk remedy with no proven benefit and
            real toxicity.</li>
        </ul>

        <h2>How much garlic is too much?</h2>
        <p>Because garlic is about one-fifth as concentrated as onion, the commonly cited
        dangerous range is around <strong>5 times higher by weight</strong> — but for practical
        safety, the answer is the same as onion: <strong>don't feed it</strong>.</p>
        <table class="dose">
          <thead><tr><th>Dog weight</th><th>Rough toxic amount (fresh clove)</th><th>Safe amount</th></tr></thead>
          <tbody>
            <tr><td>5 kg (11 lb)</td><td>a few grams (part of one clove)</td><td><strong>0 — none</strong></td></tr>
            <tr><td>10 kg (22 lb)</td><td>~5–10 g</td><td><strong>0 — none</strong></td></tr>
            <tr><td>20 kg (44 lb)</td><td>~10–20 g</td><td><strong>0 — none</strong></td></tr>
            <tr><td>30 kg (66 lb)</td><td>~15–30 g</td><td><strong>0 — none</strong></td></tr>
          </tbody>
        </table>
        <p class="note">Small breeds reach toxicity fastest. With powdered garlic, the margin
        for error is tiny — treat the safe amount as <strong>zero</strong>.</p>

        <h2>Signs of garlic poisoning</h2>
        <ul>
          <li>Lethargy and weakness</li>
          <li>Pale or yellowish gums</li>
          <li>Rapid breathing, elevated heart rate</li>
          <li>Red or brown urine</li>
          <li>Vomiting, diarrhea, drooling</li>
          <li>Loss of coordination in severe cases</li>
        </ul>
        <p>Symptoms typically develop over <strong>2–4 days</strong>, so contact a vet promptly
        even if your dog looks normal right after eating it.</p>

        <h2>What to do if your dog ate garlic</h2>
        <ol>
          <li><strong>Estimate the amount and form</strong> (fresh clove, powder, or cooked in
            food) and note the time.</li>
          <li><strong>Call your veterinarian or an animal poison hotline</strong> right away.
            Early decontamination and supportive care prevent the worst damage.</li>
          <li><strong>Bring the food label</strong> if garlic came from a packaged product.</li>
          <li><strong>Do not induce vomiting at home</strong> unless directed by a professional.</li>
        </ol>

        <h2>Garlic vs. onion</h2>
        <p>Both are Allium-family toxins with the same mechanism. Onion is the more potent of
        the two, but garlic is more frequently fed by well-meaning owners who believe the
        flea-remedy myth. For the broader picture, see our
        <a href="/dog-nutrition/can-dogs-eat-onion/">onion</a> page, plus other kitchen dangers
        like <a href="/dog-nutrition/can-dogs-eat-grapes/">grapes</a> and
        <a href="/dog-nutrition/can-dogs-eat-chocolate/">chocolate</a>.</p>
        """,
        "faq": [
            ("Is a little garlic good for dogs?", "No. Despite persistent folklore, there is no safe or beneficial dose supported by veterinary science, and the anemia risk is well documented."),
            ("Can garlic kill fleas on dogs?", "Not reliably — and feeding garlic to achieve it poisons the dog instead. Use veterinarian-approved flea prevention."),
            ("My dog ate garlic bread. Is that dangerous?", "Yes — garlic plus butter and salt. Contact your vet with the amount; small dogs are most at risk."),
            ("How much garlic powder is toxic?", "Powder is concentrated; even a small pinch can matter for a toy or small breed. Assume any intentional garlic feeding is unsafe."),
            ("How long until symptoms show?", "Usually 2–4 days. The delay is exactly why early veterinary advice matters."),
            ("Is cooked or roasted garlic safer?", "No. Cooking does not remove the organosulfides."),
            ("What about garlic oil or supplements?", "Avoid them. Oils and concentrates can deliver a large dose in a small volume."),
            ("Can cats eat garlic?", "Cats are even more sensitive to Allium toxins than dogs. Keep all forms away from them."),
        ],
        "related": ["can-dogs-eat-onion", "can-dogs-eat-grapes", "can-dogs-eat-chocolate", "foods-toxic-to-dogs"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has eaten garlic, contact your veterinarian or a pet poison hotline right away.",
    },
    {
        "slug": "can-dogs-eat-macadamia-nuts",
        "url": "/dog-nutrition/can-dogs-eat-macadamia-nuts/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Macadamia Nuts? No — They Are Toxic",
        "description": "Macadamia nuts are toxic to dogs, causing weakness, tremors, vomiting, and fever within 12 hours. Even a small amount is dangerous. Learn the signs and what to do.",
        "lede": "No — macadamia nuts are one of the most toxic nuts for dogs. Within 12 hours of eating even a small number, dogs can develop back-leg weakness, tremors, vomiting, and fever. There is no safe amount.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>no</strong>. Macadamia nuts are among the most toxic nuts
        for dogs, and unlike many kitchen hazards, the danger is not limited to a particular
        part of the nut — the whole kernel is poisonous. The exact toxin has never been
        identified, but the clinical picture is well documented: dogs who eat macadamias
        develop a distinctive combination of weakness, tremors, and fever.</p>

        <h2>What macadamia nuts do to dogs</h2>
        <p>Symptoms usually start <strong>within 3–12 hours</strong> of eating the nuts and
        typically include:</p>
        <ul>
          <li><strong>Hind-leg weakness</strong> — the classic sign; dogs wobble, stumble, or
            struggle to stand</li>
          <li>Muscle tremors and shaking</li>
          <li>Vomiting and abdominal pain</li>
          <li>Elevated body temperature (fever)</li>
          <li>Stiffness, lameness, or reluctance to move</li>
          <li>In severe cases: inability to walk, collapse</li>
        </ul>
        <p>Most dogs recover within 24–48 hours with supportive veterinary care, but severe
        cases — especially large ingestions or nut-and-chocolate combinations — can be
        life-threatening without treatment.</p>

        <h2>How many macadamia nuts are dangerous?</h2>
        <p>Very few. Toxicity has been reported at doses as low as roughly
        <strong>1 gram of nut per kg of body weight</strong> — for a 10 kg dog that is only
        a couple of kernels. Chocolate-covered macadamias are doubly dangerous because
        chocolate brings its own, separate <a href="/dog-nutrition/can-dogs-eat-chocolate/">
        toxicity</a>.</p>
        <table class="dose">
          <thead><tr><th>Dog weight</th><th>Rough concerning amount</th><th>Safe amount</th></tr></thead>
          <tbody>
            <tr><td>5 kg (11 lb)</td><td>as few as 1 kernel</td><td><strong>0 — none</strong></td></tr>
            <tr><td>10 kg (22 lb)</td><td>~1–2 kernels</td><td><strong>0 — none</strong></td></tr>
            <tr><td>20 kg (44 lb)</td><td>~2–4 kernels</td><td><strong>0 — none</strong></td></tr>
            <tr><td>30 kg (66 lb)</td><td>~4–6 kernels</td><td><strong>0 — none</strong></td></tr>
          </tbody>
        </table>
        <p class="note">Because one dropped cookie or a stolen handful can cross the line,
        treat the safe amount as <strong>zero</strong> for dogs of every size.</p>

        <h2>Hidden sources to watch for</h2>
        <ul>
          <li><strong>Cookies, biscotti, and white-chocolate macadamia treats</strong> — a
            common bakery item dogs steal off counters</li>
          <li><strong>Trail mix and nut mixes</strong> — macadamias often travel with raisins
            and chocolate, both also toxic</li>
          <li><strong>Macadamia nut butter and oils</strong> — concentrated and easy to
            over-serve</li>
          <li><strong>Guest snacking and holiday baking</strong> — most exposures happen when
            visitors drop food</li>
        </ul>

        <h2>What to do if your dog ate macadamia nuts</h2>
        <ol>
          <li><strong>Estimate the amount</strong> — how many kernels, and whether they were
            chocolate-covered or mixed with raisins.</li>
          <li><strong>Call your veterinarian or a pet poison hotline immediately</strong>,
            even if your dog seems fine — symptoms can take hours to appear and early
            decontamination works best.</li>
          <li><strong>Keep the packaging</strong> so the clinic can confirm the product.</li>
          <li><strong>Do not induce vomiting at home</strong> unless a professional directs
            you to.</li>
        </ol>

        <h2>Are other nuts safe?</h2>
        <p>Macadamias are uniquely toxic, but most nuts are still poor choices for dogs:
        they are high in fat (pancreatitis risk), often salted, and can cause choking.
        Moldy walnuts and pecans carry additional toxins. Safer crunchy treats are plain
        <a href="/dog-nutrition/can-dogs-eat-carrots/">carrots</a> or
        <a href="/dog-nutrition/can-dogs-eat-green-beans/">green beans</a>.</p>
        """,
        "faq": [
            ("Can dogs eat macadamia nuts in any amount?", "No. Toxicity has been reported at doses as low as about 1 g per kg of body weight — a couple of kernels can sicken a small dog. Treat the safe amount as zero."),
            ("How quickly do symptoms appear?", "Usually within 3–12 hours. Hind-leg weakness and tremors are the classic signs, often with vomiting and fever."),
            ("Are macadamia cookies dangerous too?", "Yes — and white-chocolate macadamia cookies add chocolate and sugar on top. Contact your vet with how much was eaten."),
            ("Can a dog recover from macadamia poisoning?", "Most dogs recover within 24–48 hours with supportive care, but severe cases need hospitalization — so do not wait it out at home."),
            ("What makes macadamias toxic to dogs?", "The exact toxin is still unidentified, but the weakness-tremor-fever syndrome it causes is well documented by veterinary toxicologists."),
            ("Are other nuts safe for dogs?", "Macadamias are uniquely toxic, but most nuts are high-fat, often salted, and a choking risk. Moldy walnuts and pecans add further toxins. Use carrots or green beans instead."),
            ("My dog ate one macadamia nut — should I worry?", "Yes, call your vet. One kernel can matter for a small dog, and professional advice is free compared with late treatment."),
            ("Is macadamia nut butter or oil safe?", "No. It is the same nut in concentrated form, and easy to over-serve. Keep all macadamia products away from dogs."),
        ],
        "related": ["can-dogs-eat-chocolate", "can-dogs-eat-grapes", "foods-toxic-to-dogs", "can-dogs-eat-carrots"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has eaten macadamia nuts, contact your veterinarian or a pet poison hotline right away.",
    },
    {
        "slug": "can-dogs-eat-cherries",
        "url": "/dog-nutrition/can-dogs-eat-cherries/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Cherries? Flesh Yes — Pits Never",
        "description": "Cherry flesh is not toxic to dogs, but the pits, stems, and leaves contain cyanide compounds and pose choking risks. Here is how the risk actually works.",
        "lede": "Cherry flesh itself is not toxic, but the pits, stems, and leaves contain cyanide compounds — and pits can also choke a dog or block the intestine. The practical answer: no cherries with pits, ever.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>the flesh, maybe — the rest, never.</strong> Cherry fruit
        itself is not poisonous to dogs, but every other part of the fruit — the
        <strong>pit, stem, and leaves</strong> — contains cyanogenic compounds that release
        cyanide when chewed and broken down. Pits also create a serious physical hazard:
        they are the right size to lodge in a dog's throat or intestine.</p>

        <h2>The cyanide issue, explained simply</h2>
        <p>Cherry pits and leaves contain <strong>cyanogenic glycosides</strong> — natural
        plant chemicals that convert to cyanide when the plant tissue is crushed or chewed.
        A single pit is unlikely to poison a large dog because the pit usually passes
        intact, but the risk is real when pits are chewed, when a small dog eats several,
        or when a dog gets into stems and leaves.</p>
        <p>Signs of cyanide poisoning are rapid and severe: bright-red gums, dilated pupils,
        difficulty breathing, and collapse. This is an <strong>emergency</strong> — go to a
        vet immediately.</p>

        <h2>The pit is also a physical hazard</h2>
        <div class="callout warn">Even without toxicity, a swallowed cherry pit can obstruct
        a dog's intestine — the same life-threatening blockage caused by a corn cob. Small
        dogs are at the highest risk, and a blocked gut often needs surgery.</div>

        <h2>What about processed cherries?</h2>
        <ul>
          <li><strong>Fresh cherries with pits</strong> — the biggest hazard; never hand a
            dog a whole cherry.</li>
          <li><strong>Pitted fresh cherry flesh</strong> — the only technically safe form,
            and even then, only in small amounts because of the sugar.</li>
          <li><strong>Maraschino and glacé cherries</strong> — sugar-loaded and sometimes
            alcohol-tinged; skip them.</li>
          <li><strong>Cherry pie filling and cherry yogurt</strong> — sugar plus flavorings;
            some products may contain xylitol, so check labels carefully.</li>
          <li><strong>Cherries in trail mix</strong> — usually dried, sweetened, and mixed
            with raisins or nuts, both worse hazards.</li>
        </ul>

        <h2>How much cherry flesh is okay?</h2>
        <p>If you do share pitted cherry flesh, keep it to a couple of cherries for a medium
        dog — fruit sugar adds up. Safer fruit treats with more reward and less hassle
        include <a href="/dog-nutrition/can-dogs-eat-blueberries/">blueberries</a>,
        <a href="/dog-nutrition/can-dogs-eat-strawberries/">strawberries</a>, and
        <a href="/dog-nutrition/can-dogs-eat-watermelon/">watermelon</a> (seedless).</p>
        <table class="dose">
          <thead><tr><th>Dog weight</th><th>Occasional pitted-flesh amount</th></tr></thead>
          <tbody>
            <tr><td>Under 5 kg (toy / small)</td><td>½ cherry, pitted</td></tr>
            <tr><td>5–10 kg (11–22 lb)</td><td>1 cherry, pitted</td></tr>
            <tr><td>10–25 kg (22–55 lb)</td><td>2–3 cherries, pitted</td></tr>
            <tr><td>Over 25 kg (55 lb)</td><td>3–4 cherries, pitted</td></tr>
          </tbody>
        </table>
        <p class="note">In practice, most vets suggest skipping cherries entirely — other
        fruits give the same joy with none of the pit risk.</p>

        <h2>What to do if your dog ate cherries</h2>
        <ol>
          <li><strong>Figure out what was eaten</strong> — flesh only, or pits, stems, or
            leaves too, and roughly how many.</li>
          <li><strong>Pits swallowed whole</strong>: call your vet to discuss monitoring for
            obstruction and whether decontamination makes sense.</li>
          <li><strong>Pits chewed, or leaves/stems eaten</strong>: treat as an emergency —
            cyanide signs move fast.</li>
          <li><strong>Watch for 24–48 hours</strong>: vomiting, loss of appetite, constipation,
            or straining can signal an intestinal blockage and need same-day care.</li>
        </ol>
        """,
        "faq": [
            ("Can dogs eat cherries without the pit?", "The flesh itself is not toxic, so a pitted cherry in small amounts is technically safe — but the sugar adds up and other fruits are better choices."),
            ("What happens if a dog eats a cherry pit?", "A whole pit usually passes, but it can obstruct the intestine — especially in small dogs. Chewed pits can release cyanide. Call your vet with how many and whether they were chewed."),
            ("Are cherry stems and leaves dangerous?", "Yes. They contain the same cyanogenic compounds as pits. Treat ingestion as urgent, especially if a dog chewed them."),
            ("Can dogs eat maraschino cherries?", "No. They are sugar-loaded, sometimes alcohol-tinged, and add nothing nutritionally. Skip them."),
            ("Is cherry pie filling safe for dogs?", "No. It is heavy in sugar and flavorings, and some cherry products may contain xylitol, which is highly toxic. Check labels and keep all pie filling away."),
            ("How many cherries are toxic?", "Toxicity depends on whether pits are chewed and the dog's size. There is no established safe pit count — prevention is keeping cherries out of reach."),
            ("What are the signs of cyanide poisoning in dogs?", "Bright-red gums, dilated pupils, rapid or labored breathing, and collapse. This is an immediate veterinary emergency."),
            ("My dog ate one cherry off the floor — what now?", "Most likely fine, but watch for vomiting or behavior change over 24–48 hours and call your vet if anything seems off, especially for a small dog."),
        ],
        "related": ["can-dogs-eat-grapes", "can-dogs-eat-blueberries", "can-dogs-eat-strawberries", "foods-toxic-to-dogs"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has eaten cherry pits, stems, or leaves, or shows breathing changes, contact your veterinarian immediately.",
    },
    {
        "slug": "can-dogs-eat-peaches",
        "url": "/dog-nutrition/can-dogs-eat-peaches/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Peaches? Flesh Yes — Pit Is a Hazard",
        "description": "Fresh peach flesh is fine for dogs in small amounts, but the pit holds cyanide compounds and can block the gut. Skip the canned syrup. Portion guide inside.",
        "lede": "Fresh peach flesh is safe for dogs in small amounts, but the pit is a double hazard: it contains cyanide compounds and can choke a dog or block the intestine. Canned peaches in syrup are out entirely.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>the flesh, yes in moderation — the pit, never.</strong>
        Peaches are stone fruits like <a href="/dog-nutrition/can-dogs-eat-cherries/">cherries</a>
        and <a href="/dog-nutrition/can-dogs-eat-plums/">plums</a>: the juicy flesh is
        harmless, but the hard pit in the middle carries the same two risks — cyanogenic
        compounds and a shape that can physically block a dog's digestive tract.</p>

        <h2>What's actually in a peach that helps or harms</h2>
        <p>Fresh peach flesh is mostly water and natural sugar with some fiber and vitamins
        A and C. In small amounts it is a perfectly fine treat. The problems are everything
        around the flesh:</p>
        <ul>
          <li><strong>The pit (stone)</strong> — contains cyanogenic glycosides, the same
            compounds as cherry and plum pits, and its rough, large shape is ideal for
            lodging in a throat or intestine.</li>
          <li><strong>The skin</strong> — not toxic, but it is where pesticide residue sits;
            wash well or peel if you share.</li>
          <li><strong>The sugar</strong> — one peach carries a lot of fruit sugar for a
            small dog; portion by weight, below.</li>
        </ul>

        <h2>Canned peaches are a firm no</h2>
        <div class="callout warn">Canned peaches sit in heavy syrup: concentrated sugar that
        upsets the stomach and adds empty calories, plus preservatives. Frozen-thawed fresh
        peach (pitted) is the only acceptable alternative when fresh is out of season.</div>

        <h2>How much peach is safe?</h2>
        <p>Keep treats under 10% of daily calories. A practical portion guide:</p>
        <table class="dose">
          <thead><tr><th>Dog weight</th><th>Safe occasional amount (pitted flesh)</th></tr></thead>
          <tbody>
            <tr><td>Under 5 kg (toy / small)</td><td>1–2 small slices</td></tr>
            <tr><td>5–10 kg (11–22 lb)</td><td>2–3 slices</td></tr>
            <tr><td>10–25 kg (22–55 lb)</td><td>up to ¼ peach</td></tr>
            <tr><td>Over 25 kg (55 lb)</td><td>up to ½ peach</td></tr>
          </tbody>
        </table>
        <p class="note">Always remove the pit first, and cut the flesh into bite-size
        pieces so nothing gets gulped down whole.</p>

        <h2>What to do if your dog ate a peach pit</h2>
        <ol>
          <li><strong>Don't panic — assess.</strong> Was the pit swallowed whole or chewed?
            How big is your dog?</li>
          <li><strong>Pit swallowed whole</strong>: call your vet for guidance; watch for
            24–48 hours for vomiting, appetite loss, constipation, or straining — signs of
            obstruction that need same-day care.</li>
          <li><strong>Pit chewed</strong>: contact a vet promptly — cyanide release is the
            concern, and signs (bright-red gums, labored breathing, dilated pupils) move
            fast.</li>
          <li><strong>Do not induce vomiting</strong> at home unless a professional tells
            you to.</li>
        </ol>

        <h2>Frequently asked questions</h2>
        """,
        "faq": [
            ("Can dogs eat peach flesh?", "Yes — fresh, pitted flesh in small amounts is safe for most dogs. Portion by weight and cut into pieces."),
            ("Is the peach pit dangerous?", "Yes, twice over: it contains cyanogenic compounds like cherry and plum pits, and its size makes it a choking and intestinal-obstruction hazard."),
            ("Can dogs eat canned peaches?", "No. The syrup is concentrated sugar with preservatives — a stomach upset and obesity risk. Offer fresh (or frozen-thawed) pitted flesh only."),
            ("Are peaches with skin okay?", "The skin is not toxic, but it holds pesticide residue. Wash thoroughly, or peel it if you want to be extra careful."),
            ("What if my dog swallowed a whole peach pit?", "Call your vet with your dog's size and when it happened, then watch for 24–48 hours for obstruction signs such as vomiting or straining. Small dogs are at the highest risk."),
            ("Can puppies eat peach flesh?", "A tiny piece is fine, but puppies have sensitive stomachs and less predictable swallowing — cut very small or skip fruit and use their regular treats."),
            ("Are dried peaches safe?", "Technically the flesh is not toxic, but dried fruit is sugar-dense and easy to over-serve. Fresh flesh is the better form."),
            ("Is peach yogurt or ice cream okay?", "No. Dairy plus added sugar, and some products contain xylitol, which is highly toxic to dogs. Keep flavored human desserts away."),
        ],
        "related": ["can-dogs-eat-cherries", "can-dogs-eat-plums", "can-dogs-eat-apples", "foods-toxic-to-dogs"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has swallowed a peach pit or shows breathing changes, contact your veterinarian right away.",
    },
    {
        "slug": "can-dogs-eat-plums",
        "url": "/dog-nutrition/can-dogs-eat-plums/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Plums? Flesh Yes — Pit Is a Hazard",
        "description": "Plum flesh is not toxic, but the pit contains cyanide compounds and can obstruct the intestine. Prunes are a concentrated sugar trap. Portion guide inside.",
        "lede": "Plum flesh is not toxic, but the pit carries the same cyanide and obstruction risks as peach and cherry pits — and plums are small enough that a dog often swallows the fruit whole. Prunes are a sugar trap.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>pitted flesh, occasionally — never the pit.</strong> Plums
        are stone fruits, in the same family of risk as
        <a href="/dog-nutrition/can-dogs-eat-peaches/">peaches</a> and
        <a href="/dog-nutrition/can-dogs-eat-cherries/">cherries</a>: sweet, safe flesh
        wrapped around a hard pit that contains cyanogenic compounds and is small enough to
        be swallowed whole — which makes it, in some ways, more dangerous than a peach pit
        for small dogs.</p>

        <h2>Why plums trip up dog owners</h2>
        <p>Plums are the perfect size for a dog to gulp in one bite — pit and all. That is
        exactly the wrong way for a dog to eat one. The two failure modes:</p>
        <ul>
          <li><strong>Obstruction</strong> — a swallowed pit can lodge in the throat or
            intestine. Small dogs are at the highest risk, and a blocked gut often needs
            surgery.</li>
          <li><strong>Cyanide compounds</strong> — if the pit is chewed, the cyanogenic
            glycosides inside release cyanide. Signs come on fast: bright-red gums, dilated
            pupils, difficulty breathing, collapse. That is an emergency.</li>
        </ul>
        <p>Fallen fruit under a plum tree is the classic exposure — sweep it up if you have
        a tree in the yard.</p>

        <h2>Prunes and dried plums: a sugar trap</h2>
        <div class="callout warn">Prunes are plum flesh with the water removed — which
        concentrates the sugar. A couple of prunes can be a serious calorie load for a small
        dog, and dried fruit in general upsets stomachs. They also sometimes appear in baked
        goods alongside raisins, which are outright toxic. Skip prunes; use fresh pitted
        flesh if you share plums at all.</div>

        <h2>How much plum is okay?</h2>
        <p>If you share, remove the pit, cut the flesh up, and keep it small:</p>
        <table class="dose">
          <thead><tr><th>Dog weight</th><th>Safe occasional amount (pitted flesh)</th></tr></thead>
          <tbody>
            <tr><td>Under 5 kg (toy / small)</td><td>1 small slice</td></tr>
            <tr><td>5–10 kg (11–22 lb)</td><td>1–2 slices</td></tr>
            <tr><td>10–25 kg (22–55 lb)</td><td>up to ½ plum, pitted</td></tr>
            <tr><td>Over 25 kg (55 lb)</td><td>up to 1 plum, pitted and cut</td></tr>
          </tbody>
        </table>
        <p class="note">Honestly, most dogs don't need plums —
        <a href="/dog-nutrition/can-dogs-eat-blueberries/">blueberries</a> or
        <a href="/dog-nutrition/can-dogs-eat-watermelon/">watermelon</a> are easier and
        safer fruit treats.</p>

        <h2>What to do if your dog ate a plum pit</h2>
        <ol>
          <li><strong>Establish the facts</strong> — how many pits, swallowed whole or
            chewed, and your dog's size.</li>
          <li><strong>Whole pit swallowed</strong>: call your vet; then monitor for 24–48
            hours for vomiting, appetite loss, constipation, or straining.</li>
          <li><strong>Pit chewed or several eaten</strong>: treat as urgent — cyanide signs
            escalate quickly.</li>
          <li><strong>Keep the scene safe</strong>: clear any fallen fruit so it doesn't
            happen twice.</li>
        </ol>

        <h2>Frequently asked questions</h2>
        """,
        "faq": [
            ("Can dogs eat plum flesh?", "Yes — pitted, cut into pieces, in small amounts. The flesh itself is not toxic."),
            ("Is the plum pit toxic to dogs?", "Yes. Like peach and cherry pits, it contains cyanogenic compounds, and its size makes it a serious choking and obstruction hazard for small dogs."),
            ("Can dogs eat prunes (dried plums)?", "It's best not to. Prunes are sugar-concentrated, easy to over-serve, and commonly cause stomach upset. Fresh pitted flesh is the better form."),
            ("My dog ate a whole plum off the ground — what should I do?", "Call your vet with your dog's size and timing, then watch for 24–48 hours for obstruction signs. If the pit was chewed, treat it as urgent."),
            ("What are the signs of cyanide poisoning from fruit pits?", "Bright-red gums, dilated pupils, rapid or labored breathing, and collapse. Go to a vet immediately — this is an emergency."),
            ("Is plum skin safe for dogs?", "The skin is not toxic, but like peaches it holds pesticide residue. Wash thoroughly before sharing."),
            ("Can dogs eat plum jam or yogurt?", "No. Added sugar, and jams often contain other fruits or sweeteners — check for xylitol, which is highly toxic. Keep all sweetened products away."),
            ("How do I stop my dog eating fallen plums in the yard?", "Pick up fallen fruit daily during the season, fence off the tree if needed, and train a solid 'leave it' — prevention beats emergency vet visits."),
        ],
        "related": ["can-dogs-eat-peaches", "can-dogs-eat-cherries", "can-dogs-eat-grapes", "foods-toxic-to-dogs"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has swallowed a plum pit or shows breathing changes, contact your veterinarian right away.",
    },
    {
        "slug": "can-dogs-eat-xylitol",
        "url": "/dog-nutrition/can-dogs-eat-xylitol/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Xylitol? No — It Can Be Deadly Fast",
        "description": "Xylitol, found in sugar-free gum and some peanut butters, triggers a fatal insulin surge in dogs. Check every label — and what to do if your dog ate it.",
        "lede": "No — xylitol (birch sugar) is one of the deadliest common ingredients for dogs. A tiny amount triggers a rapid insulin surge, crash blood sugar, and possible liver failure within hours. Check every label.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>absolutely not.</strong> Xylitol — also labeled "birch
        sugar" or "birch sap" — is an artificial sweetener that is harmless to humans but
        one of the most dangerous substances a dog can swallow. It does not take much: a
        few pieces of sugar-free gum can put a small dog in crisis within an hour.</p>

        <h2>Why xylitol is so dangerous</h2>
        <p>In humans, xylitol is absorbed slowly and barely affects insulin. In dogs, the
        body mistakes it for real sugar and releases a <strong>massive insulin surge</strong>.
        The result happens in two stages:</p>
        <ul>
          <li><strong>Stage 1 — hypoglycemia (low blood sugar)</strong>, within 30–60
            minutes: vomiting, weakness, wobbling, collapse, tremors, seizures. This stage
            can be fatal on its own.</li>
          <li><strong>Stage 2 — liver failure</strong>, which can develop 12–72 hours after
            larger doses, and can be fatal even with intensive care.</li>
        </ul>
        <p>A concerning dose can be around <strong>50 mg of xylitol per kg of body
        weight</strong> for blood-sugar crash, and roughly 10 times that for liver injury.
        One piece of many sugar-free gums contains 300–1,000 mg — so <strong>one or two
        pieces can seriously harm a small dog</strong>.</p>
        <table class="dose">
          <thead><tr><th>Dog weight</th><th>Rough concerning amount</th><th>Safe amount</th></tr></thead>
          <tbody>
            <tr><td>5 kg (11 lb)</td><td>~250 mg (part of one gum piece)</td><td><strong>0 — none</strong></td></tr>
            <tr><td>10 kg (22 lb)</td><td>~500 mg (about one gum piece)</td><td><strong>0 — none</strong></td></tr>
            <tr><td>20 kg (44 lb)</td><td>~1,000 mg (1–2 gum pieces)</td><td><strong>0 — none</strong></td></tr>
            <tr><td>30 kg (66 lb)</td><td>~1,500 mg (2–3 gum pieces)</td><td><strong>0 — none</strong></td></tr>
          </tbody>
        </table>

        <h2>Where xylitol hides — check these labels</h2>
        <div class="callout warn">Xylitol appears in more products every year. Scan
        ingredient lists on: sugar-free gum and mints, candy, breath strips, sugar-free
        peanut and other nut butters, sugar-free desserts and protein bars, chewable and
        gummy vitamins, mouthwash and toothpaste, some liquid medications, and products
        labeled "birch sugar."</div>
        <p><strong>Peanut butter deserves special attention</strong>: some brands add
        xylitol. Always check before sharing — plain, xylitol-free peanut butter is the
        only kind dogs may have, in small amounts.</p>

        <h2>What to do if your dog ate xylitol</h2>
        <ol>
          <li><strong>Treat it as an emergency</strong> — this is not a wait-and-see
            situation. Contact a veterinarian or pet poison hotline immediately, day or
            night.</li>
          <li><strong>Bring the product label</strong> — the exact product (gum, butter,
            candy) and the xylitol grams per serving let the vet calculate the risk.</li>
          <li><strong>Do not wait for symptoms</strong> — treatment before the blood sugar
            crashes is dramatically more effective.</li>
          <li><strong>Do not induce vomiting</strong> at home unless a professional
            directs you to; a collapsing dog should go straight to the clinic.</li>
          <li><strong>Watch for 72 hours</strong> if the vet advises home monitoring:
            lethargy, vomiting, or yellow gums in the following days can signal liver
            injury.</li>
        </ol>

        <h2>Frequently asked questions</h2>
        """,
        "faq": [
            ("What is xylitol and why is it deadly for dogs?", "It is a sugar alcohol sweetener, sometimes labeled birch sugar. In dogs it triggers a massive insulin release, crashing blood sugar within 30–60 minutes, and larger doses can cause fatal liver failure."),
            ("How much xylitol is toxic to dogs?", "Blood-sugar crash can occur around 50 mg per kg of body weight; liver injury at roughly ten times that. One or two pieces of sugar-free gum can seriously harm a small dog."),
            ("Is xylitol in peanut butter?", "Some brands add it — always check the ingredient list before sharing peanut butter. Look for xylitol, birch sugar, or birch sap on the label."),
            ("What are the first signs of xylitol poisoning?", "Vomiting, sudden weakness, wobbling, collapse, tremors, and seizures — usually within an hour of eating it. Liver injury can follow days later."),
            ("My dog ate sugar-free gum — what should I do?", "Treat it as an emergency. Call a vet or pet poison hotline immediately with the brand and how many pieces — do not wait for symptoms."),
            ("Can dogs recover from xylitol poisoning?", "Yes, if treated early. Dogs treated before or during the blood-sugar crash often recover with glucose support; liver failure cases have a much worse outlook, which is why speed matters."),
            ("Is xylitol bad for cats too?", "Cats appear far less sensitive and rarely eat it, but keep all sweetened products away from every pet anyway."),
            ("Is erythritol or stevia safe for dogs?", "Erythritol and stevia are not known to cause xylitol-type poisoning, but sugar alcohols can cause diarrhea. The safest policy: no sweetened products for dogs at all."),
        ],
        "related": ["can-dogs-eat-peanut-butter", "foods-toxic-to-dogs", "can-dogs-eat-chocolate", "can-dogs-eat-yogurt"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. Xylitol ingestion is an emergency — contact your veterinarian or a pet poison hotline immediately.",
    },
    {
        "slug": "can-dogs-eat-alcohol",
        "url": "/dog-nutrition/can-dogs-eat-alcohol/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Drink Alcohol? No — Even Sips Are Risky",
        "description": "Alcohol hits dogs far harder than humans — even sips can crash blood sugar and body temperature. Hidden sources like raw dough and desserts count too.",
        "lede": "No — dogs cannot tolerate alcohol at all. Their small body size means even a sip of a strong drink can cause vomiting, disorientation, low blood sugar, and seizures. Rises dough and fermented foods count too.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>no — never.</strong> Dogs are far more sensitive to alcohol
        than people because of their small body size and faster absorption. There is no
        "just a sip" safe amount: what feels trivial to a human can measurably intoxicate
        a small dog, and severe cases progress to seizures and coma.</p>

        <h2>What alcohol does to a dog</h2>
        <p>Ethanol depresses the central nervous system. In dogs the effect arrives faster
        and hits harder than in humans:</p>
        <ul>
          <li>Vomiting and drooling</li>
          <li>Wobbling, disorientation, glassy eyes</li>
          <li><strong>Low blood sugar</strong> and <strong>low body temperature</strong> —
            two of the most dangerous effects and easy to miss</li>
          <li>Slow breathing, depressed heart rate</li>
          <li>Seizures, and in severe cases, coma or death</li>
        </ul>
        <p>Signs usually appear within <strong>30–60 minutes</strong>, but the full picture
        can take hours — a dog that "slept it off" can still be in trouble.</p>

        <h2>Alcohol hides in places owners don't expect</h2>
        <ul>
          <li><strong>Raw bread dough with yeast</strong> — the most overlooked source: the
            dough keeps rising inside the warm stomach, producing alcohol (and dangerous
            stomach expansion at the same time). See our
            <a href="/dog-nutrition/can-dogs-eat-bread/">bread</a> page for the details.</li>
          <li><strong>Rotten or fermenting fruit</strong> — fallen apples or windfall plums
            fermenting under trees can intoxicate a scavenging dog.</li>
          <li><strong>Desserts</strong> — rum cake, tiramisu, liqueur chocolates
            (chocolate adds its own <a href="/dog-nutrition/can-dogs-eat-chocolate/">
            toxicity</a>).</li>
          <li><strong>Mouthwash and some medications</strong> — many contain significant
            ethanol.</li>
          <li><strong>Spilled drinks at parties</strong> — the classic exposure: guests,
            dropped cups, unattended glasses.</li>
        </ul>

        <h2>How much is dangerous?</h2>
        <p>Because toxicity starts at doses far below what a human would notice, the safe
        amount is <strong>zero</strong>. Rough scale: serious signs can develop in a 10 kg
        dog from the ethanol in a fraction of a standard beer or a few sips of spirits —
        and mixed drinks, dessert alcohols, and raw dough concentrate it further.</p>
        <table class="dose">
          <thead><tr><th>Dog weight</th><th>Safe amount</th></tr></thead>
          <tbody>
            <tr><td>Any weight</td><td><strong>0 — no alcohol in any form, ever</strong></td></tr>
          </tbody>
        </table>

        <h2>What to do if your dog drank alcohol</h2>
        <ol>
          <li><strong>Call a veterinarian or pet poison hotline immediately</strong>, even
            for a small amount — early support (warmth, fluids, blood-sugar management)
            prevents the worst outcomes.</li>
          <li><strong>Keep the dog warm</strong> — alcohol drops body temperature.</li>
          <li><strong>Note what was drunk</strong> — the type of drink, how much, and when.</li>
          <li><strong>Do not induce vomiting</strong> at home unless directed; a wobbly or
            drowsy dog can aspirate.</li>
          <li><strong>Stay watchful overnight</strong> — effects can deepen for hours.</li>
        </ol>

        <h2>Frequently asked questions</h2>
        """,
        "faq": [
            ("Can a dog have a tiny sip of beer?", "No. Even small amounts can lower a dog's blood sugar and body temperature, and small dogs reach toxic levels with very little. There is no safe sip."),
            ("What happens if a dog licks spilled wine or beer?", "A single lick of a low-alcohol drink may cause little more than drool in a large dog, but call your vet for guidance, watch closely for an hour, and keep the dog warm."),
            ("Is raw bread dough really an alcohol risk?", "Yes — yeast ferments inside the warm stomach, producing ethanol while the dough expands. It is a double emergency: alcohol poisoning plus dangerous bloating."),
            ("Can dogs get drunk?", "They can be intoxicated, but it is far more dangerous than in humans — dogs develop hypoglycemia and hypothermia and can seize or slip into a coma."),
            ("My dog ate fermented fruit off the ground — what now?", "Call your vet, keep the dog warm, and watch for wobbling or vomiting. Larger amounts or small dogs need same-day care."),
            ("Is beer safe as a 'cool' summer treat for dogs?", "No. There are special non-alcoholic 'dog beers' on the market with no ethanol; real beer must stay out of reach."),
            ("How long does alcohol stay in a dog's system?", "Signs typically peak within the first hours but can last much longer depending on the dose. Overnight monitoring is standard advice."),
            ("Can dogs drink non-alcoholic beer?", "True non-alcoholic versions without ethanol and without xylitol or hops are generally low risk, but plain water is always the right drink for a dog."),
        ],
        "related": ["can-dogs-eat-bread", "can-dogs-eat-chocolate", "foods-toxic-to-dogs", "can-dogs-eat-cherries"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has consumed alcohol or raw yeast dough, contact your veterinarian or a pet poison hotline immediately.",
    },
    {
        "slug": "can-dogs-eat-caffeine",
        "url": "/dog-nutrition/can-dogs-eat-caffeine/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Have Caffeine? No — Coffee, Tea, Pills Are Toxic",
        "description": "Caffeine is toxic to dogs — coffee, tea, energy drinks, pills, even used grounds. Small dogs reach toxic levels fast. Signs, dose table, and next steps.",
        "lede": "No — caffeine in every form (coffee, tea, energy drinks, pills, grounds) is toxic to dogs. It speeds the heart and nervous system, and small dogs reach dangerous levels with just a lap or two of coffee.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>no — never, in any form.</strong> Caffeine is a stimulant
        that dogs metabolize far more slowly than humans, so it hits their heart and nervous
        system much harder. There is no safe sip of coffee, tea, energy drink, or soda — and
        some of the most dangerous exposures come from things dogs find on the floor:
        <strong>used coffee grounds, tea bags, and dropped pills</strong>.</p>

        <h2>What caffeine does to a dog</h2>
        <p>Caffeine overstimulates the heart and nervous system. Signs typically start
        within <strong>30–60 minutes</strong> and can last many hours:</p>
        <ul>
          <li>Restlessness, pacing, hyperactivity</li>
          <li>Rapid breathing and racing heart rate</li>
          <li>Muscle tremors and twitching</li>
          <li>Vomiting and diarrhea</li>
          <li>Elevated body temperature</li>
          <li>Seizures and collapse in severe cases</li>
        </ul>

        <h2>How much caffeine is dangerous?</h2>
        <p>Mild signs can start around <strong>20 mg of caffeine per kg of body weight</strong>,
        with serious toxicity near 40–60 mg/kg. To put that in scale:</p>
        <table class="dose">
          <thead><tr><th>Source</th><th>Rough caffeine content</th></tr></thead>
          <tbody>
            <tr><td>Brewed coffee (per 250 ml cup)</td><td>~100 mg</td></tr>
            <tr><td>Espresso shot</td><td>~60–80 mg</td></tr>
            <tr><td>Black tea (per cup)</td><td>~45 mg</td></tr>
            <tr><td>Energy drink (per can)</td><td>~80–160 mg</td></tr>
            <tr><td>Cola (per 330 ml can)</td><td>~30–35 mg</td></tr>
            <tr><td>Used coffee grounds (per tablespoon)</td><td>~25–50 mg</td></tr>
            <tr><td>Caffeine pill</td><td>100–200 mg</td></tr>
          </tbody>
        </table>
        <p class="note">A 5 kg (11 lb) dog can show mild signs from roughly 100 mg —
        <strong>a single cup of coffee or half an energy drink</strong>. That is why spilled
        mugs and trash-bin grounds are the most common real-world exposures.</p>

        <h2>Hidden caffeine sources to watch for</h2>
        <ul>
          <li>Coffee, espresso, tea, and energy drinks — including half-finished mugs</li>
          <li><strong>Used grounds and tea bags</strong> in the trash or compost</li>
          <li>Caffeine and pre-workout pills — potent single doses</li>
          <li>Cola and other caffeinated sodas</li>
          <li>Chocolate-caffeine combinations — mocha desserts and coffee chocolate bars
            stack both toxicities (see our
            <a href="/dog-nutrition/can-dogs-eat-chocolate/">chocolate</a> page)</li>
        </ul>

        <h2>What to do if your dog had caffeine</h2>
        <ol>
          <li><strong>Call your veterinarian or a pet poison hotline immediately</strong> —
            even if the amount seems small and your dog seems fine.</li>
          <li><strong>Identify the source and amount</strong> — coffee vs. grounds vs.
            pills matters a lot for dosing.</li>
          <li><strong>Note the time</strong> — early decontamination (within the first
            hour) is the most effective.</li>
          <li><strong>Do not induce vomiting</strong> at home unless a professional tells
            you to.</li>
          <li><strong>Expect monitoring</strong> — because caffeine acts over many hours,
            serious cases are watched at the clinic for tremors and heart rhythm.</li>
        </ol>

        <h2>Frequently asked questions</h2>
        """,
        "faq": [
            ("Can dogs drink a little bit of coffee?", "No. Even one cup can cause tremors and a racing heart in a small dog, and caffeine acts for many hours. There is no safe sip."),
            ("Is decaf coffee safe for dogs?", "It is much lower in caffeine but not zero, and coffee compounds can still upset the stomach. Decaf is not a treat — stick to water."),
            ("Can dogs drink tea?", "No. Black and green tea contain real caffeine, and herbal teas can contain plants that are also unsafe. Skip all tea."),
            ("What about energy drinks or cola?", "Both contain caffeine plus large amounts of sugar — energy drinks can hold 80–160 mg per can, more than a cup of coffee. Never give either."),
            ("My dog ate used coffee grounds from the trash — is that bad?", "Yes — grounds are concentrated caffeine and a common emergency. Call your vet or a poison hotline right away with how much and when."),
            ("How much caffeine is toxic to dogs?", "Mild signs can start around 20 mg per kg of body weight; serious toxicity near 40–60 mg/kg. For a 5 kg dog, roughly one cup of coffee."),
            ("What are the signs of caffeine poisoning in dogs?", "Restlessness, rapid breathing, racing heart, tremors, vomiting, and seizures — usually starting within 30–60 minutes."),
            ("Is caffeine bad for cats too?", "Yes — cats are also sensitive and slower to metabolize it. Keep coffee, tea, and energy drinks away from every pet."),
        ],
        "related": ["can-dogs-eat-chocolate", "can-dogs-eat-alcohol", "foods-toxic-to-dogs", "can-dogs-eat-milk"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has consumed caffeine, contact your veterinarian or a pet poison hotline right away.",
    },
    {
        "slug": "can-dogs-eat-raw-dough",
        "url": "/dog-nutrition/can-dogs-eat-raw-dough/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Raw Dough? No — It's a Double Emergency",
        "description": "Raw yeast dough keeps rising in a dog's warm stomach — painful bloat and alcohol poisoning at once. A drop-everything emergency. Baked bread is different.",
        "lede": "No — raw yeast dough keeps rising inside a dog's warm stomach, causing painful bloat and alcohol poisoning at the same time. It is one of the few kitchen hazards that is a true drop-everything emergency.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>no — and this one is urgent.</strong> Raw dough made with
        yeast is a rare double hazard: the yeast keeps fermenting <em>inside</em> the dog's
        warm stomach, producing <strong>ethanol (alcohol)</strong> and
        <strong>expanding gas</strong> at the same time. The result is alcohol poisoning and
        a bloated, twisted stomach — two emergencies in one.</p>

        <h2>The double emergency, explained</h2>
        <ul>
          <li><strong>Alcohol poisoning</strong> — fermentation produces ethanol right in
            the stomach; dogs absorb it fast. Signs: wobbling, disorientation, drooling,
            low blood sugar and low body temperature (see our
            <a href="/dog-nutrition/can-dogs-eat-alcohol/">alcohol</a> page).</li>
          <li><strong>Stomach bloat</strong> — the dough can expand to several times its
            size. A severely distended stomach is painful, can press on the diaphragm and
            make breathing hard, and in the worst case contributes to gastric torsion —
            a life-threatening twist that needs surgery.</li>
        </ul>

        <h2>Which doughs are the problem?</h2>
        <div class="callout warn">The danger is yeast dough — bread, pizza, rolls, cinnamon
        buns, pretzel dough, and anything left to rise. Baked bread is a different story:
        see our <a href="/dog-nutrition/can-dogs-eat-bread/">bread</a> page for what baked
        bread is safe.</div>
        <ul>
          <li><strong>Bread and roll dough</strong> — the classic holiday-baking exposure.</li>
          <li><strong>Pizza dough</strong> — often sits out to rise at dog height.</li>
          <li><strong>Cinnamon bun and sweet dough</strong> — yeast plus sugar plus raisins
            in some recipes (raisins are <a href="/dog-nutrition/can-dogs-eat-grapes/">
            toxic</a> on their own).</li>
          <li><strong>Non-yeast doughs</strong> — cookie dough is not a bloat/alcohol risk,
            but raw eggs carry salmonella and raw flour has its own (rare) bacterial risk;
            keep all raw dough away.</li>
        </ul>

        <h2>What to do if your dog ate raw yeast dough</h2>
        <ol>
          <li><strong>Call an emergency veterinarian immediately</strong> — do not wait for
            symptoms. This is a same-hour problem, not a watch-it-overnight problem.</li>
          <li><strong>Do not induce vomiting</strong> unless a professional directs you —
            with a distending stomach, vomiting is risky and timing matters.</li>
          <li><strong>Do not give water or food</strong> until the vet advises — fluid can
            feed the rise.</li>
          <li><strong>Note the amount and timing</strong> — how much dough, what kind, and
            when.</li>
          <li><strong>Watch for the red flags</strong> while arranging transport: swollen,
            drum-tight belly; unproductive retching; drooling; weakness; wobbling.</li>
        </ol>

        <h2>Frequently asked questions</h2>
        """,
        "faq": [
            ("Why is raw dough dangerous for dogs?", "Yeast keeps fermenting in the warm stomach, producing alcohol (poisoning) and expanding gas (painful bloat) at the same time — two emergencies in one."),
            ("Is baked bread safe if raw dough is not?", "Plain, fully baked bread in small amounts is generally fine. The hazard is the raw yeast state — see our bread page for the full picture."),
            ("Can pizza dough hurt a dog?", "Yes — it is a yeast dough and a very common exposure because it often rises at counter height. Treat ingestion as an immediate emergency."),
            ("What are the signs of dough bloat in dogs?", "A swollen, drum-tight belly, unproductive retching, drooling, restlessness, weakness, and wobbling. These need an emergency vet now."),
            ("How quickly does raw dough cause problems?", "Rising and fermentation start within minutes and signs can appear within the first hour. Early veterinary treatment — before the dough has risen fully — works best."),
            ("Is cookie dough as dangerous as bread dough?", "Different risk: no yeast means no bloat or alcohol, but raw eggs carry salmonella and raw flour has rare bacterial risk. Still keep it away."),
            ("Can dogs eat dough that has already been baked into bread?", "Yes, in small amounts if plain — no garlic, onion, raisins, or heavy butter and salt. Large amounts of any bread still cause bloating."),
            ("How do I keep my dog safe while baking?", "Keep rising dough covered and out of reach, never leave dough unattended on the counter, and take out the trash promptly — rising-dough smells are irresistible to dogs."),
        ],
        "related": ["can-dogs-eat-bread", "can-dogs-eat-alcohol", "can-dogs-eat-grapes", "foods-toxic-to-dogs"],
        "sources": [
            ("ASPCA Animal Poison Control — People Foods to Avoid Feeding Your Pets",
             "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Hazards",
             "https://www.merckvetmanual.com/toxicology/food-hazards"),
            ("Cornell Riney Canine Health Center — Canine Health Information",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. Raw yeast dough ingestion is an emergency — contact your veterinarian immediately.",
    },
    {
        "slug": "can-dogs-eat-almonds",
        "url": "/dog-nutrition/can-dogs-eat-almonds/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Almonds? Not Recommended — Here's Why",
        "description": "Almonds are not toxic to dogs like macadamia nuts, but they are still a bad treat: choking risk, pancreatitis from fat, and salted flavorings. What to know.",
        "lede": "Almonds are not poisonous to dogs the way macadamia nuts are, but vets still say no: they are a choking hazard, hard to digest, and loaded with fat that can trigger pancreatitis. Salted or flavored almonds are worse.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>not recommended — and one nut is one too many for small
        dogs.</strong> Almonds are not truly toxic the way <a
        href="/dog-nutrition/can-dogs-eat-macadamia-nuts/">macadamia nuts</a> are, which is
        why you will see conflicting answers online. But veterinarians still advise against
        them for three solid reasons: obstruction risk, digestive upset, and the fatty,
        salty ways we usually eat them.</p>

        <h2>Why vets say no to almonds</h2>
        <ul>
          <li><strong>Choking and obstruction.</strong> Almonds are the right size and shape
          to lodge in a small dog's throat or intestine, especially whole and unchewed.</li>
          <li><strong>GI upset.</strong> Dogs digest nuts poorly. A handful can cause vomiting,
          diarrhea, and gas within hours.</li>
          <li><strong>Pancreatitis.</strong> Almonds are high in fat. A large or repeated dose
          can inflame the pancreas — a painful, sometimes life-threatening condition.</li>
          <li><strong>Seasonings.</strong> Salted, wasabi, cocoa-dusted, or honey-roasted
          almonds add sodium and sometimes <a
          href="/dog-nutrition/can-dogs-eat-xylitol/">xylitol-sweetened</a> coatings.</li>
        </ul>

        <h2>Almonds by type: what your dog grabbed</h2>
        <table class="dose">
          <thead><tr><th>Type</th><th>Risk level</th><th>What to do</th></tr></thead>
          <tbody>
            <tr><td>Plain raw almond (1–2, large dog)</td><td>Low</td><td>Watch for GI upset</td></tr>
            <tr><td>Plain almond (small dog or puppy)</td><td>Moderate</td><td>Choking risk; call vet if several eaten</td></tr>
            <tr><td>Salted almonds</td><td>Moderate</td><td>Sodium risk; provide water, monitor</td></tr>
            <tr><td>Flavored / cocoa-dusted</td><td>High</td><td>Call vet — may contain toxic flavorings</td></tr>
            <tr><td>Almond butter (xylitol-free, small lick)</td><td>Low–moderate</td><td>Check label first; high fat</td></tr>
            <tr><td>Almond milk (small sip)</td><td>Low</td><td>Usually just GI upset risk</td></tr>
          </tbody>
        </table>

        <h2>Signs to watch after almond ingestion</h2>
        <p>Most healthy dogs that steal one or two plain almonds will be fine, but monitor
        for 24 hours. Call your vet if you see:</p>
        <ul>
          <li>Repeated vomiting or diarrhea</li>
          <li>Gagging, pawing at the mouth, or drooling (possible obstruction)</li>
          <li>Loss of appetite or a painful, hunched belly</li>
          <li>Lethargy lasting more than a few hours</li>
        </ul>
        <p class="note">Toy breeds and puppies are at the highest risk of obstruction. If a
        small dog eats a large quantity, treat it as a same-day veterinary visit.</p>

        <h2>Better nut-free and nut-adjacent treats</h2>
        <p>If you want crunch, skip the nut bowl entirely and reach for safe options:
        carrot coins, apple slices (no seeds), <a
        href="/dog-nutrition/can-dogs-eat-cucumber/">cucumber rounds</a>, or plain air-popped
        popcorn. For a protein-rich bite, small pieces of cooked chicken or <a
        href="/dog-nutrition/can-dogs-eat-salmon/">cooked salmon</a> beat any nut.</p>

        <h2>My dog ate almonds — next steps</h2>
        <ol>
          <li>Estimate the amount and type (salted? flavored? chocolate-covered?).</li>
          <li>Remove access and check for choking or immediate distress.</li>
          <li>For a few plain nuts in a large dog: monitor for 24 hours.</li>
          <li>For small dogs, large amounts, flavored nuts, or any concerning sign: call your
          vet or a pet poison hotline the same day.</li>
        </ol>
        """,
        "sources": [
            ("ASPCA — People Foods to Avoid Feeding Your Pets", "https://www.aspca.org/pet-care/animal-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Cornell Riney Canine Health Center — Dog Owners", "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "related": ["can-dogs-eat-macadamia-nuts", "can-dogs-eat-walnuts", "can-dogs-eat-peanut-butter", "can-dogs-eat-xylitol"],
        "faq": [
            ("Are almonds toxic to dogs?", "Not in the poisonous sense — almonds lack the unknown toxin found in macadamia nuts. But they still cause choking, GI upset, and pancreatitis risk, so vets recommend against feeding them."),
            ("What happens if my dog eats a few almonds?", "For a large dog, one to three plain almonds usually cause no more than mild stomach upset. Watch for vomiting or diarrhea over the next 24 hours and keep water available."),
            ("Are almonds dangerous for small dogs?", "Yes, more so. Their airway and intestine are narrow enough that whole almonds can cause choking or obstruction. If a toy breed eats a handful, call your vet."),
            ("Can dogs drink almond milk?", "A small lick of unsweetened almond milk is not toxic, but it offers no benefit and can cause loose stools. Never give sweetened versions, which may contain xylitol or excess sugar."),
            ("Is almond butter safe for dogs?", "Only xylitol-free almond butter, and only in tiny amounts — it is very high in fat. Always read the ingredient label; some nut butters contain xylitol, which is extremely toxic to dogs."),
            ("What about chocolate-covered almonds?", "Call your vet. This combines two problems: chocolate toxicity and almond fat. The darker the chocolate and smaller the dog, the more urgent it is."),
            ("Can almonds cause pancreatitis in dogs?", "Yes. High-fat foods — including a large almond haul from the trash — can trigger pancreatitis, with vomiting, abdominal pain, and lethargy. This needs veterinary treatment."),
            ("Which nuts are the worst for dogs?", "Macadamia nuts are the most toxic, followed by black walnuts (mold risk). Almonds, cashews, and peanuts are lower toxicity but still discouraged. Moldy nuts of any kind are dangerous."),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has eaten a large quantity of almonds or shows distress, contact your veterinarian or a pet poison hotline.",
    },
    {
        "slug": "can-dogs-eat-walnuts",
        "url": "/dog-nutrition/can-dogs-eat-walnuts/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Walnuts? No — Especially Black Walnuts",
        "description": "Walnuts are a poor treat for dogs: high fat, choking risk, and black walnuts carry a toxic mold. English walnuts are less dangerous but still a firm no.",
        "lede": "Walnuts are not recommended for dogs at all. English walnuts mainly pose choking and pancreatitis risk, but black walnuts can carry a mold toxin that causes tremors and seizures. Moldy walnuts of any kind are an emergency.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>no — and black walnuts are a genuine emergency.</strong>
        Walnuts combine the usual nut problems (fat, choking, poor digestion) with a risk
        many owners never think about: <strong>tremorgenic mold</strong>, which grows on
        walnuts — especially black walnuts — as they sit on the ground or in a damp garage
        bag. That mold produces toxins that cause tremors and seizures in dogs.</p>

        <h2>Two different problems: English vs black walnuts</h2>
        <table class="dose">
          <thead><tr><th>Type</th><th>Main risk</th><th>Urgency</th></tr></thead>
          <tbody>
            <tr><td>English walnut (store-bought, fresh)</td><td>High fat, choking, GI upset</td><td>Monitor</td></tr>
            <tr><td>Black walnut (yard, fallen)</td><td>Tremorgenic mycotoxins</td><td>Same-day vet</td></tr>
            <tr><td>Moldy walnut (any kind)</td><td>Mycotoxins — tremors, seizures</td><td>Emergency</td></tr>
            <tr><td>Walnut shell</td><td>Obstruction, dental damage</td><td>Watch closely</td></tr>
            <tr><td>Candied / spiced walnuts</td><td>Sugar, salt, possibly xylitol</td><td>Call vet</td></tr>
          </tbody>
        </table>

        <h2>What tremorgenic mycotoxins do</h2>
        <p>Molds that grow on decaying nuts produce compounds that overstimulate the nervous
        system. Signs usually appear within 30 minutes to a few hours:</p>
        <ul>
          <li>Muscle tremors that progress to full-body shaking</li>
          <li>Panting, hyperthermia (dangerously high temperature)</li>
          <li>Ataxia (wobbly, drunken gait)</li>
          <li>Seizures in severe cases</li>
        </ul>
        <p class="note">A dog that eats moldy nuts — often stolen from a compost pile, yard,
        or garbage bin — needs veterinary care immediately. With prompt treatment, most
        dogs recover fully.</p>

        <h2>The everyday walnut problems</h2>
        <p>Even a fresh English walnut is a poor choice. Like <a
        href="/dog-nutrition/can-dogs-eat-almonds/">almonds</a> and <a
        href="/dog-nutrition/can-dogs-eat-macadamia-nuts/">macadamia nuts</a>, walnuts are
        calorie-dense and fatty: a steady walnut habit contributes to weight gain and can
        trigger pancreatitis, and a whole nut can obstruct a small dog's intestine. Shells
        add dental fractures and blockage risk.</p>

        <h2>Walnut season hazards</h2>
        <p>If you have a walnut tree — or a neighbor does — autumn is the risky season. Fallen
        walnuts sit on wet ground and mold quickly, and dogs find them fascinating. Rake and
        remove fallen nuts before your dog is let out, and teach a solid <em>leave it</em>
        cue.</p>

        <h2>My dog ate a walnut — what now?</h2>
        <ol>
          <li>Identify the type and condition: fresh store-bought, black, or visibly moldy?</li>
          <li>Estimate the quantity and whether shells were eaten.</li>
          <li>Fresh English walnut, one or two, large dog: monitor for 24 hours.</li>
          <li>Black walnut, moldy nut, many nuts, a small dog, or any tremor: call your vet
          or a pet poison hotline immediately.</li>
        </ol>

        <p>For a safe crunchy snack, stick with carrots, apple slices, or plain <a
        href="/dog-nutrition/can-dogs-eat-popcorn/">air-popped popcorn</a> — and keep the
        nut bowl for the humans.</p>
        """,
        "sources": [
            ("ASPCA — People Foods to Avoid Feeding Your Pets", "https://www.aspca.org/pet-care/animal-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Tremorgenic Mycotoxins", "https://www.merckvetmanual.com/toxicology/mycotoxicoses/tremorgenic-mycotoxins"),
            ("Cornell Riney Canine Health Center — Dog Owners", "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "related": ["can-dogs-eat-almonds", "can-dogs-eat-macadamia-nuts", "can-dogs-eat-chocolate", "can-dogs-eat-xylitol"],
        "faq": [
            ("Are walnuts toxic to dogs?", "Black walnuts and moldy walnuts can be genuinely toxic due to tremorgenic mycotoxins. Fresh English walnuts are not poisonous, but they are still unhealthy — high fat, choking risk, and possible pancreatitis."),
            ("What if my dog ate one walnut off the floor?", "If it was a fresh, store-bought English walnut and your dog is large, watch for vomiting or diarrhea over 24 hours. If it came from a yard or tree and may have molded, call your vet."),
            ("Why are black walnuts worse for dogs?", "Black walnuts are strongly associated with tremorgenic mycotoxins — poisons from mold that cause tremors, high fever, and seizures. They also drop from trees and mold quickly on the ground."),
            ("Can dogs eat walnut shells?", "No. Shells can crack teeth, splinter, and cause intestinal obstruction. If your dog swallowed shell pieces, monitor for vomiting, constipation, or belly pain and call your vet if anything changes."),
            ("Is walnut oil or walnut butter safe?", "Neither is recommended. The oil is pure fat (pancreatitis risk), and nut butters may contain xylitol or added salt. Stick to dog-safe treats."),
            ("What are the signs of moldy walnut poisoning?", "Tremors that start within minutes to hours, wobbliness, panting, high body temperature, and possibly seizures. This is an emergency — go to a vet immediately."),
            ("Can puppies eat walnuts?", "No. Puppies are smaller, so doses hit harder, and their digestive systems are more sensitive. The obstruction risk is also higher."),
            ("Which nuts can dogs eat safely?", "None are truly 'safe' treats — peanuts are the least risky and plain, unsalted peanut butter (xylitol-free) is common in dog treats. But for crunch, choose carrots or apple slices instead."),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has eaten black walnuts, moldy nuts, or shows tremors, contact your veterinarian or a pet poison hotline immediately.",
    },
    {
        "slug": "can-dogs-eat-ham",
        "url": "/dog-nutrition/can-dogs-eat-ham/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Ham? Small Nibbles Only — Here's Why",
        "description": "Ham is not toxic to dogs, but it is salty, fatty, and often processed with garlic or onion. Occasional small nibbles are okay; regular feeding is not.",
        "lede": "Ham is not poisonous, but it is one of the worst everyday meats for dogs: very salty, high in fat, and often cured with garlic or onion powder. A small plain nibble on a holiday is fine — a ham habit is not.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>only tiny, plain, occasional nibbles — and never as a
        regular treat.</strong> Ham is not toxic, but it concentrates three problems dogs
        do not handle well: <strong>sodium, fat, and seasonings</strong>. This page explains
        where the real risks are and how much ham, if any, fits into a dog's diet.</p>

        <h2>Why ham is a poor fit for dogs</h2>
        <ul>
          <li><strong>Sodium load.</strong> Cured ham can carry 1,000+ mg of sodium per 100 g.
          A dog's daily sodium requirement is a fraction of that; excess causes thirst,
          and in large amounts, sodium ion poisoning.</li>
          <li><strong>Fat and pancreatitis.</strong> Ham is fatty, and fat triggers
          pancreatitis — a painful emergency with vomiting and a hunched belly.</li>
          <li><strong>Curing ingredients.</strong> Many hams are rubbed or injected with
          garlic and onion powder — both toxic to dogs (see <a
          href="/dog-nutrition/can-dogs-eat-onion/">onion</a> and <a
          href="/dog-nutrition/can-dogs-eat-garlic/">garlic</a>).</li>
          <li><strong>Bone danger.</strong> Ham bones — cooked or smoked — splinter into
          fragments that can obstruct or puncture the gut.</li>
        </ul>

        <h2>Ham by form: what's on the plate</h2>
        <table class="dose">
          <thead><tr><th>Form</th><th>Verdict</th></tr></thead>
          <tbody>
            <tr><td>Plain cooked ham, 1–2 small cubes (large dog)</td><td>Okay as a rare treat</td></tr>
            <tr><td>Plain cooked ham, small dog</td><td>Half a cube, rarely</td></tr>
            <tr><td>Honey-glazed / maple ham</td><td>Skip — sugar and glaze</td></tr>
            <tr><td>Ham with glaze containing garlic/onion</td><td>No — toxic seasonings</td></tr>
            <tr><td>Deli / sliced ham (lunchmeat)</td><td>Avoid — highest sodium</td></tr>
            <tr><td>Prosciutto, bacon, salami</td><td>Avoid — salt plus fat plus spice</td></tr>
            <tr><td>Ham bone</td><td>Never — splinter and obstruction risk</td></tr>
            <tr><td>Ham fat trimmings</td><td>No — pancreatitis trigger</td></tr>
          </tbody>
        </table>
        <p class="note">Portion guide: keep any cured meat under roughly 10% of daily
        calories — and for most dogs, a holiday-sized taste is already at that limit.</p>

        <h2>Dogs who should never have ham</h2>
        <ul>
          <li>Dogs with <strong>heart disease or hypertension</strong> (sodium)</li>
          <li>Dogs with a history of <strong>pancreatitis</strong> (fat)</li>
          <li>Dogs on <strong>weight management</strong> plans</li>
          <li>Dogs with <strong>kidney disease</strong> (sodium and protein load)</li>
          <li>Any dog on a prescribed therapeutic diet</li>
        </ul>

        <h2>Signs your dog had too much ham</h2>
        <ul>
          <li>Excessive thirst and urination (sodium)</li>
          <li>Vomiting or diarrhea within hours (fat and salt)</li>
          <li>Hunched posture, praying position, belly pain (pancreatitis — vet now)</li>
          <li>Lethargy and loss of appetite lasting into the next day</li>
        </ul>

        <p>If you want a meat treat that is actually designed for dogs, plain cooked
        <a href="/dog-nutrition/can-dogs-eat-chicken/">chicken</a> or <a
        href="/dog-nutrition/can-dogs-eat-salmon/">salmon</a> gives the flavor without the
        salt and fat load.</p>
        """,
        "sources": [
            ("ASPCA — People Foods to Avoid Feeding Your Pets", "https://www.aspca.org/pet-care/animal-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Salt Toxicity", "https://www.merckvetmanual.com/toxicology/salt-toxicity-in-animals"),
            ("Cornell Riney Canine Health Center — Dog Owners", "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "related": ["can-dogs-eat-chicken", "can-dogs-eat-salmon", "can-dogs-eat-garlic", "foods-toxic-to-dogs"],
        "faq": [
            ("Can dogs eat ham at all?", "A small plain nibble occasionally is not harmful for a healthy dog. But ham is high in sodium and fat and often cured with garlic or onion powder, so it should never be a regular treat."),
            ("What happens if my dog eats a lot of ham?", "Expect thirst and possibly vomiting or diarrhea from the salt and fat. A large amount can trigger pancreatitis — watch for belly pain, hunched posture, and repeated vomiting, and call your vet."),
            ("Can dogs eat ham bones?", "No. Cooked or smoked ham bones splinter into sharp fragments that can obstruct or puncture the digestive tract. That risk applies to the bone itself, regardless of the meat."),
            ("Is deli ham okay for dogs?", "It is the worst form — lunchmeat carries the highest sodium plus preservatives. If you must share, use plain home-cooked ham instead and keep it to a tiny piece."),
            ("Can puppies eat ham?", "Better not. Puppies have smaller tolerances for salt and fat, and their developing digestive systems are more easily upset. Stick to puppy-formulated food and treats."),
            ("Is ham toxic like onion or chocolate?", "No — ham itself is not poisonous. The danger comes from sodium, fat, and the garlic or onion seasonings often used in curing and glazes."),
            ("My dog ate ham with the bone — what do I do?", "Watch for choking, gagging, vomiting, constipation, or belly pain over the next few days. Do not induce vomiting (bone fragments can cause damage coming back up). Call your vet for guidance, especially for a small dog."),
            ("What meat can dogs eat instead of ham?", "Plain, cooked, unseasoned chicken, turkey, or salmon. These give the same meaty flavor with a fraction of the salt and fat — and no curing ingredients."),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has eaten a large amount of ham, a ham bone, or shows distress, contact your veterinarian.",
    },
    {
        "slug": "can-dogs-eat-ice-cream",
        "url": "/dog-nutrition/can-dogs-eat-ice-cream/",
        "pillar": "dog-nutrition",
        "title": "Can Dogs Eat Ice Cream? Mostly No — Safer Options Inside",
        "description": "Most dogs should skip ice cream: lactose, sugar, and dangerous flavorings like xylitol or chocolate. A tiny vanilla lick is low risk. Dog-friendly swaps.",
        "lede": "Ice cream is not toxic in itself, but between lactose upset, sugar, and flavorings like chocolate or xylitol, it is a treat to skip. A small lick of plain vanilla is low risk — a bowl is not, and some flavors are emergencies.",
        "eyebrow": "DOG NUTRITION",
        "experts": [
            "The veterinarians of the ASPCA Animal Poison Control Center",
            "The toxicology specialists at the Cornell Riney Canine Health Center",
        ],
        "checked": "2026-10-24",
        "body": """
        <p>Short answer: <strong>a tiny lick of plain vanilla is low risk — a bowl is not,
        and some flavors are outright dangerous.</strong> Ice cream stacks four problems:
        most adult dogs are lactose intolerant, it is sugar-dense, it is fatty, and its
        flavorings can include genuinely toxic ingredients.</p>

        <h2>The four problems with ice cream</h2>
        <ul>
          <li><strong>Lactose.</strong> After puppyhood, many dogs produce little lactase.
          Milk-based ice cream commonly causes gas, bloating, and diarrhea within hours.</li>
          <li><strong>Sugar.</strong> Regular sugar contributes to obesity and dental disease,
          and is off-limits for diabetic dogs.</li>
          <li><strong>Fat.</strong> Cream is rich enough to contribute to pancreatitis risk
          in susceptible dogs.</li>
          <li><strong>Toxic flavorings.</strong> Chocolate, coffee, macadamia, raisin, and
          xylitol-sweetened "sugar-free" varieties are all hazardous (see <a
          href="/dog-nutrition/can-dogs-eat-xylitol/">xylitol</a> and <a
          href="/dog-nutrition/can-dogs-eat-chocolate/">chocolate</a>).</li>
        </ul>

        <h2>Flavors ranked: from okay-ish to emergency</h2>
        <table class="dose">
          <thead><tr><th>Flavor</th><th>Risk</th></tr></thead>
          <tbody>
            <tr><td>Plain vanilla (one small lick)</td><td>Low — monitor for GI upset</td></tr>
            <tr><td>Strawberry or plain fruit swirl</td><td>Low–moderate (sugar, lactose)</td></tr>
            <tr><td>Cookies and cream / caramel</td><td>Moderate — sugar plus sometimes chocolate bits</td></tr>
            <tr><td>Chocolate any form</td><td>Hazard — call vet for amounts eaten</td></tr>
            <tr><td>Coffee or mocha</td><td>Hazard — caffeine toxicity</td></tr>
            <tr><td>Rocky road / rum raisin</td><td>Hazard — raisins and alcohol</td></tr>
            <tr><td>Sugar-free (xylitol)</td><td>Emergency — even small amounts</td></tr>
            <tr><td>Vanilla with macadamia mix-in</td><td>Emergency — macadamia toxicity</td></tr>
          </tbody>
        </table>

        <h2>What about dog ice cream and frozen dog treats?</h2>
        <p>Pet-store "dog ice cream" and frozen yogurts made for dogs are lactose-reduced
        or dairy-free and sweetened appropriately — those are fine in moderation. Even
        simpler, DIY frozen treats work great: freeze plain <a
        href="/dog-nutrition/can-dogs-eat-yogurt/">xylitol-free yogurt</a> with mashed
        <a href="/dog-nutrition/can-dogs-eat-blueberries/">blueberries</a> in an ice cube
        tray, or freeze small cubes of <a
        href="/dog-nutrition/can-dogs-eat-watermelon/">seedless watermelon</a>.</p>

        <h2>My dog ate ice cream — what now?</h2>
        <ol>
          <li>Identify the flavor and estimated amount — especially chocolate, coffee,
          raisin, macadamia, or any sugar-free product.</li>
          <li>Toxic flavor: call your vet or a pet poison hotline immediately with details.</li>
          <li>Plain vanilla or fruit: expect possible loose stools; keep water available and
          monitor for 24 hours.</li>
          <li>Diabetic dogs: check glucose per your vet's protocol after any sugary treat.</li>
        </ol>
        <p class="note">Puppies and small dogs feel lactose and sugar effects fastest —
        the same lick that does nothing to a Labrador can scramble a Chihuahua's stomach.</p>
        """,
        "sources": [
            ("ASPCA — People Foods to Avoid Feeding Your Pets", "https://www.aspca.org/pet-care/animal-poison-control/people-foods-avoid-feeding-your-pets"),
            ("Merck Veterinary Manual — Food Allergy and Intolerance", "https://www.merckvetmanual.com/dog-owners/digestive-disorders-of-dogs/food-allergy-and-intolerance-in-dogs"),
            ("Cornell Riney Canine Health Center — Dog Owners", "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-information"),
        ],
        "related": ["can-dogs-eat-yogurt", "can-dogs-eat-milk", "can-dogs-eat-chocolate", "can-dogs-eat-xylitol"],
        "faq": [
            ("Can dogs eat a little bit of ice cream?", "One small lick of plain vanilla is low risk for a healthy adult dog. Expect possible gas or loose stools from lactose. Anything more than a lick invites stomach upset and unneeded sugar."),
            ("Is ice cream toxic to dogs?", "Plain ice cream is not toxic, but flavors containing chocolate, coffee, macadamia nuts, raisins, or xylitol absolutely are. Sugar-free ice cream is the most dangerous — xylitol can be fatal in small amounts."),
            ("What happens if my dog eats chocolate ice cream?", "Call your vet or a pet poison hotline with the amount eaten and your dog's weight. Chocolate toxicity depends on cocoa concentration and body size — dark chocolate ice cream is far more serious than a tiny taste of milk-chocolate swirl."),
            ("Can puppies have ice cream?", "No. Puppies are more sensitive to lactose and sugar, and their calorie budget is tiny. If you want to celebrate, use a puppy-safe frozen treat made for dogs."),
            ("Why does ice cream give my dog diarrhea?", "Most adult dogs are lactose intolerant — they lack the enzyme to digest milk sugar. The lactose ferments in the gut, producing gas, cramping, and loose stools within hours."),
            ("Can dogs eat dog ice cream from the pet store?", "Yes, in moderation. These products are formulated lactose-reduced or dairy-free without toxic sweeteners. Check the label for xylitol anyway, and treat it as an occasional reward."),
            ("What can I give my dog instead of ice cream?", "Freeze xylitol-free plain yogurt with mashed blueberries, or freeze seedless watermelon cubes. Frozen carrot coins also work as a crunchy summer treat."),
            ("My dog ate sugar-free ice cream — is that an emergency?", "Yes, if it contains xylitol (also called birch sugar). Go to a vet immediately and bring the packaging. Xylitol can cause life-threatening low blood sugar and liver failure in dogs."),
        ],
        "disclaimer": "This page is general safety information, not a substitute for veterinary care. If your dog has eaten ice cream containing chocolate, xylitol, or other hazardous ingredients, contact your veterinarian or a pet poison hotline immediately.",
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
        "description": "Why does my cat meow at night? The causes by age, the four night calls and what each means, the evening routine that works, and the illnesses to rule out first.",
        "lede": "A cat yelling at your bedroom door at 3 a.m. is not being difficult. The cause is usually energy, hunger, or a habit you accidentally trained — and the fix is a routine, not a punishment.",
        "eyebrow": "CAT CARE",
        "body": """
        <h2>Cats are crepuscular, not nocturnal</h2>
        <p>Cats are most active at dawn and dusk — the hunting hours of their wild ancestors. A cat that slept all day and got no exercise while you were at work is wide awake exactly when you are falling asleep. Some night noise is therefore normal; the goal is to move it, not to erase it.</p>
        <p>This matters for the plan below. You are not trying to switch a nocturnal animal to your schedule. You are trying to shift two peaks of activity — dawn and dusk — so that the dawn peak lands after your alarm rather than at 4 a.m.</p>

        <h2>Start with the sound: four night calls</h2>
        <p>Owners who say "my cat won't stop meowing at night" are usually describing one of four different sounds. They need different responses, and treating them all the same is why most behaviour plans fail.</p>
        <table>
          <tr><th style="text-align:left">What you hear</th><th style="text-align:left">What it usually means</th><th style="text-align:left">First thing to try</th></tr>
          <tr><td>Short, repeated meow at the bedroom door</td><td>A request — food, company, an open door</td><td>Full evening routine below; then stop responding</td></tr>
          <tr><td>Long, drawn-out yowl, often while walking around</td><td>Disorientation, pain, or hormonal calling</td><td>Vet check; if unneutered, neutering</td></tr>
          <tr><td>Loud calling that started in the last few weeks</td><td>Usually medical — thyroid, blood pressure, pain</td><td>Book a vet visit before any behaviour plan</td></tr>
          <tr><td>Chirping or trilling at a window</td><td>Prey drive — a moth, a bird, another cat outside</td><td>Close the blind. This one is harmless</td></tr>
        </table>
        <div class="callout">If the call is new and your cat is over seven, skip straight to the vet section. A cat that never called at night and suddenly does is reporting a change in its body, not asking for attention.</div>

        <h2>Age changes the answer</h2>
        <p>The same 3 a.m. meow has completely different likely causes in a one-year-old and a fourteen-year-old. Sort your cat into one of these three groups before you pick a plan.</p>
        <table>
          <tr><th style="text-align:left">Age</th><th style="text-align:left">Most likely causes, in order</th><th style="text-align:left">What works</th></tr>
          <tr><td>Under 1 year (kitten)</td><td>Leftover energy; hunger; teething discomfort</td><td>Three or four short play sessions a day, not just one at night. Kittens genuinely need more play than adults</td></tr>
          <tr><td>1–7 years (adult)</td><td>A habit that has been rewarded; boredom; a long gap between dinner and breakfast</td><td>Evening routine plus a timed feeder. This is the group that improves fastest</td></tr>
          <tr><td>7 years and over (senior)</td><td>Medical first — thyroid, blood pressure, kidney, joint pain, cognitive change — then hunger or habit</td><td>Vet visit and bloodwork before any training. Behaviour work comes after the medical picture is clear</td></tr>
        </table>

        <h2>The usual suspects</h2>
        <ul>
          <li><strong>Leftover energy with nowhere to go</strong> — especially in kittens and young adults. A cat that slept 16 hours has a full tank at midnight.</li>
          <li><strong>Hunger</strong> — a cat fed dinner at 6 p.m. is genuinely hungry by 4 a.m., and learns very quickly that calling brings a person with a bowl.</li>
          <li><strong>Trained behaviour</strong> — if meowing has ever produced food, an open door, or even a scolding, it was rewarded. Attention of any kind counts, including negative attention.</li>
          <li><strong>Boredom in a single-room flat</strong> — nothing to climb, nothing to watch, nothing to hunt. Vertical space and a window with a view do more than most toys.</li>
          <li><strong>Unneutered cats</strong> yowl to find mates, and an outdoor cat visible through the window can trigger territory calling that has nothing to do with you.</li>
        </ul>

        <h2>The evening routine that works</h2>
        <p>Cats run on a natural cycle: hunt, catch, kill, eat, groom, sleep. You can borrow it. The sequence matters more than the exact clock times, but keeping them steady is what builds the habit.</p>
        <table>
          <tr><th style="text-align:left">Time</th><th style="text-align:left">What you do</th><th style="text-align:left">Why</th></tr>
          <tr><td>Early evening</td><td>10–15 minutes with a wand toy, worked hard</td><td>Burns the energy that would otherwise arrive at 3 a.m.</td></tr>
          <tr><td>Before bed</td><td>A second, shorter play session</td><td>Two peaks in the evening beat one long one</td></tr>
          <tr><td>Right after play</td><td>The main meal of the day</td><td>Hunt then eat then groom then sleep is the natural order</td></tr>
          <tr><td>After the meal</td><td>Quiet enrichment — puzzle feeder, box, scratching post</td><td>Gives a second outlet without waking you</td></tr>
          <tr><td>Lights out</td><td>Nothing. No response to calling</td><td>Every response, including "be quiet", restarts the habit</td></tr>
        </table>
        <div class="callout">An automatic feeder that opens at 5 a.m. breaks the link between <em>you</em> and breakfast — the single most effective fix for food-driven dawn calling. It also removes you from the equation entirely, which is the point.</div>

        <h2>When night meowing means illness</h2>
        <p>A sudden change — a cat that never called at night now yowling loudly — deserves a vet visit before any behaviour plan. In cats over about seven, increased night-time vocalising is a recognised sign of several treatable conditions. These are the ones a vet will typically work through:</p>
        <ul>
          <li><strong>An overactive thyroid (hyperthyroidism).</strong> One of the most common hormone problems in older cats. Look for a cat that eats well or even more than usual but still loses weight, seems restless or irritable, and calls at night. It is manageable, usually with medication or a special diet.</li>
          <li><strong>High blood pressure.</strong> Often secondary to thyroid or kidney disease. It can damage the eyes, and a sudden loss of vision may show up first as a cat that cries in the dark or seems disoriented at night.</li>
          <li><strong>Chronic kidney disease.</strong> Drinking more, urinating more, losing weight, dull coat, bad breath. Cats with kidney disease often feel worse at night and become more vocal.</li>
          <li><strong>Joint pain and arthritis.</strong> Very common in older cats and easy to miss, because cats hide it. Signs include hesitating before jumping, sleeping in different places, and yowling when getting up.</li>
          <li><strong>Cognitive dysfunction.</strong> The cat equivalent of age-related dementia: night-time wandering, calling at walls, forgetting the litter tray, and a flipped sleep-wake cycle.</li>
          <li><strong>Dental or stomach pain.</strong> A cat with a painful mouth may eat reluctantly, chew on one side, drool, or call after eating.</li>
        </ul>
        <p>At the appointment, ask specifically about these five checks — it is worth naming them rather than describing the meowing alone:</p>
        <table>
          <tr><th style="text-align:left">Check</th><th style="text-align:left">What it rules in or out</th></tr>
          <tr><td>Full physical exam with weight compared to last visit</td><td>Weight loss, dental pain, joint stiffness, an enlarged thyroid</td></tr>
          <tr><td>Blood panel including T4 and kidney values</td><td>Hyperthyroidism, kidney disease, diabetes</td></tr>
          <tr><td>Blood pressure measurement</td><td>Hypertension — easy to miss, treatable, protects the eyes</td></tr>
          <tr><td>Urine test</td><td>Kidney function, diabetes, urinary infection</td></tr>
          <tr><td>X-ray or ultrasound if indicated</td><td>Arthritis, abdominal pain, masses</td></tr>
        </table>

        <h2>What to expect in the first two weeks</h2>
        <p>Changing the routine usually makes things worse before they get better. This is normal and it is the point where most owners give up.</p>
        <ul>
          <li><strong>Nights 1–3:</strong> louder, longer calling. The behaviour that used to work has stopped working, so the cat tries harder. This is often called an extinction burst.</li>
          <li><strong>Nights 4–7:</strong> the calling gets shorter and less frequent, then starts to shift towards dawn.</li>
          <li><strong>Week 2:</strong> the new pattern settles, provided everyone in the house holds the same line. One person feeding at 3 a.m. resets the whole thing.</li>
          <li><strong>No improvement after two weeks:</strong> stop and go back to the medical section. A behaviour plan cannot fix a thyroid.</li>
        </ul>

        <h2>What not to do</h2>
        <ul>
          <li><strong>Do not punish.</strong> Yelling or spraying frightens the cat and still counts as attention, so it reinforces the noise.</li>
          <li><strong>Do not give in "just once".</strong> Intermittent rewards are the strongest kind for building a habit — one exception can undo a week.</li>
          <li><strong>Do not lock the cat in a room or a carrier at night.</strong> It increases distress and often produces louder calling plus scratching at the door.</li>
          <li><strong>Do not assume all meowing is misbehaviour.</strong> A new, distressed-sounding call in an older cat is information about its health, not a nuisance to be trained away.</li>
        </ul>
        """,
        "faq": [
            ("Why does my cat meow at the bedroom door every night?", "Usually a trained habit — the meowing has produced attention, food, or an open door. Check that needs are met, then stop responding, and keep a hard play session and a late meal before your bedtime."),
            ("Should I just ignore a cat meowing at night?", "If the behaviour is a learned request and the cat is safe, yes — responding rewards it. But a sudden change in a cat that never called before, especially over age seven, needs a vet check first."),
            ("Why is my old cat yowling loudly at night?", "In senior cats, night yowling often signals an overactive thyroid, high blood pressure, kidney disease, joint pain, or cognitive decline. Most causes are treatable — see the vet, and do not dismiss it as old age."),
            ("Why does my cat meow at night but sleep all day?", "Because cats are crepuscular, not nocturnal — their natural peaks are dawn and dusk. A cat left alone all day sleeps through it and then has a full tank of energy at night. The fix is daytime enrichment plus an evening play-and-feed routine."),
            ("Will neutering stop my cat yowling at night?", "If the calling is hormonal, yes — neutering usually stops mating-related yowling within a few weeks. It will not fix night calling caused by hunger, boredom, or illness, so rule those out separately."),
            ("Should I let my cat sleep in my bedroom?", "That is a preference, not a rule. If the cat settles quietly, there is no harm. If it wakes you repeatedly, a closed door with a full evening routine is kinder than an inconsistent door that opens sometimes."),
            ("Will an automatic feeder really help?", "For food-driven early-morning calling, it is the single most effective change, because it removes you from the equation. Set it a few minutes earlier than the current waking time, then shift it later by ten minutes every few days."),
            ("Is it cruel to ignore a cat crying at night?", "Not if its needs are met and it is healthy. Ignoring a learned request is different from ignoring distress — which is why a sudden change in an older cat should go to the vet rather than be ignored."),
        ],
        "related": ["cat-hairballs", "cat-litter-training", "cat-spraying-how-to-stop", "cat-scratching-furniture"],
        "sources": [
            ("Cats Protection — Cats at Night",
             "https://www.cats.org.uk/help-and-advice/home-and-environment/cats-at-night"),
            ("ASPCA — Common Cat Behavior Issues",
             "https://www.aspca.org/pet-care/cat-care/common-cat-behavior-issues"),
            ("Merck Veterinary Manual — Behavior of Cats",
             "https://www.merckvetmanual.com/cat-owners/behavior-of-cats"),
            ("Cornell Feline Health Center — Cat Health Topics",
             "https://www.vet.cornell.edu/departments-centers-and-institutes/cornell-feline-health-center"),
            ("International Cat Care — Cat Advice",
             "https://icatcare.org/cat-advice"),
        ],
        "experts": [
            "The feline health team at Cornell University's College of Veterinary Medicine",
            "The veterinary advisors at International Cat Care",
        ],
        "checked": "2026-10-28",
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


# --- Section-page bodies -----------------------------------------------------
# 10-28: section pages were 138-296 words (a card grid plus one sentence), which
# tells Google the directory is empty. Each pillar now carries a real body above
# the card grid: a framework, a reference table, and the "when this becomes a
# vet visit" threshold. Injected after PILLARS so the dict above stays readable.
PILLAR_BODY = {}

PILLAR_BODY["dog-care"] = """
<h2>What routine care actually looks like</h2>
<p>Dogs do not complain about the things that are done to them weekly, which is exactly why routine care slips. The list is short, and almost all of it takes less time than a walk.</p>
<table>
  <tr><th style="text-align:left">Task</th><th style="text-align:left">How often</th><th style="text-align:left">Why it matters</th></tr>
  <tr><td>Brushing teeth</td><td>Daily, or at least every other day</td><td>Plaque hardens into tartar within 48 hours; most dogs over three have some periodontal disease</td></tr>
  <tr><td>Body check by hand</td><td>Weekly</td><td>Lumps, sore spots and hot ears are found by touch long before they are found by eye</td></tr>
  <tr><td>Ear check</td><td>Weekly for floppy-eared breeds</td><td>A smell or dark discharge is the first sign of infection, and it is treatable at that stage</td></tr>
  <tr><td>Brushing coat</td><td>Two to three times a week</td><td>Prevents matting and spreads skin oils; double coats need more in shedding season</td></tr>
  <tr><td>Nail trim</td><td>Every three to four weeks</td><td>Overlong nails change how the paw lands, which puts strain on the joints</td></tr>
  <tr><td>Bath</td><td>Every four to eight weeks</td><td>More often strips the coat's oils; less often is usually fine for a healthy dog</td></tr>
  <tr><td>Weigh-in</td><td>Monthly</td><td>Weight is the cheapest early warning for heart, thyroid and joint disease</td></tr>
</table>

<h2>The three things owners skip, and what they cost</h2>
<p><b>Teeth.</b> The single most skipped task and the one with the clearest consequence. By the time bad breath is obvious, there is usually tartar below the gumline, and treating it means an anaesthetic dental. Two minutes a day with a dog toothbrush is the whole intervention. If your dog has never had it done, start with a finger and toothpaste formulated for dogs — human toothpaste is not safe to swallow.</p>
<p><b>Nails.</b> Dogs that walk on pavement still need trims, because the dewclaw never touches the ground and the side nails wear unevenly. A dog that clicks on hard floors is overdue. The risk of cutting too deep is real, so take small slices and have styptic powder to hand — the full method is in <a href="/dog-care/how-to-trim-dog-nails/">how to trim dog nails without the drama</a>.</p>
<p><b>Ears.</b> Floppy ears trap warmth and moisture, which is why spaniels, retrievers and poodles top the infection statistics. A weekly sniff and a wipe of the visible folds with a vet-approved cleaner is enough. Do not push cotton buds into the canal, and do not use alcohol or vinegar mixes on a dog that already has sore ears.</p>

<h2>Care by life stage</h2>
<table>
  <tr><th style="text-align:left">Stage</th><th style="text-align:left">What moves to the front</th><th style="text-align:left">Vet rhythm</th></tr>
  <tr><td>Puppy (under 12 months)</td><td>Handling practice, teeth habit, nails while they are still small enough to hold</td><td>Vaccination course, then monthly weigh-ins</td></tr>
  <tr><td>Adult (1–7 years)</td><td>Weight maintenance, dental care, coat and ear routine</td><td>Annual check, dental check every visit</td></tr>
  <tr><td>Senior (7 years and up)</td><td>Joint comfort, softer bedding, shorter and more frequent walks</td><td>Every six months, with bloodwork</td></tr>
</table>
<p>The reason senior care is listed separately is that the routine changes shape rather than intensity. A senior dog does not need fewer checks — it needs them more often, and it needs the owner to notice slower stairs and reluctance to jump before it becomes a diagnosis.</p>

<h2>When grooming turns into a vet visit</h2>
<p>Stop and call the vet rather than continuing, if you see: bleeding that does not stop within a few minutes of pressure, a nail that keeps bleeding after styptic, gums that bleed when you brush, a head that is suddenly sensitive to being touched, a bad smell from one ear with head shaking, or a patch of skin that is red, weeping or spreading.</p>
<p>Two things are not emergencies but should be booked in: a dog that has started resisting having its paws handled (pain, not stubbornness, in most cases), and a dog that has developed a new lump you can feel but not see. Both are cheap to check and expensive to leave.</p>
"""

PILLAR_BODY["dog-training"] = """
<h2>Training is timing, not commands</h2>
<p>A dog does not learn "sit" because the word is repeated. It learns because something good arrived within about three seconds of the behaviour. That window is the whole game: reward inside it and the dog connects the two; reward outside it and you reinforce whatever happened next, which is usually standing up.</p>
<p>This is why a marker word — "yes" — earns its place. It fires the instant the behaviour happens and buys you the two seconds it takes to get a treat out of a pocket. Mark, then pay. The dog learns the marker predicts food, and the marker becomes usable at a distance and without a hand in your pocket.</p>

<h2>One behaviour at a time</h2>
<p>Most training goes wrong by trying to fix three things at once. Cut every skill into its smallest version, get that reliable in a quiet room, then add one variable at a time — distance, duration, or distraction, never two together.</p>
<table>
  <tr><th style="text-align:left">Skill</th><th style="text-align:left">First version</th><th style="text-align:left">Then add</th></tr>
  <tr><td>Recall</td><td>Two steps away, indoors, no distraction</td><td>Distance, then a garden, then a park on a long line</td></tr>
  <tr><td>Settle</td><td>Ten seconds on a mat while you stand still</td><td>Duration, then you moving, then visitors</td></tr>
  <tr><td>Loose lead</td><td>Five steps in the hallway with no tension</td><td>Front door, then pavement, then other dogs at a distance</td></tr>
  <tr><td>Leave it</td><td>Treat under a shoe, dog backs off</td><td>Food on the floor, then outdoors, then dropped items</td></tr>
</table>

<h2>How long a session should be</h2>
<p>Short and finished beats long and abandoned. A puppy has an attention span measured in minutes; five minutes twice a day teaches more than one twenty-minute session, because the last five minutes of the long session are where the mistakes and the frustration live.</p>
<p>End every session on a behaviour the dog already knows. That last success is what it remembers, and it is what makes the dog willing to come back out tomorrow. If a session has gone badly, do not push through to a win — stop, put the treats away, and reset later.</p>

<h2>The five mistakes that undo progress</h2>
<p><b>1. Repeating the cue.</b> "Sit, sit, sit" teaches the dog that the first word is background noise. Say it once, wait two seconds, then make it easier.</p>
<p><b>2. Paying for the wrong moment.</b> A dog that sits and then breaks before the treat arrives has been paid for breaking. Wait for the behaviour, mark it, then reach.</p>
<p><b>3. Training when the dog is over threshold.</b> A dog that is already barking at another dog cannot learn. Increase distance until it can eat and think, then work there.</p>
<p><b>4. Using punishment for a fear response.</b> Corrections suppress the visible behaviour and leave the emotion in place, which is how a dog that was once merely worried becomes a dog that snaps without warning. This is the one mistake with a genuine welfare cost.</p>
<p><b>5. Practising only in the easy place.</b> A dog that sits perfectly in the kitchen and nowhere else has learned the kitchen. Proof the behaviour in a new location every week, at a lower difficulty than you think you need.</p>

<h2>What "positive" actually means</h2>
<p>Reward-based training is not permissive training. The dog still has boundaries and still hears "no" — what changes is that the boundary is taught by making the wanted behaviour worth doing, and by managing the environment so the unwanted one is not rehearsed. A puppy that cannot reach the bin does not need to be told off at the bin.</p>
<p>Start with the two guides most owners need first: <a href="/dog-training/how-to-crate-train-a-puppy/">crate training a puppy</a> and <a href="/dog-training/how-to-stop-puppy-biting/">stopping puppy biting</a>. Both are built on the same three-second rule, applied to the two problems that make the first month hardest.</p>
"""

PILLAR_BODY["dog-health"] = """
<h2>Three questions that sort any symptom</h2>
<p>Owners usually want a diagnosis. What they actually need at 11pm is a triage decision, and that comes from three questions: is the dog breathing normally, is it responsive and steady on its feet, and is there blood or a distended belly. If any answer is wrong, it is a now problem regardless of what else is going on.</p>
<table>
  <tr><th style="text-align:left">What you are seeing</th><th style="text-align:left">How fast to act</th></tr>
  <tr><td>Difficulty breathing, blue or pale gums, collapse, seizure, bloated and unproductive retching</td><td><b>Emergency now</b> — call the vet while you are on the way</td></tr>
  <tr><td>Repeated vomiting, blood in stool or vomit, straining to urinate, eye injury, suspected poisoning</td><td><b>Today</b> — same-day appointment</td></tr>
  <tr><td>Soft stool for a day, mild limping, occasional reverse sneeze, one episode of vomiting with normal energy after</td><td><b>Watch 24–48 hours</b>, with a note of what changed</td></tr>
</table>
<p>The distinction that matters most is energy. A dog that vomited once and then asked for a walk is in a different category from a dog that vomited once and went to lie in a dark room. Behaviour is the signal; the symptom count is not.</p>

<h2>Normal values worth knowing by heart</h2>
<table>
  <tr><th style="text-align:left">Measure</th><th style="text-align:left">Normal range for an adult dog</th></tr>
  <tr><td>Body temperature</td><td>38.0–39.2 °C (101–102.5 °F)</td></tr>
  <tr><td>Resting breathing rate</td><td>10–30 breaths per minute</td></tr>
  <tr><td>Heart rate</td><td>Small breeds 120–160, medium 70–120, large 60–100 bpm</td></tr>
  <tr><td>Capillary refill (gum press)</td><td>Colour returns within 2 seconds</td></tr>
</table>
<p>These numbers are less useful as absolutes than as your dog's own baseline. A breathing rate that has gone from 16 to 34 at rest is worth a call even though both ends sit inside the published range. Take the readings when the dog is calm and write them down — a number you can compare against is the whole point.</p>

<h2>The combinations that are red flags</h2>
<p>Single symptoms are usually minor. Combinations are what veterinarians react to. Vomiting plus a distended abdomen plus unproductive retching is a gastric dilation pattern and is fatal within hours without surgery. Drinking a lot plus urinating a lot plus weight loss points at diabetes or kidney disease rather than a behaviour problem. A head tilt plus flicking at one ear plus loss of balance is more than an ear infection. Pale gums plus weakness plus a recent injury is internal bleeding until proven otherwise.</p>
<p>If two or more of these appear together, do not wait for the third.</p>

<h2>How to describe a symptom so the vet can help</h2>
<p>Photograph it. A stool, a limp, a lump, a pile of vomit — a phone photo taken in the moment is worth more than any description you will manage on the phone an hour later. Then note four things: when it started, whether it is getting better or worse, what the dog ate in the previous 24 hours, and whether energy and appetite have changed.</p>
<p>That last pair is what separates "bring it in" from "watch it". Appetite and energy are the two most sensitive indicators a dog has, and they are the two owners are best placed to judge.</p>
<p>For the symptoms that send most people to this section: <a href="/dog-health/dog-vomiting-causes/">vomiting</a>, <a href="/dog-health/why-is-my-dog-shaking/">shaking</a>, <a href="/dog-health/dog-not-eating-but-drinking-water/">not eating but drinking</a>, and <a href="/dog-health/dog-ear-infection-symptoms/">ear infection signs</a>.</p>
"""

PILLAR_BODY["cat"] = """
<h2>Cats are not small dogs</h2>
<p>Almost every cat problem in this section comes from applying dog logic to a cat. A dog that is shut out of a room is mildly annoyed; a cat that is shut out of a room may start urinating on the bed, because a cat's sense of security is built on territory and routine rather than on social approval. Cats are not stubborn and they are not vengeful — they are specific about conditions, and when the conditions are wrong they show it through behaviour and through hiding.</p>

<h2>The three complaints behind most cat questions</h2>
<table>
  <tr><th style="text-align:left">Problem</th><th style="text-align:left">Most common real cause</th><th style="text-align:left">First step</th></tr>
  <tr><td>Peeing outside the box</td><td>Medical, in a large share of cases — cystitis, crystals, arthritis making the box painful to climb into</td><td>Vet visit before behaviour work; a urine sample is the cheapest test you will run</td></tr>
  <tr><td>Scratching furniture</td><td>No acceptable scratching surface in the right place, or one that moves</td><td>A sturdy vertical post next to the scratched object, not in another room</td></tr>
  <tr><td>Meowing at night</td><td>Unspent energy, hunger timing, or a medical cause in older cats</td><td>Play-and-feed sequence before bed; bloodwork if the cat is over ten</td></tr>
</table>
<p>The order matters. Cats hide illness well, and a behavioural explanation is the more comfortable one to reach for, which is why it is often the wrong one. Litter box avoidance in particular should be treated as a medical question until a vet has ruled it out — the behaviour work comes after, not instead.</p>

<h2>The stress signals you are probably missing</h2>
<p>Cats advertise stress quietly. Hiding more than usual, eating only at night, a coat that has stopped being groomed, over-grooming a patch bald, sitting with the head pressed against a wall, and a tail that flicks while the cat is supposedly resting are all reports worth acting on. A cat that has stopped jumping onto the bed is often a cat with joint pain, not a cat that has gone off you.</p>
<p>Change is the other trigger. A new baby, a new flatmate, a new cat, moved furniture or a building site next door will all show up as behaviour before it shows up as anything else. Cats do not need the change removed; they need somewhere to retreat to, resources in more than one place, and time.</p>

<h2>What a cat actually needs set up</h2>
<p>The rule of thumb that resolves most multi-cat friction: one litter box per cat plus one, spread across different rooms rather than lined up together. Food and water in separate places, because cats prefer not to drink where they eat. Somewhere high to sit, because vertical space is how a cat controls its own exposure. And a scratching post that is tall enough for the cat to stretch fully — most bought posts are too short, which is why the sofa wins.</p>
<p>None of this is enrichment for its own sake. Each item removes a reason for the behaviour that brought you to this page.</p>

<h2>When it is not behavioural at all</h2>
<p>See a vet rather than adjusting the house if: a cat stops eating for more than 24 hours (in cats this is a genuine emergency, not a hunger strike), drinks and urinates noticeably more, loses weight while eating normally, has a sudden change in litter box habits after years of consistency, or starts vocalising at night when it never used to. Those five are the classic presentations of the conditions that are treatable early and difficult late.</p>
"""

PILLAR_BODY["best"] = """
<h2>How these guides are put together</h2>
<p>This section exists to answer one question: what should I buy, and what should I avoid? The honest answer starts with a limitation — there is no laboratory here, and no sponsored placement. Nothing in these guides is paid for, and no brand has been given a ranking in exchange for anything.</p>
<p>What there is instead is a specification approach. Rather than declaring one crate or harness "the best", each guide sets out the measurements and construction details that decide whether a product works, and then explains how to check those against the dog in front of you. A crate that is perfect for a 12 kg dog that settles quickly is the wrong crate for a 12 kg dog with separation anxiety.</p>

<h2>What we check before recommending anything</h2>
<table>
  <tr><th style="text-align:left">Category</th><th style="text-align:left">What decides it</th></tr>
  <tr><td>Fit</td><td>Measured dimensions against the dog, with growth allowance; harnesses checked at chest rather than neck</td></tr>
  <tr><td>Construction</td><td>Bar spacing and gauge, weld quality, latch type, whether the frame can be bent by a determined dog</td></tr>
  <tr><td>Safety failure modes</td><td>What happens when it breaks — a crate latch that pops open, a harness strap that loosens under load, a collar that can be backed out of</td></tr>
  <tr><td>Cleaning</td><td>Whether it can actually be washed, because a product that is hard to clean stops being used</td></tr>
  <tr><td>Honest limits</td><td>What the product is not for — travel vs home, crate-rest vs everyday, pulling vs lunging</td></tr>
</table>
<p>The failure-mode row is the one that gets skipped in most buying guides and the one that matters most. Almost every product functions correctly on the first day. The question that separates a good purchase is what it does on the day the dog panics.</p>

<h2>Why there is no single "best" product</h2>
<p>Ranking products requires either testing them all under the same conditions, which needs a facility, or repeating the rankings of people who have one. Most "best of" lists are the second thing wearing the clothes of the first. A specification approach is less satisfying to read and considerably more useful: it survives the product being discontinued, and it works for a dog whose size or temperament was not in anyone's test group.</p>
<p>Where a guide does make a recommendation, it is written as a fit-for-purpose statement rather than a ranking — the criterion, the range that satisfies it, and the reasons to go up or down within that range.</p>

<h2>How to use these guides</h2>
<p>Measure first, then read. Write down the dog's standing height, chest girth behind the front legs, and the length from chest to rump, and weigh it. Two of the three questions in every buying decision are answered by those numbers. Then read the section on failure modes and decide whether the risk profile matches your dog — a dog that has bent a crate before needs a different gauge, not a different colour.</p>
<p>If a guide here does not answer your question, that is worth knowing too: it means the question is specific enough that a vet, a trainer, or the manufacturer's own measurements should be the next stop rather than another list.</p>

<h2>Before you buy anything</h2>
<p>Three questions answer most of the purchase before a product is even shortlisted. How large will the dog be in six months, because a crate bought for a puppy is usually replaced inside a year. Where will this live, because a crate that has to be folded away every evening stops being used by the second week. And who else handles the dog, because a harness one person can fasten and another cannot is a harness that gets skipped on the days it matters most.</p>
<p>If those three cannot be answered yet, the specification in the guide will not help. Buy the tape measure first and come back with numbers.</p>
"""

for _k, _v in PILLAR_BODY.items():
    if _k in PILLARS:
        PILLARS[_k]["body"] = _v.strip()
