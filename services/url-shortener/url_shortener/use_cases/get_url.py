from url_shortener.data_access.repositories.base import IRepository
from url_shortener.entities.shortened_url import ShortenedURL


def build_get_url(shortened_url_repo: IRepository):


    def get_url(short_id:str) -> ShortenedURL:
        record = shortened_url_repo.find_by_id(short_id)
        return record

    return get_url