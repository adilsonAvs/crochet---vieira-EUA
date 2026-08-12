/* eslint-disable react/no-unescaped-entities */
import { useEffect, useState, createContext, useContext, useRef, useMemo } from "react";
import { BrowserRouter, Routes, Route, Link, useParams } from "react-router-dom";
import { ArrowRight, Menu, X, Mail, Instagram, Check, Cookie } from "lucide-react";
import axios from "axios";
import "./App.css";
import AdminPage from "./AdminPage";

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;
const ADSENSE_CLIENT = process.env.REACT_APP_ADSENSE_CLIENT || "";
const AUTHOR = "Claire Lawson";
const SITE = "Cozy Loop Crochet";

const DataContext = createContext({ articles: [], categories: ["All"], loading: true });
const useData = () => useContext(DataContext);

function Meta({ title, description }) {
  useEffect(() => {
    document.title = title;
    document.querySelector('meta[name="description"]')?.setAttribute("content", description);
  }, [title, description]);
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

function AdSlot({ slot = "auto", format = "auto", testId = "article-ad-placeholder" }) {
  const ref = useRef(false);
  useEffect(() => {
    if (!ADSENSE_CLIENT || ref.current) return;
    ref.current = true;
    try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) { /* noop */ }
  }, []);
  if (!ADSENSE_CLIENT) return <div className="ad-slot" data-testid={testId}><span>Advertisement</span></div>;
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
          <span className="logo-mark">CL</span>
          <span>Cozy Loop<small>CROCHET</small></span>
        </Link>
        <button data-testid="mobile-menu-button" className="icon-btn mobile-only" onClick={() => setOpen(!open)} aria-label="Toggle menu">
          {open ? <X /> : <Menu />}
        </button>
        <nav data-testid="main-navigation" className={open ? "nav-links open" : "nav-links"}>
          <Link data-testid="nav-home-link" to="/">Home</Link>
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
          <div className="logo footer-logo"><span className="logo-mark">CL</span><span>Cozy Loop<small>CROCHET</small></span></div>
          <p className="footer-copy">Practical crochet wisdom for a slower, more creative life.</p>
        </div>
        <div>
          <p className="footer-label">Explore</p>
          <Link data-testid="footer-blog-link" to="/blog">All articles</Link>
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
  return (<><Header /><main>{children}</main><Footer /><CookieBanner /><AdSenseLoader /></>);
}

function ArticleCard({ article, featured = false }) {
  return (
    <Link data-testid={`article-card-${article.slug}`} className={featured ? "article-card featured" : "article-card"} to={`/article/${article.slug}`}>
      <div className="article-image">
        <img src={article.image} alt={`Crochet project inspiration for ${article.title}`} />
        <span className="image-tag">{article.category}</span>
      </div>
      <div className="article-info">
        <span className="eyebrow">{article.read_time} · {article.date}</span>
        <h3>{article.title}</h3>
        <p>{article.excerpt}</p>
        <span className="read-link">Keep reading <ArrowRight size={15} /></span>
      </div>
    </Link>
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
  const submitNewsletter = (e) => { e.preventDefault(); setJoined(true); };
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
      <section className="section intro">
        <div><span className="eyebrow">Welcome in</span><h2>For the curious,<br />not the perfect.</h2></div>
        <div className="intro-text">
          <p>Cozy Loop Crochet is your friendly corner of the internet for making things with your hands. No gatekeeping, no intimidating jargon—just useful guidance from the first loop to the finished piece.</p>
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
              <input data-testid="newsletter-email-input" type="email" required placeholder="Your email address" aria-label="Your email address" />
              <button data-testid="newsletter-submit-button" className="button" type="submit">Join the list <ArrowRight size={15} /></button>
            </form>
          )}
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
      <Meta title={`${article.title} | ${SITE}`} description={article.excerpt} />
      <ArticleSchema article={article} />
      <article className="article-page">
        <div className="article-top">
          <Link data-testid="article-back-link" className="back-link" to="/blog">← Back to journal</Link>
          <span className="eyebrow">{article.category} · {article.read_time}</span>
          <h1>{article.title}</h1>
          <p className="article-dek">{article.excerpt}</p>
          <div className="byline">
            <span className="avatar">CL</span>
            <span>Written by <strong>{AUTHOR}</strong><br /><small>{article.date} · {SITE}</small></span>
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
      <Meta title={`Contact ${SITE}`} description="Have a crochet question? Send Cozy Loop Crochet a note." />
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

