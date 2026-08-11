from fastapi import FastAPI, APIRouter, HTTPException
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field, EmailStr
from pathlib import Path
from datetime import datetime, timezone
import os, uuid, logging

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

app.include_router(api_router)
app.add_middleware(CORSMiddleware, allow_credentials=True, allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','), allow_methods=["*"], allow_headers=["*"])
logging.basicConfig(level=logging.INFO)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()