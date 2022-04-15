from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL, make_url
from url_shortener.errors import DataAccessError


def build_create_url(shortened_url_repo: IShortenedURLRepository):

    def create_url(user_id: str, original_address: str) -> ShortenedURL:
        """
        Creates a shortened url entity which is then stored inside
        the service's persistence layer.

        Params
        ------
        user_id: `str`
        Identifier for the user which requested the update.

        original_address: `str`
        Redirect address that the URL should point to.

        Returns
        -------
        `ShortenedURL`
        """
        while True:
            # we keep generating short ids inside the make_url function
            # until we don't get collisions anymore.
            # not particularly efficient but safe
            try:
                url = make_url({
                    'user_id': user_id,
                    'original_address': original_address,
                })
                shortened_url_repo.insert(url)
                break
            except DataAccessError:
                continue

        return url

    return create_url
