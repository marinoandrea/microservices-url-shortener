
from flask import Flask

from .extensions import cors
from .users import blueprint as users_blueprint


def create_app(config_file='./config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(users_blueprint)


def register_extensions(app):
    cors.init_app(app)
