/* eslint-disable react/no-unescaped-entities */
import { useEffect, useState, createContext, useContext, useRef, useMemo } from "react";
import { BrowserRouter, Routes, Route, Link, useParams, useLocation } from "react-router-dom";
import { ArrowRight, Menu, X, Mail, Instagram, Check, Cookie } from "lucide-react";
import axios from "axios";
import "./App.css";
import AdminPage from "./AdminPage";
import CommentSection from "./CommentSection";

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;
const ADSENSE_CLIENT = process.env.REACT_APP_ADSENSE_CLIENT || "";
const GSC_VERIFICATION = process.env.REACT_APP_GOOGLE_SITE_VERIFICATION || "";
const GA4_ID = process.env.REACT_APP_GA4_MEASUREMENT_ID || "";
const PINTEREST_VERIFY = process.env.REACT_APP_PINTEREST_VERIFY || "";
const AUTHOR = "Claire Lawson";
const SITE = "Cozy Crochet Trail";
const DEFAULT_OG_IMAGE = "https://images.unsplash.com/photo-1668072587859-f0f30c8fa938?auto=format&fit=crop&w=1200&q=80";

const CATEGORY_DESCRIPTIONS = {
  "Beginners": "Your first stitches, first patterns, and the calm foundations every new crocheter deserves.",
  "Stitch School": "Tension, tidy edges, and consistent stitches—the small habits that make finished pieces feel intentional.",
  "Amigurumi": "Tiny, expressive crochet animals that live on shelves, in gift bags, and in your favorite people's pockets.",
  "Yarn Guide": "Fibers, weights, washability, and buying advice from someone who has spent too much on the wrong skein.",
  "Patterns": "Blanket, throw, and cozy home patterns for weekend afternoons and slower seasons.",
  "Clothing": "Wearable crochet—tops, sweaters, and refashioned pieces that fit your body and your style.",
  "Crochet Life": "The habits, tools, side hustles, and everyday choices that make a hook feel like a lifelong friend.",
};
const categorySlug = (name) => name.toLowerCase().replace(/ /g, "-");
const categoryFromSlug = (slug, cats) => cats.find(c => categorySlug(c) === slug);

const DataContext = createContext({ articles: [], categories: ["All"], loading: true });
const useData = () => useContext(DataContext);

function Meta({ title, description, image, type = "website" }) {
  useEffect(() => {
    document.title = title;
    const setMeta = (key, content, attr = "name") => {
      let m = document.querySelector(`meta[${attr}="${key}"]`);
      if (!m) {
        m = document.createElement("meta");
        m.setAttribute(attr, key);
        document.head.appendChild(m);
      }
      m.setAttribute("content", content);
    };
    const img = image || DEFAULT_OG_IMAGE;
    const url = typeof window !== "undefined" ? window.location.href : "";
    setMeta("description", description);
    setMeta("og:title", title, "property");
    setMeta("og:description", description, "property");
    setMeta("og:type", type, "property");
    setMeta("og:site_name", SITE, "property");
    setMeta("og:image", img, "property");
    if (url) setMeta("og:url", url, "property");
    setMeta("twitter:card", "summary_large_image");
    setMeta("twitter:title", title);
    setMeta("twitter:description", description);
    setMeta("twitter:image", img);
    // Canonical link — helps Google pick the preferred URL
    if (url) {
      let canonical = document.querySelector('link[rel="canonical"]');
      if (!canonical) {
        canonical = document.createElement("link");
        canonical.setAttribute("rel", "canonical");
        document.head.appendChild(canonical);
      }
      canonical.setAttribute("href", url.split("#")[0].split("?")[0]);
    }
  }, [title, description, image, type]);
  return null;
}

function AdSenseLoader() {
  useEffect(() => {
    if (!ADSENSE_CLIENT || document.getElementById("adsense-script")) return;
    const s = document.createElement("script");
    s.id = "adsense-script";
    s.async = true;
    s.crossOrigin = "anonymous";
    s.src = `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${ADSENSE_CLIENT}`;
    document.head.appendChild(s);
  }, []);
  return null;
}

function SearchConsoleVerification() {
  useEffect(() => {
    if (GSC_VERIFICATION && !document.querySelector('meta[name="google-site-verification"]')) {
      const m = document.createElement("meta");
      m.name = "google-site-verification";
      m.content = GSC_VERIFICATION;
      document.head.appendChild(m);
    }
    if (PINTEREST_VERIFY && !document.querySelector('meta[name="p:domain_verify"]')) {
      const m = document.createElement("meta");
      m.name = "p:domain_verify";
      m.content = PINTEREST_VERIFY;
      document.head.appendChild(m);
    }
  }, []);
  return null;
}

function GA4Loader() {
  useEffect(() => {
    if (!GA4_ID || document.getElementById("ga4-script")) return;
    const s = document.createElement("script");
    s.async = true;
    s.id = "ga4-script";
    s.src = `https://www.googletagmanager.com/gtag/js?id=${GA4_ID}`;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", GA4_ID, { send_page_view: false });
  }, []);
  return null;
}

function GA4PageView() {
  const location = useLocation();
  useEffect(() => {
    if (!GA4_ID || !window.gtag) return;
    window.gtag("event", "page_view", {
      page_path: location.pathname + location.search,
      page_title: document.title,
      page_location: window.location.href,
    });
  }, [location]);
  return null;
}

function AdSlot({ slot = "auto", format = "auto", testId = "article-ad-placeholder" }) {
  const ref = useRef(false);
  useEffect(() => {
    if (!ADSENSE_CLIENT || ref.current) return;
    ref.current = true;
    try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) { /* noop */ }
  }, []);
  if (!ADSENSE_CLIENT) return null;
  return (
    <ins className="adsbygoogle ad-slot" style={{ display: "block" }}
      data-ad-client={ADSENSE_CLIENT} data-ad-slot={slot}
      data-ad-format={format} data-full-width-responsive="true" data-testid={testId} />
  );
}

