from .base import IUserRepository
from .user import MongoDbUserRepository

user_repository: IUserRepository = MongoDbUserRepository()
