from auth_service.data_access.repositories.base import IUserRepository
from auth_service.entities.user import User
from auth_service.errors import ValidationError
from auth_service.use_cases.utils import IPasswordHasher


def build_login(
    user_repository: IUserRepository,
    password_hasher: IPasswordHasher
):

    def login(username: str, password: str) -> User:
        """
        Validates user provided credentials against the stored
        version.

        Params
        ------
        username: `str`
        Unique string name provided by the user.

        password: `str`
        Password provided by the user.

        Raises
        ------
        `auth_service.errors.ValidationError`
        If the username is not associated to a user in the system
        or the provided password doesn't match the hashed version.

        Returns
        -------
        `User`
        """
        user = user_repository.find_by_username(username)

        # NOTE: we explicitly keep the error messages vague
        if user is None:
            raise ValidationError("Wrong username or password.")

        if not password_hasher.compare_password(password, user.password):
            raise ValidationError("Wrong username or password.")

        return user

    return login
