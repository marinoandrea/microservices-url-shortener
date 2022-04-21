import os
from dataclasses import asdict
from functools import lru_cache

from auth_service.errors import ValidationError
from auth_service.use_cases import create_user, login
from flask import Blueprint, Request, jsonify, request
from flask_cors import CORS

from .authn import ITokenManager, PyJWTTokenManager

blueprint = Blueprint('users', __name__, url_prefix='/users')
CORS(blueprint)

token_manager: ITokenManager = PyJWTTokenManager()


def validate_user_request_body(request: Request) -> tuple[str, str]:
    username = request.json.get('username')
    if username is None:
        raise ValidationError(
            "The body of the request must contain a 'username' field.")
    password = request.json.get('password')
    if password is None:
        raise ValidationError(
            "The body of the request must contain a 'password' field.")
    return username, password


@blueprint.errorhandler(ValidationError)
def handle_bad_request(e):
    return str(e), 400


@blueprint.route("/", methods=['POST'])
def route_users():
    """
    This route handles create operations on the entire
    collection of the resource 'users'.
    """
    username, password = validate_user_request_body(request)

    user = create_user(username, password)

    output = asdict(user)
    output.pop("password")  # remove the hash for security

    return jsonify(output), 201


@blueprint.route("/login", methods=['POST'])
def route_users_login():
    """
    This route handles JWT-based user authentication.
    """
    username, password = validate_user_request_body(request)

    try:
        user = login(username, password)
    except ValidationError as e:
        return str(e), 403

    token = token_manager.generate_token(user.id)

    return jsonify({"token": token}), 200


@lru_cache
def read_public_key() -> str:
    path = os.getenv("RSA_PUBLIC_PATH")

    if path is None:
        raise RuntimeError(
            "A 'RSA_PUBLIC_PATH' env variable must be defined.")

    with open(path, 'r') as f:
        return f.read()


@blueprint.route("/jwt/public-keys", methods=['GET'])
def route_jwt_publickeys():
    """
    This endpoint returns a list of available public
    keys for JWT verification on external services.
    In our case, we only have one key for demo purposes.
    We identify it with an ID of "0".
    """
    return jsonify({
        "public_keys": {
            "0": read_public_key()
        }
    }), 200
