"""Seed data for the Cozy Loop Crochet articles collection.

This module is the single source of truth for the article content that is
loaded into MongoDB on first boot. Adding or editing articles here (and
then clearing the ``articles`` collection) is the recommended way to
publish new content without touching the frontend bundle.
"""

IMAGES = {
    "yarn": "https://images.unsplash.com/photo-1668072587859-f0f30c8fa938?auto=format&fit=crop&w=1200&q=80",
    "blanket": "https://images.pexels.com/photos/6216236/pexels-photo-6216236.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "amigurumi": "https://images.unsplash.com/photo-1559996279-1e9d0d508b74?auto=format&fit=crop&w=1200&q=80",
    "tops": "https://images.unsplash.com/photo-1618354691373-d851c5c3a990?auto=format&fit=crop&w=1200&q=80",
}

CATEGORY_PARAGRAPHS = {
    "Beginners": [
        "Crochet feels wonderfully tactile: one hook, one strand, and a growing line of small decisions. The fastest way to improve is not to rush through a giant project, but to understand what your hands are doing. Start with a smooth, medium-weight yarn and a comfortable hook. Make a slip knot that slides, not one that grips the hook like a vise.",
        "Your first rows may look uneven. That is normal. Count the loops on your hook, pause at the end of every row, and use a scrap of yarn to mark the first stitch. Consistency arrives through repetition, not talent. If a motion feels awkward, slow it down until the yarn has a chance to teach you its path.",
        "Keep practicing in small sessions. Ten focused minutes can teach more than an hour spent tugging at tight stitches. For the next step, explore our guide to even stitches, then return to this page whenever a pattern abbreviation feels unfamiliar.",
    ],
    "Stitch School": [
        "Even fabric starts with a relaxed grip and a repeatable rhythm. Let the hook do the lifting rather than squeezing it. When tension changes, your stitches change size; when your breathing settles, your hands usually follow. A simple swatch is not wasted yarn—it is a map of how your yarn, hook, and hands cooperate.",
        "Look at the top edge of your work before inserting the hook. The small V shapes are the stitch tops, and finding them is more reliable than guessing by feel. Count periodically, especially after a turning chain. If a stitch disappears, stop at once and inspect instead of building a mystery into the next ten rows.",
        "A tidy finish is built one calm choice at a time. Try a small swatch today, and use our mistake-fixing guide when your fabric takes an unexpected turn.",
    ],
    "Yarn Guide": [
        "Yarn choice changes the entire experience of a project. Fiber affects drape, warmth, stitch definition, washability, and how quickly your hands tire. Weight affects scale. Before buying a basketful, make a tiny sample and wash it the way the finished item will be washed.",
        "Cotton gives structure and clear stitches, wool offers bounce and warmth, and acrylic is often practical for gifts that need easy care. None is universally best. Ask what the finished object must do, then choose the fiber that supports that job. A beautiful skein that fights the pattern is not a bargain.",
        "Read the label, check yardage rather than only skein weight, and buy a little extra when dye lots matter. Thoughtful yarn choices make every pattern feel more manageable.",
    ],
    "Amigurumi": [
        "Small crochet animals are approachable because their shapes are built from familiar stitches. The magic ring, single crochet, increases, and decreases create a soft sphere; a few carefully placed details create personality. Work with a firm tension so stuffing does not peek through.",
        "Count every round and use a stitch marker. Place facial features before closing the body so you can adjust the expression. Safety eyes are convenient, but embroidered features are a thoughtful option for very young recipients. Stuff gradually, checking the shape from several angles.",
        "The best tiny animals are not perfect—they are expressive. Start with one simple body, keep notes, and celebrate the moment your flat circle becomes something that looks back at you.",
    ],
    "Patterns": [
        "A blanket is a generous project: repetitive enough to soothe, varied enough to keep your attention. Choose a pattern whose repeat you can recognize by sight. This makes it easier to pause, resume, and catch an error before it travels across the row.",
        "Think about the person and the room before choosing colors. Three shades can feel intentional when they share a temperature, while one unexpected accent can make a classic palette sing. Swatch the stitch, not just the color, because texture changes how much light a yarn reflects.",
        "Give yourself a realistic finish line. A smaller lap blanket may become a beloved everyday object sooner than a huge throw. Keep a project note with the hook, yarn, and row count so future-you can pick up without detective work.",
    ],
    "Crochet Life": [
        "Crochet becomes more joyful when it fits real life. Keep a small project bag ready, store hooks where you can see them, and write down the next step before you put work away. These tiny systems protect your creative energy from avoidable friction.",
        "If you share or sell your work, let the handmade quality be the story. Photograph texture in natural light, describe materials honestly, and price for time as well as supplies. A clear process builds trust with readers, customers, and your future self.",
        "There is no single correct way to make a crochet life. Choose the habits that make you want to return to your hook tomorrow, and let your practice grow from there.",
    ],
}

