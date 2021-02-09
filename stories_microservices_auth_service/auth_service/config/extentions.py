from flask_migrate import Migrate
from ..app import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flasgger import Swagger
from flask_login import LoginManager
from flask_jwt_extended import (
    JWTManager, 
    jwt_required, 
    create_access_token,
    get_jwt_identity
)
import os


settings = {
    'prod': 'auth_service.config.production.ProdConfig',
    'dev': 'auth_service.config.development.DevConfig',
}


def get_config():
    if PROD:
        return settings.get('prod')
    return settings.get('dev')

DEBUG = False if os.environ.get('DEBUG') else True
PROD = not DEBUG


app.config.from_object(get_config())


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://db_user:bTmNECmEZOrdUcX4DQkAGevLtRakY@127.0.0.1:5433/db_name'
# app.config['SECRET_KEY'] = 'this is private'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['JWT_SECRET_KEY'] = 'super-secret'
# app.config['SECURITY_PASSWORD_SALT'] = 'my_precious_two'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
swagger = Swagger(app)
jwt = JWTManager(app)