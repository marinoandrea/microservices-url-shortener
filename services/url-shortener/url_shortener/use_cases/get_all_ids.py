from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL


def build_get_ids(shortened_url_repo: IShortenedURLRepository):


    def get_ids():
        record = shortened_url_repo.get_all_ids()
        return record

    return get_ids