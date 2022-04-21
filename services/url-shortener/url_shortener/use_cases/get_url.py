from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL
from url_shortener.errors import AuthorizationError, DataAccessError


def build_get_url(shortened_url_repo: IShortenedURLRepository):

    def get_url(short_id: str) -> ShortenedURL:
        """
        Retrieves a shortened url entity given its unique
        short id.

        Params
        ------
        user_id: `str`
        Identifier for the user which requested to access the url.

        short_id: `str`
        Short identifier for the URL.

        Returns
        -------
        `ShortenedURL`
        """
        url = shortened_url_repo.find_by_short_id(short_id)

        if url is None:
            raise DataAccessError("This url does not exist.")

        return url

    return get_url
