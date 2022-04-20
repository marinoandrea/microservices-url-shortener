
import logging

from flask import Flask, Response
from flask import logging as flask_logging
from flask import request

from .core import blueprint as core_blueprint
from .extensions import cors


def create_app(config_file='./config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    flask_logging.default_handler.setFormatter(
        logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s"))

    register_blueprints(app)
    register_extensions(app)

    @app.after_request
    def log_request_info(res: Response):
        app.logger.info(f"{request.method} {request.path} -> {res.status}")
        return res

    return app


def register_blueprints(app):
    app.register_blueprint(core_blueprint)


def register_extensions(app):
    cors.init_app(app)