function JsonLd({ data, id }) {
  useEffect(() => {
    const existing = document.getElementById(id);
    if (existing) existing.remove();
    const s = document.createElement("script");
    s.type = "application/ld+json";
    s.id = id;
    s.text = JSON.stringify(data);
    document.head.appendChild(s);
    return () => { document.getElementById(id)?.remove(); };
  }, [id, data]);
  return null;
}

function Header() {
  const [open, setOpen] = useState(false);
  return (
    <header className="site-header">
      <div className="nav-wrap">
        <Link data-testid="site-logo-link" className="logo" to="/">
          <span className="logo-mark">CT</span>
          <span>Cozy Crochet<small>TRAIL</small></span>
        </Link>
        <button data-testid="mobile-menu-button" className="icon-btn mobile-only" onClick={() => setOpen(!open)} aria-label="Toggle menu">
          {open ? <X /> : <Menu />}
        </button>
        <nav data-testid="main-navigation" className={open ? "nav-links open" : "nav-links"}>
          <Link data-testid="nav-home-link" to="/">Home</Link>
          <Link data-testid="nav-start-here-link" to="/start-here">Start Here</Link>
          <Link data-testid="nav-blog-link" to="/blog">Read &amp; Learn</Link>
          <Link data-testid="nav-about-link" to="/about">Our Story</Link>
          <Link data-testid="nav-contact-link" className="nav-cta" to="/contact">Say hello <ArrowRight size={15} /></Link>
        </nav>
      </div>
    </header>
  );
}

function Footer() {
  return (
    <footer>
      <div className="footer-grid">
        <div>
          <div className="logo footer-logo"><span className="logo-mark">CT</span><span>Cozy Crochet<small>TRAIL</small></span></div>
          <p className="footer-copy">Practical crochet wisdom for a slower, more creative life.</p>
        </div>
        <div>
          <p className="footer-label">Explore</p>
          <Link data-testid="footer-start-link" to="/start-here">Start here</Link>
          <Link data-testid="footer-blog-link" to="/blog">All articles</Link>
          <Link data-testid="footer-author-link" to="/author/claire">Meet Claire</Link>
          <Link data-testid="footer-about-link" to="/about">About us</Link>
          <Link data-testid="footer-contact-link" to="/contact">Contact</Link>
        </div>
        <div>
          <p className="footer-label">Good to know</p>
          <Link data-testid="footer-privacy-link" to="/privacy">Privacy policy</Link>
          <Link data-testid="footer-terms-link" to="/terms">Terms of use</Link>
          <a data-testid="footer-instagram-link" href="https://instagram.com" target="_blank" rel="noreferrer"><Instagram size={15} /> Instagram</a>
        </div>
      </div>
      <div className="footer-bottom"><span>© 2026 {SITE}</span><span>Made with care in the USA</span></div>
    </footer>
  );
}

function CookieBanner() {
  const [show, setShow] = useState(() => !localStorage.getItem("cookie-choice"));
  if (!show) return null;
  const decide = (v) => { localStorage.setItem("cookie-choice", v); setShow(false); };
  return (
    <aside data-testid="cookie-consent-banner" className="cookie-banner">
      <Cookie size={22} />
      <div>
        <strong>A little note about cookies</strong>
        <p>We use essential cookies to keep this site working. Optional analytics cookies help us understand what readers enjoy.</p>
        <Link data-testid="cookie-privacy-link" to="/privacy">Read our privacy policy</Link>
      </div>
      <div className="cookie-actions">
        <button data-testid="cookie-reject-button" className="text-button" onClick={() => decide("rejected")}>Reject optional</button>
        <button data-testid="cookie-accept-button" className="button small" onClick={() => decide("accepted")}>Accept all</button>
      </div>
    </aside>
  );
}

function Layout({ children }) {
  return (<><Header /><main>{children}</main><Footer /><CookieBanner /><AdSenseLoader /><SearchConsoleVerification /><GA4Loader /><GA4PageView /></>);
}

function ArticleCard({ article, featured = false }) {
  return (
    <div className={featured ? "article-card featured" : "article-card"} data-testid={`article-card-${article.slug}`}>
      <Link className="article-card-link" to={`/article/${article.slug}`}>
        <div className="article-image">
          <img src={article.image} alt={`Crochet project inspiration for ${article.title}`} />
          {article.draft && <span className="draft-badge" data-testid={`draft-badge-${article.slug}`}>Draft</span>}
        </div>
      </Link>
      <Link className="image-tag image-tag-link"
        data-testid={`article-card-category-${article.slug}`}
        to={`/category/${categorySlug(article.category)}`}>{article.category}</Link>
      <Link className="article-card-link article-info-link" to={`/article/${article.slug}`}>
        <div className="article-info">
          <span className="eyebrow">{article.read_time} · {article.date}</span>
          <h3>{article.title}</h3>
          <p>{article.excerpt}</p>
          <span className="read-link">Keep reading <ArrowRight size={15} /></span>
        </div>
      </Link>
    </div>
  );
}

