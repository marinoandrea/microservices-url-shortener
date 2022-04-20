from auth_service.data_access.repositories.base import IUserRepository
from auth_service.entities.user import User, make_user
from auth_service.errors import DataAccessError, ValidationError
from auth_service.use_cases.utils import IPasswordHasher


def build_create_user(
    user_repository: IUserRepository,
    password_hasher: IPasswordHasher
):

    def create_user(username: str, password: str) -> User:
        """
        Creates a user entity with hashed credentials
        which is then stored inside the service's persistence layer.

        Params
        ------
        username: `str`
        Unique string name provided by the user.

        password: `str`
        Password provided by the user.

        Returns
        -------
        `User`
        """
        hashed_password = password_hasher.hash_password(password)
        user = make_user({'username': username, 'password': hashed_password})

        try:
            user_repository.insert(user)
        except DataAccessError:
            raise ValidationError("This username is already in use.")

        return user

    return create_user
