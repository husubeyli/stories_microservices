from flask import Flask


app = Flask(__name__)

from .config.extentions import db
from .models import *
from .api.routers import *
from .subscriber import subscribe


@app.before_first_request
def _run_on_start():
    subscribe()
# app.config["APPLICATION_ROOT"] = "api/v1.0/post/"

if __name__ == '__main__':
    # app.init_app(db)
    app.run(port=5001, debug=True)

