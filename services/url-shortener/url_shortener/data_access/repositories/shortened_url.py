import time
from dataclasses import asdict
from typing import Optional

from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.data_access.vendors.mongodb import MongoDbRepository
from url_shortener.entities.shortened_url import ShortenedURL, make_url
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
        return output

    def delete(self, id: str):
        self.data.pop(id)

    def delete_by_short_id(self, short_id: str):
        target = None
        for surl in self.data.values():
            if surl.short_id == short_id:
                target = surl
                break
        if target is None:
            raise DataAccessError(
                "There is no url associated with this short id.")
        self.data.pop(target.id)

    def update(self, id: str, data: dict) -> ShortenedURL:
        raise NotImplementedError()

    def update_by_short_id(self, short_id: str, data: dict) -> ShortenedURL:
        target = None
        for surl in self.data.values():
            if surl.short_id == short_id:
                target = surl
                break
        if target is None:
            raise DataAccessError(
                "There is no url associated with this short id.")
        self.data[target.id] = make_url({
            **asdict(target),
            **data,
            "updated_at": int(time.time() * 1000)
        })
        return self.data[target.id]

    def get_all_ids_by_user(self, user_id: str) -> list[str]:
        output = []
        for surl in self.data.values():
            if surl.user_id != user_id:
                continue
            output.append(surl.short_id)
        return output

    def delete_by_user_id(self, user_id: str):
        target_ids = []
        for surl in self.data.values():
            if surl.user_id == user_id:
                target_ids.append(surl.id)
        for url_id in target_ids:
            self.data.pop(url_id)


class MongoDbShortenedURLRepository(
    IShortenedURLRepository,
    MongoDbRepository[ShortenedURL]
):

    def __init__(self) -> None:
        super().__init__("shortened_urls")

    def find_by_original_address(self, addr: str) -> Optional[ShortenedURL]:
        result = self.connection.find({"original_address": addr})
        return make_url({**result, "id": result["_id"]})

    def insert(self, url: ShortenedURL):
        obj = asdict(url)
        id = obj.pop("id")
        self.connection.insert_one({**obj, "_id": id})

    def find_by_id(self, id: str) -> Optional[ShortenedURL]:
        result = self.connection.find_one({"_id": id})
        if result is None:
            return None
        return make_url({**result, "id": result["_id"]})

    def find_by_short_id(self, short_id: str) -> Optional[ShortenedURL]:
        result = self.connection.find_one({"short_id": short_id})
        if result is None:
            return None
        return make_url({**result, "id": result["_id"]})

    def get_all_ids(self) -> list[str]:
        out = []
        for r in self.connection.find():
            out.append(r["short_id"])
        return out

    def delete(self, id: str):
        self.connection.delete_one({"_id": id})

    def delete_by_short_id(self, short_id: str):
        self.connection.delete_one({"short_id": short_id})

    def update(self, id: str, data: dict) -> ShortenedURL:
        raise NotImplementedError()

    def update_by_short_id(self, short_id: str, data: dict) -> ShortenedURL:
        target = self.find_by_short_id(short_id)

        if target is None:
            raise DataAccessError(
                "There is no url associated with this short id.")

        return self.connection.update_one(
            {"_id": target.id},
            {**asdict(data), "updated_at": int(time.time() * 1000)})

    def get_all_ids_by_user(self, user_id: str) -> list[str]:
        out = []
        for r in self.connection.find():
            if r["user_id"] != user_id:
                continue
            out.append(r["short_id"])
        return out

    def delete_by_user_id(self, user_id: str):
        self.connection.delete_many({"user_id": user_id})
