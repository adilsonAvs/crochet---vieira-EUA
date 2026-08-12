/* eslint-disable react/no-unescaped-entities */
import { useEffect, useState, useCallback } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { ArrowRight, Plus, Trash2, Edit3, X, Save, LogOut } from "lucide-react";

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
      <p className="admin-hint">Use <code>[[slug|anchor text]]</code> inside any paragraph to create an internal link to another article.</p>
      <button type="submit" className="button" disabled={busy} data-testid="admin-editor-save">
        {busy ? "Saving…" : <><Save size={14} /> Save article</>}
      </button>
    </form>
  );
}

function AdminList({ token, articles, onEdit, onDelete, onNew, onLogout }) {
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
          <div className="admin-row" data-testid={`admin-row-${a.slug}`} key={a.slug}>
            <div className="admin-row-main">
              <span className="image-tag">{a.category}</span>
              <div>
                <Link to={`/article/${a.slug}`} target="_blank" rel="noreferrer">{a.title}</Link>
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
    const res = await axios.get(`${API}/articles`);
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
            onLogout={() => { localStorage.removeItem(TOKEN_KEY); setToken(""); }} />
        )}
      </section>
    </>
  );
}
