from ..config.base import Config


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_user:bTmNECmEZOrdUcX4DQkAGevLtRakY@127.0.0.1:5434/db_name'
    CELERY_BROKER_URL = "redis://:12345@localhost:6379/0"