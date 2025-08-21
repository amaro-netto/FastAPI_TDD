from motor.motor_asyncio import AsyncIOMotorClient
from store.core.config import settings

class MongoClient:
    def __init__(self):
        self._client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)

    def __call__(self) -> AsyncIOMotorClient:
        return self._client

db_client = MongoClient()