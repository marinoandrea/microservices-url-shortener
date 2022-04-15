from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.errors import AuthorizationError, ValidationError


def build_delete_url(shortened_url_repo: IShortenedURLRepository):

    def delete_url(user_id: str, short_id: str):
        """
        Deletes the specified url from the service.

        Params
        ------
        user_id: `str`
        Identifier for the user which requested the update.

        short_id: `str`
        Short identifier for the URL.
        """
        url = shortened_url_repo.find_by_short_id(short_id)

        if url is None:
            raise ValidationError("This url does not exist.")

        if url.user_id != user_id:
            raise AuthorizationError(
                "You are not authorized to delete this url.")

        shortened_url_repo.delete_by_short_id(short_id)

    return delete_url
