from url_shortener.data_access.repositories.base import IShortenedURLRepository


def build_delete_url(shortened_url_repo: IShortenedURLRepository):

    def delete_url(short_id: str):
        shortened_url_repo.delete_by_short_id(short_id)

    return delete_url
