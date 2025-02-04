from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager

from backend.api.limiter import limiter
from backend.api.config import Config
from backend.api.models.db import db
from backend.api.models.user import user_datastore, security, User, UserRoles
from backend.api.models.town import Town
from backend.api.models.hero import Hero
from backend.api.router import api
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)


def configure_database(app):
    @app.before_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager = LoginManager()

    CORS(app, origins=["http://localhost:5173", "http://localhost:5174"], supports_credentials=True)
    security.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    configure_database(app)
    api.init_app(app)
    limiter.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        try:
            if user_id.isdigit():
                return user_datastore.find_user(id=int(user_id))
            else:
                return user_datastore.find_user(fs_uniquifier=user_id)
        except (ValueError, TypeError) as e:
            app.logger.error("Error loading user: %s", e)
            return None

    return app