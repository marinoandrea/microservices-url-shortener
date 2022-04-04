
from flask import Flask, Response

from .core import blueprint as core_blueprint


def create_app(config_file='./config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    register_blueprints(app)

    @app.after_request
    def after_request(response: Response):
        response.headers['Access-Control-Allow-Credentials'] = 'true'
        return response

    return app


def register_blueprints(app):
    app.register_blueprint(core_blueprint)