function InfoPage({ type }) {
  const privacy = type === "privacy";
  const headings = privacy
    ? ["Information we collect", "Cookies and analytics", "Advertising", "Your US privacy rights", "Contact us"]
    : ["Using our content", "Intellectual property", "Reader contributions", "Limitation of liability", "Contact us"];
  const bodies = privacy
    ? [
      "When you submit our contact form, we collect the name, email address, subject, and message you choose to provide. We use it only to respond and retain it for reasonable business records.",
      "Essential cookies help the site function. If you choose to accept optional cookies, we may use analytics to understand broad, anonymous reading trends. You can change your choice by clearing site data.",
      "We may display Google AdSense advertising in the future. Advertising partners may use cookies as described in their own policies; we never ask readers to click ads.",
      "Depending on your state, you may request access, correction, deletion, or information about sharing. Email hello@cozyloopcrochet.com and we will verify and respond to your request.",
      "Questions about this policy can be sent to hello@cozyloopcrochet.com."
    ]
    : [
      "Our tutorials and articles are for education and inspiration. Please use good judgment when selecting materials and techniques.",
      "Cozy Loop Crochet content, words, and original photography belong to Cozy Loop Crochet unless otherwise noted.",
      "Only submit material you have permission to share. By sending a note, you allow us to use it to respond, not to publish it without asking.",
      "We work to keep information useful and accurate, but projects involve materials and personal skill levels. You are responsible for your choices.",
      "Questions can be sent to hello@cozyloopcrochet.com."
    ];
  return (
    <>
      <Meta title={`${privacy ? "Privacy Policy" : "Terms of Use"} | ${SITE}`}
        description={privacy ? "How Cozy Loop Crochet handles information, cookies, and privacy." : "Simple, clear terms for using Cozy Loop Crochet."} />
      <section className="page-head compact">
        <span className="eyebrow">Good to know</span>
        <h1>{privacy ? <>Privacy<br /><em>policy.</em></> : <>Terms of<br /><em>use.</em></>}</h1>
      </section>
      <section className="legal section">
        <p className="lead">Last updated: June 12, 2026</p>
        <h2>{privacy ? "Your privacy matters" : "Welcome to Cozy Loop"}</h2>
        <p>{privacy ? "Cozy Loop Crochet respects your privacy. This page explains what information we collect, why we use it, and the choices available to you." : "These terms keep Cozy Loop Crochet useful, respectful, and clear for everyone who visits."}</p>
        {headings.map((h, i) => (<div key={h}><h2>{i + 1}. {h}</h2><p>{bodies[i]}</p></div>))}
      </section>
    </>
  );
}

function About() {
  return (
    <>
      <Meta title={`About ${SITE}`} description="Meet the maker behind Cozy Loop Crochet." />
      <section className="page-head compact"><span className="eyebrow">Our story</span><h1>Made slowly.<br /><em>Shared openly.</em></h1></section>
      <section className="about-layout section">
        <img src="https://images.pexels.com/photos/6216236/pexels-photo-6216236.jpeg?auto=compress&cs=tinysrgb&w=1000" alt="A handmade crochet blanket ready for a cozy afternoon" />
        <div>
          <span className="eyebrow">Hello, I'm Claire</span>
          <h2>There is always<br />room for one more loop.</h2>
          <p>Cozy Loop Crochet grew out of a little kitchen table in Portland, Oregon, and a belief that craft should feel welcoming. I started this journal to share the practical things I wish someone had told me sooner: how to read a pattern, rescue a wonky edge, and choose yarn without second-guessing every skein.</p>
          <p>Today, it is a growing collection of honest guides for makers across the US. Come as you are, make at your own pace, and know that the occasional tangled stitch is part of the story.</p>
          <Link data-testid="about-blog-link" className="button" to="/blog">Read the journal <ArrowRight size={16} /></Link>
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

function DataProvider({ children }) {
  const [state, setState] = useState({ articles: [], categories: ["All"], loading: true });
  useEffect(() => {
    let cancelled = false;
    axios.get(`${API}/articles`).then(res => {
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
            <Route path="/admin" element={<AdminPage />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </Layout>
      </DataProvider>
    </BrowserRouter>
  );
}
