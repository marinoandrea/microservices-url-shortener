import time
import uuid
from dataclasses import dataclass

from url_shortener.errors import ValidationError


@dataclass
class UniqueEntity:
    """
    Represents a base class for business entities that can be stored 
    in the data layer via a repository manager.
    """
    id: str
    created_at: int
    updated_at: int


def make_unique_entity(data: dict) -> UniqueEntity:
    """
    Returns a `UniqueEntity` populated with the values in `data`
    or throws an exception if the data does not contain valid fields.

    Parameters
    ----------
    data: `dict` Dictionary containing entity data

    Returns
    -------
    `UniqueEntity`
    """
    time_ms = int(time.time() * 1000)

    # unique entity fields are very often generated on entity creation
    # so there is no need to pass them unless you are rebuilding the
    # entity from the data layer.
    if 'id' in data and type(data['id']) != str:
        raise ValidationError("A UniqueEntity must contain a valid id.")

    if 'created_at' in data and (type(data['created_at']) != int or data['created_at'] > time_ms):
        raise ValidationError("A UniqueEntity must contain a valid timestamp for created_at.")

    if 'updated_at' in data and (type(data['updated_at']) != int or data['updated_at'] > time_ms):
        raise ValidationError("A UniqueEntity must contain a valid timestamp for updated_at.")

    return UniqueEntity(
        id=data.get('id', str(uuid.uuid4())),
        created_at=data.get('created_at', time_ms),
        updated_at=data.get('updated_at', time_ms)
    )
