from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL
from url_shortener.errors import ValidationError


def build_update_url(shortened_url_repo: IShortenedURLRepository):

    def update_url(short_id: str, original_address: str) -> ShortenedURL:
        """
        This function allows to update the redirect address
        for shortened urls entities.
        """
        record = shortened_url_repo.find_by_short_id(short_id)
        if record is None:
            raise ValidationError("There is no URL associated with this id.")

        record = shortened_url_repo.update_by_short_id(
            short_id, {'original_address': original_address})

        return record

    return update_url
