

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from url_shortener.entities.shortened_url import ShortenedURL

T = TypeVar('T')


class IRepository(ABC, Generic[T]):

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[T]:
        ...


class IShortenedURLRepository(IRepository):

    @abstractmethod
    def find_by_original_address(self, addr: str) -> Optional[ShortenedURL]:
        ...

    @abstractmethod
    def insert(self, url: ShortenedURL):
        ...

    @abstractmethod
    def get_all_ids(self):
        ...
    