function CategoryPage() {
  const { slug } = useParams();
  const { articles, categories, loading } = useData();
  if (loading) return <LoadingState />;
  const name = categoryFromSlug(slug, categories.filter(c => c !== "All"));
  if (!name) return <NotFound />;
  const inCategory = articles.filter(a => a.category === name);
  const description = CATEGORY_DESCRIPTIONS[name] || `Crochet articles about ${name}.`;
  const heroImage = inCategory[0]?.image || DEFAULT_OG_IMAGE;
  const origin = typeof window !== "undefined" ? window.location.origin : "";
  const collectionSchema = {
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": `${name} · ${SITE}`,
    "description": description,
    "url": `${origin}/category/${slug}`,
    "isPartOf": { "@type": "WebSite", "name": SITE, "url": `${origin}/` },
    "mainEntity": {
      "@type": "ItemList",
      "numberOfItems": inCategory.length,
      "itemListElement": inCategory.map((a, i) => ({
        "@type": "ListItem",
        "position": i + 1,
        "url": `${origin}/article/${a.slug}`,
        "name": a.title,
      })),
    },
  };
  return (
    <>
      <Meta title={`${name} | ${SITE}`} description={description} image={heroImage} />
      <JsonLd id="category-schema" data={collectionSchema} />
      <section className="page-head">
        <span className="eyebrow">The journal · {name}</span>
        <h1>All our {name}<br /><em>stories.</em></h1>
        <p>{description}</p>
      </section>
      <section className="section blog-section">
        <div className="filter-row" data-testid="category-nav">
          {categories.filter(c => c !== "All").map(c => (
            <Link key={c} to={`/category/${categorySlug(c)}`}
              data-testid={`category-nav-${categorySlug(c)}`}
              className={c === name ? "filter active" : "filter"}>{c}</Link>
          ))}
          <Link data-testid="category-nav-all" to="/blog" className="filter">All articles</Link>
        </div>
        {inCategory.length === 0 ? (
          <p className="admin-hint" data-testid="category-empty" style={{ padding: "40px 0" }}>No articles in this category yet—check back soon.</p>
        ) : (
          <div className="article-grid blog-grid" data-testid="category-article-grid">
            {inCategory.map(a => <ArticleCard key={a.slug} article={a} />)}
          </div>
        )}
      </section>
    </>
  );
}

function renderParagraph(text) {
  const parts = text.split(/(\[\[[^\]]+\]\])/g);
  return parts.map((part, i) => {
    const match = part.match(/^\[\[([^|]+)\|([^\]]+)\]\]$/);
    if (match) return <Link key={i} data-testid={`inline-link-${match[1]}`} to={`/article/${match[1]}`}>{match[2]}</Link>;
    return <span key={i}>{part}</span>;
  });
}

function LoadingState({ label = "Loading stories…" }) {
  return <section className="page-head compact"><span className="eyebrow">One moment</span><h1>{label}</h1></section>;
}

function Home() {
  const { articles } = useData();
  const [joined, setJoined] = useState(false);
  const [nlError, setNlError] = useState("");
  const [nlBusy, setNlBusy] = useState(false);
  const submitNewsletter = async (e) => {
    e.preventDefault();
    setNlError(""); setNlBusy(true);
    const email = e.target.elements.email.value;
    try {
      await axios.post(`${API}/newsletter/subscribe`, { email, source: "home" });
      setJoined(true);
    } catch (err) {
      setNlError(err.response?.data?.detail?.[0]?.msg || err.response?.data?.detail || "Please double-check your email and try again.");
    } finally { setNlBusy(false); }
  };
  return (
    <>
      <Meta title={`${SITE} | Thoughtful crochet for everyday makers`} description="Crochet guides, stitch wisdom, yarn advice, and cozy patterns for curious makers." />
      <section className="hero">
        <div className="hero-inner">
          <div className="hero-copy">
            <span className="eyebrow light">A softer way to make</span>
            <h1>Make room for<br /><em>creative</em> days.</h1>
            <p>Practical crochet guides, honest yarn advice, and the little breakthroughs that make handmade feel easy.</p>
            <Link data-testid="hero-read-button" className="button light-button" to="/blog">Explore the journal <ArrowRight size={17} /></Link>
          </div>
          <div className="hero-note"><span>01 / 10</span><p>"The best projects are the ones that teach you something about yourself."</p></div>
        </div>
      </section>
      <Link data-testid="start-here-cta-banner" className="start-cta-banner" to="/start-here">
        <span className="eyebrow light">New here?</span>
        <strong>Follow the 6-step Start Here path — from first stitch to studio habits.</strong>
        <ArrowRight size={16} />
      </Link>
      <section className="section intro">
        <div><span className="eyebrow">Welcome in</span><h2>For the curious,<br />not the perfect.</h2></div>
        <div className="intro-text">
          <p>Cozy Crochet Trail is your friendly corner of the internet for making things with your hands. No gatekeeping, no intimidating jargon—just useful guidance from the first loop to the finished piece.</p>
          <Link data-testid="intro-about-link" className="underlined-link" to="/about">Meet the maker <ArrowRight size={15} /></Link>
        </div>
      </section>
      <section className="section latest">
        <div className="section-heading">
          <div><span className="eyebrow">From the journal</span><h2>Start somewhere lovely.</h2></div>
          <Link data-testid="latest-view-all-link" className="underlined-link" to="/blog">View all stories <ArrowRight size={15} /></Link>
        </div>
        <div className="article-grid">
          {articles.slice(0, 3).map((a, i) => <ArticleCard key={a.slug} article={a} featured={i === 0} />)}
        </div>
      </section>
      <section className="newsletter">
        <div><span className="eyebrow">A note in your inbox</span><h2>Good things,<br /><em>looped in.</em></h2></div>
        <div>
          <p>Occasional inspiration, fresh tutorials, and a gentle nudge to pick up your hook.</p>
          {joined ? (
            <p data-testid="newsletter-success-message" className="newsletter-success"><Check size={16} /> You're on the list—watch your inbox.</p>
          ) : (
            <form data-testid="newsletter-form" className="fake-form" onSubmit={submitNewsletter}>
              <input data-testid="newsletter-email-input" name="email" type="email" required placeholder="Your email address" aria-label="Your email address" />
              <button data-testid="newsletter-submit-button" className="button" type="submit" disabled={nlBusy}>{nlBusy ? "Joining…" : <>Join the list <ArrowRight size={15} /></>}</button>
            </form>
          )}
          {nlError && <p data-testid="newsletter-error-message" className="newsletter-error" style={{color:"#8c3e2a",fontSize:12,marginTop:8}}>{nlError}</p>}
          <small>No spam. Just thoughtful stitches.</small>
        </div>
      </section>
    </>
  );
}

