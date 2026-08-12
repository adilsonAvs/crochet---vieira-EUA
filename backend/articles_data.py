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
    "denim": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=1200&q=80",
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
    {
        "slug": "scrap-yarn-projects",
        "title": "What to Do With Leftover Yarn: 12 Creative Scrap Yarn Ideas You'll Actually Use",
        "category": "Yarn Guide",
        "excerpt": "Twelve practical, cozy ways to turn a scrap yarn stash into finished projects—plus the sorting, color, and storage tricks that make everything look intentional.",
        "image": IMAGES["yarn"],
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
        "image": IMAGES["blanket"],
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
        "image": IMAGES["yarn"],
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
        "image": IMAGES["blanket"],
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
        "image": IMAGES["denim"],
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
        "image": IMAGES["tops"],
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
        "image": IMAGES["blanket"],
        "read_time": "10 min read",
        "date": "March 8, 2026",
        "sections": None,
        "body": TISSUE_BOX_COVER_BODY,
        "draft": False,
    },
]

CATEGORIES = ["All", "Beginners", "Stitch School", "Amigurumi", "Yarn Guide", "Patterns", "Clothing", "Crochet Life"]
