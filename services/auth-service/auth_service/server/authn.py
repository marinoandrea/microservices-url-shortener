import os
import uuid
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

import jwt

JWT_TTL_MINS = 30


class ITokenManager(ABC):

    @abstractmethod
    def generate_token(self, user_id: str) -> str:
        ...


class PyJWTTokenManager(ITokenManager):
    rsa_private_key: bytes

    def __init__(self):
        path = os.getenv("RSA_PRIVATE_PATH")

        if path is None:
            raise RuntimeError(
                "A 'RSA_PRIVATE_PATH' env variable must be defined.")

        with open(path, 'rb') as f:
            self.rsa_private_key = f.read()

    def generate_token(self, user_id: str) -> str:
        current_time = datetime.utcnow()
        return jwt.encode(
            {
                "iss": "auth-service",
                "aud": ["url-shortener", "front-service"],
                "iat": current_time,
                "exp": current_time + timedelta(minutes=JWT_TTL_MINS),
                "sub": user_id,
                "jti": str(uuid.uuid4())
            },
            self.rsa_private_key,
            algorithm="RS256")
