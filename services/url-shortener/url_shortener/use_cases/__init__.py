from url_shortener.data_access.repositories import shortened_url_repository

from .create_url import build_create_url

create_url = build_create_url(shortened_url_repository)
