import { useEffect, useState, useCallback } from "react";
import axios from "axios";
import { ArrowRight, MessageCircle, Check } from "lucide-react";

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

function formatDate(iso) {
  try {
    return new Date(iso).toLocaleDateString("en-US", { year: "numeric", month: "long", day: "numeric" });
  } catch {
    return iso;
  }
}

export default function CommentSection({ slug }) {
  const [comments, setComments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [form, setForm] = useState({ author_name: "", body: "", website: "" });
  const [sent, setSent] = useState(false);
  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  const load = useCallback(async () => {
    setLoading(true);
    try {
      const res = await axios.get(`${API}/articles/${slug}/comments`);
      setComments(res.data.comments || []);
    } catch {
      setComments([]);
    } finally {
      setLoading(false);
    }
  }, [slug]);

  useEffect(() => { load(); }, [load]);

  const submit = async (e) => {
    e.preventDefault();
    setError(""); setSubmitting(true);
    try {
      await axios.post(`${API}/articles/${slug}/comments`, form);
      setSent(true);
      setForm({ author_name: "", body: "", website: "" });
    } catch (err) {
      setError(err.response?.data?.detail?.[0]?.msg || err.response?.data?.detail || "Could not post your comment.");
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <section className="comment-section section" data-testid="comment-section">
      <div className="section-heading">
        <div>
          <span className="eyebrow">Join the conversation</span>
          <h2>{comments.length === 0 ? "Be the first to comment." : `${comments.length} comment${comments.length === 1 ? "" : "s"}.`}</h2>
        </div>
      </div>
      <div className="comment-list" data-testid="comment-list">
        {loading && <p className="comment-loading">Loading comments…</p>}
        {!loading && comments.length === 0 && (
          <p className="comment-empty"><MessageCircle size={16} /> No comments yet—your kind words could start the thread.</p>
        )}
        {comments.map(c => (
          <div key={c.id} className="comment-item" data-testid={`comment-item-${c.id}`}>
            <div className="comment-avatar">{c.author_name.slice(0, 2).toUpperCase()}</div>
            <div className="comment-body-wrap">
              <div className="comment-meta">
                <strong>{c.author_name}</strong>
                <small>{formatDate(c.created_at)}</small>
              </div>
              <p>{c.body}</p>
            </div>
          </div>
        ))}
      </div>
      <div className="comment-form-wrap">
        <h3>Leave a thoughtful reply</h3>
        <p className="comment-hint">Comments are moderated to keep the thread friendly. Your name and message post publicly; nothing else is stored.</p>
        <form className="contact-form" onSubmit={submit} data-testid="comment-form">
          {sent && <div className="success" data-testid="comment-success"><Check size={18} /> Thanks! Your comment is awaiting moderation.</div>}
          {error && <div className="error" data-testid="comment-error">{error}</div>}
          <label>Name
            <input data-testid="comment-name-input" required minLength="2" maxLength="60"
              value={form.author_name} onChange={e => setForm({ ...form, author_name: e.target.value })} />
          </label>
          <label>Comment
            <textarea data-testid="comment-body-input" required minLength="5" maxLength="2000" rows="4"
              value={form.body} onChange={e => setForm({ ...form, body: e.target.value })} />
          </label>
          {/* Honeypot — hidden from humans, filled by bots */}
          <label style={{ position: "absolute", left: "-9999px", opacity: 0 }} aria-hidden="true" tabIndex={-1}>
            Website
            <input tabIndex={-1} autoComplete="off"
              value={form.website} onChange={e => setForm({ ...form, website: e.target.value })} />
          </label>
          <button type="submit" className="button" disabled={submitting} data-testid="comment-submit">
            {submitting ? "Posting…" : <>Post comment <ArrowRight size={15} /></>}
          </button>
        </form>
      </div>
    </section>
  );
}
