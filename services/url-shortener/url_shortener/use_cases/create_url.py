from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL, make_url


def build_create_url(shortened_url_repo: IShortenedURLRepository):

    def create_url(original_address: str) -> ShortenedURL:
        """

        """
        record = shortened_url_repo.find_by_original_address(original_address)
        if record is not None:
            return record

        url = make_url({'original_address': original_address})
        shortened_url_repo.insert(url)

        return url

    return create_url
