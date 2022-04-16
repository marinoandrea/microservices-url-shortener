import hashlib
import os
from abc import ABC, abstractmethod

SALT_ROUNDS = 16
SALT_LENGTH = 16


class IPasswordHasher(ABC):

    @abstractmethod
    def hash_password(self, password: str) -> bytes:
        ...

    @abstractmethod
    def compare_password(self, password: str, hashed: str) -> bool:
        ...


class PBKDF2PasswordHasher(IPasswordHasher):
    salt: bytes
    rounds: int

    def __init__(self) -> None:
        self.rounds = SALT_ROUNDS
        salt_str = os.getenv("PASSWORD_SALT")

        if salt_str is None:
            raise RuntimeError(
                "A 'PASSWORD_SALT' env variable must be defined.")

        self.salt = salt_str.encode()

    def hash_password(self, password: str) -> bytes:
        return hashlib.pbkdf2_hmac(
            "sha512",
            password.encode(),
            self.salt,
            self.rounds)

    def compare_password(self, password: str, hashed: bytes) -> bool:
        new_hash = hashlib.pbkdf2_hmac(
            "sha512",
            password.encode(),
            self.salt,
            self.rounds)
        return new_hash == hashed
