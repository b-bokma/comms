from flask import Flask
from config import Config # import config object
import os.path


def create_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        # Include our Routes
        from . import routes

        return app