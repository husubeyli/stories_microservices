import os
from ..config.base import Config


class ProdConfig(Config):
    DB_USER = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
    DB_NAME = os.environ.get('MONGO_INITDB_DATABASE')
    DB_PASS = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
    DB_HOST = os.environ.get('MONGO_INITDB_ROOT_HOST')
    DB_PORT = os.environ.get('MONGO_INITDB_ROOT_PORT')
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_PORT = os.environ.get('REDIS_PORT')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'mongodb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    CELERY_BROKER_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0"