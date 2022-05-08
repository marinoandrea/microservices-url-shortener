from .base import IShortenedURLRepository
from .shortened_url import MongoDbShortenedURLRepository

shortened_url_repository: IShortenedURLRepository = MongoDbShortenedURLRepository()
