
import os
from dataclasses import asdict

from flask import Blueprint, jsonify, request,make_response
from url_shortener.use_cases import create_url
from url_shortener.use_cases import get_url,get_ids

blueprint = Blueprint('core', __name__, url_prefix='/')


@blueprint.route("/", methods=['POST', 'GET','PUT','DELETE'])
def route_urls():

    if request.method == 'POST':
        url = create_url(request.json.get('url'))
        if url != None:
            output = jsonify({**asdict(url), "new_url": f"{os.getenv('DOMAIN_NAME','https://bit.g4')}/{url.short_id}"})
            response = make_response(output, 201)
        else:
            response = make_response('Error', 400)      
        return response
    else:
        if request.method == 'GET': 
            short_id = (request.json.get('id'))
            if short_id != None:
                url = get_url(short_id)
                output = jsonify({**asdict(url)})
                response = make_response(output, 301)
            else:
                output = jsonify(Keys = get_ids())
                response = make_response(output, 200)           
            return  response
        else:
            if request.method == 'PUT':
                short_id = (request.json.get('id'))
                if short_id != None:
                    url = get_url(short_id)
                    output = jsonify({**asdict(url)})
                    response = make_response(output, 200)
                else:
                    response = make_response('Error',400)
                return  response
            else:
                if request.method == 'DELETE':
                    response = make_response('Not Found',404)
                    return response


        
