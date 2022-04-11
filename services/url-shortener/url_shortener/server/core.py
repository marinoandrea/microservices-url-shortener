from flask import Blueprint, abort, jsonify, redirect, request
from url_shortener.errors import ValidationError
from url_shortener.use_cases import (create_url, delete_url, get_ids, get_url,
                                     update_url)

blueprint = Blueprint('core', __name__, url_prefix='/')


@blueprint.errorhandler(ValidationError)
def handle_bad_request(e):
    return str(e), 400


@blueprint.route("/", methods=['POST', 'GET'])
def route_urls():
    """
    This route handles CRUD operations on the entire 
    collection of the resource 'shortened url'.
    """
    if request.method == 'POST':
        # validate user request
        original_address = request.json.get('url')
        if original_address is None:
            raise ValidationError(
                "The body of the request must contain a 'url' field.")
        # create a shortened url
        url = create_url(original_address)
        # return a json representation of the entity
        return jsonify(url), 201

    if request.method == 'GET':
        output = jsonify(get_ids())
        return output, 200


@blueprint.route("/<string:id>", methods=['GET', 'PUT', 'DELETE'])
def route_url(id: str):
    """
    This route handles CRUD operations on a single instance
    of the resource 'shortened url' uniquely identified by
    the :id url parameter.
    """
    if request.method == 'GET':
        url = get_url(id)
        if url is None:
            abort(404)
        return redirect(url.original_address)

    if request.method == 'DELETE':
        url = get_url(id)
        if url is None:
            abort(404)
        try:
            delete_url(id)
        except ValidationError:
            abort(400)
        return "", 204

    if request.method == 'PUT':
        url = get_url(id)
        if url is None:
            abort(404)
        # validate user request
        original_address = request.json.get('url')
        if original_address is None:
            raise ValidationError(
                "The body of the request must contain a 'url' field.")
        # create a shortened url
        url = update_url(id, original_address)
        # return a json representation of the entity
        return jsonify(url), 201
