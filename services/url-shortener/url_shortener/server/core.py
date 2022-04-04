
import os
from dataclasses import asdict

from flask import Blueprint, jsonify, request
from url_shortener.use_cases import create_url

blueprint = Blueprint('core', __name__, url_prefix='/')


@blueprint.route("/", methods=['POST', 'GET'])
def route_urls():

    if request.method == 'POST':
        url = create_url(request.json.get('original_address', ''))
        return jsonify({**asdict(url), "new_url": f"{os.getenv('DOMAIN_NAME')}/{url.short_id}"})
