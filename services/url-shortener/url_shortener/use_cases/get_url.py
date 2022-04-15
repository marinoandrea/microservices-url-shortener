from typing import Optional

from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL


def build_get_url(shortened_url_repo: IShortenedURLRepository):

    def get_url(short_id: str) -> Optional[ShortenedURL]:
        """
        Retrieves a shortened url entity given its unique
        short id.

        Params
        ------
        short_id: `str`
        Short identifier for the URL.

        Returns
        -------
        `Optional[ShortenedURL]`
        """
        return shortened_url_repo.find_by_short_id(short_id)

    return get_url
