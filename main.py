from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
login_manager = LoginManager()


@login_manager.user_loader
def user_loader(user_id):
    from .model import User

    users = {
        "Lucasvenezian@gmail.com": User(
            name="Lucas Venezian Povoa",
            email="Lucasvenezian@gmail.com",
            password="12345678",
            birthdate="1990-02-01"
        )
    }
    return users.get(user_id)


def create_app():
    application = Flask(__name__)
    application.config.from_object(
        "config.DevelopmentConfig")

    from index.index import index_blueprint
    application.register_blueprint(index_blueprint)

    from character.routes import character_blueprint
    application.register_blueprint(character_blueprint)

    db.init_app(application)
    login_manager.init_app(application)

    if application.config["TESTING"]:
        with application.app_context():
            db.drop_all()
            db.create_all()
            from util.crawler import get_data_from_rick_and_morty_apis
            get_data_from_rick_and_morty_apis(db)

    return application

from model import *

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=5000)
