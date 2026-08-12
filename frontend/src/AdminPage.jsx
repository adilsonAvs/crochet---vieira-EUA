/* eslint-disable react/no-unescaped-entities */
import { useEffect, useState, useCallback } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { ArrowRight, Plus, Trash2, Edit3, X, Save, LogOut, Key, Check, MessageCircle, Mail, Download } from "lucide-react";

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;
const TOKEN_KEY = "clc-admin-token";

const EMPTY_ARTICLE = {
  slug: "",
  title: "",
  category: "Clothing",
  excerpt: "",
  image: "",
  read_time: "6 min read",
  date: new Date().toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" }),
  body: [{ id: "intro", heading: "Introduction", paragraphs: ["Write your first paragraph here."] }],
  sections: null,
  draft: true,
};

function authHeaders(token) {
  return { headers: { "X-Admin-Token": token } };
}

function LoginGate({ onAuthed }) {
  const [pw, setPw] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);
  const submit = async (e) => {
    e.preventDefault();
    setBusy(true); setError("");
    try {
      await axios.post(`${API}/admin/verify`, {}, authHeaders(pw));
      localStorage.setItem(TOKEN_KEY, pw);
      onAuthed(pw);
    } catch (err) {
      setError(err.response?.data?.detail || "Could not verify token.");
    } finally { setBusy(false); }
  };
  return (
    <section className="page-head compact admin-login">
      <span className="eyebrow">Editors only</span>
      <h1>Sign in to the<br /><em>studio.</em></h1>
      <form className="contact-form admin-login-form" onSubmit={submit} data-testid="admin-login-form">
        {error && <div data-testid="admin-login-error" className="error">{error}</div>}
        <label>Admin token
          <input data-testid="admin-token-input" type="password" required autoFocus value={pw} onChange={e => setPw(e.target.value)} />
        </label>
        <button data-testid="admin-login-submit" className="button" type="submit" disabled={busy}>
          {busy ? "Verifying…" : <>Enter <ArrowRight size={15} /></>}
        </button>
        <p className="admin-hint">Set <code>ADMIN_TOKEN</code> in <code>backend/.env</code> to change this secret.</p>
      </form>
    </section>
  );
}

