from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.errors import DataAccessError, ValidationError


def build_delete_url(shortened_url_repo: IShortenedURLRepository):

    def delete_url(short_id: str):
        try:
            shortened_url_repo.delete_by_short_id(short_id)
        except DataAccessError as e:
            raise ValidationError(str(e))

    return delete_url
