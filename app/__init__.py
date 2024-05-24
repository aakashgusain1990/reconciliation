from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask import Blueprint

db = SQLAlchemy()

v1 = Blueprint("v1", __name__)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():

        # Register Models
        from app.models.customers import Customer
        db.create_all()

        # API Versioning
        app.register_blueprint(v1, url_prefix="/v1")
    return app