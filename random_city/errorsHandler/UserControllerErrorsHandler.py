import random_city.exceptions.ExistingUserException
import random_city.exceptions.BadRequestException
from random_city import app
from flask import jsonify, make_response


@app.errorhandler(random_city.exceptions.ExistingUserException.ExistingUserException)
def handle_existing_user(e):
    responseObject = {
        'status': 'fail',
        'message': e.message,
        'status_code': '409',
    }
    return make_response(jsonify(responseObject)), 409
app.register_error_handler(409, handle_existing_user)

@app.errorhandler(random_city.exceptions.BadRequestException.BadRequestException)
def handle_bad_request(e):
    responseObject = {
        'status': 'fail',
        'message': e.message,
        'status_code': '401',
    }
    return make_response(jsonify(responseObject)), 401
app.register_error_handler(401, handle_bad_request)