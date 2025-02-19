from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

class Database:
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect(cls):
        cls.client = AsyncIOMotorClient(settings.mongo_url)
        cls.db = cls.client[settings.mongo_db_name]

    @classmethod
    async def disconnect(cls):
        cls.client.close()

db = Database()