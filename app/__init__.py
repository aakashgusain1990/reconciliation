from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config, LoggingConfig, Logger
from logging.handlers import RotatingFileHandler
import logging

app = Flask(__name__)
logging.basicConfig(level=LoggingConfig.LOGGING_LEVEL)
# 10 MB with 5 backup files
handler = RotatingFileHandler(LoggingConfig.LOGGING_LOCATION,
                                            maxBytes=10*1024*1024,
                                            backupCount=5)
handler.setLevel(LoggingConfig.LOGGING_LEVEL)
formatter = logging.Formatter(LoggingConfig.LOGGING_FORMAT)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.config.from_object(Config)
db = SQLAlchemy(app)
Logger = app.logger
from app.models.customers import Customer

# Register API Endpoints
from app.controllers.identify_controllers import base_path_blueprint
app.register_blueprint(base_path_blueprint)


with app.app_context():
    db.create_all()
    db.session.commit()