function Blog() {
  const { articles, categories } = useData();
  const [active, setActive] = useState("All");
  const [page, setPage] = useState(1);
  const filtered = active === "All" ? articles : articles.filter(a => a.category === active);
  const perPage = 6;
  const totalPages = Math.max(1, Math.ceil(filtered.length / perPage));
  const shown = filtered.slice((page - 1) * perPage, page * perPage);
  return (
    <>
      <Meta title={`Crochet Journal | ${SITE}`} description="Explore crochet tutorials, yarn guides, stitch school, and handmade life stories." />
      <section className="page-head">
        <span className="eyebrow">The journal</span>
        <h1>Stories for your<br /><em>making time.</em></h1>
        <p>Guides and ideas to meet you wherever your hook is today.</p>
      </section>
      <section className="section blog-section">
        <div className="filter-row">
          {categories.map(c => (
            <button data-testid={`category-filter-${c.toLowerCase().replaceAll(" ", "-")}`} key={c}
              className={active === c ? "filter active" : "filter"}
              onClick={() => { setActive(c); setPage(1); }}>{c}</button>
          ))}
        </div>
        <div className="article-grid blog-grid">{shown.map(a => <ArticleCard key={a.slug} article={a} />)}</div>
        {totalPages > 1 && (
          <div className="pagination">
            {Array.from({ length: totalPages }, (_, i) => i + 1).map(n => (
              <button data-testid={`pagination-page-${n}`} key={n} className={page === n ? "page active" : "page"} onClick={() => setPage(n)}>{n}</button>
            ))}
          </div>
        )}
      </section>
    </>
  );
}

function RelatedReads({ current, articles }) {
  const same = articles.filter(a => a.slug !== current.slug && a.category === current.category);
  const others = articles.filter(a => a.slug !== current.slug && a.category !== current.category);
  const list = [...same, ...others].slice(0, 3);
  if (list.length === 0) return null;
  return (
    <section className="related-reads" data-testid="related-reads-section">
      <div className="section-heading">
        <div><span className="eyebrow">Keep reading</span><h2>Related stories.</h2></div>
      </div>
      <div className="article-grid">{list.map(a => <ArticleCard key={a.slug} article={a} />)}</div>
    </section>
  );
}

function ArticleSchema({ article }) {
  const origin = typeof window !== "undefined" ? window.location.origin : "";
  const url = `${origin}/article/${article.slug}`;
  const data = {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Article",
        "headline": article.title,
        "description": article.excerpt,
        "image": [article.image],
        "datePublished": article.date,
        "dateModified": article.date,
        "author": { "@type": "Person", "name": AUTHOR },
        "publisher": { "@type": "Organization", "name": SITE, "logo": { "@type": "ImageObject", "url": `${origin}/favicon.ico` } },
        "mainEntityOfPage": { "@type": "WebPage", "@id": url },
        "articleSection": article.category
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          { "@type": "ListItem", "position": 1, "name": "Home", "item": `${origin}/` },
          { "@type": "ListItem", "position": 2, "name": "Journal", "item": `${origin}/blog` },
          { "@type": "ListItem", "position": 3, "name": article.title, "item": url }
        ]
      }
    ]
  };
  return <JsonLd id="article-schema" data={data} />;
}

function Article() {
  const { slug } = useParams();
  const { articles, loading } = useData();
  if (loading) return <LoadingState />;
  const article = articles.find(a => a.slug === slug);
  if (!article) return <NotFound />;
  const hasBody = Array.isArray(article.body) && article.body.length > 0;
  return (
    <>
      <Meta title={`${article.title} | ${SITE}`} description={article.excerpt} image={article.image} type="article" />
      <ArticleSchema article={article} />
      <article className="article-page">
        <div className="article-top">
          <Link data-testid="article-back-link" className="back-link" to="/blog">← Back to journal</Link>
          <span className="eyebrow"><Link data-testid="article-category-link" to={`/category/${categorySlug(article.category)}`}>{article.category}</Link> · {article.read_time}</span>
          <h1>{article.title}</h1>
          <p className="article-dek">{article.excerpt}</p>
          <div className="byline">
            <span className="avatar">CL</span>
            <span>Written by <Link data-testid="byline-author-link" to="/author/claire"><strong>{AUTHOR}</strong></Link><br /><small>{article.date} · {SITE}</small></span>
          </div>
        </div>
        <img data-testid="article-hero-image" className="article-hero" src={article.image} alt={`Detailed crochet inspiration for ${article.title}`} />
        <div className="article-layout">
          {hasBody ? (
            <>
              <aside className="toc">
                <span className="eyebrow">In this story</span>
                {article.body.map(s => <a key={s.id} data-testid={`toc-${s.id}-link`} href={`#${s.id}`}>{s.heading}</a>)}
              </aside>
              <div className="article-body">
                <p className="lead">{article.excerpt}</p>
                {article.body.map((section, si) => (
                  <div key={section.id}>
                    <h2 id={section.id}>{section.heading}</h2>
                    {section.paragraphs.map((p, pi) => <p key={pi}>{renderParagraph(p)}</p>)}
                    {si === 1 && <AdSlot slot="1234567890" testId="article-ad-mid" />}
                  </div>
                ))}
                <div className="article-cta">
                  <strong>Ready for another thoughtful project?</strong>
                  <Link data-testid="related-article-link" to={`/article/${(articles[(articles.findIndex(a => a.slug === slug) + 1) % articles.length] || article).slug}`}>Read the next story <ArrowRight size={15} /></Link>
                </div>
              </div>
            </>
          ) : (
            <>
              <aside className="toc">
                <span className="eyebrow">In this story</span>
                <a data-testid="toc-start-link" href="#start">A gentle start</a>
                <a data-testid="toc-practice-link" href="#practice">Practice that sticks</a>
                <a data-testid="toc-next-link" href="#next">Your next loop</a>
              </aside>
              <div className="article-body" id="start">
                <p className="lead">There is a particular kind of satisfaction in making something useful from a single strand. This guide is here to make the process feel clear, generous, and entirely yours.</p>
                {(article.sections || []).map((p, i) => (
                  <div key={p}>
                    <h2 id={i === 1 ? "practice" : i === 2 ? "next" : undefined}>{["A gentle start", "The part that makes it click", "Your next loop"][i]}</h2>
                    <p>{p}</p>
                  </div>
                ))}
                <AdSlot slot="1234567890" testId="article-ad-mid" />
                <p>Keep this page nearby, save the parts that help, and give yourself permission to make a few imperfect things. That is how the good stuff begins.</p>
                <div className="article-cta">
                  <strong>Ready for another thoughtful project?</strong>
                  <Link data-testid="related-article-link" to={`/article/${(articles[(articles.findIndex(a => a.slug === slug) + 1) % articles.length] || article).slug}`}>Read the next story <ArrowRight size={15} /></Link>
                </div>
              </div>
            </>
          )}
        </div>
        <div className="section related-wrap"><RelatedReads current={article} articles={articles} /></div>
        <div className="section"><CommentSection slug={article.slug} /></div>
      </article>
    </>
  );
}

