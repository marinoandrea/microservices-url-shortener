import logging
from dataclasses import asdict
from typing import Optional

from auth_service.data_access.repositories.base import IUserRepository
from auth_service.data_access.vendors.mongodb import MongoDbRepository
from auth_service.entities.user import User, make_user
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


class MongoDbUserRepository(
    IUserRepository,
    MongoDbRepository[User]
):

    def __init__(self) -> None:
        super().__init__("users")

    def insert(self, u: User):
        if self.connection.find_one({"username": u.username}) is not None:
            raise DataAccessError("This username is already in use.")
        obj = asdict(u)
        id = obj.pop("id")
        self.connection.insert_one({**obj, "_id": id})

    def find_by_id(self, id: str) -> Optional[User]:
        result = self.connection.find_one({"_id": id})
        if result is None:
            return None
        return make_user({**result, "id": result["_id"]})

    def find_by_username(self, username: str) -> Optional[User]:
        result = self.connection.find_one({"username": username})
        logging.error(result)
        if result is None:
            return None
        return make_user({**result, "id": result["_id"]})

    def delete(self, id: str):
        self.connection.delete_one({"_id": id})

    def update(self, id: str, data: dict) -> User:
        raise NotImplementedError()
