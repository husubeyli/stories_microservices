from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from subscribers_service.app import app
from flask_marshmallow import Marshmallow
from flasgger import Swagger

import os

settings = {
    'prod': 'subscribers_service.config.production.ProdConfig',
    'dev': 'subscribers_service.config.development.DevConfig',
}

DEBUG = False if os.environ.get('DEBUG') else True
PROD = not DEBUG

def get_config():
    if PROD:
        return settings.get('prod')
    return settings.get('dev')
print(get_config(), 'sasasas')



app.config.from_object(get_config())





db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
ma = Marshmallow(app)
swagger = Swagger(app)
