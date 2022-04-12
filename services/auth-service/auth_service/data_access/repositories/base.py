

from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

from auth_service.entities.user import User

T = TypeVar('T')


class IRepository(ABC, Generic[T]):

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[T]:
        ...

    @abstractmethod
    def insert(self, url: T):
        ...

    @abstractmethod
    def delete(self, id: str):
        ...

    @abstractmethod
    def update(self, id: str, data: dict) -> T:
        ...


class IUserRepository(IRepository[User]):
    ...
