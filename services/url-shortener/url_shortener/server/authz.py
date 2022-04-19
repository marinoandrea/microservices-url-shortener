import os
from abc import ABC, abstractmethod
from time import sleep
from typing import Optional

import jwt
import requests


class ITokenManager(ABC):

    @abstractmethod
    def decode_token(self, token: str) -> Optional[dict]:
        ...


class PyJWTTokenManager(ITokenManager):
    rsa_public_key: bytes

    def __init__(self):
        auth_service_url = os.getenv("AUTH_SERVICE_URL")

        if auth_service_url is None:
            raise RuntimeError(
                "A 'AUTH_SERVICE_URL' env variable must be defined.")

        res = requests.get(f"{auth_service_url}/users/jwt/public-keys")
        while res.status_code != 200:
            res = requests.get(f"{auth_service_url}/users/jwt/public-keys")
            sleep(0.1)

        # NOTE: in this simple scenario we know that we are getting a single
        # key with ID "0", however we should store the entire dictionary with
        # all the keys returned by the auth service.
        self.rsa_public_key = str(res.json()["public_keys"]["0"]).encode()

    def decode_token(self, token: str) -> Optional[dict]:
        try:
            return jwt.decode(
                token,
                self.rsa_public_key,
                algorithms=["RS256"],
                audience="url-shortener")
        except (jwt.DecodeError, jwt.ExpiredSignatureError):
            return None
