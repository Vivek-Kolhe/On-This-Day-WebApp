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
    from .error_handling import error_bp
    app.register_blueprint(views, url_prefix = "/")
    app.register_blueprint(error_bp, url_prefix = "/")

    from .models import WikiData
    create_db(app)
    return app

def create_db(app):
    if not path.exists("app/" + DB_NAME):
        with app.app_context():
            db.create_all()
        print("DB Created!")
