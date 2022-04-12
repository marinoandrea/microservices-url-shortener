from .base import IUserRepository
from .user import InMemoryUserRepository

user_repository: IUserRepository = InMemoryUserRepository()
