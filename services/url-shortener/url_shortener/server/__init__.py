
from flask import Flask, Response

from .core import blueprint as core_blueprint
from .extensions import cors


def create_app(config_file='./config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    register_blueprints(app)
    register_extensions(app)

    @app.after_request
    def after_request(response: Response):
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, PUT, DELETE, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Origin, Content-Type, X-Auth-Token')
        return response

    return app


def register_blueprints(app):
    app.register_blueprint(core_blueprint)


def register_extensions(app):
    cors.init_app(app)
