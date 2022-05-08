import os
from typing import TypeVar

import pymongo
from url_shortener.data_access.repositories.base import IRepository

MONGODB_USER = os.getenv("MONGODB_USER")
MONGODB_PASS = os.getenv("MONGODB_PASS")
MONGODB_NAME = os.getenv("MONGODB_NAME")
MONGODB_HOST = os.getenv("MONGODB_HOST")

MONGODB_URI = f"mongodb://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_HOST}/{MONGODB_NAME}?authSource=admin"

client = pymongo.MongoClient(MONGODB_URI, connect=True)
database = client.get_database(MONGODB_NAME)

T = TypeVar("T")


class MongoDbRepository(IRepository[T]):
    connection: pymongo.database.Collection

    def __init__(self, collection: str):
        self.connection = database[collection]
