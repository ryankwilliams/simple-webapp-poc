from flask import Flask
from flask_cors import CORS

from app import api, views


def create_app():
    """Create application."""
    app = Flask(__name__)
    CORS(app)

    # api
    app.register_blueprint(api.requests.blueprint)

    # views
    app.register_blueprint(views.base.blueprint)
    app.register_blueprint(views.requests.blueprint)

    return app
