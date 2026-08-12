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
]

CATEGORIES = ["All", "Beginners", "Stitch School", "Amigurumi", "Yarn Guide", "Patterns", "Clothing", "Crochet Life"]
