from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.helpers import utils, api_endpoints

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "this_is_a_secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix = "/")

    from .models import WikiData
    create_db(app)
    return app

def create_db(app):
    if not path.exists("app/" + DB_NAME):
        db.create_all(app = app)
        print("DB Created!")
