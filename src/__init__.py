import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app_settings = config.DevelopmentConfig
    app.config.from_object(app_settings)

    db.init_app(app)
    from src.api.file.views import file_api

    app.register_blueprint(file_api)

    return app
