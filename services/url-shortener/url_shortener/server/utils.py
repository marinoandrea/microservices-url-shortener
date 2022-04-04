from flask import current_app
from url_shortener.errors import ValidationError


def throws_error(f):

    def inner(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except ValidationError as e:
            return str(e), 400
        except Exception as e:
            if current_app.debug:
                print(e)
            return "Sorry, something went wrong", 500

    return inner
