from flask import Flask
from flask_cors import CORS

from app.views import default, requests


def create_app():
    """Create application."""
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(default.blueprint)
    app.register_blueprint(requests.blueprint)

    return app
