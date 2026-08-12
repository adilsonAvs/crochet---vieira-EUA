from fastapi import FastAPI, APIRouter, HTTPException, Header, Response
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field, EmailStr
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, List, Dict, Any
import os, uuid, logging, hashlib, hmac, xml.sax.saxutils as _xml

from articles_data import ARTICLES_SEED, CATEGORIES

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]
SITE_ORIGIN = os.environ.get('SITE_ORIGIN', 'https://cozyloopcrochet.com')
app = FastAPI(title="Cozy Loop Crochet API")
api_router = APIRouter(prefix="/api")

class ContactMessage(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    subject: str = Field(min_length=2, max_length=160)
    message: str = Field(min_length=10, max_length=5000)

class ContactResponse(BaseModel):
    id: str
    message: str

class ArticleBodySection(BaseModel):
    id: str = Field(min_length=1, max_length=80)
    heading: str = Field(min_length=1, max_length=200)
    paragraphs: List[str] = Field(min_length=1)

class ArticleIn(BaseModel):
    slug: str = Field(min_length=2, max_length=120, pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
    title: str = Field(min_length=3, max_length=240)
    category: str = Field(min_length=2, max_length=60)
    excerpt: str = Field(min_length=10, max_length=400)
    image: str = Field(min_length=6, max_length=1000)
    read_time: str = Field(min_length=2, max_length=40)
    date: str = Field(min_length=4, max_length=40)
    body: Optional[List[ArticleBodySection]] = None
    sections: Optional[List[str]] = None
    draft: bool = False

class ArticleUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=240)
    category: Optional[str] = Field(default=None, min_length=2, max_length=60)
    excerpt: Optional[str] = Field(default=None, min_length=10, max_length=400)
    image: Optional[str] = Field(default=None, min_length=6, max_length=1000)
    read_time: Optional[str] = Field(default=None, min_length=2, max_length=40)
    date: Optional[str] = Field(default=None, min_length=4, max_length=40)
    body: Optional[List[ArticleBodySection]] = None
    sections: Optional[List[str]] = None
    draft: Optional[bool] = None

class RotateTokenIn(BaseModel):
    new_token: str = Field(min_length=8, max_length=200)

class CommentIn(BaseModel):
    author_name: str = Field(min_length=2, max_length=60)
    body: str = Field(min_length=5, max_length=2000)
    website: Optional[str] = Field(default="", max_length=200)  # honeypot; real users leave empty

class NewsletterSubscribe(BaseModel):
    email: EmailStr
    source: Optional[str] = Field(default="home", max_length=40)

def _hash_token(token: str) -> str:
    return hashlib.sha256(token.strip().encode("utf-8")).hexdigest()

async def _get_stored_hash() -> Optional[str]:
    doc = await db.admin_config.find_one({"key": "admin_token"})
    return doc.get("hash") if doc else None

async def _is_admin(x_admin_token: Optional[str]) -> bool:
    if not x_admin_token:
        return False
    stored = await _get_stored_hash()
    if stored:
        return hmac.compare_digest(_hash_token(x_admin_token), stored)
    env_token = os.environ.get('ADMIN_TOKEN', '').strip()
    return bool(env_token) and hmac.compare_digest(x_admin_token.strip(), env_token)

async def _require_admin(x_admin_token: Optional[str]):
    if not await _is_admin(x_admin_token):
        env_token = os.environ.get('ADMIN_TOKEN', '').strip()
        if not env_token and not await _get_stored_hash():
            raise HTTPException(status_code=503, detail="Admin dashboard is not configured. Set ADMIN_TOKEN in backend/.env.")
        raise HTTPException(status_code=401, detail="Invalid admin token.")

@api_router.get("/")
async def root():
    return {"message": "Cozy Loop Crochet is ready"}

@api_router.post("/contact", response_model=ContactResponse)
async def create_contact(payload: ContactMessage):
    doc = payload.model_dump()
    doc.update({"id": str(uuid.uuid4()), "created_at": datetime.now(timezone.utc).isoformat()})
    await db.contact_messages.insert_one(doc)
    return ContactResponse(id=doc["id"], message="Thanks for reaching out! We'll be in touch soon.")

@api_router.get("/articles")
async def list_articles(x_admin_token: Optional[str] = Header(default=None)):
    is_admin = await _is_admin(x_admin_token)
    query = {} if is_admin else {"draft": {"$ne": True}}
    docs = await db.articles.find(query, {"_id": 0}).sort("order", 1).to_list(length=200)
    return {"articles": docs, "categories": CATEGORIES, "admin": is_admin}

@api_router.get("/articles/{slug}")
async def get_article(slug: str, x_admin_token: Optional[str] = Header(default=None)):
    is_admin = await _is_admin(x_admin_token)
    query: Dict[str, Any] = {"slug": slug}
    if not is_admin:
        query["draft"] = {"$ne": True}
    doc = await db.articles.find_one(query, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Article not found")
    return doc

@api_router.post("/admin/verify")
async def admin_verify(x_admin_token: Optional[str] = Header(default=None)):
    await _require_admin(x_admin_token)
    return {"ok": True}

@api_router.post("/admin/rotate-token")
async def admin_rotate_token(payload: RotateTokenIn, x_admin_token: Optional[str] = Header(default=None)):
    await _require_admin(x_admin_token)
    if _hash_token(payload.new_token) == _hash_token(x_admin_token or ""):
        raise HTTPException(status_code=400, detail="New token must be different from the current one.")
    await db.admin_config.update_one(
        {"key": "admin_token"},
        {"$set": {"hash": _hash_token(payload.new_token), "updated_at": datetime.now(timezone.utc).isoformat()}},
        upsert=True,
    )
    return {"ok": True, "message": "Admin token rotated. Sign in again with the new token."}

@api_router.post("/admin/articles")
async def admin_create(payload: ArticleIn, x_admin_token: Optional[str] = Header(default=None)):
    await _require_admin(x_admin_token)
    if await db.articles.find_one({"slug": payload.slug}):
        raise HTTPException(status_code=409, detail="An article with this slug already exists.")
    last = await db.articles.find({}, {"order": 1}).sort("order", -1).limit(1).to_list(length=1)
    order = (last[0]["order"] + 1) if last else 0
    doc: Dict[str, Any] = payload.model_dump()
    doc.update({
        "id": str(uuid.uuid4()),
        "order": order,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    })
    await db.articles.insert_one(doc)
    doc.pop("_id", None)
    return doc

@api_router.put("/admin/articles/{slug}")
async def admin_update(slug: str, payload: ArticleUpdate, x_admin_token: Optional[str] = Header(default=None)):
    await _require_admin(x_admin_token)
    updates = {k: v for k, v in payload.model_dump(exclude_unset=True).items()}
    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update.")
    updates["updated_at"] = datetime.now(timezone.utc).isoformat()
    result = await db.articles.update_one({"slug": slug}, {"$set": updates})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Article not found")
    doc = await db.articles.find_one({"slug": slug}, {"_id": 0})
    return doc

@api_router.delete("/admin/articles/{slug}")
async def admin_delete(slug: str, x_admin_token: Optional[str] = Header(default=None)):
    await _require_admin(x_admin_token)
    result = await db.articles.delete_one({"slug": slug})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Article not found")
    await db.comments.delete_many({"article_slug": slug})
    return {"deleted": slug}

@api_router.get("/articles/{slug}/comments")
async def list_comments(slug: str):
    docs = await db.comments.find({"article_slug": slug, "approved": True}, {"_id": 0, "id": 1, "author_name": 1, "body": 1, "created_at": 1}).sort("created_at", 1).to_list(length=500)
    return {"comments": docs}

@api_router.post("/articles/{slug}/comments")
async def create_comment(slug: str, payload: CommentIn):
    if payload.website:  # honeypot triggered - silently accept but never store
        return {"message": "Thanks! Your comment is awaiting moderation.", "approved": False}
    article = await db.articles.find_one({"slug": slug, "draft": {"$ne": True}}, {"_id": 0, "slug": 1})
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    doc = {
        "id": str(uuid.uuid4()),
        "article_slug": slug,
        "author_name": payload.author_name.strip(),
        "body": payload.body.strip(),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "approved": False,
    }
    await db.comments.insert_one(doc)
    return {"message": "Thanks! Your comment is awaiting moderation.", "approved": False}

@api_router.get("/admin/comments")
async def admin_list_comments(status: str = "all", x_admin_token: Optional[str] = Header(default=None)):
    await _require_admin(x_admin_token)
    query: Dict[str, Any] = {}
    if status == "pending":
        query["approved"] = False
    elif status == "approved":
        query["approved"] = True
    docs = await db.comments.find(query, {"_id": 0}).sort("created_at", -1).to_list(length=1000)
    return {"comments": docs}

@api_router.post("/admin/comments/{comment_id}/approve")
async def admin_approve_comment(comment_id: str, x_admin_token: Optional[str] = Header(default=None)):
    await _require_admin(x_admin_token)
    result = await db.comments.update_one({"id": comment_id}, {"$set": {"approved": True, "approved_at": datetime.now(timezone.utc).isoformat()}})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"approved": comment_id}

@api_router.delete("/admin/comments/{comment_id}")
async def admin_delete_comment(comment_id: str, x_admin_token: Optional[str] = Header(default=None)):
    await _require_admin(x_admin_token)
    result = await db.comments.delete_one({"id": comment_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"deleted": comment_id}

@api_router.post("/newsletter/subscribe")
async def newsletter_subscribe(payload: NewsletterSubscribe):
    email = payload.email.lower().strip()
    existing = await db.newsletter_subscribers.find_one({"email": email})
    if existing:
        return {"message": "You're already on the list—thanks for the reminder!", "already_subscribed": True}
    doc = {
        "id": str(uuid.uuid4()),
        "email": email,
        "source": payload.source or "home",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    await db.newsletter_subscribers.insert_one(doc)
    return {"message": "You're on the list—watch your inbox.", "already_subscribed": False}

@api_router.get("/admin/newsletter")
async def admin_list_subscribers(x_admin_token: Optional[str] = Header(default=None)):
    await _require_admin(x_admin_token)
    docs = await db.newsletter_subscribers.find({}, {"_id": 0}).sort("created_at", -1).to_list(length=5000)
    return {"subscribers": docs, "count": len(docs)}

@api_router.delete("/admin/newsletter/{sub_id}")
async def admin_delete_subscriber(sub_id: str, x_admin_token: Optional[str] = Header(default=None)):
    await _require_admin(x_admin_token)
    result = await db.newsletter_subscribers.delete_one({"id": sub_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Subscriber not found")
    return {"deleted": sub_id}

def _fmt_lastmod(iso_or_pretty: str) -> str:
    """Best-effort ISO date for <lastmod>. Falls back to today."""
    for fmt in ("%B %d, %Y", "%b %d, %Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(iso_or_pretty, fmt).date().isoformat()
        except (ValueError, TypeError):
            continue
    return datetime.now(timezone.utc).date().isoformat()

@api_router.get("/sitemap.xml")
async def dynamic_sitemap():
    docs = await db.articles.find({"draft": {"$ne": True}}, {"_id": 0, "slug": 1, "date": 1, "updated_at": 1}).sort("order", 1).to_list(length=500)
    today = datetime.now(timezone.utc).date().isoformat()
    static_pages = [
        ("", "1.0", "weekly"),
        ("blog", "0.9", "weekly"),
        ("start-here", "0.9", "monthly"),
        ("about", "0.5", "monthly"),
        ("author/claire", "0.6", "monthly"),
        ("contact", "0.5", "monthly"),
        ("privacy", "0.3", "yearly"),
        ("terms", "0.3", "yearly"),
    ]
    parts = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, priority, freq in static_pages:
        loc = f"{SITE_ORIGIN}/{path}" if path else f"{SITE_ORIGIN}/"
        parts.append(f"<url><loc>{_xml.escape(loc)}</loc><lastmod>{today}</lastmod><changefreq>{freq}</changefreq><priority>{priority}</priority></url>")
    # Category landing pages — one per non-"All" category
    for cat in [c for c in CATEGORIES if c != "All"]:
        cat_slug = cat.lower().replace(" ", "-")
        loc = f"{SITE_ORIGIN}/category/{cat_slug}"
        parts.append(f"<url><loc>{_xml.escape(loc)}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>0.7</priority></url>")
    for d in docs:
        lastmod = _fmt_lastmod(d.get("updated_at") or d.get("date") or "")
        loc = f"{SITE_ORIGIN}/article/{d['slug']}"
        parts.append(f"<url><loc>{_xml.escape(loc)}</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>")
    parts.append("</urlset>")
    xml_body = "".join(parts)
    return Response(content=xml_body, media_type="application/xml")

app.include_router(api_router)
app.add_middleware(CORSMiddleware, allow_credentials=True, allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','), allow_methods=["*"], allow_headers=["*"])
logging.basicConfig(level=logging.INFO)

@app.on_event("startup")
async def seed_admin_token():
    """Populate admin_config with a hashed copy of ADMIN_TOKEN env var on first
    boot so the token can be rotated at runtime without editing .env."""
    if await db.admin_config.count_documents({"key": "admin_token"}) == 0:
        env_token = os.environ.get('ADMIN_TOKEN', '').strip()
        if env_token:
            await db.admin_config.insert_one({
                "key": "admin_token",
                "hash": _hash_token(env_token),
                "created_at": datetime.now(timezone.utc).isoformat(),
            })
            logging.info("Admin token seeded from ADMIN_TOKEN env var")

@app.on_event("startup")
async def seed_articles():
    """Populate the articles collection on first boot; keeps existing docs in sync
    for slugs that already exist so editing the seed file is enough to refresh
    content without dropping the collection."""
    existing_slugs = {d["slug"] async for d in db.articles.find({}, {"slug": 1})}
    for i, article in enumerate(ARTICLES_SEED):
        doc = {**article, "order": i}
        if article["slug"] in existing_slugs:
            await db.articles.update_one({"slug": article["slug"]}, {"$set": doc})
        else:
            doc["id"] = str(uuid.uuid4())
            await db.articles.insert_one(doc)
    logging.info("Articles seed applied: %s items", len(ARTICLES_SEED))

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