function Contact() {
  const [form, setForm] = useState({ name: "", email: "", subject: "", message: "" });
  const [sent, setSent] = useState(false);
  const [error, setError] = useState("");
  const submit = async (e) => {
    e.preventDefault(); setError("");
    try {
      await axios.post(`${API}/contact`, form);
      setSent(true); setForm({ name: "", email: "", subject: "", message: "" });
    } catch (err) {
      setError(err.response?.data?.detail?.[0]?.msg || "Please check your details and try again.");
    }
  };
  return (
    <>
      <Meta title={`Contact ${SITE}`} description="Have a crochet question? Send Cozy Crochet Trail a note." />
      <section className="page-head compact">
        <span className="eyebrow">Come say hello</span>
        <h1>Let's talk<br /><em>crochet.</em></h1>
        <p>Questions, kind notes, pattern ideas—we'd love to hear from you.</p>
      </section>
      <section className="contact-layout section">
        <div className="contact-aside">
          <span className="eyebrow">Find us here</span>
          <h2>A real person<br />reads every note.</h2>
          <p>For collaborations, corrections, or just to share what you're making:</p>
          <a data-testid="support-email-link" className="email-link" href="mailto:hello@cozyloopcrochet.com"><Mail size={16} /> hello@cozyloopcrochet.com</a>
        </div>
        <form data-testid="contact-form" className="contact-form" onSubmit={submit}>
          {sent && <div data-testid="contact-success-message" className="success"><Check size={18} /> Thanks for reaching out! We'll be in touch soon.</div>}
          {error && <div data-testid="contact-error-message" className="error">{error}</div>}
          <label>Name<input data-testid="contact-name-input" required value={form.name} onChange={e => setForm({ ...form, name: e.target.value })} /></label>
          <label>Email<input data-testid="contact-email-input" type="email" required value={form.email} onChange={e => setForm({ ...form, email: e.target.value })} /></label>
          <label>Subject<input data-testid="contact-subject-input" required value={form.subject} onChange={e => setForm({ ...form, subject: e.target.value })} /></label>
          <label>Message<textarea data-testid="contact-message-input" required minLength="10" rows="5" value={form.message} onChange={e => setForm({ ...form, message: e.target.value })} /></label>
          <button data-testid="contact-submit-button" className="button" type="submit">Send my note <ArrowRight size={16} /></button>
        </form>
      </section>
    </>
  );
}

const PRIVACY_SECTIONS = [
  {
    heading: "Information we collect",
    paragraphs: [
      "We collect only the information you choose to give us. When you submit the contact form, we store the name, email address, subject, and message you type. When you subscribe to the newsletter, we store your email address and the page you signed up from. When you leave a comment on an article, we store your chosen display name and the comment body so we can moderate and publish it.",
      "We do not sell, rent, or trade personal information to third parties. We do not use fingerprinting or profile-building trackers.",
    ],
  },
  {
    heading: "How we use your information",
    paragraphs: [
      "Contact submissions are used only to respond to you. Newsletter subscriptions are used to send you occasional emails you asked to receive; you can unsubscribe from any email or by writing to hello@cozyloopcrochet.com. Comments are shown publicly under the article they were posted on, alongside the name you provided.",
    ],
  },
  {
    heading: "Cookies and tracking technologies",
    paragraphs: [
      "This site uses two categories of cookies. Essential cookies keep the website functional and remember your cookie-consent choice. Optional analytics cookies (see the next section) only load if you accept them in the cookie banner.",
      "You can change your consent at any time by clearing your browser's site data for this domain and reloading the site. Most modern browsers also let you block all cookies through their settings, though doing so may affect functionality across the web.",
    ],
  },
  {
    heading: "Google Analytics",
    paragraphs: [
      "When you accept optional cookies, this site loads Google Analytics 4 to understand aggregate reading trends — which articles get read most, how long visitors stay, and which countries readers come from. Google Analytics 4 collects information such as your IP address (anonymized), device type, browser, referring page, and pages viewed. Google is the data controller for this data under its own privacy policy at policies.google.com/privacy.",
      "You can opt out of Google Analytics site-wide by installing the official Google Analytics Opt-out Browser Add-on at tools.google.com/dlpage/gaoptout, or by rejecting optional cookies in our banner.",
    ],
  },
  {
    heading: "Google AdSense and third-party advertising",
    paragraphs: [
      "We plan to display advertising served by Google AdSense on this site. Google, as a third-party vendor, uses cookies (including the DoubleClick DART cookie) to serve ads based on your prior visits to this and other websites. These ads may be targeted to your interests based on general demographic information Google infers, not on personally identifiable data supplied by us.",
      "You may opt out of personalized advertising by visiting Google's Ads Settings at adssettings.google.com. To opt out of many other third-party vendors' use of cookies for personalized ads, visit aboutads.info/choices (US) or youronlinechoices.eu (EU).",
      "We never ask readers to click ads, and we do not place ads in a way that could cause accidental clicks. Advertising revenue helps us keep publishing free crochet guides.",
    ],
  },
  {
    heading: "Third-party links and embeds",
    paragraphs: [
      "Articles may link to third-party websites for further reading, materials, or references. We are not responsible for the privacy practices of those sites; please review their own policies before providing information.",
    ],
  },
  {
    heading: "Your California privacy rights (CCPA/CPRA)",
    paragraphs: [
      "If you are a California resident, the California Consumer Privacy Act (as amended by the CPRA) gives you the right to (1) know what personal information we hold about you, (2) request deletion of your personal information, (3) request correction of inaccurate personal information, and (4) opt out of the sale or sharing of personal information.",
      "We do not sell or share personal information for cross-context behavioral advertising. To exercise any right, email hello@cozyloopcrochet.com from the address associated with your account, and we will respond within 45 days.",
    ],
  },
  {
    heading: "Data retention and security",
    paragraphs: [
      "Contact form submissions and newsletter subscriptions are retained until you ask us to delete them or until we determine they are no longer needed for the purpose they were collected. Comments are retained as long as the article they belong to remains published. We use industry-standard security controls, but no method of transmission over the internet is 100% secure.",
    ],
  },
  {
    heading: "Children's privacy",
    paragraphs: [
      "This site is intended for a general audience and is not directed at children under 13. We do not knowingly collect personal information from children under 13. If you believe a child has provided personal information to us, please contact hello@cozyloopcrochet.com and we will delete it promptly.",
    ],
  },
  {
    heading: "Changes to this policy",
    paragraphs: [
      "We may update this Privacy Policy from time to time. When we make changes, we update the \"last updated\" date at the top of this page. For material changes we will publish a note on the home page for at least seven days.",
    ],
  },
  {
    heading: "Contact us",
    paragraphs: [
      "Questions, requests, or corrections about this policy can be sent to hello@cozyloopcrochet.com. We read every note and respond personally.",
    ],
  },
];

const TERMS_SECTIONS = [
  {
    heading: "Using our content",
    paragraphs: [
      "Our tutorials, guides, and articles are provided for personal education and inspiration. You are welcome to print articles for personal reference, share links to any page on your social channels, and use the techniques you learn to make items for yourself or as personal gifts.",
      "You may not republish our text, images, or patterns on your own website or in a commercial publication without prior written permission. To request permission, email hello@cozyloopcrochet.com with the specific piece you want to use.",
    ],
  },
  {
    heading: "Intellectual property",
    paragraphs: [
      "All original words, photographs, illustrations, and patterns on Cozy Crochet Trail are the copyrighted work of Cozy Crochet Trail unless otherwise credited. The Cozy Crochet Trail name, logo, and brand marks are trademarks of the site owner.",
    ],
  },
  {
    heading: "Reader comments and submissions",
    paragraphs: [
      "By posting a comment or emailing us a note, you grant Cozy Crochet Trail a non-exclusive license to display and moderate your submission on the site. Only submit content you have the right to share. We moderate every comment before it appears; we may remove comments that are spam, defamatory, off-topic, promotional, or otherwise inappropriate at our discretion.",
    ],
  },
  {
    heading: "Advertising disclosure",
    paragraphs: [
      "This site displays advertising served by third parties (including Google AdSense). We may also participate in affiliate programs in the future, in which case we will clearly disclose any affiliate links inside the relevant article. Recommendations are always based on our honest opinion.",
    ],
  },
  {
    heading: "No professional advice; no warranties",
    paragraphs: [
      "Our content is educational in nature and is not professional advice. Crochet, sewing, and upcycling involve tools, fibers, and personal skill; results vary by individual. We provide our content \"as is\" without warranties of any kind, express or implied, including warranties of merchantability or fitness for a particular purpose.",
    ],
  },
  {
    heading: "Limitation of liability",
    paragraphs: [
      "To the maximum extent permitted by law, Cozy Crochet Trail and its team are not liable for any direct, indirect, incidental, or consequential damages arising from your use of the site, the techniques described, or any materials you purchase based on our recommendations.",
    ],
  },
  {
    heading: "External links",
    paragraphs: [
      "Our articles may link to external websites for reference or shopping. We are not responsible for the content, accuracy, or practices of any third-party site.",
    ],
  },
  {
    heading: "Changes to these terms",
    paragraphs: [
      "We may update these Terms of Use from time to time. Continued use of the site after changes are posted constitutes acceptance of the updated terms.",
    ],
  },
  {
    heading: "Governing law",
    paragraphs: [
      "These terms are governed by the laws of the State of Oregon, United States, without regard to its conflict of laws principles. Any dispute arising from these terms will be resolved in the state or federal courts located in Multnomah County, Oregon.",
    ],
  },
  {
    heading: "Contact us",
    paragraphs: [
      "Questions about these terms can be sent to hello@cozyloopcrochet.com.",
    ],
  },
];

function InfoPage({ type }) {
  const privacy = type === "privacy";
  const sections = privacy ? PRIVACY_SECTIONS : TERMS_SECTIONS;
  return (
    <>
      <Meta title={`${privacy ? "Privacy Policy" : "Terms of Use"} | ${SITE}`}
        description={privacy
          ? "How Cozy Crochet Trail handles your information, cookies, Google Analytics, Google AdSense, and your privacy rights."
          : "Simple, clear terms for using Cozy Crochet Trail articles, patterns, and community features."} />
      <section className="page-head compact">
        <span className="eyebrow">Good to know</span>
        <h1>{privacy ? <>Privacy<br /><em>policy.</em></> : <>Terms of<br /><em>use.</em></>}</h1>
      </section>
      <section className="legal section">
        <p className="lead">Last updated: February 18, 2026</p>
        <h2>{privacy ? "Your privacy matters" : "Welcome to Cozy Loop"}</h2>
        <p>{privacy
          ? "Cozy Crochet Trail respects your privacy. This page explains what information we collect, why we use it, the third parties involved (including Google Analytics and Google AdSense), and the choices available to you."
          : "These terms keep Cozy Crochet Trail useful, respectful, and clear for everyone who visits. By using this site you agree to the terms below."}</p>
        {sections.map((s, i) => (
          <div key={s.heading} data-testid={`legal-section-${i + 1}`}>
            <h2>{i + 1}. {s.heading}</h2>
            {s.paragraphs.map((p, pi) => <p key={pi}>{p}</p>)}
          </div>
        ))}
      </section>
    </>
  );
}

function About() {
  return (
    <>
      <Meta title={`About ${SITE}`} description="Meet the maker behind Cozy Crochet Trail." />
      <section className="page-head compact"><span className="eyebrow">Our story</span><h1>Made slowly.<br /><em>Shared openly.</em></h1></section>
      <section className="about-layout section">
        <img src="https://images.pexels.com/photos/6216236/pexels-photo-6216236.jpeg?auto=compress&cs=tinysrgb&w=1000" alt="A handmade crochet blanket ready for a cozy afternoon" />
        <div>
          <span className="eyebrow">Hello, I'm Claire</span>
          <h2>There is always<br />room for one more loop.</h2>
          <p>Cozy Crochet Trail grew out of a little kitchen table in Portland, Oregon, and a belief that craft should feel welcoming. I started this journal to share the practical things I wish someone had told me sooner: how to read a pattern, rescue a wonky edge, and choose yarn without second-guessing every skein.</p>
          <p>Today, it is a growing collection of honest guides for makers across the US. Come as you are, make at your own pace, and know that the occasional tangled stitch is part of the story.</p>
          <Link data-testid="about-blog-link" className="button" to="/blog">Read the journal <ArrowRight size={16} /></Link>
          <Link data-testid="about-author-link" className="underlined-link" style={{ marginLeft: 20 }} to="/author/claire">Read Claire's full bio <ArrowRight size={15} /></Link>
        </div>
      </section>
    </>
  );
}

function NotFound() {
  return (
    <section className="not-found">
      <span className="eyebrow">Oops, that loop slipped</span>
      <h1>404</h1>
      <p>We couldn't find that page, but there's plenty more to make.</p>
      <Link data-testid="404-home-link" className="button" to="/">Back to the beginning <ArrowRight size={16} /></Link>
    </section>
  );
}

const START_HERE_STEPS = [
  {
    number: "01",
    id: "foundations",
    title: "Start with the very first stitch",
    copy: "If you have never picked up a hook, begin here. This guide walks through slip knots, chains, and the first rows in plain language.",
    slugs: ["crochet-for-absolute-beginners"],
  },
  {
    number: "02",
    id: "practice",
    title: "Build tidy, even stitches",
    copy: "Once you can make a chain, focus on tension and consistency. A relaxed rhythm is what separates messy fabric from work you want to wear.",
    slugs: ["even-crochet-stitches", "common-crochet-mistakes"],
  },
  {
    number: "03",
    id: "patterns",
    title: "Learn to read a pattern",
    copy: "Abbreviations, repeats, and charts stop feeling like a foreign language after one careful walk-through. Read this before your next pattern.",
    slugs: ["read-crochet-pattern"],
  },
  {
    number: "04",
    id: "yarn",
    title: "Choose the right yarn for your project",
    copy: "Yarn choice changes drape, warmth, and how much your hands enjoy each session. Match fiber and weight to the job before you spend anything.",
    slugs: ["best-yarn-for-crochet"],
  },
  {
    number: "05",
    id: "rescue",
    title: "Rescue your work without starting over",
    copy: "Every crocheter drops a stitch. Learn to unfasten calmly, tink back to the mistake, and re-hook the loop so your project survives.",
    slugs: ["fix-dropped-stitch"],
  },
  {
    number: "06",
    id: "shortcuts",
    title: "Adopt studio habits that save hours",
    copy: "Five small routines—stitch markers, project bags, note-keeping—that turn crochet from occasional hobby into a calm daily practice.",
    slugs: ["crochet-hacks"],
  },
];

function StartHere() {
  const { articles, loading } = useData();
  if (loading) return <LoadingState />;
  const resolve = (slugs) => slugs.map(s => articles.find(a => a.slug === s)).filter(Boolean);
  return (
    <>
      <Meta title={`Start Here | ${SITE}`} description="A step-by-step crochet learning path for absolute beginners—hooks, stitches, patterns, yarn, and studio habits, in the right order." />
      <section className="page-head">
        <span className="eyebrow">Beginner bundle</span>
        <h1>Start here—<br /><em>you've got this.</em></h1>
        <p>A calm reading path from your very first slip knot to the studio habits that make crochet feel effortless.</p>
      </section>
      <section className="section start-here-intro">
        <div>
          <span className="eyebrow">How this works</span>
          <h2>Six short reads,<br />in the order that helps most.</h2>
        </div>
        <div className="intro-text">
          <p>Every guide below builds on the one before it. Save this page, come back between projects, and treat it like a table of contents for the first weeks of your practice.</p>
          <Link data-testid="start-here-blog-link" className="underlined-link" to="/blog">Or browse every article <ArrowRight size={15} /></Link>
        </div>
      </section>
      {START_HERE_STEPS.map(step => {
        const items = resolve(step.slugs);
        if (items.length === 0) return null;
        return (
          <section key={step.id} id={step.id} className="section start-here-step" data-testid={`start-here-step-${step.id}`}>
            <div className="step-heading">
              <span className="step-number">{step.number}</span>
              <div>
                <h2>{step.title}</h2>
                <p>{step.copy}</p>
              </div>
            </div>
            <div className="article-grid blog-grid">{items.map(a => <ArticleCard key={a.slug} article={a} />)}</div>
          </section>
        );
      })}
      <section className="section start-here-cta">
        <span className="eyebrow">Ready for more?</span>
        <h2>Keep the momentum going.</h2>
        <p>When these six feel familiar, the full journal has amigurumi, blanket patterns, top adjustments, and more.</p>
        <Link data-testid="start-here-cta-link" className="button" to="/blog">Explore the journal <ArrowRight size={16} /></Link>
      </section>
    </>
  );
}

function AuthorPage() {
  const { articles, loading } = useData();
  const origin = typeof window !== "undefined" ? window.location.origin : "";
  const url = `${origin}/author/claire`;
  const personSchema = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": AUTHOR,
    "url": url,
    "jobTitle": "Editor and Founder",
    "worksFor": { "@type": "Organization", "name": SITE, "url": `${origin}/` },
    "description": "Self-taught crocheter and educator based in Portland, Oregon, writing practical guides for makers across the United States.",
    "image": "https://images.pexels.com/photos/6217617/pexels-photo-6217617.jpeg?auto=compress&cs=tinysrgb&w=1000",
    "sameAs": ["https://instagram.com/cozyloopcrochet"],
    "email": "hello@cozyloopcrochet.com",
    "knowsAbout": ["Crochet", "Amigurumi", "Yarn selection", "Crochet pattern reading", "Handmade garments"],
  };
  return (
    <>
      <Meta title={`Meet Claire Lawson | ${SITE}`} description="Meet Claire Lawson—self-taught crocheter, educator, and founder of Cozy Crochet Trail. Read every article she has written, from beginner basics to plus-size top adjustments." />
      <JsonLd id="author-schema" data={personSchema} />
      <section className="page-head compact">
        <span className="eyebrow">About the author</span>
        <h1>Claire Lawson,<br /><em>your crochet friend.</em></h1>
      </section>
      <section className="section author-hero">
        <img data-testid="author-avatar" src={personSchema.image} alt="Claire Lawson working at a wooden table with a crochet hook and yarn" />
        <div>
          <span className="eyebrow">Editor · Cozy Crochet Trail</span>
          <h2>A decade of quiet<br />practice, shared openly.</h2>
          <p>I taught myself crochet at a kitchen table in Portland, Oregon after a friend handed me a hook and a leftover ball of cotton. Ten years later, that same table is where I write, swatch, and photograph everything you read on Cozy Crochet Trail.</p>
          <p>I believe good craft writing does two things: it removes the mystery and it keeps the joy. Every guide on this site is tested by me first, rewritten in plain English, and reviewed for accuracy before it ever goes live. If something on the site is wrong, I want to hear about it—email me directly and I will fix it.</p>
          <p>Outside of the site, I teach small-group crochet workshops at community centers around the Pacific Northwest, mentor a handful of new fiber-business owners each year, and hoard cotton scraps like they are currency.</p>
          <div className="author-meta">
            <div><span className="eyebrow">Based in</span><strong>Portland, Oregon</strong></div>
            <div><span className="eyebrow">Teaching since</span><strong>2018</strong></div>
            <div><span className="eyebrow">Reach me</span><a data-testid="author-email-link" href="mailto:hello@cozyloopcrochet.com">hello@cozyloopcrochet.com</a></div>
          </div>
        </div>
      </section>
      <section className="section author-articles">
        <div className="section-heading">
          <div><span className="eyebrow">By this author</span><h2>Everything Claire has written.</h2></div>
          <Link data-testid="author-blog-link" className="underlined-link" to="/blog">Full journal <ArrowRight size={15} /></Link>
        </div>
        {loading ? <p>Loading articles…</p> : (
          <div className="article-grid blog-grid" data-testid="author-article-list">
            {articles.map(a => <ArticleCard key={a.slug} article={a} />)}
          </div>
        )}
      </section>
    </>
  );
}

