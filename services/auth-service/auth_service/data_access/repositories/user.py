from typing import Optional

from auth_service.data_access.repositories.base import IUserRepository
from auth_service.entities.user import User
from auth_service.errors import DataAccessError


class InMemoryUserRepository(IUserRepository):
    data: dict[str, User]

    def __init__(self):
        self.data = {}

    def insert(self, new_user: User):
        for user in self.data.values():
            if user.username == new_user.username:
                raise DataAccessError("This username is already in use.")
        self.data[new_user.id] = new_user

    def find_by_id(self, id: str) -> Optional[User]:
        return self.data.get(id, None)

    def delete(self, id: str):
        self.data.pop(id)

    def update(self, id: str, data: dict) -> User:
        raise NotImplementedError()

    def find_by_username(self, username: str) -> Optional[User]:
        for user in self.data.values():
            if user.username == username:
                return user
        return None
