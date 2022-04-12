from auth_service.errors import ValidationError
from flask import Blueprint, abort
from flask_cors import CORS

blueprint = Blueprint('users', __name__, url_prefix='/users')
CORS(blueprint)


@blueprint.errorhandler(ValidationError)
def handle_bad_request(e):
    return str(e), 400


@blueprint.route("/", methods=['POST'])
def route_urls():
    """
    This route handles CRUD operations on the entire
    collection of the resource 'users'.
    """
    abort(404)


@blueprint.route("/login", methods=['POST'])
def route_url(id: str):
    abort(404)
