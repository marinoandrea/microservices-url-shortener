from url_shortener.data_access.repositories.base import IShortenedURLRepository
from url_shortener.entities.shortened_url import ShortenedURL
from url_shortener.errors import AuthorizationError, ValidationError


def build_update_url(shortened_url_repo: IShortenedURLRepository):

    def update_url(
        user_id: str, short_id: str, original_address: str
    ) -> ShortenedURL:
        """
        Updates the redirect address for shortened urls entities.

        Params
        ------
        user_id: `str`
        Identifier for the user which requested the update.

        short_id: `str`
        Short identifier for the URL.

        original_address: `str`
        Redirect address that the URL should point to from now on.

        Returns
        -------
        `ShortenedURL`
        """
        url = shortened_url_repo.find_by_short_id(short_id)

        if url is None:
            raise ValidationError("This url does not exist.")

        if url.user_id != user_id:
            raise AuthorizationError(
                "You are not authorized to update this url.")

        return shortened_url_repo.update_by_short_id(
            short_id, {'original_address': original_address})

    return update_url
