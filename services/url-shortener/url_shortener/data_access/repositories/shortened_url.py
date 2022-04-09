from typing import Optional

from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL
from url_shortener.errors import DataAccessError


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
        for surl in self.data.values():
            if surl.short_id == url.short_id:
                raise DataAccessError(
                    "This short id is already in use. Collision detected.")
        self.data[url.id] = url

    def find_by_id(self, id: str) -> Optional[ShortenedURL]:
        return self.data.get(id, None)

    def find_by_short_id(self, short_id: str) -> Optional[ShortenedURL]:
        for surl in self.data.values():
            if surl.short_id == short_id:
                return surl
        return None

    def get_all_ids(self) -> list[str]:
        output = []
        for surl in self.data.values():
            output.append(surl.short_id)
        return

    def delete(self, id: str):
        self.data.pop(id)

    def delete_by_short_id(self, short_id: str):
        target = None
        for surl in self.data.values():
            if surl.short_id == short_id:
                target = surl
                break
        if target is None:
            return DataAccessError(
                "There is no url associated with this short id.")
        self.data.pop(target.id)
