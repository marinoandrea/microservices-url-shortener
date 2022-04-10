from url_shortener.data_access.repositories import shortened_url_repository

from .create_url import build_create_url
from .delete_url import build_delete_url
from .get_all_ids import build_get_ids
from .get_url import build_get_url
from .update_url import build_update_url

create_url = build_create_url(shortened_url_repository)
get_url = build_get_url(shortened_url_repository)
get_ids = build_get_ids(shortened_url_repository)
delete_url = build_delete_url(shortened_url_repository)
update_url = build_update_url(shortened_url_repository)
