import re
from dataclasses import asdict, dataclass

import cuid
from url_shortener.errors import ValidationError

from .unique_entity import UniqueEntity, make_unique_entity


@dataclass
class ShortenedURL(UniqueEntity):
    """
    Represents a shortened URL record.
    """
    original_address: str
    short_id: str


def make_url(data: dict) -> ShortenedURL:
    """
    Returns a `ShortenedURL` populated with the values in `data`
    or throws an exception if the data does not contain valid fields.

    Parameters
    ----------
    data: `dict` Dictionary containing entity data

    Returns
    -------
    `ShortenedURL`
    """
    entity = make_unique_entity(data)

    if (
        'original_address' not in data or
        type(data['original_address']) != str or
        re.fullmatch(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            data['original_address']
        ) is None
    ):
        raise ValidationError("A ShortenedURL must contain a valid address.")

    if 'short_id' in data and type(data['short_id']) != str:
        raise ValidationError("A ShortenedURL must contain a valid short id.")

    return ShortenedURL(
        **asdict(entity),
        original_address=data['original_address'],
        short_id=data.get('short_id', cuid.slug())
    )
