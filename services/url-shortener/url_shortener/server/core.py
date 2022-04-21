from typing import Optional

from flask import Blueprint, Request, abort, jsonify, redirect, request
from flask_cors import CORS
from url_shortener.errors import (AuthorizationError, DataAccessError,
                                  ValidationError)
from url_shortener.server.authz import ITokenManager, PyJWTTokenManager
from url_shortener.use_cases import (create_url, delete_url, delete_user_urls,
                                     get_ids, get_url, update_url)

blueprint = Blueprint('core', __name__, url_prefix='/')
CORS(blueprint)

token_manager: ITokenManager = PyJWTTokenManager()


def parse_authorization_header(request: Request) -> Optional[dict]:
    try:
        header = request.headers.get('Authorization', None)
        if header is None:
            return None
    except KeyError:
        return None
    token = header.removeprefix("Bearer ")
    return token_manager.decode_token(token)


def get_user_id(request: Request) -> str:
    payload = parse_authorization_header(request)
    if payload is None:
        abort(403)
    user_id = payload.get("sub", None)
    if user_id is None:
        abort(403)
    return user_id


@blueprint.errorhandler(ValidationError)
def handle_bad_request(e):
    return str(e), 400


@blueprint.errorhandler(AuthorizationError)
def handle_unauthorized_request(e):
    return str(e), 403


@blueprint.route("/", methods=['POST', 'GET', 'DELETE'])
def route_urls():
    """
    This route handles CRUD operations on the entire
    collection of the resource 'shortened url'.
    """
    user_id = get_user_id(request)

    if request.method == 'POST':
        # validate user request
        original_address = request.json.get('url')
        if original_address is None:
            raise ValidationError(
                "The body of the request must contain a 'url' field.")
        # create a shortened url
        url = create_url(user_id, original_address)
        # return a json representation of the entity
        return jsonify(url), 201

    if request.method == 'GET':
        output = jsonify(get_ids(user_id))
        return output, 200

    if request.method == 'DELETE':
        output = delete_user_urls(user_id)
        return "", 204


@blueprint.route("/<string:id>", methods=['GET', 'PUT', 'DELETE'])
def route_url(id: str):
    """
    This route handles CRUD operations on a single instance
    of the resource 'shortened url' uniquely identified by
    the :id url parameter.
    """
    if request.method == 'GET':
        try:
            url = get_url(id)
        except DataAccessError:
            abort(404)
        return redirect(url.original_address)

    user_id = get_user_id(request)

    if request.method == 'DELETE':
        try:
            delete_url(user_id, id)
        except DataAccessError:
            abort(404)
        return "", 204

    if request.method == 'PUT':
        # validate user request
        original_address = request.json.get('url')
        if original_address is None:
            raise ValidationError(
                "The body of the request must contain a 'url' field.")
        # create a shortened url
        try:
            url = update_url(user_id, id, original_address)
        except DataAccessError:
            abort(404)
        # return a json representation of the entity
        return jsonify(url), 201
