from flask import request, jsonify, send_from_directory
from flasgger import swag_from
from http import HTTPStatus
from ..app import app
from marshmallow.exceptions import ValidationError
from ..schemas.schmas import SubscriberSchema



@app.route('/subscribers-email/', methods=['POST'])
def email():
    try:
        data = request.json or request.form
        serializer = SubscriberSchema()
        email = serializer.load(data)
        email.save()
        return SubscriberSchema().jsonify(email), HTTPStatus.CREATED
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST




