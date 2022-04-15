import hashlib
import os
from abc import ABC, abstractmethod

SALT_ROUNDS = 16
SALT_LENGTH = 16


class IPasswordHasher(ABC):

    @abstractmethod
    def hash_password(self, password: str) -> str:
        ...


class PBKDF2PasswordHasher(IPasswordHasher):
    salt: str
    rounds: int

    def __init__(self) -> None:
        self.rounds = SALT_ROUNDS
        self.salt = os.getenv("PASSWORD_SALT")

        if self.salt is None:
            raise RuntimeError(
                "A 'PASSWORD_SALT' env variable must be defined.")

    def hash_password(self, password: str) -> str:
        return hashlib.pbkdf2_hmac("sha512", password, self.salt, self.rounds)\
            .decode("base64")

    def compare_password(self, password: str, hashed: str) -> bool:
        new_hash = hashlib.pbkdf2_hmac(
            "sha512", password, self.salt, self.rounds)\
            .decode("base64")
        return new_hash == hashed
