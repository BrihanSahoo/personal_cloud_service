from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import DATABASE,MONGO_URL

client = AsyncIOMotorClient(MONGO_URL)

db = client[DATABASE]

users_collection = db["users"]
files_collection = db["files"]