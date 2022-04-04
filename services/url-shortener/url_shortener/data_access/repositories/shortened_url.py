from typing import Optional

from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL


class InMemoryShortenedURLRepository(IShortenedURLRepository):
    data: dict[str, ShortenedURL]

    def __init__(self):
        self.data = {}

    def find_by_original_address(self, addr: str) -> Optional[ShortenedURL]:
        for surl in self.data.values():
            if surl.original_address == addr:
                return surl
        return None

    def insert(self, url: ShortenedURL):
        self.data[url.id] = url

    def find_by_id(self, id: str) -> Optional[ShortenedURL]:
        return self.data.get(id, None)
