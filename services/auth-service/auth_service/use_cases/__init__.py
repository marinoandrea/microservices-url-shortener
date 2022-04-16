from auth_service.data_access.repositories import user_repository

from .create_user import build_create_user
from .login import build_login
from .utils import PBKDF2PasswordHasher

password_hasher = PBKDF2PasswordHasher()

create_user = build_create_user(user_repository, password_hasher)
login = build_login(user_repository, password_hasher)
