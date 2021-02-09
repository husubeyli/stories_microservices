from flask import Flask


app = Flask(__name__)

from .config.extentions import *
from .models import *
from .api.routers import *




# app.config["APPLICATION_ROOT"] = "api/v1.0/post/"

# if __name__ == '__main__':
#     # app.init_app(db)
#     app.run(port=5002, debug=True)