function ArticleEditor({ token, initial, onSaved, onCancel }) {
  const isNew = !initial;
  const [form, setForm] = useState(initial || EMPTY_ARTICLE);
  const [bodyText, setBodyText] = useState(JSON.stringify(form.body || [], null, 2));
  const [sectionsText, setSectionsText] = useState(JSON.stringify(form.sections || [], null, 2));
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  const update = (k, v) => setForm(f => ({ ...f, [k]: v }));

  const submit = async (e) => {
    e.preventDefault();
    setError(""); setBusy(true);
    let parsedBody = null; let parsedSections = null;
    try {
      const b = bodyText.trim();
      parsedBody = b && b !== "[]" ? JSON.parse(b) : null;
      const s = sectionsText.trim();
      parsedSections = s && s !== "[]" ? JSON.parse(s) : null;
    } catch (err) {
      setError("Body/Sections must be valid JSON.");
      setBusy(false);
      return;
    }
    if (!parsedBody && !parsedSections) {
      setError("Provide either a body (long-form) or sections (3 short paragraphs).");
      setBusy(false);
      return;
    }
    const payload = { ...form, body: parsedBody, sections: parsedSections };
    try {
      if (isNew) {
        await axios.post(`${API}/admin/articles`, payload, authHeaders(token));
      } else {
        const { slug, ...updates } = payload;
        await axios.put(`${API}/admin/articles/${slug}`, updates, authHeaders(token));
      }
      onSaved();
    } catch (err) {
      setError(err.response?.data?.detail?.[0]?.msg || err.response?.data?.detail || "Save failed.");
    } finally { setBusy(false); }
  };

  return (
    <form className="contact-form admin-editor" onSubmit={submit} data-testid="admin-editor-form">
      <div className="admin-editor-header">
        <h2>{isNew ? "New article" : `Editing ${form.slug}`}</h2>
        <button type="button" className="text-button" onClick={onCancel} data-testid="admin-editor-cancel"><X size={14} /> Cancel</button>
      </div>
      {error && <div className="error" data-testid="admin-editor-error">{error}</div>}
      <div className="admin-grid">
        <label>Slug (URL)
          <input data-testid="admin-field-slug" required value={form.slug} disabled={!isNew}
            onChange={e => update("slug", e.target.value)} placeholder="my-new-article" />
        </label>
        <label>Category
          <input data-testid="admin-field-category" required value={form.category}
            onChange={e => update("category", e.target.value)} />
        </label>
        <label>Read time
          <input data-testid="admin-field-read-time" required value={form.read_time}
            onChange={e => update("read_time", e.target.value)} placeholder="6 min read" />
        </label>
        <label>Date
          <input data-testid="admin-field-date" required value={form.date}
            onChange={e => update("date", e.target.value)} placeholder="February 4, 2026" />
        </label>
      </div>
      <label>Title
        <input data-testid="admin-field-title" required value={form.title}
          onChange={e => update("title", e.target.value)} />
      </label>
      <label>Excerpt (meta description)
        <textarea data-testid="admin-field-excerpt" required rows="2" value={form.excerpt}
          onChange={e => update("excerpt", e.target.value)} />
      </label>
      <label>Hero image URL
        <input data-testid="admin-field-image" required value={form.image}
          onChange={e => update("image", e.target.value)} />
      </label>
      <label>Body (long-form JSON — array of &#123;id, heading, paragraphs[]&#125;)
        <textarea data-testid="admin-field-body" rows="10" value={bodyText}
          onChange={e => setBodyText(e.target.value)} spellCheck="false" />
      </label>
      <label>Sections (fallback — array of 3 short paragraph strings)
        <textarea data-testid="admin-field-sections" rows="4" value={sectionsText}
          onChange={e => setSectionsText(e.target.value)} spellCheck="false" />
      </label>
      <label className="admin-checkbox">
        <input data-testid="admin-field-draft" type="checkbox" checked={!!form.draft}
          onChange={e => update("draft", e.target.checked)} />
        Save as draft (hidden from the public blog and sitemap until unchecked)
      </label>
      <p className="admin-hint">Use <code>[[slug|anchor text]]</code> inside any paragraph to create an internal link to another article.</p>
      <button type="submit" className="button" disabled={busy} data-testid="admin-editor-save">
        {busy ? "Saving…" : <><Save size={14} /> Save article</>}
      </button>
    </form>
  );
}

function NewsletterList({ token }) {
  const [subs, setSubs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [busy, setBusy] = useState("");

  const load = useCallback(async () => {
    setLoading(true);
    try {
      const res = await axios.get(`${API}/admin/newsletter`, authHeaders(token));
      setSubs(res.data.subscribers || []);
    } finally { setLoading(false); }
  }, [token]);
  useEffect(() => { load(); }, [load]);

  const remove = async (id) => {
    if (!window.confirm("Remove this subscriber?")) return;
    setBusy(id);
    try {
      await axios.delete(`${API}/admin/newsletter/${id}`, authHeaders(token));
      await load();
    } finally { setBusy(""); }
  };

  const exportCsv = () => {
    const header = "email,source,subscribed_at\n";
    const rows = subs.map(s => `${s.email},${s.source || ""},${s.created_at}`).join("\n");
    const blob = new Blob([header + rows], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = `cozy-loop-subscribers-${new Date().toISOString().slice(0, 10)}.csv`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  };

  return (
    <div className="mod-section" data-testid="newsletter-section">
      <h3>
        <Mail size={16} style={{ verticalAlign: "middle", marginRight: 6 }} /> Newsletter subscribers
        <span className="mod-approved-badge" style={{ marginLeft: 10 }}>{subs.length}</span>
      </h3>
      <p>Every email that opts in on the Home page lands here. Export the list any time you're ready to send a broadcast from your favorite email tool.</p>
      <button type="button" className="button small" onClick={exportCsv} disabled={subs.length === 0} data-testid="newsletter-export-csv">
        <Download size={13} /> Export CSV
      </button>
      {loading && <p className="admin-hint" style={{ marginTop: 15 }}>Loading subscribers…</p>}
      {!loading && subs.length === 0 && <p className="admin-hint" data-testid="newsletter-empty" style={{ marginTop: 15 }}>No subscribers yet. Once someone signs up on the Home page they'll show up here.</p>}
      <div style={{ marginTop: 15 }}>
        {subs.map(s => (
          <div key={s.id} className="mod-item" data-testid={`newsletter-item-${s.id}`}>
            <div className="mod-item-body">
              <strong>{s.email}</strong>
              <div className="mod-item-meta">Source: {s.source || "unknown"} · {new Date(s.created_at).toLocaleString("en-US")}</div>
            </div>
            <div className="mod-actions">
              <button className="text-button danger" onClick={() => remove(s.id)} disabled={busy === s.id} data-testid={`newsletter-delete-${s.id}`}>
                <Trash2 size={13} /> Remove
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function CommentModeration({ token }) {
  const [comments, setComments] = useState([]);
  const [filter, setFilter] = useState("pending");
  const [busy, setBusy] = useState("");

  const load = useCallback(async () => {
    const res = await axios.get(`${API}/admin/comments?status=${filter}`, authHeaders(token));
    setComments(res.data.comments || []);
  }, [filter, token]);

  useEffect(() => { load(); }, [load]);

  const approve = async (id) => {
    setBusy(id);
    try {
      await axios.post(`${API}/admin/comments/${id}/approve`, {}, authHeaders(token));
      await load();
    } finally { setBusy(""); }
  };
  const remove = async (id) => {
    if (!window.confirm("Delete this comment?")) return;
    setBusy(id);
    try {
      await axios.delete(`${API}/admin/comments/${id}`, authHeaders(token));
      await load();
    } finally { setBusy(""); }
  };

  const pendingCount = comments.filter(c => !c.approved).length;

  return (
    <div className="mod-section" data-testid="comment-moderation-section">
      <h3><MessageCircle size={16} style={{ verticalAlign: "middle", marginRight: 6 }} /> Comment moderation
        {pendingCount > 0 && filter === "pending" && <span className="mod-pending-badge" style={{ marginLeft: 10 }}>{pendingCount} pending</span>}
      </h3>
      <p>Approve friendly comments, delete spam. Only approved comments appear under articles.</p>
      <div className="filter-row" style={{ marginBottom: 20 }}>
        {["pending", "approved", "all"].map(f => (
          <button data-testid={`mod-filter-${f}`} key={f}
            className={filter === f ? "filter active" : "filter"}
            onClick={() => setFilter(f)}>{f[0].toUpperCase() + f.slice(1)}</button>
        ))}
      </div>
      {comments.length === 0 && <p className="admin-hint" data-testid="mod-empty">No comments in this view.</p>}
      {comments.map(c => (
        <div key={c.id} className="mod-item" data-testid={`mod-item-${c.id}`}>
          <div className="mod-item-body">
            <span className={c.approved ? "mod-approved-badge" : "mod-pending-badge"}>{c.approved ? "Approved" : "Pending"}</span>
            <strong>{c.author_name}</strong> · <Link to={`/article/${c.article_slug}`} target="_blank" rel="noreferrer">{c.article_slug}</Link>
            <p>{c.body}</p>
            <div className="mod-item-meta">{new Date(c.created_at).toLocaleString("en-US")}</div>
          </div>
          <div className="mod-actions">
            {!c.approved && (
              <button className="text-button" onClick={() => approve(c.id)} disabled={busy === c.id} data-testid={`mod-approve-${c.id}`}>
                <Check size={13} /> Approve
              </button>
            )}
            <button className="text-button danger" onClick={() => remove(c.id)} disabled={busy === c.id} data-testid={`mod-delete-${c.id}`}>
              <Trash2 size={13} /> Delete
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}

function RotateTokenForm({ token, onRotated }) {
  const [newToken, setNewToken] = useState("");
  const [confirm, setConfirm] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [busy, setBusy] = useState(false);
  const submit = async (e) => {
    e.preventDefault();
    setError(""); setSuccess("");
    if (newToken !== confirm) { setError("New tokens do not match."); return; }
    if (newToken.length < 8) { setError("New token must be at least 8 characters."); return; }
    setBusy(true);
    try {
      await axios.post(`${API}/admin/rotate-token`, { new_token: newToken }, authHeaders(token));
      localStorage.setItem(TOKEN_KEY, newToken);
      setSuccess("Token rotated. It is already active for this session.");
      setNewToken(""); setConfirm("");
      onRotated(newToken);
    } catch (err) {
      setError(err.response?.data?.detail || "Could not rotate token.");
    } finally { setBusy(false); }
  };
  return (
    <div className="rotate-section" data-testid="rotate-token-section">
      <h3><Key size={16} style={{ verticalAlign: "middle", marginRight: 6 }} /> Rotate admin token</h3>
      <p>Pick a long, random secret you actually remember. The new token replaces the current one immediately for every browser except this one, which is refreshed automatically.</p>
      <form className="contact-form" onSubmit={submit} data-testid="rotate-token-form">
        {error && <div className="error" data-testid="rotate-token-error">{error}</div>}
        {success && <div className="success" data-testid="rotate-token-success"><Check size={16} /> {success}</div>}
        <div className="admin-grid">
          <label>New token
            <input data-testid="rotate-token-new" type="password" required minLength="8" value={newToken}
              onChange={e => setNewToken(e.target.value)} />
          </label>
          <label>Confirm new token
            <input data-testid="rotate-token-confirm" type="password" required minLength="8" value={confirm}
              onChange={e => setConfirm(e.target.value)} />
          </label>
        </div>
        <button type="submit" className="button" disabled={busy} data-testid="rotate-token-submit">
          {busy ? "Rotating…" : <>Rotate now <ArrowRight size={14} /></>}
        </button>
      </form>
    </div>
  );
}

function AdminList({ token, articles, onEdit, onDelete, onNew, onLogout, onRotated }) {
  return (
    <>
      <div className="admin-toolbar">
        <div>
          <span className="eyebrow">Studio</span>
          <h2>{articles.length} articles published</h2>
        </div>
        <div className="admin-toolbar-actions">
          <button className="button small" onClick={onNew} data-testid="admin-new-article-button"><Plus size={14} /> New article</button>
          <button className="text-button" onClick={onLogout} data-testid="admin-logout-button"><LogOut size={14} /> Sign out</button>
        </div>
      </div>
      <div className="admin-table" data-testid="admin-article-table">
        {articles.map(a => (
          <div className={a.draft ? "admin-row admin-row-draft" : "admin-row"} data-testid={`admin-row-${a.slug}`} key={a.slug}>
            <div className="admin-row-main">
              <span className="image-tag">{a.category}</span>
              <div>
                <Link to={`/article/${a.slug}`} target="_blank" rel="noreferrer">
                  {a.draft && <span data-testid={`admin-draft-flag-${a.slug}`} style={{color:"#a86f10",fontWeight:700,marginRight:8}}>[DRAFT]</span>}
                  {a.title}
                </Link>
                <small>{a.slug} · {a.date} · {a.read_time}</small>
              </div>
            </div>
            <div className="admin-row-actions">
              <button className="text-button" onClick={() => onEdit(a)} data-testid={`admin-edit-${a.slug}`}><Edit3 size={14} /> Edit</button>
              <button className="text-button danger" onClick={() => onDelete(a)} data-testid={`admin-delete-${a.slug}`}><Trash2 size={14} /> Delete</button>
            </div>
          </div>
        ))}
      </div>
      <RotateTokenForm token={token} onRotated={onRotated} />
      <NewsletterList token={token} />
      <CommentModeration token={token} />
    </>
  );
}

export default function AdminPage() {
  const [token, setToken] = useState(() => localStorage.getItem(TOKEN_KEY) || "");
  const [checking, setChecking] = useState(!!token);
  const [articles, setArticles] = useState([]);
  const [editing, setEditing] = useState(null); // { article } or { new: true }
  const [flash, setFlash] = useState("");

  const load = useCallback(async () => {
    const t = localStorage.getItem(TOKEN_KEY) || "";
    const res = await axios.get(`${API}/articles`, t ? authHeaders(t) : {});
    setArticles(res.data.articles || []);
  }, []);

  useEffect(() => {
    document.title = "Studio · Cozy Loop Crochet";
    if (!token) { setChecking(false); return; }
    (async () => {
      try {
        await axios.post(`${API}/admin/verify`, {}, authHeaders(token));
        await load();
      } catch (err) {
        localStorage.removeItem(TOKEN_KEY); setToken("");
      } finally { setChecking(false); }
    })();
  }, [token, load]);

  if (checking) return <section className="page-head compact"><span className="eyebrow">One moment</span><h1>Loading studio…</h1></section>;

  if (!token) return <LoginGate onAuthed={t => { setToken(t); setChecking(true); }} />;

  const doDelete = async (a) => {
    if (!window.confirm(`Delete "${a.title}"? This cannot be undone.`)) return;
    try {
      await axios.delete(`${API}/admin/articles/${a.slug}`, authHeaders(token));
      setFlash(`Deleted "${a.title}"`);
      await load();
    } catch (err) {
      setFlash("Could not delete: " + (err.response?.data?.detail || "unknown error"));
    }
  };

  return (
    <>
      <section className="page-head compact">
        <span className="eyebrow">Editor studio</span>
        <h1>Publish new<br /><em>crochet stories.</em></h1>
        <p>Add, edit and remove journal entries. Changes go live instantly.</p>
      </section>
      <section className="section admin-section">
        {flash && <div className="success" data-testid="admin-flash">{flash}</div>}
        {editing ? (
          <ArticleEditor token={token}
            initial={editing.article}
            onCancel={() => setEditing(null)}
            onSaved={async () => { setEditing(null); setFlash("Saved."); await load(); }} />
        ) : (
          <AdminList token={token} articles={articles}
            onEdit={(a) => setEditing({ article: a })}
            onDelete={doDelete}
            onNew={() => setEditing({ article: null })}
            onLogout={() => { localStorage.removeItem(TOKEN_KEY); setToken(""); }}
            onRotated={(t) => setToken(t)} />
        )}
      </section>
    </>
  );
}
