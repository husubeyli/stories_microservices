from datetime import timedelta
from ..app import app
from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine
from flasgger import Swagger
from flask_jwt_extended import (
    JWTManager,

    )


app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=15)

db = MongoEngine(app)
ma = Marshmallow(app)
swagger = Swagger(app)
jwt = JWTManager(app)