from .base import IShortenedURLRepository
from .shortened_url import InMemoryShortenedURLRepository

shortened_url_repository: IShortenedURLRepository = InMemoryShortenedURLRepository()
