import json
from random_city.models.User import User
from random_city import db
from flask import Blueprint, jsonify, make_response, request
from random_city.exceptions.ExistingUserException import ExistingUserException
from random_city.exceptions.BadRequestException import BadRequestException


userBluePrint = Blueprint('UserBluePrint', __name__)


@userBluePrint.route("/user", methods=['GET'])
def getAllUsers():
    users = User.query.all()
    return jsonify(result=[user.to_dict() for user in users])


@userBluePrint.route('/user/<id>', methods=['GET'])
def getUserById(id):
    user = User.query.get(id)
    return jsonify(user.to_dict())


@userBluePrint.route('/user/register', methods=['POST'])
def addUser():
    request_data = json.loads(request.get_data())
    if 'first_name' in request_data and 'last_name' in request_data \
            and 'password' in request_data and 'mail' in request_data and 'pseudo' in request_data:
        user = User.query.filter((User.mail == request_data['mail']) | (User.pseudo == request_data['pseudo'])).first()
        if not user:
            try:
                first_name = request_data['first_name']
                last_name = request_data['last_name']
                password = request_data['password']
                mail = request_data['mail']
                pseudo = request_data['pseudo']
                user = User(first_name, last_name, password, mail, pseudo)
                db.session.add(user)
                db.session.commit()
                auth_token = user.encode_auth_token()
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered',
                    'status_code': '201',
                    'auth_token': auth_token
                }
                return make_response(jsonify(responseObject)), 201
            except Exception:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occured . Please try again',
                    'status_code': '500',
                }
                return make_response(jsonify(responseObject)), 500
        else:
            raise ExistingUserException()
    else:
        raise BadRequestException()


@userBluePrint.route('/user/login', methods=['POST'])
def login():
    request_data = json.loads(request.get_data())
    if 'mail' in request_data and 'password' in request_data:
        user = User.query.filter_by(mail=request_data['mail'], password=request_data['password']).first()
        if user != None:
            try:
                auth_token = user.encode_auth_token()
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered',
                    'status_code': '200',
                    'auth_token': auth_token
                    }
                return make_response(jsonify(responseObject)), 200
            except Exception:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occured . Please try again',
                    'status_code': '500',
                }
                return make_response(jsonify(responseObject)), 500
        else:
            raise BadRequestException('Bad Credentials. Please try again')
    else:
        raise BadRequestException()


@userBluePrint.route('/user/validPseudo/<pseudo>', methods=['GET'])
def validPseudo(pseudo):
    if User.query.filter_by(pseudo=pseudo).first() is not None:
        responseObject = {
            'status': 'success',
            'result': False
        }
        return make_response(jsonify(responseObject)), 200
    else:
        responseObject = {
            'status': 'success',
            'result': True
        }
        return make_response(jsonify(responseObject)), 200
