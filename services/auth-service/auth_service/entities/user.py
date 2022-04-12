from dataclasses import asdict, dataclass

from auth_service.errors import ValidationError

from .unique_entity import UniqueEntity, make_unique_entity


@dataclass
class User(UniqueEntity):
    """
    Represents a shortened URL record.
    """
    username: str
    password: str


def make_user(data: dict) -> User:
    """
    Returns a `User` populated with the values in `data`
    or throws an exception if the data does not contain valid fields.

    Parameters
    ----------
    data: `dict` Dictionary containing entity data

    Returns
    -------
    `User`
    """
    entity = make_unique_entity(data)

    if ("username" not in data or type(data["username"]) != str):
        raise ValidationError("A user must have a valid username.")

    # we expect the password to be hashed by the business logic
    if ("password" not in data or type(data["password"]) != str):
        raise ValidationError("A user must have a valid password.")

    return User(
        **asdict(entity),
        username=data["username"],
        password=data["password"]
    )
