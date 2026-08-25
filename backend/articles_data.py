"""Seed data for the Cozy Loop Crochet articles collection.

This module is the single source of truth for the article content that is
loaded into MongoDB on first boot. Adding or editing articles here (and
then clearing the ``articles`` collection) is the recommended way to
publish new content without touching the frontend bundle.
"""

IMAGES = {
    # Verified crochet-relevant stock photos from Pexels/Unsplash crochet collections.
    # Each article gets a unique image matched to its topic for the AdSense
    # quality-signals fix (Feb 2026).
    "yarn": "https://images.pexels.com/photos/35155839/pexels-photo-35155839.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "blanket": "https://images.pexels.com/photos/5806996/pexels-photo-5806996.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "amigurumi": "https://images.pexels.com/photos/38972275/pexels-photo-38972275.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "tops": "https://images.pexels.com/photos/5035233/pexels-photo-5035233.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "denim": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=1200&q=80",
    "beginner_hook": "https://images.pexels.com/photos/7585569/pexels-photo-7585569.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "mistakes": "https://images.pexels.com/photos/7585570/pexels-photo-7585570.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "even_stitches": "https://images.pexels.com/photos/29889874/pexels-photo-29889874.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "pattern_read": "https://images.pexels.com/photos/7585792/pexels-photo-7585792.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "yarn_variety": "https://images.pexels.com/photos/35155839/pexels-photo-35155839.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "amigurumi_alt": "https://images.pexels.com/photos/38699405/pexels-photo-38699405.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "hacks_studio": "https://images.pexels.com/photos/4792062/pexels-photo-4792062.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "dropped_stitch": "https://images.pexels.com/photos/36238478/pexels-photo-36238478.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "blanket_stack": "https://images.pexels.com/photos/5806996/pexels-photo-5806996.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "sell_business": "https://images.pexels.com/photos/38745727/pexels-photo-38745727.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "placemat_home": "https://images.pexels.com/photos/36644650/pexels-photo-36644650.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "micro_jewelry": "https://images.pexels.com/photos/7585583/pexels-photo-7585583.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "lamp_cozy": "https://images.pexels.com/photos/29889872/pexels-photo-29889872.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "knot_bag": "https://images.pexels.com/photos/7585259/pexels-photo-7585259.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "granny_fashion": "https://images.pexels.com/photos/18971489/pexels-photo-18971489.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "tissue_home": "https://images.pexels.com/photos/18971494/pexels-photo-18971494.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "denim_flowers": "https://images.pexels.com/photos/18971492/pexels-photo-18971492.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "scrap_yarn": "https://images.pexels.com/photos/3693232/pexels-photo-3693232.jpeg?auto=compress&cs=tinysrgb&w=1200",
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


SCRAP_YARN_BODY = [
    {
        "id": "why-plan",
        "heading": "Why scrap yarn deserves a plan",
        "paragraphs": [
            "Every crocheter builds a quiet collection of leftovers: half a skein from a scarf, three yards of a favorite blue, a fistful of bright oranges that never quite fit a project. Those scraps are more valuable than they look. They are already paid for, already tested, already loved. Yet they tend to migrate to a bag, then a bin, then a closet corner where they slowly go from \"future magic\" to \"guilt pile.\"",
            "The trick is not saving less—it is having a clear plan for what your scraps become. A little intention turns leftover yarn from clutter into a rotating library of small, satisfying makes. In this guide you will find twelve ways to use scrap yarn on purpose, plus the color and storage tricks that make everything look intentional. Whether you have two feet of chunky wool or a rainbow tangle of cotton, there is a project here you can start today and finish before the week is out.",
        ],
    },
    {
        "id": "sort",
        "heading": "Sort before you save",
        "paragraphs": [
            "Before you decide what to make, spend twenty minutes sorting. Group scraps by weight first (lace, sport, DK, worsted, bulky) and then loosely by color family. Anything shorter than an arm's length gets set aside as a \"stuffing scrap\"—perfect for filling amigurumi. Anything longer than a yard becomes a \"project scrap.\"",
            "Ball each scrap into a mini cake or wind it into a tidy pull-skein so it does not tangle on the shelf. Store weight groups in clear jars, bins, or zip pouches so choosing yarn later takes seconds, not minutes. A quick label with the yarn's name and hook suggestion saves future-you from a mystery. This one afternoon of sorting is what makes every scrap project feel effortless afterward.",
        ],
    },
    {
        "id": "fast-useful",
        "heading": "Fast, useful scraps (Ideas 1–3)",
        "paragraphs": [
            "The best entry point is a project that finishes in one sitting. Coasters are the classic answer: a magic circle, three rounds of double crochet, and a color change on the final round gives you a set of four in under an hour. Use cotton scraps because they hold shape and wash beautifully.",
            "Next, try yarn scrunchies—wrap a scrap around a fabric elastic with tight single crochets and you have a hair tie that survives ponytail after ponytail. Cotton and cotton-blend scraps work best here too. Finally, dishcloths turn tiny amounts of cotton into something you will use every day. A basic eight-by-eight-inch square in half double crochet uses about forty yards, and stripes make it easy to combine two or three different colors from your scrap jar.",
            "All three ideas photograph beautifully for gifting, and they teach you exactly how a color pairing behaves before you commit to a bigger blanket.",
        ],
    },
    {
        "id": "cute-companions",
        "heading": "Cute companions (Ideas 4–6)",
        "paragraphs": [
            "Small, sculpted pieces are where scraps really shine. Try tiny amigurumi—a two-inch mushroom, a palm-sized bumblebee, or a stubby carrot with a leafy top can be finished with less than fifty yards of worsted. If you are new to tiny animals, start with a simple shape and a clear pattern from [[amigurumi-101|our amigurumi 101 guide]] before free-styling.",
            "Next, make keychain critters or bag charms: a stitched loop plus a swivel clip turns any tiny amigurumi into a functional accessory. Kids adore them, and they are wonderful stocking-stuffer gifts. Finally, appliqués add character to plain clothes and hats. A small crocheted heart, star, or flower stitched onto a store-bought beanie makes it feel handmade without committing to an entire hat. Appliqués also make excellent hair clips when glued to a barrette base.",
            "Because these projects are so small, they let you experiment with color combinations you might avoid on a big piece—use the neon orange, the neon pink, the mystery variegated skein. The scale forgives everything.",
        ],
    },
    {
        "id": "small-useful",
        "heading": "Small useful objects (Ideas 7–9)",
        "paragraphs": [
            "Not every scrap project has to be decorative. Bookmarks work with lace-weight or sock-weight leftovers—a slim strip of filet crochet or a tiny amigurumi charm attached to a chain makes a thoughtful gift for a reader. Phone cozies and glasses cases are another quick win: a slip-stitched pouch sized to your device protects screens and uses roughly thirty to sixty yards of worsted.",
            "For plant lovers, a mini plant hanger built from four twisted lengths of chunkier scrap yarn holds a small pot beautifully in a sunny window and takes about an hour. If you sell your work, these three items are also among the most popular first-timer purchases at craft fairs because they are affordable, useful, and read as handmade at a glance.",
            "Match the yarn fiber to the job: cotton for anything that will be washed often, wool for warmth, and acrylic for items headed to a busy household.",
        ],
    },
    {
        "id": "big-projects",
        "heading": "Big projects from tiny bits (Ideas 10–12)",
        "paragraphs": [
            "Some of the most sentimental crochet projects come from months of collected scraps. A \"magic ball\" is a single continuous strand made by knotting or splicing your scraps together in random order. Wind it into one ball and use it as a single yarn for a scarf, hat, or blanket. The result looks like intentional stripes without any pattern reading.",
            "A patchwork blanket uses the same idea in reverse: crochet dozens of small granny squares from your scraps, then join them once you have enough for a lap-sized throw. Because each square is small, this project fits neatly into evenings and weekends over the course of a season.",
            "Finally, a memory blanket honors leftovers from meaningful projects—the yarn from your child's first hat, your grandmother's afghan, your favorite sweater. Working these into one blanket turns individual scraps into a heirloom you will keep forever. All three projects reward patience, and none of them require buying anything new.",
        ],
    },
    {
        "id": "intentional",
        "heading": "Making scraps look intentional",
        "paragraphs": [
            "The difference between \"scrap chic\" and \"scrap chaos\" is usually color theory, not skill. Group scraps into a palette before you begin. Choose three to five colors that share either a temperature (all warm, all cool) or a value (all pastel, all saturated). Add one contrasting accent for interest.",
            "If you struggle with color picking, photograph your scraps in daylight and use a phone filter to convert to grayscale—colors with similar grayscale values look harmonious together. Repetition also helps: use each color at least three times so nothing looks accidental. When you are ready, try one of the small studio habits from [[crochet-hacks|our crochet hacks guide]] to keep color changes tidy on the wrong side of your fabric.",
        ],
    },
    {
        "id": "storing",
        "heading": "Storing what you keep",
        "paragraphs": [
            "A scrap library only helps you if you can see what is in it. Clear glass jars, mason jars, and small acrylic bins let you shop your stash without dumping bags on the floor. Sort by weight first because that is the number that determines whether a scrap is usable for a given project.",
            "Add loose labels with fiber content if you remember it—cotton, wool, and acrylic behave very differently, and you will thank yourself later. If you buy new yarn often, [[best-yarn-for-crochet|our yarn buyer's guide]] can help you choose fibers that already play well with what is in your scrap jar.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Leftover yarn is not clutter, and it is not a mistake. It is a slow, growing record of every project you have finished and every color you have loved. Pick one idea from this list, pull a handful of scraps that make you smile, and give yourself a single evening to start. The finished object might be tiny, but it will be entirely yours—and that quiet satisfaction is the whole point of a hook in your hand.",
        ],
    },
]


MICRO_CROCHET_JEWELRY_BODY = [
    {
        "id": "intro",
        "heading": "Where fiber art meets fine jewelry",
        "paragraphs": [
            "Micro-crochet jewelry is where fiber art meets fine jewelry—and it happens to be one of the most satisfying rabbit holes a hook can lead you down. If you have ever admired a delicate pair of crochet lace earrings and wondered how anyone could possibly make something so small by hand, the honest answer is: with six-strand embroidery floss, a steel hook the size of a sewing needle, and a very quiet afternoon.",
            "This guide walks through everything I wish someone had told me the first time I tried micro-crochet jewelry—from separating embroidery floss down to the exact number of strands that hold their shape, to choosing an ultra-fine steel hook that will not fight your hands, to stiffening a finished piece so it hangs like an heirloom instead of a curl of thread. Ten years of embroidery floss crochet have taught me that the difference between messy and magical is almost always tension and blocking, and both are learnable in one weekend.",
        ],
    },
    {
        "id": "why-patience",
        "heading": "Why micro-crochet jewelry is worth the patience",
        "paragraphs": [
            "Working small requires slower hands, brighter light, and a willingness to redo a row when your tension drifts. In return, you get pieces that photograph beautifully, cost pennies in materials, and read as far more valuable than they are. A single skein of embroidery floss makes ten to fifteen pairs of earrings; a spool of DMC pearl cotton makes fifty. That kind of yield is impossible with any other fiber craft.",
            "Micro-crochet also travels well. A finished pair fits in a business-card holder. A work-in-progress fits in a coat pocket. If you sell at craft fairs, jewelry can be your entry-level price point—the ten- to twenty-dollar impulse buy that pays for the whole table before lunch.",
        ],
    },
    {
        "id": "supplies",
        "heading": "Your exact supply list",
        "paragraphs": [
            "Everything below is exactly what I keep in my micro-crochet kit. If a supply is missing, the project is harder than it needs to be; if you have all of them, you can start today.",
            "• Six-strand embroidery floss in one to three colors (DMC, Anchor, or CosmoLecien). One skein makes ten to fifteen pairs.",
            "• Ultra-fine steel crochet hook, size 0.6 mm (US 14) for beginners, or 0.4 mm (US 16) for advanced makers who want ultra-fine lace.",
            "• Fabric stiffener OR a homemade blocker of 50/50 white glue and water in a small dish.",
            "• Hypoallergenic ear wires (surgical stainless steel, sterling silver, or gold-fill). Fifty pairs cost about eight dollars online.",
            "• Small jump rings (3–4 mm).",
            "• Two pairs of jewelry pliers (chain-nose and flat-nose).",
            "• Tiny sharp scissors—embroidery snips work perfectly.",
            "• Straight pins and a piece of stiff foam or corkboard for blocking.",
            "• Optional but life-changing: a lighted magnifying visor if you are over forty or working in dim light.",
        ],
    },
    {
        "id": "floss",
        "heading": "Choosing embroidery floss and hook sizes",
        "paragraphs": [
            "Not all six-strand floss is equal. DMC, Anchor, and CosmoLecien are the standards for a reason—the fibers are combed evenly, colors are consistent across dye lots, and strands separate cleanly. Avoid unbranded bulk floss from craft-store multipacks; the fibers pill and colors sometimes bleed when you stiffen the finished piece.",
            "For heirloom-quality crochet lace earrings, work with three strands separated from the six-strand skein. Three strands is the sweet spot—enough body for the stitches to show, thin enough to work a 0.6 mm hook comfortably. Reserve two-strand work for advanced makers with 0.4 mm hooks.",
            "If you have never worked with anything finer than sport-weight yarn, spend an evening practicing basic stitches with three-strand floss on a 0.6 mm hook before you try a jewelry pattern. It builds the same muscle memory that [[crochet-for-absolute-beginners|our absolute beginners guide]] builds for standard yarn—just in miniature.",
        ],
    },
    {
        "id": "pattern",
        "heading": "The magic ring earring pattern (step-by-step)",
        "paragraphs": [
            "This pattern makes a pair of small lace medallions about three-quarters of an inch across—perfect for everyday wear. It uses only chain, single crochet, and double crochet. All abbreviations are US crochet terms.",
            "1. Start with a magic ring. Wrap the floss around your fingertip twice, insert the hook under both loops, and pull up a working loop. Chain 1 to secure. The magic ring gives you a closed, invisible center.",
            "2. Round 1: Work 8 single crochet (sc) into the ring. Pull the tail tight to close the center. Do not join yet—we work continuously.",
            "3. Round 2: Chain 3 (counts as first double crochet). Work 2 double crochet (dc) into the same stitch as the chain. Chain 1. Skip the next stitch. In the following stitch, work 3 dc, then chain 1. Repeat around: (3 dc, ch 1, skip 1) three more times. You will have four \"shells\" separated by chain-1 spaces. Slip stitch to the top of the beginning chain-3 to join.",
            "4. Round 3: Chain 5 (counts as first dc + chain 2). In the chain-1 space between shells, work 1 double crochet, chain 2. In the next chain-1 space, work 1 double crochet, chain 2. Repeat around: (dc in ch-sp, ch 2) three more times. Slip stitch to the third chain of the beginning chain-5 to close.",
            "5. Round 4 (picot border): Chain 1. In each chain-2 space around, work: 3 single crochet, chain 3, slip stitch to the top of the last sc (that's your picot), then 3 more single crochet. Slip stitch to the first sc to close.",
            "6. Fasten off. Cut the floss, leaving a six-inch tail. Weave the tail through three or four stitches on the wrong side using a fine tapestry or sharp sewing needle, then trim.",
            "7. Repeat the entire pattern for the second earring. Making two matching pieces in one sitting is the easiest way to keep tension consistent.",
        ],
    },
    {
        "id": "pro-tips",
        "heading": "Pro tips: tension, blocking, and stiffening",
        "paragraphs": [
            "Tension is the whole game in micro-crochet. Because the stitches are so small, any looseness reads as chaos. Hold the floss taut against your index finger; a relaxed grip on standard yarn becomes a firm grip on floss. If your stitches drift in size across a piece, revisit the fundamentals in [[even-crochet-stitches|our guide on perfectly even stitches]] and practice with two-inch swatches until your rhythm returns.",
            "Blocking: Pin the finished piece to a corkboard or foam block using straight pins, gently stretching each picot into a rounded point. Spritz with water until saturated. Let it dry completely—twelve hours minimum. Blocking transforms an okay-looking medallion into something that reads as intentional.",
            "Stiffening: For jewelry that keeps its shape through years of wear, brush the blocked piece with commercial fabric stiffener or a homemade 50/50 mix of white glue and water. Let it dry pinned to the block for another twelve hours. The finished piece will hold its shape like a tiny sculpture. Reapply every year or so if the piece softens with heavy wear.",
            "This same slow-then-fast studio habit is what separates casual makers from professionals—see the small workflow tricks in [[crochet-hacks|our crochet hacks guide]] for more time-saving habits at the table.",
        ],
    },
    {
        "id": "attach",
        "heading": "Attaching to hypoallergenic ear wires",
        "paragraphs": [
            "Once your medallion is stiffened and dry, attach a small jump ring through the top picot. Open the jump ring by twisting sideways (never pulling straight apart), thread it through the top picot, then through the loop of a hypoallergenic ear wire, and twist closed. Repeat for the second earring.",
            "If you plan to sell your work, invest in surgical stainless steel or sterling silver wires—the small price difference prevents allergic reactions and keeps your reviews at five stars.",
        ],
    },
    {
        "id": "care",
        "heading": "Care and heirloom keeping",
        "paragraphs": [
            "Micro-crochet earrings are delicate but not fragile. Store them flat in a small compartmented jewelry box, or hang them on a fabric-covered card. Avoid direct contact with perfume and body lotion—oils slowly dissolve the stiffener. To clean, brush gently with a soft dry paintbrush.",
            "If a piece loses shape after months of wear, re-block and re-stiffen in about twenty minutes. With basic care, a pair of well-made micro-crochet earrings will still look intentional a decade from now—which is exactly the definition of an heirloom.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "A pair of micro-crochet jewelry pieces is one of the most rewarding weekend projects in the entire fiber-art world. The techniques are simple; the payoff is disproportionate. Start with one pair. Wear them for a week. Notice how often someone asks where they came from. Then pick a friend, choose a color that matches her wardrobe, and make her a pair too. The best gifts weigh almost nothing.",
        ],
    },
]


PLACEMAT_BODY = [
    {
        "id": "why-placemat",
        "heading": "Why this placemat is the perfect quick project",
        "paragraphs": [
            "Not every finished project takes weeks. A round crochet placemat—the kind that sits under a plate at a quiet dinner or a busy holiday table—comes off the hook in under two hours, uses stitches every beginner already knows, and instantly makes a meal feel a little more considered.",
            "Placemats are also one of the most forgiving first patterns because they hide small tension inconsistencies inside the natural texture of double crochet. If your circle warps a bit, blocking fixes it. If your count is off by one, no one at the table will notice. That kind of low-stakes practice is exactly what builds confidence.",
            "This guide walks through the exact pattern I use when I want a table full of matching placemats before dinner—materials, hook size, round-by-round instructions, a simple scalloped edge, and the two mistakes to look out for. If you have never worked in the round before, spend five minutes with [[crochet-for-absolute-beginners|our absolute beginners guide]] first, then come back here.",
        ],
    },
    {
        "id": "materials",
        "heading": "What you'll need",
        "paragraphs": [
            "You do not need a specialty store to start. The materials for one placemat are simple and affordable.",
            "Yarn: worsted-weight cotton or fine macramé cotton cord, about 100 to 120 yards per placemat. Look for skeins labeled \"worsted cotton\" or \"4/4 cotton.\" Cotton holds shape at the table, washes cleanly, and takes color beautifully.",
            "Hook: a 3.5 mm (US E-4) hook for a firm, structured mat, or a 4.0 mm (US G-6) hook for a softer drape. If your yarn label suggests a different size, follow the label.",
            "Notions: sharp scissors and a tapestry needle for weaving in ends. Optional but helpful: one stitch marker (or a scrap of contrast yarn) to keep track of the first stitch in each round.",
        ],
    },
    {
        "id": "yarn-choice",
        "heading": "A note on yarn and hook choice",
        "paragraphs": [
            "If you are new to placemats, choose a light, solid color first—cream, natural, pale yellow, or dove gray. Light shades make it far easier to see individual stitches and count them correctly. Variegated or dark yarns look beautiful but hide stitch definition, which turns counting into a guessing game on your first project.",
            "Cotton is non-negotiable for anything that touches food. It resists heat, does not pill under a plate, and machine-washes without shrinking to strange proportions. Acrylic can melt near a hot pan. Wool felts in the wash. Cotton is the honest friend here. If you want a deeper dive into fibers, weights, and washability, our [[best-yarn-for-crochet|complete yarn buyer's guide]] breaks down every trade-off before you spend a dollar.",
        ],
    },
    {
        "id": "abbreviations",
        "heading": "US crochet abbreviations used in this pattern",
        "paragraphs": [
            "This pattern uses standard US crochet terms. Here are the four you'll need to know before we start.",
            "ch — chain. dc — double crochet. sl st — slip stitch (closes each round). sc — single crochet (used only in the border). inc — increase, which means two double crochets worked into the same stitch.",
            "We work in joined rounds. Every round begins with a chain-3 (which counts as your first dc) and ends by joining with a slip stitch into the top of that chain-3. If you remember only one rule from this pattern, remember that the ch-3 counts as a stitch—not as a filler chain—so you will only work eleven additional dc in round one, twenty-three in round two, and so on.",
        ],
    },
    {
        "id": "pattern",
        "heading": "The pattern, round by round",
        "paragraphs": [
            "Round 1: Make a magic ring (or ch 4 and join with a sl st into the first chain to form a small loop). Ch 3—this counts as your first dc. Work 11 dc into the ring. Sl st to the top of the ch-3 to close. Total: 12 stitches.",
            "Round 2 (all increases): Ch 3. Work 1 dc in the same base stitch—that's your first increase. Then work an inc (2 dc) into every dc around. Sl st to close. Total: 24 stitches.",
            "Round 3: Ch 3. In the next stitch, work an inc. Continue in the pattern of one dc followed by one inc all the way around. Sl st to close. Total: 36 stitches.",
            "Round 4: Ch 3, 1 dc in the next stitch. In the third stitch, work an inc. Continue with two dc followed by one inc around. Sl st to close. Total: 48 stitches.",
            "Round 5: Continue the widening pattern—three dc followed by one inc, repeated around. Sl st to close. Total: 60 stitches.",
            "Round 6: Four dc, one inc, repeated around. Sl st to close. Total: 72 stitches.",
            "Round 7: Five dc, one inc, repeated around. Sl st to close. Total: 84 stitches.",
            "If your circle stays flat, keep going. If it starts to ruffle or curl at the edges, pause here. Every crocheter's tension is a little different, and your placemat may be finished at 72 or 84 stitches. The number that matters is whether the fabric lies flat when you set it down on the table.",
        ],
    },
    {
        "id": "edging",
        "heading": "The simple shell edging",
        "paragraphs": [
            "A small shell border turns a plain circle into something guest-ready in about fifteen minutes.",
            "Border round: Ch 1, sc in the same stitch. Skip 1 stitch. In the next stitch, work 5 dc (this forms one shell). Skip 1 stitch. Sc in the next stitch. Continue the pattern of skip one, five dc in next, skip one, sc in next, all the way around. Sl st to the first sc to close. Cut the yarn, leaving a six-inch tail, and pull it through the last loop.",
            "Weave in every tail with the tapestry needle by running it through at least four stitches in one direction and reversing back through two more. That's the whole thing—one placemat in under two hours.",
        ],
    },
    {
        "id": "care",
        "heading": "Blocking, care, and gifting ideas",
        "paragraphs": [
            "Even if your circle looks slightly waved, a gentle blocking makes it lie perfectly flat. Wet the finished mat, gently press out the excess water in a clean towel, and pin it flat on a foam mat or clean carpet to dry overnight. Cotton takes to blocking beautifully—one round of blocking is often the entire difference between \"handmade\" and \"professional.\"",
            "For everyday care, machine wash on cold and lay flat to dry. Skip the dryer for the first three washes to help the shape settle in. A set of four matching placemats in a warm neutral makes a thoughtful housewarming gift; a set in a friend's wedding colors is unforgettable at a bridal shower.",
            "For consistent stitch height across all four mats, revisit the tension tips in [[even-crochet-stitches|our guide on perfectly even stitches]] before starting the second one—your future self will thank you.",
        ],
    },
    {
        "id": "mistakes",
        "heading": "Common mistakes and how to fix them",
        "paragraphs": [
            "Almost every beginner makes one of two mistakes on a round placemat. The first is skipping the ch-3 join at the end of a round—this creates a small hole where the round closes. The second is forgetting that the ch-3 counts as a dc, which throws off every increase count that follows.",
            "If your circle starts to warp into a bowl shape, you have too few increases; add one extra inc every few stitches on the next round to open the fabric. If the edge ruffles or waves, you have too many increases; stop increasing and work one straight round of dc to redistribute the fabric before continuing.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "A round placemat is the perfect gateway project—enough structure to feel finished, enough simplicity to enjoy the process. Make one this weekend. Make a matching set the weekend after. And when you are ready to try something a little more sculptural, our journal has small animal tutorials, blanket patterns, and clothing adjustments waiting for your hook.",
        ],
    },
]


DENIM_UPCYCLE_BODY = [
    {
        "id": "why-upcycle",
        "heading": "Why upcycle denim with crochet",
        "paragraphs": [
            "There is a growing gap between how quickly clothing lands in landfills and how slowly it degrades. A pair of jeans takes decades to break down, and the average American throws away roughly seventy pounds of textiles every year. Meanwhile, thrift stores overflow with sturdy, honest denim that just needs a little imagination.",
            "Crochet is one of the most forgiving crafts for rescuing worn clothes because it does not require pattern-perfect precision. A hook, a length of yarn, and a bit of intuition can turn a stiff, forgotten jean jacket into something you actually reach for. Freeform crochet edges add texture, softness, and personality to fabric that otherwise reads as flat and rigid.",
            "Better still, working with what already exists costs less than buying yarn for a full sweater, and every finished piece is genuinely one of a kind. This guide walks through sourcing, prepping, and adding freeform edges to thrifted denim—plus the care instructions that keep your work looking beautiful long after the first wash.",
        ],
    },
    {
        "id": "source",
        "heading": "Sourcing the right thrifted denim",
        "paragraphs": [
            "Not every jean jacket at Goodwill is worth the effort. Read the label first: aim for at least ninety-eight percent cotton with less than two percent elastane. Fabrics with high polyester content pill quickly, resist dye, and do not accept stitches cleanly. Feel the weight next—heavier denim (twelve ounces or more) holds a crochet border without sagging over time.",
            "Look at the seams carefully. A jacket with reinforced double stitching will survive the extra tension your crochet edge adds. Check zippers, buttons, and pockets; you want a garment that functions well even before your improvements. Finally, sit with the color. Faded indigo pairs beautifully with almost any yarn shade, while crisp raw denim looks stunning against pastels and cream tones. Choose one intentional focal point—a collar, a cuff, or a hemline—before you commit. Deciding where the crochet will live saves hours of second-guessing at the table.",
        ],
    },
    {
        "id": "yarn",
        "heading": "Choosing yarn that survives denim's daily life",
        "paragraphs": [
            "Denim is heavier and rougher than most crocheted fabric, so match the yarn to the job. Sport-weight or DK-weight mercerized cotton is the sweet spot: strong enough to hold shape, soft enough not to scratch, and machine-washable with the garment. Avoid anything wool-heavy—it will felt over time when washed with cotton denim.",
            "Acrylic works if you want vivid color and low cost, but expect a slightly less refined finish. If you want a linen texture that ages with the jacket, look for cotton-linen blends. Choose colors that either echo something already in the garment (a wash tone, a stitching color) or contrast intentionally—cream against dark indigo, for example, makes the border pop.",
            "As a rough estimate, buy about forty yards for a cuff edge, one hundred yards for a full collar, and a full skein for a jean hem. Our full breakdown of fibers, weights, and washability lives in [[best-yarn-for-crochet|our yarn buyer's guide]] if you want to dig deeper before spending.",
        ],
    },
    {
        "id": "prep",
        "heading": "Prepare the garment before you touch a hook",
        "paragraphs": [
            "Wash the thrifted piece twice before you begin. Thrifted denim often carries residual detergent, dye, or fragrance that shifts after a single home wash, and waiting a second cycle prevents color surprises later. Let it dry fully, then iron every seam flat and snip any loose threads with sharp scissors.",
            "Decide where your crochet edge will attach and mark the line with tailor's chalk. If you are adding a border to a raw edge (like a chopped hem), fold the raw edge under half an inch and topstitch with a sewing machine to prevent fraying under crochet tension. For attaching along an existing seam—say, a jacket cuff—you will pierce through denim with a large-eye tapestry needle, no pre-holes required. Test tension on a scrap of the same denim before you commit. Wristband denim behaves very differently from stiff yoke denim.",
        ],
    },
    {
        "id": "attach",
        "heading": "Attaching crochet to denim",
        "paragraphs": [
            "Two methods work reliably. Method A—single-crochet foundation row—starts with an embroidery needle pre-piercing evenly spaced holes (about every quarter inch) along your chalk line. Skip the pre-piercing if your denim is soft enough for a size G or H hook to pass through directly. Insert your hook through each hole, pull up a loop, and single crochet along the entire edge to establish a base. This foundation row is the anchor for everything that follows.",
            "Method B—blanket-stitch foundation—is better for thicker or older denim. Hand-sew a blanket stitch in matching thread first, then work your first crochet row into each blanket stitch loop rather than through the denim itself. This method is gentler on delicate garments and gives you a cleaner attachment.",
            "Whichever method you choose, keep your tension consistent. Pulled tight, the crochet warps the denim; too loose, and the edge gapes. Consistency is the whole game, and the same principles from [[even-crochet-stitches|perfectly even stitches]] apply here too.",
        ],
    },
    {
        "id": "freeform",
        "heading": "Freeform crochet—no pattern needed",
        "paragraphs": [
            "Once your foundation row is done, the fun part begins. Freeform means no pattern, no counted repeats, no gauge stress—just improvised stitches that respond to the shape you are decorating. Combine chain spaces with shell stitches. Add a picot every three stitches. Work three double crochets into one stitch to create a scallop. Vary the height of stitches within a single row so the edge grows organically instead of in a rigid line.",
            "If you get stuck, alternate between one row of single crochet and one row of half doubles until inspiration returns. The beauty of freeform is that mistakes quickly become design choices—a taller stitch here, a cluster there, and suddenly you have a signature detail.",
            "Take photos of your progress every ten minutes so you can retrace your steps if a section goes sideways. Working in short bursts also lets you see how the border sits on the garment as it grows, which is impossible to picture from a flat swatch alone.",
        ],
    },
    {
        "id": "design",
        "heading": "Design ideas by garment type",
        "paragraphs": [
            "For a jacket collar, a wide shell-stitch panel in cream cotton transforms a classic denim jacket into something that reads bespoke. Work outward from the neckline for three to five inches, then finish with a picot row.",
            "For jacket cuffs, small ruffled cuffs in a contrast color are the fastest upcycle possible—under two hours per cuff. For jean hems, fold the hem inward twice, crochet a soft one-inch scalloped border in colored cotton, and let it peek out from under a fold. For front pockets, trace the pocket opening and add a slim quarter-inch crochet edge in metallic thread for evening styling.",
            "For advanced makers, work a freeform crochet panel that sits below the collar and above the chest, echoing the shape of a Victorian yoke. These are starting points, not rules. The most memorable upcycles usually mix two techniques—a subtle pocket edge with a bold hem, or matched cuff and collar in the same yarn. If sizing is a concern (denim runs strict), the fit adjustments in [[crochet-tops-for-every-body|our guide on crochet tops for every body]] translate directly to jacket alterations.",
        ],
    },
    {
        "id": "finishing",
        "heading": "Finishing and long-term care",
        "paragraphs": [
            "Weave in every yarn tail with a large tapestry needle, running the tail through at least four stitches in one direction and then reversing back through two more. This prevents the ends from working loose during washing.",
            "Machine wash your finished piece on cold, inside out, inside a mesh laundry bag to protect the crochet from snagging on zippers. Skip the dryer entirely for the first three washes—lay the garment flat to dry so the border sets into the shape you want. After the third wash, the yarn and denim have essentially learned each other, and normal drying is fine.",
            "Store the garment hanging when possible, and spot-clean rather than washing the whole piece if you can. A well-finished upcycled jacket will still look intentional five years from now—that is the whole point.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Upcycled fashion is not a compromise. It is a slower, kinder, more creative version of shopping—and crochet is the perfect tool for the job. Start with one small edge: a single cuff, a pocket outline, a hem detail. Wear it for a week. Notice how differently you feel about a garment you helped shape. Then find the next thrifted piece waiting for a hook and a length of yarn. The best wardrobe is the one you keep saving.",
        ],
    },
]


DENIM_FLOWERS_BANDANAS_BODY = [
    {
        "id": "intro",
        "heading": "Where boho crochet meets urban denim",
        "paragraphs": [
            "Ten years of working crochet into denim has taught me one thing above everything else: the small details are what people actually notice. A perfectly worked freeform edge is beautiful, but a single crochet flower stitched onto the back pocket of a favorite jean jacket is what makes strangers stop and ask where the piece came from. Details are what turn plain denim into something with a story.",
            "This guide is about those exact details—crochet flowers and small crochet bandanas added to jean jackets, jeans, denim skirts, and denim shirts. It is the middle ground between untouched denim and full freeform upcycling. If you want a project that finishes in one Saturday afternoon and immediately upgrades a piece you already own, this is the technique. Small motifs. Big visual payoff. Zero risk to your denim.",
            "The techniques below assume basic crochet knowledge (chain, single crochet, double crochet, magic ring) and a fondness for looking a little more interesting than everyone else on the sidewalk.",
        ],
    },
    {
        "id": "vs-upcycle",
        "heading": "How this differs from full denim upcycling",
        "paragraphs": [
            "In an earlier guide on [[upcycle-thrifted-denim-crochet|freeform crochet edges on thrifted denim]] we walked through building crochet borders directly into the fabric with a hook. That approach is dramatic, transformative, and requires a real commitment—you are working new fabric onto the garment permanently.",
            "This guide is different. We are not crocheting into the denim at all. We are making small standalone crochet pieces separately, then attaching them with a sewing needle and matching thread. That means the appliqués are removable if you change your mind, cheaper on yarn, and safer on delicate or vintage denim. You can add and remove flowers seasonally, swap a summer bandana for a fall flower on the same jacket, or transfer a favorite motif from a worn-out pair of jeans to a fresh pair.",
        ],
    },
    {
        "id": "flower",
        "heading": "The small crochet flower pattern",
        "paragraphs": [
            "This is the exact flower I have been sewing onto denim for a decade. It works up in about ten minutes, uses less than five yards of yarn per flower, and holds up to washing and daily wear. All abbreviations are US crochet terms: ch (chain), sc (single crochet), dc (double crochet), sl st (slip stitch).",
            "Center: Make a magic ring. Ch 3 (counts as first dc). Work 11 dc into the ring. Pull the ring tight. Sl st to the top of the ch-3 to close. Total: 12 dc around a firm center.",
            "Petal round: In the same stitch as the sl st, work: ch 2, 3 dc, ch 2, sl st into the same stitch. That is one petal. Skip the next stitch. Into the following stitch, sl st, then repeat: ch 2, 3 dc, ch 2, sl st. Continue around, skipping one stitch between each petal. You will get 6 petals evenly spaced around the center.",
            "Fasten off, leaving a six-inch tail for sewing to the garment. Weave a small amount of the tail through the back of the center to secure any loose stitches before you sew.",
            "For a two-color flower: work the center in one color, fasten off, then join a second color at any stitch to start the petal round. The color contrast at the center reads as intentional and photographs beautifully in natural light.",
            "For a smaller flower (perfect for a lapel or shirt pocket): work only 8 dc in the ring instead of 12, then work 4 petals in the second round.",
        ],
    },
    {
        "id": "bandana",
        "heading": "The small crochet bandana motif",
        "paragraphs": [
            "The bandana is a small triangular motif inspired by classic western bandanas and Persian handkerchief prints. It measures about three inches on each side—perfect for a back pocket accent, a belt loop dangle, or a tiny triangle sewn to the collar of a denim shirt.",
            "Row 1: Ch 4. Work 2 dc into the fourth chain from the hook. Ch 2, turn. This is your first row—a small pointed shape.",
            "Row 2: Skip the first ch-2. Work 2 dc in the next stitch, 1 dc in the ch-2 space, 2 dc in the top of the ch-3 from the previous row. Ch 2, turn. You are increasing by one stitch on each end.",
            "Rows 3–6: Continue the same increase pattern—2 dc in the first stitch, 1 dc in each middle stitch, 2 dc in the last stitch. Each row grows the triangle wider by two stitches.",
            "Row 7 (fringe row, optional): Work sc across the top edge. For each sc, cut a two-inch length of matching yarn, fold in half, and pull the loop through the sc, then pull the ends through the loop to create fringe. A row of tiny fringe along the top edge sells the bandana feel instantly.",
            "Fasten off with a long tail. A finished bandana takes about fifteen minutes.",
        ],
    },
    {
        "id": "placement",
        "heading": "Where flowers go, where bandanas go",
        "paragraphs": [
            "Placement is what separates \"crafty\" from \"designed.\" Flowers work best in clusters of three, placed asymmetrically. Try three small flowers running diagonally across the left front pocket of a jean jacket; a single larger flower on the outside of a jeans back pocket; two flowers stitched near the collar edge of a denim shirt.",
            "Bandanas prefer to hang. Sew a bandana motif to a jean-jacket belt loop by stitching only the top point, letting the rest dangle like a decorative kerchief. Or stitch one flat to the outside of a back pocket, points down, for a subtle Western-inspired accent. For a bolder statement, sew a small bandana to the shoulder seam of a denim jacket where a military patch would traditionally go.",
            "Both motifs read stronger when placed off-center rather than centered. Symmetry looks costume-y; asymmetry looks intentional.",
        ],
    },
    {
        "id": "sewing",
        "heading": "Sewing to denim without damaging the fabric",
        "paragraphs": [
            "Use a sharp hand-sewing needle (a size 8 or 9 works well) and matching all-purpose thread. Do not use tapestry needles here—they leave large holes in denim that never fully close.",
            "Position the appliqué exactly where you want it. Pin in place with two straight pins to prevent shifting. Working from the wrong side of the denim, take small stitches around the outer edge of the appliqué, catching only the backing yarn of the crochet piece and just a shallow bite of the denim fabric. Deep stitches leave permanent holes; shallow stitches disappear.",
            "For flowers, stitch only around the center circle and let the petals sit freely. This keeps the petals soft and dimensional. For bandanas, stitch across the top edge only, leaving the bottom points free to move slightly. Consistent, tiny stitches are what makes this look professional—if your hand-sewing rhythm drifts, borrow the tension principles from [[even-crochet-stitches|our guide on perfectly even stitches]]; the same rules apply to sewing.",
        ],
    },
    {
        "id": "care",
        "heading": "Care after adding crochet details",
        "paragraphs": [
            "Wash the finished garment inside out on cold in a mesh laundry bag. The mesh bag protects the appliqués from snagging on the washer drum, zippers, or other clothing. Skip the dryer for the first three washes so the crochet fibers relax into the denim naturally.",
            "If a flower comes loose after months of wear, resewing takes about two minutes with the same needle and thread you used the first time. Small crochet scraps left over from these projects are perfect for tiny appliqué work—if you have a collection building up, our [[scrap-yarn-projects|leftover yarn ideas guide]] has more small projects that use exactly this kind of remnant.",
        ],
    },
    {
        "id": "styling",
        "heading": "Design stories by outfit style",
        "paragraphs": [
            "For a boho-leaning look, cluster three cream flowers across the front yoke of a denim shirt worn tucked into a flowy midi skirt. For an urban streetwear feel, add a single bold-colored flower (neon coral or bright saffron) to the shoulder of a plain black-denim jacket over a white tee. For a Western-inspired look, sew a small bandana with fringe to the belt loop of high-waisted jeans and wear with a plain white blouse.",
            "For evening, upgrade the flowers with a metallic thread center—work the center round in gold cotton, then complete the petals in your regular color. The metallic accent catches light beautifully under restaurant lighting.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "The best handmade details are the ones that make a familiar piece feel new. A small crochet flower on a jean jacket does that; a tiny bandana dangling from a belt loop does that; both together on the right outfit make the piece unmistakably yours. Start with one flower on a favorite jacket. Add a bandana next weekend. Six months from now you will have a denim wardrobe that reads as personal, layered, and quietly designed—and every piece will have taken less than an evening of work.",
        ],
    },
]


TISSUE_BOX_COVER_BODY = [
    {
        "id": "intro",
        "heading": "A small object that quietly upgrades a room",
        "paragraphs": [
            "A cardboard tissue box is one of those objects nobody plans for in their decor. It sits on the coffee table in a hallway of gray plastic wrap, on the kitchen counter in mint green, on the nightstand in a wildly patterned floral that clashes with everything else. A crochet tissue box cover fixes all of that in one afternoon. Better still, a well-designed cover fits any standard box because you can pop the old empty one out and slip a fresh full one in without dismantling anything.",
            "This guide walks through a beginner-friendly crochet tissue box cover pattern with side buttons instead of sewn seams. The buttons are the whole point: they let you unbutton one side, drop a new tissue box in, and re-button in about twenty seconds. No struggling to shove a fresh box through a fixed opening. No unpicking a seam every three weeks. Just a small, tidy accessory that behaves like real furniture across all 365 days of the year.",
        ],
    },
    {
        "id": "why-buttons",
        "heading": "Why side buttons beat sewn seams",
        "paragraphs": [
            "Most crochet tissue box covers online use fully sewn side seams. They look tidy on day one and become a small daily annoyance the moment the first box runs out. The whole cover has to be lifted off, sometimes turned inside out, and wrestled back over the new box. Cotton stretches during that struggle, buttons of imagination pop, and after a few refills the whole cover looks tired.",
            "A buttoned side is designed for real houses. Ten to twelve small buttons run along one seam. To refill, unbutton, slide the empty box out, drop the new box in, and re-button. It takes twenty seconds, it never stretches the fabric, and it turns into a small satisfying ritual instead of a chore. The buttons themselves become a design feature—a row of wooden or fabric-covered buttons in a coordinating color reads as intentional trim rather than construction.",
        ],
    },
    {
        "id": "materials",
        "heading": "Materials and sizing",
        "paragraphs": [
            "This pattern fits a standard US cube tissue box measuring roughly 5 by 5 by 5 inches (the classic Kleenex Cube size). A rectangular version follows in a later section.",
            "You will need worsted-weight cotton yarn, about 120 yards. Cotton is the right choice because it does not stretch out of shape on an object that is picked up ten times a day. Wool is soft but pills quickly on a well-used surface. Acrylic works if you want vivid colors on a budget, but expect a less refined finish over time.",
            "You will also need a 4.0 mm (US G-6) crochet hook, a tapestry needle, sharp scissors, ten to twelve small buttons (about half an inch across), matching sewing thread, and a small hand-sewing needle for attaching buttons. If you are unsure which cotton to buy, our [[best-yarn-for-crochet|yarn buyer's guide]] compares brands, blends, and washability for home decor projects like this one.",
        ],
    },
    {
        "id": "buttons",
        "heading": "Choosing buttons that hold up to daily use",
        "paragraphs": [
            "The button choice quietly determines whether the cover reads as \"crafty\" or \"designed.\" Skip plastic buttons—they scratch, they clash with cotton, and they age poorly. Wooden buttons are the classic honest choice: they feel warm to the touch, come in dozens of natural tones, and are inexpensive at any craft store.",
            "For a slightly elevated look, use fabric-covered buttons in a color that echoes the cotton, or vintage mother-of-pearl buttons in cream. Whatever you pick, buy fifteen buttons even if you only need ten—one will inevitably vanish under the couch during the sewing step. Choose a button size close to half an inch across; smaller than that becomes fiddly to fasten daily.",
        ],
    },
    {
        "id": "pattern",
        "heading": "The pattern, panel by panel",
        "paragraphs": [
            "This cover is worked in five flat panels—four sides and one top with a rectangular opening—then joined at three of the four side seams. The fourth seam becomes the buttoned side. All abbreviations are US crochet terms: ch (chain), sc (single crochet), hdc (half double crochet), dc (double crochet), sl st (slip stitch), st (stitch).",
            "Side panels (make 4): Ch 21. Row 1: hdc in the third chain from hook and in each chain across. Ch 2, turn. Total: 20 hdc.",
            "Rows 2–13: hdc in each stitch across. Ch 2, turn. This creates a 5-by-5-inch square panel with enough drape to sit cleanly against the box.",
            "Row 14 (top edge): sc in each stitch across to firm the top edge. Fasten off, weave in ends.",
            "Top panel with opening: Ch 21. Rows 1–4: hdc in each st, ch 2, turn. Row 5: hdc in the first 6 sts, ch 8, skip 8 sts, hdc in the last 6 sts (this creates the tissue opening). Rows 6–9: hdc in each st and each chain across. Row 10: sc in each st across.",
            "Alternatively, work all 13 rows of hdc, then cut a rectangular opening in the center with sharp scissors and single-crochet around the raw edge to finish it. The scissor method is faster but requires care—cotton frays quickly.",
        ],
    },
    {
        "id": "joining",
        "heading": "Joining panels and building the buttoned edge",
        "paragraphs": [
            "Lay the four side panels in a row on a flat surface. Whip-stitch panels 1-2, 2-3, and 3-4 together along their vertical edges using matching yarn. Do not sew panel 4 to panel 1 yet—that is the buttoned side.",
            "Now attach the top panel. Whip-stitch its four edges to the top of each side panel, aligning the tissue opening with the center of the cover. Take care to keep the corners square as you sew; a wonky corner shows immediately on a rectangular object.",
            "For the buttoned edge, work one row of sc along the vertical edge of panel 4 for stability. On panel 1, work one row of sc along its matching vertical edge, but this time create buttonholes: sc for 3 stitches, ch 2, skip 2 sc, sc for 3 stitches, ch 2, skip 2, and continue evenly for 10 to 12 buttonholes total. Sew the buttons onto panel 4 at positions that line up with the buttonholes on panel 1.",
        ],
    },
    {
        "id": "rectangular",
        "heading": "Sizing for rectangular tissue boxes",
        "paragraphs": [
            "For a standard US rectangular tissue box (roughly 9 by 5 by 3 inches, the Kleenex Long size), scale the panels: two long panels at ch 37 and 8 rows tall, two short panels at ch 21 and 8 rows tall, and one top panel at ch 37 with a longer rectangular opening in the center.",
            "The buttoned side goes on one of the long panels for easier daily access. Use 14 to 16 buttons instead of 10 to 12 to keep the seam even along the longer edge. Everything else follows the exact same construction as the cube version.",
        ],
    },
    {
        "id": "variations",
        "heading": "Design variations by season and room",
        "paragraphs": [
            "For a spring bedroom, work the cover in soft sage green with cream wooden buttons. For a winter living room, use a warm oatmeal cotton with dark walnut buttons and add a single embroidered pine branch on one side. For a nursery, use a pale pink or yellow with matching fabric-covered buttons—babies chew on everything, so avoid small buttons here in favor of larger flat ones sewn extra securely.",
            "For a modern minimalist kitchen, work the cover in solid black with matte black buttons; the monochrome reads like a designer object. If you have a bag of coordinating cotton scraps, granny-stripe versions look wonderful and are a great way to use up the small remnants in our [[scrap-yarn-projects|leftover yarn ideas guide]].",
            "Consistent stitch height across all five panels is what makes the finished cover look boutique rather than homemade—revisit the fundamentals in [[even-crochet-stitches|our perfectly even stitches guide]] before starting if your tension tends to drift.",
        ],
    },
    {
        "id": "care",
        "heading": "Care and everyday use",
        "paragraphs": [
            "To refill, unbutton the side, tip the empty box out through the bottom, drop the new box in the same way, and re-button. Whole process: about twenty seconds. Hand-wash the cover every few months in cool water with mild soap and lay flat to dry. Skip the dryer—heat can shrink cotton and warp the button placement.",
            "A well-made buttoned tissue box cover will still look intentional five years from now, quietly upgrading whichever room it lives in through every season.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Small home accessories are how a room stops feeling generic and starts feeling like yours. A buttoned tissue box cover is one of the fastest, most rewarding examples—two hours of work, four dollars of materials, and a small object you interact with every day that is now unmistakably handmade. Start with one in your favorite everyday color. Make a second in a seasonal palette. And when a friend admires yours, make her one too—it is the small handmade gift that never goes unused.",
        ],
    },
]


GRANNY_SQUARE_FASHION_BODY = [
    {
        "id": "intro",
        "heading": "The granny square, all grown up",
        "paragraphs": [
            "The granny square has spent decades tucked into afghans and pot holders, but the last few years have quietly transformed it into one of the most exciting shapes in modern crochet fashion. A granny square skirt or vest built from asymmetric, boldly colored motifs reads as contemporary streetwear on the runway and as thrift-store cool on the sidewalk. The stitch is a hundred years old. The styling is completely new.",
            "This guide walks through the design decisions that turn a traditional granny square into a wearable, editorial-looking garment: choosing a scale of square, planning an asymmetric layout, mixing colors like a designer instead of a beginner, and joining panels so the finished piece drapes on a real body. Whether you want a knee-length skirt for spring or a cropped vest for summer, the same design principles apply.",
            "This is a modern granny square fashion guide written for makers who want their finished garment to look intentional rather than crafty.",
        ],
    },
    {
        "id": "why-modern",
        "heading": "What makes a granny square garment feel modern",
        "paragraphs": [
            "Three design choices separate contemporary granny square fashion from the retro version your grandmother made. First: scale. Old-school garments used tiny two-inch squares by the dozen. Modern versions use larger squares—four to six inches—joined in fewer, bolder pieces. Bigger squares read as intentional; small squares read as busy.",
            "Second: asymmetry. A traditional granny cardigan uses identical squares in a grid. A modern granny vest breaks that rule—one large square on the front, two medium squares in a diagonal on the back, an unexpected color in a single corner. Asymmetry is what makes the garment feel designed.",
            "Third: color restraint. Vintage grannies used every color in the bin. Modern designs use a palette of four to six colors, one of which is a strong accent (rust, cobalt, chartreuse) surrounded by neutrals (cream, oat, black). Palette discipline is the whole game.",
        ],
    },
    {
        "id": "yarn",
        "heading": "Yarn choices for wearable squares",
        "paragraphs": [
            "For a garment that will actually be worn, choose DK-weight or worsted-weight cotton, or a cotton-linen blend. Wool works for winter vests but pills quickly under a coat. Acrylic is affordable but does not breathe—not ideal against skin for a skirt or vest worn all day.",
            "A mercerized cotton with a slight sheen photographs beautifully and holds stitch definition. Buy one full skein of your accent color and half a skein of each supporting color. For a knee-length skirt, plan on 900–1,100 yards total. For a cropped vest, 500–700 yards is plenty.",
            "If you have a bag of scraps in coordinating colors, granny square garments are the perfect way to use them—see our [[scrap-yarn-projects|leftover yarn ideas guide]] for how to sort and pair scraps before starting a wearable project. Our [[best-yarn-for-crochet|full yarn buyer's guide]] compares blends and washability side by side.",
        ],
    },
    {
        "id": "square",
        "heading": "The classic granny square, resized",
        "paragraphs": [
            "The standard granny square is worked in the round using clusters of double crochet separated by chain-1 or chain-2 corners. Here is the four-inch version we use as the base unit for most modern garments.",
            "Round 1: Magic ring. Ch 3 (counts as first dc), 2 dc into the ring. Ch 2 (corner). Then work three more clusters separated by ch 2: (3 dc, ch 2) three times. Sl st to the top of the ch-3 to close.",
            "Round 2: Sl st across to the first ch-2 corner space. Ch 3, work (2 dc, ch 2, 3 dc) in the same corner space. Then in each remaining corner space work (3 dc, ch 2, 3 dc). Between corners, work ch 1. Sl st to close.",
            "Round 3: Sl st into the next ch-1 space. Ch 3, 2 dc in the same space. Ch 1. In the corner space work (3 dc, ch 2, 3 dc). Ch 1. Continue around, working 3 dc in each ch-1 space and (3 dc, ch 2, 3 dc) in each corner. Sl st to close.",
            "That is your base square. Adjust the number of rounds up or down to change size—each additional round adds roughly one inch to the finished square. For a six-inch square, add one more round following the same pattern.",
        ],
    },
    {
        "id": "layout",
        "heading": "Designing an asymmetric layout",
        "paragraphs": [
            "Before you make a single square, sketch your garment on paper as a flat pattern. For a skirt, draw two rectangles (front and back panel) and divide each into a grid of squares. For a vest, draw two shorter rectangles for front and back with armhole cutouts. Then break the grid intentionally—remove one square from the corner, replace one square with two half-squares, place your accent color in an off-center spot rather than the middle.",
            "A reliable formula for modern asymmetry: use your accent color exactly three times in each panel, and place those three squares in a diagonal rather than a straight line or a symmetric cluster. Diagonal placement pulls the eye across the garment and looks unmistakably designed.",
            "Sketch first, count squares needed, then start crocheting. A skirt typically uses 24–36 squares depending on hip size. A cropped vest uses 12–18 squares. Adjust up or down based on your measurements—the same shaping ideas from [[crochet-tops-for-every-body|our guide on crochet tops for every body]] translate directly to granny square garments.",
        ],
    },
    {
        "id": "joining",
        "heading": "Joining squares so the garment drapes on a real body",
        "paragraphs": [
            "The join method changes the entire feel of the finished piece. Whip-stitching with matching yarn creates almost invisible seams and keeps the garment supple. Slip-stitching creates a visible ridge that can be a design feature if worked in a contrast color. Join-as-you-go crochet builds the seam into the final round of each square and is the neatest but slowest option.",
            "For a first modern granny garment, use whip-stitching in the same color as the outermost round of your squares. The seam disappears; the fabric drapes. Skip crocheted-together joins on skirts—they can create rigid seams that fight the natural fall of the fabric.",
            "When joining a skirt panel, stitch top-to-top with the right sides facing so seams sit inside the garment. When joining a vest, keep shoulder seams on the outside slightly for a small design detail, and hide side seams inside.",
        ],
    },
    {
        "id": "finish",
        "heading": "Finishing edges and adding a waistband",
        "paragraphs": [
            "Raw square edges look unfinished on a garment. After joining, work a round of single crochet around every finished edge—hem of the skirt, armholes and neckline of the vest, and top edge of the skirt. This one round transforms the piece from \"in progress\" to \"finished.\"",
            "For a skirt waistband, work three to four rounds of half double crochet in a solid color at the top, then thread a fabric elastic through the last round. This gives you a comfortable, adjustable waist that fits real bodies through weight fluctuations and different tops.",
            "For a vest, add a single-crochet border in a contrast color around the entire outline—armholes, neckline, and bottom edge. The contrast border reads as intentional trim and pulls the whole design together visually.",
        ],
    },
    {
        "id": "styling",
        "heading": "Styling your finished granny piece",
        "paragraphs": [
            "A modern granny square skirt looks striking with a plain white tee tucked in and simple sandals or boots. Keep the top half simple—the skirt is the focal point. For evening, style it with a black tank and heeled sandals for a look that reads as intentional couture rather than costume.",
            "A cropped granny vest works over a plain long-sleeved shirt in fall or a simple silk cami in warmer weather. Layer it under a denim jacket for a texture story. Both pieces travel well because they fold flat and shake out wrinkle-free—rare qualities in handmade garments.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "A modern granny square garment is proof that the oldest patterns can still surprise you. The stitch is simple. The math is honest. The design choices you make about scale, asymmetry, and color are what turn a familiar shape into something that reads as unmistakably now. Start with a small vest to test your palette. Move up to a skirt when your confidence catches up. And save one square from every wearable project you make—stitched together over the years, they will become the memory blanket you never planned to knit but always wanted.",
        ],
    },
]


JAPANESE_KNOT_BAG_BODY = [
    {
        "id": "intro",
        "heading": "Practical geometry, made by hand",
        "paragraphs": [
            "A Japanese knot bag is one of those quiet designs that looks effortlessly modern and turns out to be surprisingly practical. Two asymmetrical handles—one short, one long—slip through each other to close the bag without a zipper, a snap, or a single piece of hardware. The whole thing folds flat when empty, holds an entire trip to the farmers' market when full, and photographs like a piece of wearable sculpture.",
            "The best part is that a crochet knot bag comes together in under three hours from first stitch to finished handle. It uses only single crochet and half double crochet. It costs about six dollars in cotton. And once you understand the geometry, you can scale it up for a beach tote or down for an evening bag without changing a thing about the technique. This is a beginner-friendly Japanese knot bag crochet pattern that behaves like a real bag on a real day out—not a decorative one that stays on the coffee table.",
            "In this guide we walk through the exact materials, the shaping, the step-by-step pattern, and the small studio choices that make the difference between \"cute\" and \"I get asked where I bought this every time I use it.\"",
        ],
    },
    {
        "id": "why-knot",
        "heading": "What makes a Japanese knot bag special",
        "paragraphs": [
            "Traditional Japanese knot bags (musubi bags) trace back to obi sashes and simple wrapped textiles. The genius of the design is the closure: the longer handle threads through the shorter one, and the weight of whatever you carry inside keeps the bag firmly closed. No buttons to fumble, no zipper to break, no clasp to lose. It is the kind of quiet solution that only shows up in cultures that have been refining textile design for centuries.",
            "For a crocheter, this design is a gift because the shaping is almost entirely rectangular. If you can crochet a flat panel, you can crochet a knot bag. The handles are the only sculptural part, and even those are just simple loops. This is the ideal first bag project for a beginner who is ready for something more useful than a coaster but not yet ready for a fully lined, hardware-heavy purse.",
        ],
    },
    {
        "id": "materials",
        "heading": "Materials and hook size",
        "paragraphs": [
            "For one medium-sized bag (finished dimensions about 11 inches wide by 10 inches tall, plus handles) you will need:",
            "• Worsted-weight cotton yarn, about 220 yards. Cotton is essential here because it does not stretch when carrying weight. Wool blends sag under a full grocery load; acrylic pills after a few weeks of daily use.",
            "• 4.0 mm (US G-6) or 4.5 mm (US 7) crochet hook. The larger hook creates a slightly softer fabric that folds more easily.",
            "• Tapestry needle for weaving in ends.",
            "• Sharp scissors.",
            "• Optional: a piece of cotton or linen fabric cut to size for a simple lining if you plan to carry small objects that could slip through stitches (keys, coins, hair pins).",
            "Choose a solid or subtly heathered color for your first bag. Variegated yarns hide stitch definition and make the handle geometry look muddy. If you are torn on which yarn to pick, our [[best-yarn-for-crochet|full yarn buyer's guide]] compares brands, blends, and washability for exactly this kind of everyday project.",
        ],
    },
    {
        "id": "shape",
        "heading": "Understanding the shape before you begin",
        "paragraphs": [
            "A Japanese knot bag is essentially two identical panels sewn together at the bottom and up both sides, with two asymmetrical handles worked into the top edge. The short handle is roughly six inches long. The long handle is roughly twelve inches long. When you close the bag, the long handle passes through the loop of the short handle and drapes over your wrist or shoulder.",
            "The shaping trick most crocheters miss on their first try: the handles are worked continuously off the top edge of each panel, not sewn on afterward. This gives the bag a clean, seamless silhouette and prevents the handles from ever separating from the body under weight. We work each panel from the bottom edge up, transition into the handle, and fasten off at the top of the handle. Then we seam the two panels together. That is the whole architecture.",
        ],
    },
    {
        "id": "pattern",
        "heading": "The pattern, step by step",
        "paragraphs": [
            "This pattern uses US crochet terms. Abbreviations: ch (chain), sc (single crochet), hdc (half double crochet), sl st (slip stitch), st (stitch).",
            "Make two identical panels—one becomes the front, one the back.",
            "Foundation: Ch 42. Turn.",
            "Rows 1–3: Sc in the second chain from hook and in each stitch across. Ch 1, turn. (41 sc across each row.)",
            "Rows 4–24: Hdc in each stitch across. Ch 2 (counts as first hdc of the next row), turn. This creates the body of the bag—a soft, sturdy panel about ten inches tall.",
            "Row 25 (top edge): Sc in each stitch across to firm the top. Ch 1, turn.",
            "Row 26 (start of the short handle on this panel): Sc in the first 8 stitches. Chain 25 (this forms the short handle loop). Skip the middle 25 stitches of the top edge, sc in the last 8 stitches. Fasten off, leaving a 10-inch tail for seaming.",
            "Repeat the entire pattern for the second panel, but on row 26 chain 45 instead of 25. This makes the second handle noticeably longer than the first—exactly the asymmetry the knot bag needs to close properly.",
            "Now hold the two panels together with right sides facing out. Using the tapestry needle and a long tail of matching yarn, whip-stitch or slip-stitch along both sides and the bottom edge, leaving the top open. Weave in every remaining tail. Turn the bag right-side out if you seamed it inside-out (either method works; each gives a slightly different edge finish).",
            "That is the whole bag. Consistent hdc rows are the entire game here—if your rows drift in size, revisit the tension fundamentals in [[even-crochet-stitches|our guide to perfectly even stitches]] before starting the second panel.",
        ],
    },
    {
        "id": "handles",
        "heading": "Reinforcing the handles",
        "paragraphs": [
            "Chain-only handles look pretty but stretch over time. To reinforce, work back along each chain handle with a row of single crochet. Start where you finished the chain, sc in each chain across, and slip stitch to the top of the panel at the other end. This adds body and prevents the handle from thinning out where it takes the most weight—right at the top of your wrist.",
            "For an even sturdier finish, work two rows of sc along the handle. Two rows create a small tube-like handle that feels professional and holds shape after months of daily use. This step adds about ten minutes per handle and is the single biggest quality upgrade you can make.",
        ],
    },
    {
        "id": "variations",
        "heading": "Design variations for every use case",
        "paragraphs": [
            "Once you have made one knot bag, the design invites experimentation. For a beach tote, start with ch 60 instead of 42 and work 35 rows tall—the bigger panel holds a towel, sunscreen, and a book. For an evening clutch, scale down to ch 30 and 15 rows tall, and use fingering-weight cotton with a 3.5 mm hook for a delicate finish.",
            "For color-block versions, work rows 1–12 in one color and rows 13–25 in another. The horizontal stripe is subtle but instantly modernizes the design. For an embroidered version, leave the bag plain and add a small flower motif in cross-stitch or French knots after finishing—cotton takes embroidery beautifully.",
            "If you sell your work at craft fairs, knot bags in three sizes (mini, everyday, tote) make a compelling display and price ladder. Our [[sell-crochet-online|guide to selling crochet online]] has more on pricing and photography if you are considering this route.",
        ],
    },
    {
        "id": "care",
        "heading": "Care and everyday use",
        "paragraphs": [
            "Machine wash on cold, inside out, in a mesh laundry bag. Skip the dryer for the first three washes so the shape sets—lay flat to dry. After that, a low-heat tumble is fine. Do not carry more than about six pounds in a medium-sized knot bag; cotton has beautiful drape but limited structural strength. For heavier hauls, either add a fabric lining or step up to the tote version.",
            "Spot-clean small marks with a damp cloth and a drop of mild soap. Store folded flat rather than hanging—hanging by the handles for months can permanently elongate them.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "A Japanese knot bag is proof that beautifully designed objects do not need hardware, lining, or pattern complexity. Two panels, two asymmetric handles, and a simple hdc body add up to something you will genuinely reach for on real Tuesdays and real Saturday errands. Make one in a solid neutral for daily use. Make another in an accent color for weekends. And when you feel confident, scale up to the tote version and treat yourself to a bag that fits everything you actually want to carry.",
        ],
    },
]


LAMPSHADE_BODY = [
    {
        "id": "intro",
        "heading": "The quietest way to change a room",
        "paragraphs": [
            "There is a specific kind of warmth that comes from lighting a room with something you made yourself. A crochet lampshade takes an ordinary lamp and turns it into the kind of object friends notice the moment they walk in. Add a small pendant lantern in the corner and suddenly the whole room reads as intentional, layered, and softly lit—the visual definition of cozy.",
            "This guide walks through two beginner-friendly crochet projects that transform small spaces without renovating them: a simple lantern cover you can slip over an LED tea light or battery lantern, and a hanging pendant cover finished with small crocheted floral buttons. Both projects use less than a full skein of cotton, take under three hours from first stitch to hanging, and cost about four dollars in materials once you already own a hook.",
            "Whether you are decorating a reading nook, a hallway, or a guest room that could use a little more personality, crochet lighting is the most affordable way to soften a room's edges.",
        ],
    },
    {
        "id": "why-lamps",
        "heading": "Why crochet lamp covers deserve a spot on your project list",
        "paragraphs": [
            "Store-bought lampshades in the budget aisle are almost always plain fabric drums that add nothing to a room. A crochet cover, by contrast, casts patterned shadows across the walls when the light is on and reads as a textured sculpture when the light is off. It is decor that does two jobs at once.",
            "Crochet covers are also endlessly customizable—swap the color to match a season, add flower embellishments for spring, work in metallic yarn for a holiday version, or overlay a plain shade for a completely new look every year. Small-space living especially benefits from this kind of flexibility because you cannot store dozens of holiday lamps in a studio apartment. One base lamp, a rotating collection of crochet covers, and you have a lighting library that fits in a shoebox.",
        ],
    },
    {
        "id": "safety",
        "heading": "Safety first: which lamps work (and which don't)",
        "paragraphs": [
            "Before you crochet a single loop, know which lamps are safe to cover and which are not. Any lamp with an incandescent bulb (the old traditional kind that gets hot) or a halogen bulb should never be covered directly with yarn—the bulb generates enough heat to scorch cotton and start a fire. Safe options are LED bulbs, LED tea lights, battery-powered fairy lights, and modern battery lanterns. LEDs run cool to the touch even after hours of use, which makes them ideal for fabric covers.",
            "For pendant lamps, keep the crochet cover at least one inch away from the bulb itself. Work a cage-style cover that sits below the bulb rather than wrapping it directly. If you have any doubts about your specific lamp, feel the bulb after ten minutes of use—if you can hold it comfortably, it is safe to add crochet. If it is even warm, stop and switch to an LED first. Better safe than sorry.",
        ],
    },
    {
        "id": "supplies",
        "heading": "Supplies and yarn choices",
        "paragraphs": [
            "For both projects in this guide you will need worsted-weight cotton yarn (about 60–100 yards per cover, less than half a skein), a 4.0 mm (US G-6) crochet hook, a tapestry needle, and sharp scissors. Optional but recommended: fabric stiffener or a homemade 50/50 white glue and water mix if you want your finished cover to hold a specific sculptural shape.",
            "For the lantern cover you also need one battery-powered LED lantern or a small LED pillar candle (available at any craft store for four to six dollars). For the pendant cover you need a plain paper or wire lampshade frame—the kind sold as \"DIY lampshade kits\"—plus one to three small buttons for the floral accents.",
            "Cotton is non-negotiable in every case because it does not stretch out of shape and washes cleanly. If you want a deeper dive into fiber weights, blends, and washability, our [[best-yarn-for-crochet|full yarn buyer's guide]] breaks down every option before you spend anything.",
        ],
    },
    {
        "id": "lantern",
        "heading": "Simple crochet lantern cover pattern",
        "paragraphs": [
            "This cover fits a standard four-inch LED tea light lantern (about six inches tall). Adjust the number of rounds up or down if your lantern is a different height.",
            "1. Chain 40. Slip stitch to the first chain to form a ring, taking care not to twist.",
            "2. Round 1: Ch 3 (counts as first dc). Work 1 dc in each chain around. Slip stitch to close. Total: 40 dc.",
            "3. Rounds 2–6: Ch 3. In the same stitch, work a V-stitch (1 dc, ch 1, 1 dc). Skip the next stitch and work a V-stitch in the following stitch. Continue around. Slip stitch to close.",
            "4. Round 7: Ch 1. Sc in each stitch around to firm up the top edge. Slip stitch to close.",
            "5. Fasten off, weave in the tail with your tapestry needle.",
            "Slip the finished cover over your battery lantern. The V-stitch pattern casts a lovely open lattice of shadows when the LED is on, and reads as a textured sculpture when off. Time from start to finish: about ninety minutes for a first attempt.",
        ],
    },
    {
        "id": "pendant",
        "heading": "Hanging pendant cover with floral buttons",
        "paragraphs": [
            "This project uses a plain paper lampshade frame—the kind that clips onto a hanging pendant socket. Total yarn used: about one hundred yards of worsted cotton.",
            "1. Measure the circumference of the widest part of the paper shade. Chain a multiple of 4 that comes close to that measurement (usually 48–64 chains).",
            "2. Round 1: Slip stitch to form a ring, taking care not to twist. Ch 3, dc in each chain around. Slip stitch to close.",
            "3. Rounds 2–8: Work a granny-stitch repeat—ch 3, then work 3 dc into each ch-1 space around, separated by ch 1. This creates an open granny-style mesh perfect for a soft light diffuser.",
            "4. Round 9: Ch 1. Sc around the bottom edge to firm it up. Fasten off and weave in ends.",
            "For the floral buttons: chain 6, slip stitch to form a small ring. Ch 3, work 5 dc into the ring, ch 3, sl st to the top of the ch-3—that is one petal. Repeat for four more petals. Fasten off. Make three or five flowers in accent colors, then sew them evenly around the widest part of the pendant cover using matching thread.",
            "The flowers add sculptural texture and are the visual signature of the piece. If you already have scraps set aside for the accent colors, our [[scrap-yarn-projects|leftover yarn ideas guide]] has more small projects for the tiny remnants that were begging for a home.",
        ],
    },
    {
        "id": "small-spaces",
        "heading": "Design ideas for small spaces",
        "paragraphs": [
            "A single crochet lantern cover changes an entire reading corner. A trio of small hanging lanterns above a dining nook adds height and softens a low ceiling. Group three floor lanterns of different heights in a corner to create a cozy vignette without buying furniture. In a bedroom, a crochet pendant cover in a warm neutral cream over a bed reads as a natural extension of any minimalist or Scandinavian style.",
            "For rented apartments where you cannot change the ceiling fixtures, use a small plug-in pendant lamp with a swag hook—you get the pendant look without any wiring, and the crochet cover clips onto the shade in seconds. Layer warm and cool lighting: a warm pendant over the reading chair, a cool LED lantern on the shelf. The mix creates depth in a small room.",
            "Small studio habits like these are worth revisiting in [[crochet-hacks|our crochet hacks guide]] for cross-project ideas that make the whole practice smoother.",
        ],
    },
    {
        "id": "care",
        "heading": "Care and cleaning",
        "paragraphs": [
            "Crochet lamp covers gather dust over time. Once a month, take the cover off the lamp and gently vacuum it with the brush attachment on low suction. Every six months, hand-wash in cool water with a small drop of mild soap, press the excess water out in a clean towel, and lay flat to dry. Skip the dryer entirely—heat can shrink cotton.",
            "If you used fabric stiffener during the initial finish, reapply after each wash if you want the sculptural hold to stay firm. A well-made crochet lamp cover will still look intentional a decade from now.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Crochet lighting is one of the fastest ways to change how a small space feels. A single afternoon of work turns a plain LED lantern or a bare pendant bulb into something intentional, layered, and unmistakably yours. Start with the simple lantern cover this weekend. Add the pendant with floral buttons next weekend. In two Saturdays you will have transformed a corner of your home—and the finished pieces cost less than a takeout dinner.",
        ],
    },
]


BEGINNERS_GUIDE_BODY = [
    {
        "id": "welcome",
        "heading": "Welcome to your first hook",
        "paragraphs": [
            "Crochet has a reputation for being intimidating, but it is one of the friendliest crafts you can pick up. You only need three things—a hook, a ball of yarn, and about twenty minutes—to make your first row of stitches. There is no expensive machine, no complicated setup, and no rule that says your first project has to look perfect. Every experienced crocheter you admire once held a hook awkwardly and pulled a stitch far too tight. That awkwardness is not a warning sign; it is the beginning of muscle memory.",
            "This guide walks you through the very first steps, from choosing supplies to finishing a first small square. Read it slowly, keep your yarn nearby, and give yourself permission to stop and re-read any part that feels fuzzy. The goal is not speed. The goal is a calm, confident start that makes you want to pick up your hook again tomorrow.",
        ],
    },
    {
        "id": "supplies",
        "heading": "The three supplies you actually need",
        "paragraphs": [
            "Skip the huge starter kit for now. A single 5.0 mm or 5.5 mm aluminum hook, one skein of smooth worsted-weight yarn in a light color, and a pair of small scissors will get you through the entire first week. Light yarn matters because dark strands make it hard to see individual stitches while you are still learning to spot them. Smooth means no fuzz, no bouclé, and no metallic strands—those are wonderful yarns for later, but they hide beginner mistakes exactly when you most need to see them.",
            "Cotton or a soft acrylic both work. Cotton shows stitch definition more clearly and washes beautifully; acrylic is cheaper and forgiving on your wrist. A small stitch marker (or even a paperclip) helps you find the first stitch of each row. That is it. Once you have finished a small project, you can slowly expand your supplies with intention rather than filling a bin with impulse buys.",
        ],
    },
    {
        "id": "slip-knot-chain",
        "heading": "Your slip knot and first chain",
        "paragraphs": [
            "Everything in crochet grows out of two motions: making a slip knot and pulling a loop through another loop. Practice the slip knot on its own three or four times before you worry about anything else. A good slip knot slides gently when you pull the tail, but does not grip the hook like a vise. If your knot squeezes the hook so tightly you cannot pull yarn through, loosen it and start again. Tight grip equals sore hands and stitches that refuse to move.",
            "Once your slip knot is on the hook, wrap the yarn over the hook (this is called a yarn-over, abbreviated 'yo') and pull it through the loop. That single motion just made your first chain stitch. Repeat it twenty times. Look at the results: you should see a row of small V shapes, each about the same size. If some are tight and some are loose, that is normal. Consistency comes from repetition, not talent.",
        ],
    },
    {
        "id": "single-crochet",
        "heading": "The single crochet: your first real stitch",
        "paragraphs": [
            "Single crochet (abbreviated 'sc' in US terms) is the smallest, densest, most beginner-friendly stitch. To work it into your practice chain, skip the loop directly on the hook, insert your hook into the second chain from the hook, yarn over, and pull up a loop. You now have two loops on your hook. Yarn over one more time and pull through both loops. That is one complete single crochet.",
            "Work a single crochet into every chain across the row. When you reach the end, chain one, turn your work over so the yarn tail is on the right if you are right-handed (or the left if you are left-handed), and start a new row. The first stitch of the new row goes into the first stitch of the previous row—not into the turning chain. This is the most common beginner confusion, and marking that first stitch with a paper clip saves an entire evening of unraveling.",
        ],
    },
    {
        "id": "practice-swatch",
        "heading": "Make a real practice swatch",
        "paragraphs": [
            "Set a small goal: chain 15, then work five rows of single crochet. That gives you a swatch roughly the size of a coaster, and it teaches you almost everything you need for a bigger project. Count your stitches at the end of each row. If you started with 14 single crochets and finish with 13, you missed the last stitch. If you finish with 15, you added a stitch somewhere—probably into the turning chain by accident. Both are extremely common. Just pull back to the mistake and rework it. This is called 'frogging' because you 'rip it, rip it.'",
            "Aim to work in short, focused sessions of ten to fifteen minutes at first. Long sessions tighten your grip and cramp your hand. If your hands ache, take a break, stretch your fingers, and come back later. Comfortable hands make consistent stitches, and consistent stitches make fabric you actually want to keep.",
        ],
    },
    {
        "id": "reading-help",
        "heading": "When patterns start to make sense",
        "paragraphs": [
            "The next skill after your first swatch is reading a pattern with confidence. Crochet patterns look intimidating because they are full of abbreviations, but they are actually shorter to read than plain English. 'sc' is single crochet, 'ch' is chain, 'dc' is double crochet, and '*repeat from *' tells you which section to repeat. Our full walkthrough is in [[read-crochet-pattern|how to read a crochet pattern like a pro]]—read it once your first swatch feels comfortable and you will unlock hundreds of free patterns online.",
            "As you progress, common frustrations pop up: curling edges, growing or shrinking stitch counts, holes where you did not want them. Every one of these has a simple fix. Bookmark [[common-crochet-mistakes|our common mistakes guide]] and refer back to it whenever a row starts looking off.",
        ],
    },
    {
        "id": "first-project",
        "heading": "A first project you can finish this week",
        "paragraphs": [
            "For your very first finished object, try a simple washcloth: chain 25, single crochet in each chain across, and continue for about 20 rows or until the piece looks roughly square. Fasten off, weave in the ends with a yarn needle, and you have a functional handmade thing. It will be a little wonky. Use it anyway. The first washcloth is a portrait of everything your hands learned that week, and every washcloth after this one will look better than the last.",
            "Once you can finish a washcloth, the door opens wide. A dishcloth, a coaster set, a scarf, a headband, a chunky market bag—all are approachable variations of the same skills. Choose whichever project makes you smile when you picture it finished.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Crochet is a craft of small returns. Ten minutes today teaches your hands something. Ten more minutes tomorrow builds on it. In two weeks the hook feels natural in your grip, and in two months you will be making things you did not think you could make. Give yourself permission to be a beginner for as long as it takes. Then keep going, quietly, one loop at a time.",
        ],
    },
]


COMMON_MISTAKES_BODY = [
    {
        "id": "why-mistakes",
        "heading": "Why crochet mistakes are actually good news",
        "paragraphs": [
            "Every crochet mistake tells you something specific about what your hands, hook, or yarn are doing. That means every mistake is also fixable once you know how to read it. New crocheters often assume their work looks 'wrong' because they lack talent. The truth is far kinder: the ten most common beginner problems all trace back to one of three habits—tight tension, uncounted stitches, or a missed turning stitch. Once you learn to spot them, they lose their power to derail a project.",
            "This guide walks through ten mistakes that show up over and over in beginner and intermediate crochet, with a specific fix for each one. Bookmark the list. Every time a piece starts looking odd, run through it before you get frustrated.",
        ],
    },
    {
        "id": "curling",
        "heading": "1. Your fabric curls",
        "paragraphs": [
            "Single crochet fabric that curls upward almost always means tight tension. The stitches are pulling in on themselves faster than the fabric can lie flat. Try going up one hook size—a 5.5 mm instead of a 5.0 mm—without changing the yarn. That single change fixes most curling problems immediately. If you crochet very loosely, curling is rarely your issue; look at edge stitches instead.",
            "Blocking also helps. Wet the finished piece, gently shape it flat, and let it dry on a towel. Cotton and acrylic block a little; wool and wool blends block dramatically. If you like the density of your current tension, blocking is often enough to keep a finished piece flat.",
        ],
    },
    {
        "id": "growing-shrinking",
        "heading": "2. Your row count keeps changing",
        "paragraphs": [
            "Starting a row with 20 stitches and ending with 22 is a classic beginner problem. It usually means one of two things: you are crocheting into the turning chain when the pattern says not to, or you are missing the last stitch of the previous row. Count your stitches at the end of every row until it becomes automatic. Use a scrap of contrasting yarn to mark the first and last stitches of your first row so you can always find them.",
            "If you routinely finish with fewer stitches, you are probably skipping the very last stitch because it looks smaller than the others. That last stitch is real—it is just hiding under the turning chain. Insert your hook one stitch further than feels natural.",
        ],
    },
    {
        "id": "tension",
        "heading": "3. Your tension is inconsistent",
        "paragraphs": [
            "Uneven tension shows up as fabric that alternates between tight, dense sections and loose, floppy sections. The most common cause is a changing grip. Try holding the hook the same way for the whole project, and rest your hands every ten to fifteen minutes. Long sessions almost always tighten. A full breakdown of tension mechanics lives in [[even-crochet-stitches|our even stitches guide]] and it is worth reading twice.",
            "Yarn tension in your non-hook hand matters as much as hook grip. Wrap the working yarn around your pinky finger and over your index finger so it feeds smoothly. If yarn snags on your fingers, add a small amount of hand lotion (fully absorbed) so the fiber glides.",
        ],
    },
    {
        "id": "wrong-stitch",
        "heading": "4. You worked the wrong stitch",
        "paragraphs": [
            "Single crochet, half double crochet, and double crochet look surprisingly similar on the hook. If a row unexpectedly gets taller or shorter, you probably switched stitch types by accident. Always confirm the pattern's abbreviation at the start of each row and mumble it to yourself until you finish the row. It sounds silly. It works.",
            "Charts help too. If you are a visual thinker, look up the pattern's chart version and put it next to your written instructions. Symbol charts show stitch height and repeats at a glance, and they catch mistakes long before your written pattern does.",
        ],
    },
    {
        "id": "twisted",
        "heading": "5. Your foundation chain is twisted",
        "paragraphs": [
            "This one strikes when you are working in the round. If your starting chain twists before you join it, every round after will spiral, and you will notice the shape looking wrong five rounds in. Always lay your foundation chain flat before joining. The V-shapes should all face the same direction. If even one V has flipped, untwist and join again.",
            "For flat pieces, twisted foundations show up as an odd wave along the bottom edge. If yours does this, try the chainless foundation single crochet method: it uses one motion to create a chain and a single crochet at the same time, and it produces a stretchier, less-twist-prone edge.",
        ],
    },
    {
        "id": "ends",
        "heading": "6. Ends are unraveling",
        "paragraphs": [
            "Weaving in ends is not decorative. It is structural. A tail woven for only an inch will slip out with the first wash. Weave in each end for at least three inches, changing direction once mid-weave. Split the plies of the yarn tail if you can, and weave each half in a different direction; the fibers grip each other and stay put.",
            "For amigurumi and blankets, tie a small square knot before weaving. For garments, avoid knots and rely entirely on the length and direction of the woven tail. Test a woven end by tugging firmly. If it moves, add another inch of weaving.",
        ],
    },
    {
        "id": "turning-chain",
        "heading": "7. The turning chain confusion",
        "paragraphs": [
            "The turning chain (ch 1 for single crochet, ch 2 for half double, ch 3 for double) exists to give your first stitch enough height. But whether the turning chain counts as a stitch depends on the pattern. Read the first row of the pattern carefully. If it says 'ch 3 (counts as first dc)' you skip the first stitch of the row below and work into the second. If it does not, you work into the very first stitch.",
            "Getting this wrong causes ever-growing or ever-shrinking rows. Highlight the turning-chain rule in your pattern before you start.",
        ],
    },
    {
        "id": "holes",
        "heading": "8. Random holes appear",
        "paragraphs": [
            "Small unplanned holes usually mean you worked into a space between stitches instead of into the top of the stitch. The tops are the visible V's. The spaces between them are gaps. Always aim for the two loops of the V, not the space just below.",
            "For patterns with intentional lace, holes are on purpose. For dense fabric like single crochet, they are not. Slow down for a row and inspect where the hook is going each time. Ten deliberate stitches teach more than a hundred rushed ones.",
        ],
    },
    {
        "id": "hook-slipping",
        "heading": "9. The hook keeps slipping out",
        "paragraphs": [
            "If your hook slips out of loops constantly, the throat of the hook may be too narrow for your yarn, or your grip is angling the head away from the yarn. Try a hook with a wider throat (many crocheters prefer inline hooks like Susan Bates for tight tension and tapered hooks like Boye or Clover for loose tension). A soft rubber grip cushion also helps if wrist strain is contributing.",
            "Check your yarn too. Very slippery yarns like bamboo or silk slide off metal hooks easily. Switch to a wooden hook, which grips slippery fibers more securely.",
        ],
    },
    {
        "id": "gauge-ignored",
        "heading": "10. You ignored gauge",
        "paragraphs": [
            "For scarves and blankets, gauge is optional. For anything that needs to fit—hats, sweaters, mitts—gauge is everything. If you skip the swatch and jump straight into the pattern, the finished piece often ends up two sizes off. It is heartbreaking and completely preventable.",
            "Work a swatch at least four inches by four inches, wash it if the finished item will be washed, and measure it after it dries. Adjust hook size until your stitch count matches the pattern's stated gauge. Once your gauge is right, choose your project from [[crochet-blanket-patterns|our blanket ideas guide]] or any wearable pattern and enjoy a finished piece that actually fits the way you imagined.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Every one of these mistakes is repairable, and none of them mean you are bad at crochet. They mean you are learning. Pick one issue you recognize in your own work, work through the fix on your next project, and see how much smoother the next hour of crochet feels. Small corrections compound quickly.",
        ],
    },
]


EVEN_STITCHES_BODY = [
    {
        "id": "why-tension",
        "heading": "Why tension is the whole game",
        "paragraphs": [
            "Even stitches are almost never about talent. They are about tension—how tightly or loosely you hold the working yarn and the hook. When tension is consistent from one stitch to the next, the fabric looks intentional and the finished piece drapes correctly. When tension shifts, some stitches pull in and some flop out, and the fabric develops a wavy, uneven look that new crocheters often blame on themselves. It is not you. It is the yarn asking for a more consistent grip.",
            "The good news is that tension is a habit, not a gift. This guide walks through the specific physical and mental adjustments that produce even fabric in every project, whether you crochet for ten minutes a day or ten hours a weekend.",
        ],
    },
    {
        "id": "grip-styles",
        "heading": "Choose a grip and commit to it",
        "paragraphs": [
            "There are two common ways to hold a crochet hook: the knife grip and the pencil grip. Neither is objectively better. The knife grip (holding the hook like you are about to butter toast) tends to feel more powerful and is easier on the wrist for long sessions. The pencil grip (holding the hook the way you would write) offers finer control for delicate work.",
            "Try both for ten minutes each. Whichever feels more natural is the one to commit to for the next three projects. Switching grips mid-project changes tension almost immediately, and inconsistent tension is exactly what we are trying to avoid.",
        ],
    },
    {
        "id": "yarn-hand",
        "heading": "The role of your non-hook hand",
        "paragraphs": [
            "Most beginners obsess over their hook and forget that the non-hook hand controls half of tension. The working yarn must feed evenly from your fingers to the hook. If it drags, stitches tighten. If it flows too freely, stitches loosen. A common setup wraps the yarn once around the pinky, up and over the ring and middle fingers, and across the top of the index finger. The index finger becomes a tiny yarn tension gauge you can adjust in real time.",
            "Experiment for one full project. Try one wrap around the pinky, then two, then no wrap. Note how each setup feels. Once you find a comfortable feed, use it for every project going forward. Stability wins over cleverness.",
        ],
    },
    {
        "id": "hook-choice",
        "heading": "Hook choice matters more than you think",
        "paragraphs": [
            "Inline hooks (like Susan Bates) have a straight throat and grab yarn firmly. Tapered hooks (like Boye or Clover) have a curved throat and slide through loops more easily. If your stitches are consistently too tight, a tapered hook can loosen them. If your stitches are too loose, an inline hook can tighten them. This is a free tension adjustment you can make just by changing tools.",
            "The material also matters. Aluminum is fast and slick, wood grips slippery yarns like bamboo and silk, and ergonomic rubber grips reduce wrist strain during long sessions. A hook that feels comfortable will always produce more even stitches than a hook that fights your grip.",
        ],
    },
    {
        "id": "breath-rhythm",
        "heading": "Breath and body rhythm",
        "paragraphs": [
            "This sounds unusual, but it is one of the most consistent secrets among experienced crocheters: breath affects tension. Held breath tightens the whole body, including the hands. Slow, steady breathing keeps grip pressure consistent. If you catch yourself hunching over a difficult stitch, exhale, relax your shoulders, and try the stitch again.",
            "Take a two-minute break every twenty minutes for a long project. Stand up, roll your shoulders, and shake your hands out. This resets your grip, restores blood flow, and prevents the slow tightening that produces uneven fabric over the course of an hour.",
        ],
    },
    {
        "id": "swatching",
        "heading": "Swatching is not optional",
        "paragraphs": [
            "A four-inch by four-inch swatch tells you everything: your tension with the current hook, whether the yarn behaves the way the label claims, and whether you need to size up or down. Skipping the swatch is the fastest route to a project that ends up two inches too small or two inches too wide.",
            "Swatch the exact stitch pattern the project uses, not just single crochet. Different stitch patterns produce different tension. Once the swatch matches the pattern's gauge, you can start the real project knowing every measurement will be true. If gauge feels unfamiliar, [[common-crochet-mistakes|our mistakes guide]] covers this exact issue in more detail.",
        ],
    },
    {
        "id": "edges",
        "heading": "Tidy edges are a tension signal",
        "paragraphs": [
            "Uneven side edges usually mean the turning chain is inconsistent or the first stitch of each row is inserted in the wrong place. Decide once whether the turning chain counts as a stitch in your project, and stick with that rule for every row. Insert the first stitch of every row in the exact same place—either the very first stitch or the second, depending on your pattern rule.",
            "For side stitches that appear looser than the middle, tighten the yarn slightly on the last stitch of every row. This tiny adjustment produces edges that look ruled with a straightedge.",
        ],
    },
    {
        "id": "blocking",
        "heading": "Blocking hides small sins",
        "paragraphs": [
            "Even with careful tension, small variations show up in every fabric. Blocking evens them out. Wet the finished piece in cool water, gently squeeze out excess moisture in a towel, and shape it flat on a blocking mat or clean towel. Pin the corners into a rectangle and let it dry completely.",
            "Cotton and acrylic block modestly; wool blocks dramatically. A well-blocked piece looks intentional even if a few stitches wandered along the way. Do not use blocking as an excuse for careless work, but do use it as the final step that turns a good piece into a beautiful one.",
        ],
    },
    {
        "id": "practice",
        "heading": "Practice the boring stuff",
        "paragraphs": [
            "Even stitches come from repetition, not novelty. Work five identical washcloths in the same yarn and hook. By washcloth five, your tension will be dramatically more consistent than it was on washcloth one. This is the least glamorous crochet advice you will ever receive, and it works every single time.",
            "When you are ready for a project that rewards your new tension skills, try one of the smooth-drape patterns from [[best-yarn-for-crochet|our yarn buyer's guide]]. Even tension shines most in projects with clear stitch definition.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Perfectly even stitches are a byproduct of a comfortable grip, a steady rhythm, and enough practice to make consistency automatic. Slow down for the next few rows, notice how your hands are moving, and let calm consistency do the work. The fabric that emerges will look like it was made by someone who has been crocheting for years—because now, in a small, quiet way, you are.",
        ],
    },
]


READ_PATTERN_BODY = [
    {
        "id": "pattern-language",
        "heading": "Crochet patterns look weird for a reason",
        "paragraphs": [
            "The first time you open a crochet pattern, it looks like a foreign language. 'Row 3: ch 3 (counts as first dc), *sk 1 st, dc in next st, ch 1; rep from * to end.' That single line contains six pieces of information, and once you can read it, hundreds of free patterns online become instantly usable. This guide unpacks the language piece by piece so nothing on that line feels mysterious.",
            "The best way to learn is with a hook in your hand. Print or bookmark a beginner-friendly pattern before you start reading below—working through examples as you learn makes the abbreviations click in a way that reading alone never can.",
        ],
    },
    {
        "id": "abbreviations",
        "heading": "The core abbreviations",
        "paragraphs": [
            "Most patterns you find online use US crochet terminology. The core abbreviations are: ch (chain), sl st (slip stitch), sc (single crochet), hdc (half double crochet), dc (double crochet), tr (treble crochet), sk (skip), st (stitch), sts (stitches), rep (repeat), and yo (yarn over). Almost every pattern uses these ten. Memorize them by writing them once by hand, then look up new ones as you encounter them.",
            "UK terminology uses the same words but shifts the meaning by one height: UK double crochet is US single crochet, UK treble is US double, and so on. Always check which system the pattern uses. Free patterns from UK designers on Ravelry and Etsy sometimes catch new crocheters off guard.",
        ],
    },
    {
        "id": "repeats",
        "heading": "How repeats work",
        "paragraphs": [
            "The asterisk (*) marks a repeat section. When a pattern says '*dc in next 3 sts, ch 1; rep from * to end,' you work three double crochets, chain one, and then repeat that same sequence—dc 3, ch 1, dc 3, ch 1—until you reach the end of the row. Some patterns use brackets [] or parentheses () the same way. When both appear, work the innermost bracket first, then the outer.",
            "Count the stitches called for in one full repeat before you begin. If a repeat needs four stitches and your row has eighteen, four repeats leave two stitches over. Read the pattern carefully to see how it handles those extras. Sometimes the pattern accounts for them; sometimes you need to adjust your foundation chain.",
        ],
    },
    {
        "id": "counts",
        "heading": "Stitch counts in parentheses",
        "paragraphs": [
            "At the end of a row you will often see something like '(24 sts).' This tells you how many stitches you should have at the end of that row. It is a checkpoint. If your count matches, keep going. If it does not, stop and find the mistake before it multiplies.",
            "For flat pieces, stitch counts stay the same on every row unless the pattern is intentionally increasing or decreasing for shaping. For shaped pieces like sleeves or hats, the counts change on purpose. Always cross-check counts after any shaping row.",
        ],
    },
    {
        "id": "charts",
        "heading": "Reading charts and symbols",
        "paragraphs": [
            "Charts are visual maps of a pattern. Each stitch is drawn as a symbol: a plus sign for single crochet, a T for half double, a T with one slash for double, a T with two slashes for treble. Chains look like small ovals. The chart is read from bottom to top and, on right-side rows, from right to left. On wrong-side rows, it flips.",
            "Charts are especially useful for lace, mandalas, and stitch patterns with repeating motifs. If a written pattern feels confusing, look up the chart version and let the picture tell the story.",
        ],
    },
    {
        "id": "sizes",
        "heading": "Working with multi-size patterns",
        "paragraphs": [
            "Wearable patterns often list all sizes on one line: 'ch 60 (66, 72, 78, 84).' The first number is the smallest size, and the numbers in parentheses are the larger sizes in order. Circle or highlight your size number every place it appears in the pattern before you start—accidentally flipping to a different size mid-project is a common frustration and easy to prevent.",
            "If your body falls between two sizes, choose the larger one and shorten as needed. For plus and diverse bodies, [[crochet-tops-for-every-body|our top-fitting guide]] covers the specific adjustments that make ready-made patterns actually fit.",
        ],
    },
    {
        "id": "gauge-section",
        "heading": "The gauge section is not optional",
        "paragraphs": [
            "At the top of every wearable pattern, you will see a gauge line: '14 sts x 10 rows = 4 in (10 cm) in hdc using a 5.5 mm hook.' This is not a suggestion. Match this exactly with a swatch before you start the real project. If your swatch has 15 stitches over four inches, go up a hook size. If it has 13, go down.",
            "For scarves, blankets, and other flat pieces where fit does not matter, you can skip gauge if you want. For anything that needs to fit a body, gauge is non-negotiable.",
        ],
    },
    {
        "id": "specialty-terms",
        "heading": "Common specialty terms",
        "paragraphs": [
            "A few terms appear in almost every pattern: 'work in the back loop only' (blo), 'work in the front loop only' (flo), 'magic ring' or 'magic circle' (a technique to start crocheting in the round), and 'right side' vs 'wrong side.' Each is worth a quick internet video—two minutes of watching hands do the motion is more valuable than pages of text.",
            "Whenever a pattern uses an unfamiliar term, pause and search 'crochet [term] tutorial' before continuing. Two minutes of learning now saves twenty minutes of frogging later.",
        ],
    },
    {
        "id": "notes",
        "heading": "Take pattern notes as you go",
        "paragraphs": [
            "Every experienced crocheter keeps a small notebook of pattern quirks: which turning chain method worked, whether they went up or down a hook size, and any modifications they made. This becomes priceless when you set a project aside and pick it up a week later. Even a Post-it stuck to the pattern is better than nothing.",
            "Write the finished measurements in your notes too. Future-you will want to compare a new pattern to something that already fit correctly, and specific measurements make that possible.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "The first pattern you decode feels like magic. The tenth feels like second nature. Choose a small, well-reviewed beginner pattern for your first read-through, work it slowly, and cross-reference every abbreviation as it appears. Within a few projects, patterns stop being intimidating and start being maps to finished objects you already know how to make.",
        ],
    },
]


BEST_YARN_BODY = [
    {
        "id": "yarn-decides",
        "heading": "Yarn decides how a project feels",
        "paragraphs": [
            "The same pattern worked in three different yarns produces three completely different finished objects. A blanket in cotton feels crisp and structured. The same blanket in wool feels warm and squishy. The same blanket in acrylic feels light and easy to wash. None of these is better—each is right for a different purpose. This guide walks through the yarn choices that actually matter for real projects, so your next skein makes the finished piece feel exactly the way you imagined it.",
            "There is no universal 'best' yarn. There is only the best yarn for a specific job, a specific budget, and a specific pair of hands. Learn to read the label, feel the twist, and imagine the finished object before you commit.",
        ],
    },
    {
        "id": "weight-system",
        "heading": "The weight system, explained simply",
        "paragraphs": [
            "Yarn weight is a system of thickness, and it goes from lace (0) to jumbo (7). The most common weights for beginners are worsted (4) and DK (3), because they are easy to see, easy to hold, and produce quick results. Bulky (5) works up even faster and is great for cozy blankets. Sport (2) is thinner and better for delicate garments. Lace (0) is used for shawls, doilies, and intricate work with very small hooks.",
            "The label always shows a small yarn-icon symbol with a number inside. That is the weight category. Match it to what the pattern calls for, or substitute carefully: swapping worsted for DK will produce a smaller, denser piece unless you resize.",
        ],
    },
    {
        "id": "cotton",
        "heading": "Cotton: crisp, structured, forgiving",
        "paragraphs": [
            "Cotton is dense, non-stretchy, and shows every stitch clearly. It is the best fiber for beginners because mistakes are easy to see, and it is the ideal fiber for items that need structure—washcloths, market bags, dishcloths, coasters, and any home decor that should hold its shape. Cotton also washes beautifully in a machine and gets softer with each wash.",
            "The downside: cotton has no memory. Once stretched, it stays stretched. That makes it a poor choice for hats or fitted garments. For beginners, cotton in a light color (cream, pale blue, mint green) is the friendliest first yarn. Save dark blacks and navies for after your eyes are trained to see stitches.",
        ],
    },
    {
        "id": "wool",
        "heading": "Wool: warm, bouncy, and full of memory",
        "paragraphs": [
            "Wool is the classic yarn for warmth and stitch definition. It springs back into shape, blocks beautifully, and produces fabric that looks intentional even with slightly wobbly tension. It is the best choice for winter hats, mittens, cardigans, and blankets that will actually be used through cold weather. Merino wool is soft enough for scarves and next-to-skin projects; Peruvian and worsted wool are hardier and more affordable.",
            "The tradeoff is care. Most wool requires hand washing, and untreated wool felts if agitated. Superwash wool is treated to survive the washing machine, and it is worth every penny for gifts headed to households that will not baby a handmade item.",
        ],
    },
    {
        "id": "acrylic",
        "heading": "Acrylic: practical, affordable, gift-friendly",
        "paragraphs": [
            "Acrylic yarn gets a bad reputation online, and that reputation is out of date. Modern acrylics are soft, washable, come in every color imaginable, and cost a fraction of natural fibers. They are the practical choice for baby blankets, throws, and gifts where the recipient will not lovingly hand-wash a handmade item. They are also excellent for beginners because a full-size skein costs less than a good sandwich, and mistakes feel less expensive.",
            "The downside: acrylic does not block dramatically, and cheap acrylic can feel a little plasticky. Choose brands with a soft twist and a good customer reputation, and skip the very cheapest supermarket options for anything you want to last.",
        ],
    },
    {
        "id": "blends",
        "heading": "Blends: the best of two fibers",
        "paragraphs": [
            "Yarn blends combine two or more fibers to get the best qualities of each. Cotton-acrylic blends are soft, structured, and machine-washable—an ideal beginner yarn for wearables. Wool-acrylic blends are warm, elastic, and cheaper than pure wool. Cotton-linen blends produce beautiful drape for summer garments. Silk-wool blends feel luxurious and glide across the hook.",
            "Read the fiber percentage on the label. A '80% cotton, 20% acrylic' blend behaves mostly like cotton with a little more give. A '50/50 cotton-acrylic' behaves like something in between. Match the blend to what your project needs to do—structure, drape, warmth, or wash tolerance.",
        ],
    },
    {
        "id": "matching-projects",
        "heading": "Matching yarn to project",
        "paragraphs": [
            "For blankets, choose a soft, washable yarn in worsted or bulky weight. Cotton-acrylic blends and superwash wool are both excellent. For scarves, wool or wool blends drape beautifully and hold blocked shape. For hats, superwash wool or merino keep their fit through many washes. For amigurumi, tight, non-stretchy fiber like cotton is ideal because stuffing does not peek through the stitches. For market bags, mercerized cotton is the classic answer.",
            "When in doubt, buy a single ball of a candidate yarn and swatch it in the pattern's stitch. A twenty-minute swatch teaches more than an hour of online reviews. Refer to [[crochet-blanket-patterns|our blanket guide]] for specific yarn recommendations by blanket style.",
        ],
    },
    {
        "id": "yardage",
        "heading": "Read yardage, not weight",
        "paragraphs": [
            "Skein weight is misleading. A 100-gram skein of bulky yarn contains far fewer yards than a 100-gram skein of sport yarn. When comparing prices or estimating how much yarn a project needs, always look at total yardage. Patterns usually list yardage required, not weight.",
            "Buy at least ten percent more yarn than the pattern calls for, and check that all skeins share the same dye lot number. Dye lots vary noticeably between batches, and buying an extra skein three months later almost always produces a visible stripe.",
        ],
    },
    {
        "id": "buying-tips",
        "heading": "Buying tips that save money",
        "paragraphs": [
            "Big-box stores often have excellent sales two or three times a year on their store-brand yarns. Independent yarn shops carry higher-quality fibers with expert advice; the price is higher but so is the finished result. Online retailers offer the widest selection, but you cannot feel the yarn before buying—stick to brands you already know, or buy a single test skein first.",
            "For scrap collectors, our [[scrap-yarn-projects|leftover yarn guide]] covers twelve ways to use what you already own before adding more to the stash.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Great yarn choices are practical, not fancy. Ask what the finished piece needs to do, choose the fiber that supports that job, and buy enough of one dye lot to finish the project. The rest is preference, and preference gets clearer with every skein you use. Pick one weight and one fiber for your next project, use it fully, and note what you learned. That is how experienced crocheters build a working yarn library over time.",
        ],
    },
]


AMIGURUMI_101_BODY = [
    {
        "id": "why-ami",
        "heading": "Why amigurumi is the best gateway to sculpture",
        "paragraphs": [
            "Amigurumi is the Japanese-influenced style of crocheting small, stuffed animals and characters. What makes it a wonderful beginner project is that a single amigurumi teaches almost every core crochet skill: working in the round, tight tension, single crochet mastery, increases, decreases, and simple assembly. Finish one small animal, and you have practiced the fundamentals of every advanced amigurumi pattern you will ever see.",
            "The scale is also friendly. A small mushroom or bumblebee takes an afternoon, not a season. That means you can experiment, make mistakes, and try again without a huge time investment. If a stitch pattern is not clicking, a two-hour amigurumi is a much lower stakes practice piece than a two-week garment.",
        ],
    },
    {
        "id": "supplies",
        "heading": "Supplies for your first tiny animal",
        "paragraphs": [
            "You need a smooth medium-weight yarn (cotton or a plush acrylic like Hobbii Amigo work beautifully), a hook one full size smaller than the yarn label suggests (a 3.5 mm or 4.0 mm for worsted yarn), polyester fiberfill, a tapestry needle, and a small pair of safety eyes or plain black embroidery floss.",
            "The reason for a smaller hook is critical: tight stitches keep stuffing from peeking through. If your amigurumi looks 'holey' after stuffing, your hook is too big for the yarn. Go down a size and try again. The fabric should feel firm and dense, almost like a soft cardboard.",
        ],
    },
    {
        "id": "magic-ring",
        "heading": "The magic ring: your amigurumi foundation",
        "paragraphs": [
            "Almost every amigurumi starts with a magic ring. It is a slip knot that stays loose enough to work stitches into, then pulls closed at the center. To make one, wrap the yarn around your fingers, insert the hook under both strands, pull up a loop, chain one, and work your first round of stitches into the ring. When the round is complete, pull the tail firmly to close the center.",
            "If magic rings feel awkward, an alternative is chain 2 and work all round-one stitches into the second chain from the hook. This is called the 'chain 2 method,' and it produces a tiny hole in the center that most people never notice. Either method is perfectly acceptable.",
        ],
    },
    {
        "id": "increases-decreases",
        "heading": "Increases and invisible decreases",
        "paragraphs": [
            "An amigurumi ball is made by increasing stitches evenly through the first several rounds, working straight for the middle, and then decreasing evenly toward the end. Increases (inc) are simply two single crochets worked into the same stitch. Decreases (dec) are two stitches worked together into one.",
            "The 'invisible decrease' method produces a much cleaner finish than a standard decrease. Insert your hook into the front loop of the next stitch, then into the front loop of the following stitch (two front loops on your hook), yarn over, and pull through both loops. Yarn over once more and pull through both loops on the hook. This tiny modification is what separates amateurish amigurumi from pieces that look designer-made.",
        ],
    },
    {
        "id": "markers",
        "heading": "Stitch markers are essential",
        "paragraphs": [
            "Amigurumi is worked in continuous spirals, not joined rounds. That means the end of one round flows straight into the next without a slip stitch. To find the start of each round, place a small stitch marker (a paperclip works fine) in the first stitch of every round. Move it up as you complete each round.",
            "Without markers, you will lose count within five rounds. Even experienced amigurumi crocheters use them for every project. Count stitches at the end of every round, and mark the first stitch of every round without exception.",
        ],
    },
    {
        "id": "stuffing",
        "heading": "Stuffing shapes your character",
        "paragraphs": [
            "Firm stuffing is the difference between a shapeless blob and a piece with clear silhouette. Stuff in small pieces, packing each piece firmly with the eraser end of a pencil or a chopstick. Stop stuffing about two rounds before you close the shape; the last rounds hold everything in place.",
            "Adjust firmness to the shape. Round shapes like heads and berries look best when stuffed firm enough that they hold their spherical shape without dents. Long shapes like arms and legs can be a little softer so they bend naturally.",
        ],
    },
    {
        "id": "faces",
        "heading": "Faces make personality",
        "paragraphs": [
            "Two identical animals with different faces feel like completely different creatures. Place safety eyes before closing the head so you can adjust position freely. A common rule of thumb: place eyes on round 8 or 9 of a 12-round head, five to seven stitches apart. Adjust by holding the eyes in place and looking at the piece from a few feet away.",
            "For young children (under three years old), embroider features with black yarn or embroidery floss instead of using safety eyes. A simple satin stitch for each eye works beautifully. Add a tiny pink cheek in embroidery floss for extra charm.",
        ],
    },
    {
        "id": "assembly",
        "heading": "Assembly is a design choice",
        "paragraphs": [
            "How you attach limbs, ears, and tails changes the entire feel of the finished piece. Pin body parts in different positions before sewing to see what feels right. A slightly tilted head, arms raised in a hug, or legs positioned mid-run all give personality. Use long tails from cast-off ends to sew parts together—no fresh yarn needed.",
            "Use a whip stitch or invisible ladder stitch for cleanest results. Take your time. A well-assembled amigurumi with slightly wonky stitches looks better than a technically perfect one that is sewn together crooked.",
        ],
    },
    {
        "id": "practice-plan",
        "heading": "A four-project practice plan",
        "paragraphs": [
            "Your first four amigurumi should build skills in order. Start with a simple mushroom (round shape, one color, no assembly). Then a bumblebee (color changes, small wings sewn on). Then a rabbit (multiple body parts assembled together). Finally, a bigger character with clothing details (adds complexity like embroidery and detail work).",
            "By the fourth project, most of the confusion has been replaced with confidence. If you have leftover yarn from these projects, [[scrap-yarn-projects|our scrap yarn guide]] has ideas for the tiny amounts amigurumi always leaves behind.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Amigurumi rewards slowness and attention. Every tiny animal you finish is a small sculpture, a tiny gift, and a snapshot of the specific week you made it. Pick a simple pattern this weekend, work it in bright cotton, and enjoy watching a flat spiral become a small friend that looks back at you from your shelf.",
        ],
    },
]


CROCHET_HACKS_BODY = [
    {
        "id": "why-hacks",
        "heading": "Small habits that add up to hours saved",
        "paragraphs": [
            "Crochet 'hacks' are not miracle shortcuts. They are small studio habits that add up to real time savings over the course of a project—or the course of a lifetime. Every one of the five habits below solves a specific real-world friction: finding the beginning of a row, keeping ends from unraveling, transporting a project without a tangle, sitting comfortably for hours, and switching colors without a jog.",
            "None of these tricks changes what your hands do at the hook. They change what your studio does around your hands, so the hook can move without interruption. Try one this week and notice how much more relaxing your next project feels.",
        ],
    },
    {
        "id": "hack-1-markers",
        "heading": "Hack 1: A stitch marker in every project",
        "paragraphs": [
            "The single most valuable habit in crochet is placing a stitch marker at the start of every row of every project. It sounds excessive. It is not. Locking-loop stitch markers cost a few dollars for a pack of fifty. Clip one onto the first stitch of row one as soon as you finish that stitch. Move it up one row at a time.",
            "This tiny habit means you never lose your place when you set a project down. It means you can spot a growing or shrinking row within one row instead of five. And it means picking up a project after a long break feels instant instead of confusing. Every experienced crocheter I know does this. Every frustrated beginner I know does not.",
        ],
    },
    {
        "id": "hack-2-tail-management",
        "heading": "Hack 2: Weave in ends as you go",
        "paragraphs": [
            "Weaving in ends is the least loved part of crochet. Almost every crocheter procrastinates it, then finishes ten ends in one exhausted evening at the end of a big project. Try the opposite: weave in every yarn tail immediately after joining a new color or finishing a section. It takes ninety seconds each time. Skipping it saves nothing, because you still have to do it eventually.",
            "For projects with many color changes, carry the non-working yarn along the top of the previous row and crochet over it. This traps the strand inside the fabric and eliminates a tail entirely. It works especially well for tapestry crochet and color-block blankets.",
        ],
    },
    {
        "id": "hack-3-project-bag",
        "heading": "Hack 3: A dedicated project bag per project",
        "paragraphs": [
            "One project, one bag. Do not mix yarn from different projects in the same tote. Even the most careful crocheter ends up with tangled strands and missing hooks when two skeins share a bag. A five-dollar zippered pouch dedicated to one specific project keeps everything together—yarn, hook, pattern, notes, and a stitch marker.",
            "For traveling crocheters, add a small pair of folding scissors and a tapestry needle to the bag. Then any waiting room, airport gate, or car ride becomes an opportunity to work a few rows. Progress without extra setup is the whole point.",
        ],
    },
    {
        "id": "hack-4-ergonomics",
        "heading": "Hack 4: Small ergonomic adjustments prevent big pain",
        "paragraphs": [
            "Wrist and neck pain are the biggest reasons crocheters take unwanted breaks from the craft. Prevent them with three simple changes. First, sit with the project supported in your lap rather than reaching for a hook held in the air. Second, rest your hands every twenty minutes, even briefly, and stretch your fingers. Third, use an ergonomic hook if you already feel tension in your grip—rubber grips or wooden hooks with a barrel-shaped handle both reduce strain significantly.",
            "For long sessions, work in shorter blocks of twenty to thirty minutes rather than one long marathon. Small breaks preserve your hands. Marathon sessions punish them.",
        ],
    },
    {
        "id": "hack-5-jogless-stripes",
        "heading": "Hack 5: The jogless stripe",
        "paragraphs": [
            "When you change colors in the round, the join usually looks jaggy—the last stitch of the old color sits slightly higher than the first stitch of the new. This is called a 'jog.' The fix is quick: when you start the new color, work the first stitch of the round into the stitch below the join instead of the stitch directly at the join. This drops the new color down one round so the seam smoothly aligns.",
            "It takes one round of practice to feel natural. After that, every color change in the round looks like a professional finish. Combined with the other four hacks, this is the difference between crochet that says 'homemade' and crochet that says 'handmade.'",
        ],
    },
    {
        "id": "beyond",
        "heading": "Beyond the five: making them stick",
        "paragraphs": [
            "Reading a hack list is easy. Making the habits automatic takes about three projects. Choose one hack, use it on your next project without exception, and notice how it feels. Then add a second. In a few months, all five will be automatic parts of how you work.",
            "For studio organization, our [[best-yarn-for-crochet|yarn buyer's guide]] pairs well with these habits—buying yarn thoughtfully means less yarn wasted on mistakes and less clutter over time.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Crochet gets more joyful when small friction disappears. Every hack in this guide removes one source of friction. Pick the one that solves the problem you notice most often, use it this week, and let it become part of how your hands work. That is how a craft turns into a long-term practice—one small habit at a time.",
        ],
    },
]


FIX_DROPPED_STITCH_BODY = [
    {
        "id": "dont-panic",
        "heading": "First: do not unravel the whole thing",
        "paragraphs": [
            "The moment you notice a dropped stitch, a mistake three rows back, or an unexpected hole in your fabric, your first instinct is often to pull the whole piece apart and start over. Resist that instinct for at least five minutes. Almost every crochet mistake can be repaired without destroying the piece, and the repair usually takes less time than restarting.",
            "This guide walks through the most common in-progress repairs so you can confidently fix a mistake and keep going. Bookmark this page and refer back the next time your work looks off. Panic wastes yarn; patience saves projects.",
        ],
    },
    {
        "id": "identify",
        "heading": "Identify the mistake first",
        "paragraphs": [
            "Before doing anything, put the work flat on a table and examine it in good light. Look for the specific mistake: a dropped stitch (an empty loop where a stitch should be), an added stitch (extra bump in the row), a stitch worked in the wrong place, or a color that started or ended in the wrong row. Naming the mistake makes the fix obvious.",
            "Count your stitches in the current row and the previous row. If the counts disagree, the mistake is on the higher row. If they agree, the mistake is somewhere in the pattern—maybe a wrong stitch type or the wrong turning chain.",
        ],
    },
    {
        "id": "ladder-rescue",
        "heading": "The ladder rescue for a dropped stitch",
        "paragraphs": [
            "If a single stitch dropped several rows down and 'laddered' (fell open like a run in a stocking), you can rescue it with a spare hook. Insert the hook into the live loop at the bottom of the ladder, catch the loose horizontal strand above it, and pull it through. Repeat up the ladder, one strand at a time, until the stitch reaches the current row.",
            "This works best in single crochet and half double crochet. For taller stitches like double crochet, the reconstruction is trickier—it may be faster to tink back to the mistake instead. Practice this technique on a small swatch before you need it on a real project.",
        ],
    },
    {
        "id": "tink",
        "heading": "Tink back one stitch at a time",
        "paragraphs": [
            "'Tinking' is knitting slang for unworking stitches one at a time. In crochet, it means undoing one stitch backward until you reach the mistake. Take out your hook, pull the working yarn to open the last stitch, and reinsert the hook one stitch earlier. Repeat until you are just before the mistake, then work forward again with the correction.",
            "Tinking is precise and preserves the surrounding fabric perfectly. It is the right choice when you cannot see the mistake clearly enough to isolate it, or when the mistake is a wrong stitch type rather than a dropped loop.",
        ],
    },
    {
        "id": "frog",
        "heading": "Frog when you have to, and only what you have to",
        "paragraphs": [
            "'Frogging' means pulling out multiple rows or an entire section. Sometimes it is the fastest fix, especially when a mistake is more than five rows back or the pattern went off in a way that would be tedious to tink. Frog carefully—slide your hook out first, then pull the yarn slowly to unravel row by row rather than yanking.",
            "Wind the freed yarn back into a small ball as you go so it does not tangle. Once you reach the row just before the mistake, insert your hook into the live loop, pull the working yarn firmly, and resume the pattern. Frogging is not a failure; it is a normal part of the craft.",
        ],
    },
    {
        "id": "lifelines",
        "heading": "Use lifelines for complex patterns",
        "paragraphs": [
            "For lace, colorwork, and other patterns where a mistake could cascade, use a lifeline. A lifeline is a piece of contrasting-color scrap yarn threaded through every stitch of a completed row. If you make a serious mistake later, you can rip back safely to the lifeline without losing the whole piece below.",
            "Place a lifeline every ten rows or after every completed pattern repeat. This tiny piece of insurance is what allows experienced crocheters to work confidently through complex charts.",
        ],
    },
    {
        "id": "post-repair",
        "heading": "After the repair: check tension carefully",
        "paragraphs": [
            "A repair almost always disturbs surrounding tension slightly. Look at the fixed area from a distance to spot any tight or loose stitches. If a repaired area is slightly tighter than the rest, blocking the finished piece usually evens it out. If it is much looser, tighten by pulling the yarn tail gently and reworking the ends into the fabric.",
            "For a full breakdown of what causes uneven tension in the first place, [[even-crochet-stitches|our even stitches guide]] covers the specific habits that prevent most of these repairs from being needed at all.",
        ],
    },
    {
        "id": "prevention",
        "heading": "Prevention is easier than repair",
        "paragraphs": [
            "The best repair is the one you never have to make. Count stitches at the end of every row. Use stitch markers to lock the first and last stitches of each row. Photograph a completed section before starting a new one; if something goes wrong, the photo shows you exactly what the piece is supposed to look like. Small habits like these prevent the majority of the mistakes this guide teaches you to fix.",
            "Common mistakes and their fixes are covered in more depth in [[common-crochet-mistakes|our ten mistakes guide]]—read it alongside this one to build a full mental library of common problems and their solutions.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Every experienced crocheter has repaired their work dozens of times. The difference between an experienced and a beginner crocheter is not fewer mistakes—it is faster, calmer recovery from them. Practice one of these repair techniques on a scrap swatch this week, and the next time a real project needs a fix, your hands will already know what to do.",
        ],
    },
]


BLANKET_PATTERNS_BODY = [
    {
        "id": "blankets-anchor",
        "heading": "Why blankets are the anchor project of crochet",
        "paragraphs": [
            "Blankets are the reason many people start crocheting and the reason many keep going. They are big enough to feel meaningful, forgiving enough to work through beginner mistakes, and practical enough to actually use for the rest of your life. A finished blanket says 'someone made this on purpose' in a way that few store-bought objects ever manage. Whether you are making one for yourself, a friend's baby shower, or a housewarming gift, the right pattern turns hours of stitching into a finished object you will love.",
            "This guide walks through choosing a blanket size, matching stitch style to skill level, calculating yarn needs, joining strategies, and finishing touches. Read the whole thing before starting your first blanket—the small decisions before you cast on shape the entire experience.",
        ],
    },
    {
        "id": "size",
        "heading": "Choose a size before choosing a stitch",
        "paragraphs": [
            "Blanket size determines almost everything else: yarn needed, hours required, and portability of the work in progress. A small lap blanket (about 36x48 inches) uses about 1,000 yards of worsted yarn and finishes in 20-30 hours. A throw (50x60 inches) uses 1,600-2,000 yards. A queen bed cover (90x90 inches) can use 4,000-5,000 yards and take a full season. Match the size to the amount of time and yarn you can realistically commit.",
            "Baby blankets are the best first blanket because they finish quickly (600-1,000 yards is typical) and let you experiment with color and stitch pattern without a huge commitment. A finished baby blanket also makes an unforgettable gift for any new parent in your life.",
        ],
    },
    {
        "id": "granny",
        "heading": "The classic granny square: beginner-friendly and portable",
        "paragraphs": [
            "A granny square blanket is made of many small squares stitched together. It is the most beginner-friendly blanket style because each square finishes quickly (usually in under 15 minutes for a small square), the pattern is simple to memorize, and portability is excellent—you can work squares anywhere. Making 40-80 squares and joining them produces a stunning blanket that looks intentional even from your first granny.",
            "Modern granny squares don't have to look grandma-vintage. Choose a modern palette—muted terracottas, sages, and creams—for a contemporary feel. For a designer-look interpretation, [[modern-granny-square-skirt-vest|our modern granny fashion guide]] shows how the same square translates to garment design.",
        ],
    },
    {
        "id": "c2c",
        "heading": "Corner-to-corner (C2C): fast and forgiving",
        "paragraphs": [
            "The corner-to-corner method starts with a single square in one corner and grows diagonally, adding one small square-block per row. It works up surprisingly fast and is very forgiving of tension inconsistencies because each block resets the count. C2C is also excellent for graphghans—blankets that display a pixelated image, from initials to full pictures.",
            "C2C shines in bold color-block patterns. Choose 2-4 colors for maximum impact. Beginners can master this style in a single afternoon of practice, and each finished row shows visible progress that motivates continued work.",
        ],
    },
    {
        "id": "textured",
        "heading": "Textured stitches for cozy weight",
        "paragraphs": [
            "Textured stitches—bobbles, popcorns, cables, and puff stitches—produce blankets with visible depth and satisfying weight. They use more yarn per square inch than plain stitches, so plan for 20-30% more yarn than a comparable stitch pattern. Textured blankets are especially rewarding to touch and photograph beautifully in soft neutrals.",
            "The chevron and shell stitch patterns are the most beginner-friendly textured options. Both use stitch groups worked over a repeat, and both look impressive from row one. If you have never worked a shell or chevron, practice on a small square before committing yarn for a full blanket.",
        ],
    },
    {
        "id": "mosaic",
        "heading": "Mosaic crochet: modern, striking, meditative",
        "paragraphs": [
            "Mosaic crochet is a modern style that uses two colors and simple stitches (mostly single and double crochet) to create bold geometric patterns. Unlike tapestry crochet, you only carry one color per row—no juggling multiple strands. The finished fabric looks like a painting made of stitches, and once the rhythm clicks, it is one of the most meditative crochet styles.",
            "Mosaic charts look intimidating but are surprisingly simple once you understand the rules. Read a mosaic tutorial before starting a full blanket, and always work a full pattern repeat on a swatch to make sure the yarn colors have enough contrast to read clearly.",
        ],
    },
    {
        "id": "yarn-planning",
        "heading": "How to plan yarn for a blanket",
        "paragraphs": [
            "Start with a total yardage estimate for your chosen pattern (patterns almost always list this). Divide that number by the yards per skein of your chosen yarn to know how many skeins to buy. Add 10-15% extra for safety and to account for dye lot variations. If your blanket needs 8 skeins, buy 9. If it needs 15, buy 17.",
            "Always buy from the same dye lot. Dye lot numbers appear on the yarn label and slightly different lots can produce visibly different color stripes in the finished blanket. If you cannot get one dye lot for the full amount, plan color changes so each dye lot occupies its own section. Full guidance is in [[best-yarn-for-crochet|our yarn buyer's guide]].",
        ],
    },
    {
        "id": "joining",
        "heading": "Joining squares and adding borders",
        "paragraphs": [
            "For blankets made of separate squares, joining is a design decision. Slip stitch joins produce a clean seam and add minimal bulk. Whip stitch joins are almost invisible and drape beautifully. The join-as-you-go method connects each square to the previous ones during the last round of that square, and it is the tidiest option once you have practice.",
            "A border adds finish and structure. Even one simple round of single crochet cleans up the edges dramatically. For a fancier finish, add two or three rounds in a contrasting color or a shell edge. Do not skip the border, especially for gifting; a bordered blanket looks intentional in a way an unbordered one never does.",
        ],
    },
    {
        "id": "care",
        "heading": "Blocking, washing, and long-term care",
        "paragraphs": [
            "Once the blanket is finished, wet block it. Fill a bathtub with cool water and a small amount of gentle detergent, submerge the blanket, gently squeeze out excess water in towels, and lay flat to dry on more towels. This evens tension and softens the fabric permanently.",
            "For long-term care, wash in cool water on a gentle cycle if the yarn is superwash or acrylic. Hand-wash any wool or delicate fibers. Store the blanket folded, not hung; hanging distorts the shape over time. Well-made blankets last for decades if cared for gently.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "The blanket you make this year could be the one your family reaches for a decade from now. Choose a pattern that excites you, buy enough yarn from one dye lot, and give yourself weekly milestones so the size feels manageable. Every square finished is progress, and every finished blanket is a small piece of your care made physical. Start this weekend.",
        ],
    },
]


SELL_ONLINE_BODY = [
    {
        "id": "hobby-to-business",
        "heading": "From hobby to income, honestly",
        "paragraphs": [
            "Turning crochet into a small income stream is possible, but it looks very different from what most social media makes it look like. Building a sustainable side income takes six to twelve months of steady work: photography, pricing, product listings, customer service, and shipping logistics all matter as much as the stitching itself. If you approach it with realistic expectations and a plan, it can become a meaningful supplement to your income and a satisfying creative career.",
            "This guide walks through the practical decisions that separate a hobby from a small business. Read the whole thing before opening a shop—the choices you make in month one shape everything that follows. Nothing here is fluff, and nothing promises overnight success.",
        ],
    },
    {
        "id": "pricing",
        "heading": "Pricing that actually pays you",
        "paragraphs": [
            "Most new sellers underprice by a factor of three. The formula that works: (materials + hourly labor + overhead) x profit margin. For example, an amigurumi that used $4 of yarn and took 3 hours of your time at $15/hour uses $49 in cost before overhead. Add 20-30% for platform fees, taxes, and business expenses, then apply a 2x markup for profit. Sale price: roughly $110-130.",
            "Many hobbyists feel awkward pricing this high, but underpricing hurts everyone: it burns you out and it lowers the market price for other crocheters. If your target market cannot afford your true price, reconsider the product, not the price. Simpler patterns, faster stitches, or larger production runs can lower cost without lowering value.",
        ],
    },
    {
        "id": "photography",
        "heading": "Photography sells more than the product",
        "paragraphs": [
            "Buyers cannot touch a handmade item online. They can only trust your photos. Great photography does not require professional equipment—a modern smartphone in natural window light produces excellent results. Photograph each product against a clean, neutral background (a white sheet or a wood table both work), from at least four angles, plus one lifestyle shot showing the piece in use.",
            "Edit lightly: brighten, straighten, and crop. Do not oversaturate colors. Your customer needs to see accurate color so they are not disappointed when the physical piece arrives. Product photography quality often has more effect on sales than product quality itself.",
        ],
    },
    {
        "id": "platforms",
        "heading": "Where to sell: Etsy, Instagram, or your own site",
        "paragraphs": [
            "Etsy is the easiest starting point: built-in audience, established trust with buyers, straightforward listings. The tradeoff is fees (10-15% total after payment processing) and competition from thousands of similar shops. Instagram sells through direct messages and stories; it has zero fees but requires steady content creation to build an audience.",
            "Your own website (Shopify, Squarespace, or a simple hosted store) offers full control and no per-sale fees, but it requires you to drive all your own traffic. Start with Etsy or Instagram for the first year. Move to your own site once you have a repeat-customer base large enough to sustain a launch.",
        ],
    },
    {
        "id": "listings",
        "heading": "Listings that actually convert",
        "paragraphs": [
            "A great listing has four parts: a clear title (product type + material + audience: 'Handmade Cotton Amigurumi Bumblebee for Baby Room'), a detailed description that answers common questions (size, care, shipping, materials), keyword-rich tags, and honest photos. Buyers scan; they do not read. Put the most important information in the first two sentences of every description.",
            "Include care instructions, size measurements, and estimated shipping time. Every question your listing does not answer becomes a message that delays purchase. The best listings feel like a friendly, informed salesperson who happens to be reading the buyer's mind.",
        ],
    },
    {
        "id": "shipping",
        "heading": "Shipping without losing money",
        "paragraphs": [
            "Shipping is where many new sellers lose money. Weigh a fully packaged sample of each product on a kitchen scale before setting shipping prices. Include the box, tissue paper, business card, and any padding. Use flat-rate shipping options whenever possible—USPS Priority Mail flat-rate boxes are your friend for small-to-medium items.",
            "Package everything as if it were a gift for a friend. Tissue paper, a small thank-you card, and a business card add almost no cost but transform the unboxing experience. Repeat buyers come from small delights like this.",
        ],
    },
    {
        "id": "customer-service",
        "heading": "Customer service builds a business",
        "paragraphs": [
            "Reply to every message within 24 hours. Address concerns kindly, even when the buyer is being unreasonable. Offer solutions before defending yourself. A single well-handled negative review often produces more sales than avoiding negative reviews entirely, because it shows future buyers how you treat problems.",
            "Track every sale in a simple spreadsheet: buyer name, item, ship date, tracking number, and any special notes. This becomes the backbone of your business as it grows and prevents the small errors that create bad reviews.",
        ],
    },
    {
        "id": "taxes",
        "heading": "Legal and tax basics",
        "paragraphs": [
            "In the United States, income from selling handmade items is taxable. Track every sale and every expense from day one. Save receipts for yarn, tools, packaging supplies, and shipping. Most small crochet businesses file as sole proprietors on Schedule C of a regular tax return.",
            "Once your business exceeds $600 in a year, platforms like Etsy report your income to the IRS. Consult a local accountant for state-specific sales tax rules and business license requirements. This step feels tedious but prevents surprises at tax time.",
        ],
    },
    {
        "id": "sustainability",
        "heading": "Building a sustainable practice",
        "paragraphs": [
            "The biggest risk in selling handmade is burnout. If every crochet project becomes a job, the joy that made you start selling disappears. Set clear working hours, take real breaks, and give yourself permission to close the shop temporarily when needed. Repeat customers understand.",
            "Diversify what you sell over time. Pattern PDFs, tutorial ebooks, and finished items each have different labor profiles and different customer bases. Our full [[best-yarn-for-crochet|yarn buyer's guide]] can also help you source materials at prices that keep your profit margins healthy.",
        ],
    },
    {
        "id": "next-loop",
        "heading": "Your next loop",
        "paragraphs": [
            "Turning crochet into income is a marathon, not a sprint. Choose one product, price it correctly, photograph it well, list it once, and see what happens. Adjust based on real feedback, not imagined pressure. In a year of small, consistent choices, you will have a real small business that pays you fairly for the beautiful work you already know how to do.",
        ],
    },
]



def _full(slug, title, category, excerpt, image_key, read_time, date, body):
    """Assemble a full article entry with a unique long-form body."""
    return {
        "slug": slug,
        "title": title,
        "category": category,
        "excerpt": excerpt,
        "image": IMAGES[image_key],
        "read_time": read_time,
        "date": date,
        "sections": None,
        "body": body,
        "draft": False,
    }


ARTICLES_SEED = [
    _full("crochet-for-absolute-beginners", "Crochet for Absolute Beginners: The Only Guide You'll Ever Need", "Beginners", "A calm, confidence-building first step into hooks, yarn, and your very first row.", "beginner_hook", "9 min read", "January 8, 2026", BEGINNERS_GUIDE_BODY),
    _full("common-crochet-mistakes", "10 Common Crochet Mistakes (and How to Fix Them Fast)", "Beginners", "The little fixes that make your stitches neater, your edges straighter, and practice more fun.", "mistakes", "9 min read", "January 12, 2026", COMMON_MISTAKES_BODY),
    _full("even-crochet-stitches", "The Secret to Perfectly Even Stitches Every Single Time", "Stitch School", "A practical rhythm for consistent tension, tidy edges, and fabric you actually love.", "even_stitches", "8 min read", "January 15, 2026", EVEN_STITCHES_BODY),
    _full("read-crochet-pattern", "How to Read a Crochet Pattern Like a Pro (Step-by-Step)", "Beginners", "Decode abbreviations, repeats, and charts without losing your place.", "pattern_read", "10 min read", "January 18, 2026", READ_PATTERN_BODY),
    _full("best-yarn-for-crochet", "Best Yarn for Every Type of Crochet Project (Buyer's Guide)", "Yarn Guide", "Choose fibers and weights with confidence, from soft blankets to sturdy bags.", "yarn_variety", "11 min read", "January 22, 2026", BEST_YARN_BODY),
    _full("amigurumi-101", "Amigurumi 101: Cute Crochet Animals for Beginners", "Amigurumi", "Start with friendly shapes, simple stuffing, and the details that bring tiny animals to life.", "amigurumi_alt", "10 min read", "January 25, 2026", AMIGURUMI_101_BODY),
    _full("crochet-hacks", "5 Crochet Hacks That Will Save You Hours of Frustration", "Crochet Life", "Five small studio habits that rescue time, yarn, and your patience.", "hacks_studio", "8 min read", "January 28, 2026", CROCHET_HACKS_BODY),
    _full("fix-dropped-stitch", "How to Fix a Dropped Stitch or Mistake Without Starting Over", "Stitch School", "Repair your work with a hook, a calm breath, and a simple visual check.", "dropped_stitch", "9 min read", "January 30, 2026", FIX_DROPPED_STITCH_BODY),
    _full("crochet-blanket-patterns", "Crochet Blanket Patterns: Cozy Projects for Every Skill Level", "Patterns", "Find the right blanket rhythm for a weekend, a season, or a lifetime keepsake.", "blanket_stack", "10 min read", "February 1, 2026", BLANKET_PATTERNS_BODY),
    _full("sell-crochet-online", "From Hobby to Side Hustle: How to Sell Your Crochet Creations Online", "Crochet Life", "A grounded starter plan for pricing, photographing, and sharing handmade work.", "sell_business", "11 min read", "February 3, 2026", SELL_ONLINE_BODY),
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
    {
        "slug": "scrap-yarn-projects",
        "title": "What to Do With Leftover Yarn: 12 Creative Scrap Yarn Ideas You'll Actually Use",
        "category": "Yarn Guide",
        "excerpt": "Twelve practical, cozy ways to turn a scrap yarn stash into finished projects—plus the sorting, color, and storage tricks that make everything look intentional.",
        "image": IMAGES["scrap_yarn"],
        "read_time": "9 min read",
        "date": "February 12, 2026",
        "sections": None,
        "body": SCRAP_YARN_BODY,
        "draft": False,
    },
    {
        "slug": "upcycle-thrifted-denim-crochet",
        "title": "From Trash to Trend: Upcycling Thrifted Denim with Freeform Crochet Edges",
        "category": "Clothing",
        "excerpt": "A step-by-step, sustainability-first guide to sourcing thrifted denim, choosing durable yarn, and adding freeform crochet edges that make forgotten jackets and jeans wearable again.",
        "image": IMAGES["denim"],
        "read_time": "10 min read",
        "date": "February 15, 2026",
        "sections": None,
        "body": DENIM_UPCYCLE_BODY,
        "draft": False,
    },
    {
        "slug": "easy-round-crochet-placemat",
        "title": "How to Crochet an Easy Round Placemat in Under 2 Hours (Step-by-Step)",
        "category": "Patterns",
        "excerpt": "A beginner-friendly round crochet placemat pattern using US crochet terms, worsted cotton, and only three stitches — finished in under two hours with a soft shell edging.",
        "image": IMAGES["placemat_home"],
        "read_time": "9 min read",
        "date": "February 18, 2026",
        "sections": None,
        "body": PLACEMAT_BODY,
        "draft": False,
    },
    {
        "slug": "micro-crochet-jewelry-embroidery-floss-earrings",
        "title": "Micro-Crochet Jewelry: Turning Embroidery Floss into Heirloom Earrings",
        "category": "Patterns",
        "excerpt": "A practical, tension-first guide to making delicate micro-crochet jewelry with six-strand embroidery floss, ultra-fine steel hooks, and a magic-ring lace earring pattern you can finish this weekend.",
        "image": IMAGES["micro_jewelry"],
        "read_time": "11 min read",
        "date": "February 22, 2026",
        "sections": None,
        "body": MICRO_CROCHET_JEWELRY_BODY,
        "draft": False,
    },
    {
        "slug": "crochet-lampshades-cozy-lighting",
        "title": "Crochet Lampshades and Lantern Covers: Cozy Lighting Ideas for Small Spaces",
        "category": "Patterns",
        "excerpt": "Two beginner-friendly crochet lighting projects—a simple LED lantern cover and a hanging pendant cover with floral buttons—that transform small spaces in a single weekend.",
        "image": IMAGES["lamp_cozy"],
        "read_time": "10 min read",
        "date": "February 25, 2026",
        "sections": None,
        "body": LAMPSHADE_BODY,
        "draft": False,
    },
    {
        "slug": "japanese-knot-bag-crochet-pattern",
        "title": "The Japanese Knot Bag: A Beginner Crochet Pattern With Real-Life Geometry",
        "category": "Patterns",
        "excerpt": "A modern, hardware-free Japanese knot bag crochet pattern with asymmetric handles, sturdy cotton body, and everyday utility—finished in under three hours and worn like it came from a boutique.",
        "image": IMAGES["knot_bag"],
        "read_time": "10 min read",
        "date": "March 1, 2026",
        "sections": None,
        "body": JAPANESE_KNOT_BAG_BODY,
        "draft": False,
    },
    {
        "slug": "modern-granny-square-skirt-vest",
        "title": "Modern Granny Square Fashion: How to Design Asymmetric Skirts and Vests",
        "category": "Clothing",
        "excerpt": "A designer-minded guide to turning classic granny squares into modern, asymmetric skirts and cropped vests—scale, palette, layout, joining, and finishing choices that make handmade look editorial.",
        "image": IMAGES["granny_fashion"],
        "read_time": "11 min read",
        "date": "March 5, 2026",
        "sections": None,
        "body": GRANNY_SQUARE_FASHION_BODY,
        "draft": False,
    },
    {
        "slug": "crochet-tissue-box-cover-buttons",
        "title": "Crochet Tissue Box Cover with Side Buttons: A Year-Round Home Accessory",
        "category": "Patterns",
        "excerpt": "A practical crochet tissue box cover pattern with side buttons instead of sewn seams—refills in twenty seconds, fits cube and rectangular boxes, and quietly upgrades every room of the house.",
        "image": IMAGES["tissue_home"],
        "read_time": "10 min read",
        "date": "March 8, 2026",
        "sections": None,
        "body": TISSUE_BOX_COVER_BODY,
        "draft": False,
    },
    {
        "slug": "crochet-flowers-bandanas-on-denim",
        "title": "Details Worth Their Weight: Adding Crochet Flowers and Bandanas to Denim",
        "category": "Clothing",
        "excerpt": "A ten-year-tested guide to sewing small crochet flowers and mini bandanas onto denim—patterns, placement, and boho-meets-urban styling that upgrades any jean jacket, shirt, or pair of jeans in an afternoon.",
        "image": IMAGES["denim_flowers"],
        "read_time": "10 min read",
        "date": "March 12, 2026",
        "sections": None,
        "body": DENIM_FLOWERS_BANDANAS_BODY,
        "draft": False,
    },
]

CATEGORIES = ["All", "Beginners", "Stitch School", "Amigurumi", "Yarn Guide", "Patterns", "Clothing", "Crochet Life"]
