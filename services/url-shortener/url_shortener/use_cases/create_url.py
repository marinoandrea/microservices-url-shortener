from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL, make_url
from url_shortener.errors import DataAccessError


def build_create_url(shortened_url_repo: IShortenedURLRepository):

    def create_url(original_address: str) -> ShortenedURL:
        """
        This function allows to create shortened urls entities
        which are then stored from an original url string.
        """
        record = shortened_url_repo.find_by_original_address(original_address)
        if record is not None:
            return record

        while True:
            # we keep generating short ids inside the make_url function
            # until we don't get collisions anymore.
            # not particularly efficient but safe
            try:
                url = make_url({'original_address': original_address})
                shortened_url_repo.insert(url)
                break
            except DataAccessError:
                continue

        return url

    return create_url
