from auth_service.data_access.repositories.base import IUserRepository
from auth_service.entities.user import User, make_user
from auth_service.use_cases.utils import IPasswordHasher


def build_create_user(
    user_repository: IUserRepository,
    password_hasher: IPasswordHasher
):

    def create_user(username: str, password: str) -> User:
        hashed_password = password_hasher.hash_password(password)
        user = make_user({'username': username, 'password': hashed_password})
        user_repository.insert(user)
        return user

    return create_user
