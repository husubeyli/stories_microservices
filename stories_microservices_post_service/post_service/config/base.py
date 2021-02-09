import os
import redis
from logging.config import dictConfig

BASE_DIRS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIRS, 'media')

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
        'format': '[%(asctime)s] %(levelname)s: %(message)s',
    },
    'simple': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    },
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default',
        },
        'file': {
                'class': 'logging.FileHandler',
                'formatter': 'simple',
                'filename': 'WARN.log'
            }
        },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'file']
    }
})


class Config:
    SECRET_KEY = 'this is private'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']


class RedisConfig:
    HOST = os.environ.get('REDIS_HOST', 'localhost')
    PORT = os.environ.get('REDIS_PORT', 6379)
    CHANNEL_NAME = 'events'
    PASSWORD = os.environ.get('REDIS_PASSWORD', '12345')

    @classmethod
    def client(cls):
        return redis.Redis(host=cls.HOST, port=cls.PORT, password=cls.PASSWORD, db=0)