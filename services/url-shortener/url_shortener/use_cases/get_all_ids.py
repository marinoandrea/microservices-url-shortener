from url_shortener.data_access.repositories.base import IShortenedURLRepository


def build_get_ids(shortened_url_repo: IShortenedURLRepository):

    def get_ids(user_id: str) -> list[str]:
        """
        Returns a list of short ids associated with URLs
        owned by the user.

        Params
        ------
        user_id: `str`
        Identifier for the user which requested the ids.

        Returns
        -------
        `list[str]` List of URL short ids.
        """
        return shortened_url_repo.get_all_ids_by_user(user_id)

    return get_ids