PLUS_SIZE_BODY = [
    {
        "id": "why-fit",
        "heading": "Why fit is a design choice, not a compromise",
        "paragraphs": [
            "Crochet tops feel like magic when they fit—and quietly frustrating when they do not. A pattern printed for one body is a starting point, not a rulebook. The good news is that crochet is unusually forgiving when you decide to redesign a piece. Because you build fabric one stitch at a time, you can add width exactly where you need it, shorten where you want it, and shape a neckline that actually flatters your shoulders.",
            "The trick is knowing which numbers to change and when to change them. Most patterns are graded for a fairly narrow range of sizes, and the largest sizes are sometimes the smallest version stretched close to breaking point. That is where personal adjustments come in. Instead of chasing size labels, we chase measurements. Instead of hoping a top will fit, we plan for the exact silhouette we want. This guide walks through the practical adjustments that make a crochet top feel custom: measuring honestly, choosing adaptable patterns, calculating a truthful gauge, and shaping the bust, waist, and hips with confidence.",
        ],
    },
    {
        "id": "measure",
        "heading": "Start with real measurements",
        "paragraphs": [
            "Before touching a hook, grab a soft measuring tape, a mirror, and ten quiet minutes. Write down your full bust, high bust (just under the underarms), waist at its narrowest, full hip, cross-back (shoulder to shoulder), armhole depth, and finished length from shoulder to where you want the hem. Wear a bra similar to the one you plan to wear with the finished top so the numbers reflect real life.",
            "If your full bust is significantly larger than your high bust, look for patterns that offer bust darts or extra shaping in the front piece. Do not round measurements down to feel better about a number—round up if anything, because a little extra ease is easier to remove later than to add. Finally, decide on your ease preference: one to two inches of positive ease for a snug fit, three to four for a comfortable everyday tee, and five or more for a boxy or oversized look. These numbers become your target dimensions, and every pattern adjustment starts from here.",
        ],
    },
    {
        "id": "choose-pattern",
        "heading": "Choose patterns that adapt well",
        "paragraphs": [
            "Not every pattern is worth grading up. Look for tops written in stitch counts (like \"chain 120\") rather than only inches, because that makes the math predictable. Simple stitch repeats—half double crochet, moss stitch, granite stitch, extended single crochet—are the friendliest to add width to without breaking a pattern. Complex lace panels that only work over a very specific stitch count are harder to expand cleanly.",
            "Rectangles and simple raglan constructions are especially generous for plus and diverse bodies. A tee that is essentially two rectangles seamed at the shoulders can be scaled to almost any size just by adding stitches and rows. Top-down raglans let you try the piece on as you go, which is priceless when you are new to grading. If pattern language still feels like a foreign dialect, spend a few minutes with [[read-crochet-pattern|our guide on reading crochet patterns like a pro]] before you start rewriting numbers.",
        ],
    },
    {
        "id": "gauge",
        "heading": "Gauge, honestly",
        "paragraphs": [
            "Gauge is not decoration. It is the whole equation. Work at least a six-by-six-inch swatch in the pattern stitch, wash it the way you will wash the finished top, and let it dry flat. Then measure. If your swatch says fourteen stitches over four inches, you have three and a half stitches per inch. Multiply your target bust circumference by that number to know how many stitches you need across the widest part of your top.",
            "If your gauge does not match the pattern, resist the urge to force it—recalculate every number based on your gauge instead. Consistency matters here more than matching the designer's number. If your tension shifts as you work, revisit the fundamentals of [[even-crochet-stitches|perfectly even stitches]] before starting the real project. A relaxed rhythm, a comfortable hook, and periodic counting save hours of ripping back later.",
        ],
    },
    {
        "id": "add-width",
        "heading": "Add stitches for width, thoughtfully",
        "paragraphs": [
            "The most common adjustment is simply adding stitches across the front and back. If your pattern says the small size uses ninety stitches and your gauge calls for one hundred and thirty-two, you need forty-two extra stitches, split evenly between pieces. Add stitches in multiples that respect the stitch pattern's repeat—if the pattern repeats every four stitches, add stitches in groups of four so the texture stays clean.",
            "Distribute added stitches so shaping still lands in flattering places: keep the same number of edge stitches for seaming, and add to the middle where the pattern repeats live. When you add width, remember to add matching stitches to the sleeves and armholes so proportions stay balanced. For curvier busts, add most of the extra width to the front piece only, keeping the back closer to the original count. This creates a natural forward drape without a boxy front. Two to four extra stitches on each front side is often enough to shift a top from \"pulling across the chest\" to \"sitting exactly right.\"",
        ],
    },
    {
        "id": "shape",
        "heading": "Adjust length, sleeves, and necklines",
        "paragraphs": [
            "Length is the easiest adjustment: add or remove rows until the piece matches your measurement, then finish with a border. For sleeves, work them flat if the pattern allows, so you can try them on with a safety pin as a stitch marker to see where the elbow bends. Cap sleeves and short sleeves are often the most forgiving on arms of any size, but a well-fitted three-quarter sleeve can be equally flattering when the armhole depth is generous.",
            "Necklines are where a top becomes personal. Plus and diverse bodies often look best with slightly wider necklines—boat neck, wide scoop, or a soft V—because they balance the shoulders and give the top a graceful line. If a pattern gives a small round neckline, widen it by starting the neck decreases one to two inches earlier and stopping them earlier too. Try the piece on before finishing the border; the raw edge is very close to the final shape and gives you a real preview.",
        ],
    },
    {
        "id": "yarn",
        "heading": "Yarn and hook choices for drape",
        "paragraphs": [
            "Fabric weight can flatter or overwhelm depending on the body underneath it. Bulky, dense fabric adds visual volume everywhere it sits, so it works beautifully on shoulders and shoulder-adjacent shaping but can feel heavy at the waist. Lighter fabrics—cotton blends, DK weight, or a linen-cotton mix—drape softly and move with the body.",
            "For plus sizes, cotton and cotton blends often feel most comfortable because they breathe and skim rather than cling. Choose a hook one half-size larger than the label suggests if you naturally crochet tight; a slightly looser fabric drapes better on curves. Our full breakdown of fibers and weights lives inside [[best-yarn-for-crochet|our yarn buyer's guide]], and it is worth reading before you buy ten skeins of anything for a wearable project.",
        ],
    },
    {
        "id": "finishing",
        "heading": "Final fitting and finishing touches",
        "paragraphs": [
            "Blocking is not optional for garments. Wet block your finished top on a flat surface, gently coax it to your target measurements, and let it dry completely. Blocking evens out tension, opens stitch definition, and often adds up to an inch across the bust—so measure again after blocking before you decide anything is wrong.",
            "Once dry, try the top on with the outfit you plan to wear it with, and look in a full-length mirror. Adjust the neckline border tightness if it gapes, and add a decorative row at the hem if the length still needs a touch more. Small finishing choices—matched buttons, a folded-hem cuff, or a thin ribbon at the neck—turn a home-made top into something you will actually reach for on a Tuesday morning.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "A crochet top made to fit your body is not a special request. It is the whole point of making things by hand. The next time a pattern feels like it was written for someone else, remember these adjustments and rewrite it for you. Save this guide, keep your measurements in your project notebook, and let your next make be the one that makes you feel seen in your own closet.",
        ],
    },
]


