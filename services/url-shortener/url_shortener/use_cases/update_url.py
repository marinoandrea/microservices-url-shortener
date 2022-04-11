from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL


def build_update_url(shortened_url_repo: IShortenedURLRepository):

    def update_url(short_id: str, original_address: str) -> ShortenedURL:
        """
        This function allows to update the redirect address
        for shortened urls entities.
        """
        return shortened_url_repo.update_by_short_id(
            short_id, {'original_address': original_address})

    return update_url
