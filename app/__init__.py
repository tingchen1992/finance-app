from flask import Flask
from .routes import main
from .models import db
import os  


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.urandom(
        24
    )  

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
