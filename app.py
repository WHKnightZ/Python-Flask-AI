from flask import Flask

import api

from setting import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api.yolo.api, url_prefix="/api/yolo")
