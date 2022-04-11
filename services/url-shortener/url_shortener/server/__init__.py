
from flask import Flask

from .core import blueprint as core_blueprint
from .extensions import cors


def create_app(config_file='./config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    app.register_blueprint(core_blueprint)


def register_extensions(app):
    cors.init_app(app)
