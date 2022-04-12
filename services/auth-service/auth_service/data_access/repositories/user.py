from typing import Optional

from auth_service.data_access.repositories.base import IUserRepository
from auth_service.entities.user import User
from auth_service.errors import DataAccessError


class InMemoryUserRepository(IUserRepository):
    data: dict[str, User]

    def __init__(self):
        self.data = {}

    def insert(self, url: User):
        for surl in self.data.values():
            if surl.short_id == url.short_id:
                raise DataAccessError(
                    "This short id is already in use. Collision detected.")
        self.data[url.id] = url

    def find_by_id(self, id: str) -> Optional[User]:
        return self.data.get(id, None)

    def delete(self, id: str):
        self.data.pop(id)

    def update(self, id: str, data: dict) -> User:
        raise NotImplementedError()
