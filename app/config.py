from logging import Logger
import os
from dotenv import load_dotenv
import logging

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGER = None

class Routes:
    BASEPATH = '/v1'
    IDENTIFYPATH = '/identify'

class ResponseMessages:
    SUCCESS = {"message":"Success", "status_code":200}
    FAILED = {"message":"Internal Server Error", "status_code":500}
    GIT_REPO_NOT_FOUND = {"message": "git repo doesn't exists", "status_code":400}
    BAD_REQUEST = {"message": "bad request", "status_code":400}

class LoggingConfig:
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'reconcialation.log'
    LOGGING_LEVEL = logging.DEBUG