def _short(slug, title, category, excerpt, image_key, read_time):
    return {
        "slug": slug,
        "title": title,
        "category": category,
        "excerpt": excerpt,
        "image": IMAGES[image_key],
        "read_time": read_time,
        "date": "June 12, 2026",
        "sections": CATEGORY_PARAGRAPHS[category],
        "body": None,
    }


ARTICLES_SEED = [
    _short("crochet-for-absolute-beginners", "Crochet for Absolute Beginners: The Only Guide You'll Ever Need", "Beginners", "A calm, confidence-building first step into hooks, yarn, and your very first row.", "yarn", "8 min read"),
    _short("common-crochet-mistakes", "10 Common Crochet Mistakes (and How to Fix Them Fast)", "Beginners", "The little fixes that make your stitches neater, your edges straighter, and practice more fun.", "blanket", "7 min read"),
    _short("even-crochet-stitches", "The Secret to Perfectly Even Stitches Every Single Time", "Stitch School", "A practical rhythm for consistent tension, tidy edges, and fabric you actually love.", "yarn", "6 min read"),
    _short("read-crochet-pattern", "How to Read a Crochet Pattern Like a Pro (Step-by-Step)", "Beginners", "Decode abbreviations, repeats, and charts without losing your place.", "blanket", "8 min read"),
    _short("best-yarn-for-crochet", "Best Yarn for Every Type of Crochet Project (Buyer's Guide)", "Yarn Guide", "Choose fibers and weights with confidence, from soft blankets to sturdy bags.", "yarn", "9 min read"),
    _short("amigurumi-101", "Amigurumi 101: Cute Crochet Animals for Beginners", "Amigurumi", "Start with friendly shapes, simple stuffing, and the details that bring tiny animals to life.", "amigurumi", "8 min read"),
    _short("crochet-hacks", "5 Crochet Hacks That Will Save You Hours of Frustration", "Crochet Life", "Five small studio habits that rescue time, yarn, and your patience.", "yarn", "5 min read"),
    _short("fix-dropped-stitch", "How to Fix a Dropped Stitch or Mistake Without Starting Over", "Stitch School", "Repair your work with a hook, a calm breath, and a simple visual check.", "blanket", "7 min read"),
    _short("crochet-blanket-patterns", "Crochet Blanket Patterns: Cozy Projects for Every Skill Level", "Patterns", "Find the right blanket rhythm for a weekend, a season, or a lifetime keepsake.", "blanket", "9 min read"),
    _short("sell-crochet-online", "From Hobby to Side Hustle: How to Sell Your Crochet Creations Online", "Crochet Life", "A grounded starter plan for pricing, photographing, and sharing handmade work.", "amigurumi", "10 min read"),
    {
        "slug": "crochet-tops-for-every-body",
        "title": "Crochet Tops for Every Body: How to Adapt Patterns for Plus Sizes and Diverse Body Types",
        "category": "Clothing",
        "excerpt": "Practical adjustments—measurements, gauge, width, shaping, and yarn choices—that make a crochet top actually fit your body.",
        "image": IMAGES["tops"],
        "read_time": "9 min read",
        "date": "February 4, 2026",
        "sections": None,
        "body": PLUS_SIZE_BODY,
    },
]

CATEGORIES = ["All", "Beginners", "Stitch School", "Amigurumi", "Yarn Guide", "Patterns", "Clothing", "Crochet Life"]