function DataProvider({ children }) {
  const [state, setState] = useState({ articles: [], categories: ["All"], loading: true });
  useEffect(() => {
    let cancelled = false;
    const token = localStorage.getItem("clc-admin-token");
    const config = token ? { headers: { "X-Admin-Token": token } } : {};
    axios.get(`${API}/articles`, config).then(res => {
      if (cancelled) return;
      setState({
        articles: res.data.articles || [],
        categories: res.data.categories || ["All"],
        loading: false,
      });
    }).catch(() => {
      if (cancelled) return;
      setState({ articles: [], categories: ["All"], loading: false });
    });
    return () => { cancelled = true; };
  }, []);
  const value = useMemo(() => state, [state]);
  return <DataContext.Provider value={value}>{children}</DataContext.Provider>;
}

export default function App() {
  return (
    <BrowserRouter>
      <DataProvider>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/blog" element={<Blog />} />
            <Route path="/article/:slug" element={<Article />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/privacy" element={<InfoPage type="privacy" />} />
            <Route path="/terms" element={<InfoPage type="terms" />} />
            <Route path="/start-here" element={<StartHere />} />
            <Route path="/category/:slug" element={<CategoryPage />} />
            <Route path="/author/claire" element={<AuthorPage />} />
            <Route path="/admin" element={<AdminPage />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </Layout>
      </DataProvider>
    </BrowserRouter>
  );
}
