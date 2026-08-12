from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field, EmailStr
from pathlib import Path
from datetime import datetime, timezone
import os, uuid, logging

from articles_data import ARTICLES_SEED, CATEGORIES

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]
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
async def list_articles():
    docs = await db.articles.find({}, {"_id": 0}).sort("order", 1).to_list(length=200)
    return {"articles": docs, "categories": CATEGORIES}

@api_router.get("/articles/{slug}")
async def get_article(slug: str):
    doc = await db.articles.find_one({"slug": slug}, {"_id": 0})
    if not doc:
        raise HTTPException(status_code=404, detail="Article not found")
    return doc

app.include_router(api_router)
app.add_middleware(CORSMiddleware, allow_credentials=True, allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','), allow_methods=["*"], allow_headers=["*"])
logging.basicConfig(level=logging.INFO)

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
