from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.errors import AuthorizationError, DataAccessError


def build_delete_user_urls(shortened_url_repo: IShortenedURLRepository):

    def delete_user_urls(user_id: str):
        """
        Deletes all the urls owned by the user from the service.

        Params
        ------
        user_id: `str`
        Identifier for the user which requested the deletion.
        """
        shortened_url_repo.delete_by_user_id(user_id)

    return delete_user_urls
