import json

from sqlalchemy import exists
from random_city import app
from random_city.models.User import User
from random_city.database import db_session, init_db
from flask import jsonify, Response, make_response, request


@app.route("/user", methods=['GET'])
def getAllUsers():
    users = User.query.all()
    return jsonify(result = [user.to_dict() for user in users])

@app.route('/user/<id>', methods=['GET'])
def getUserById(id):
    user = User.query.get(id)        
    return jsonify(user.to_dict())

@app.route('/user/register', methods=['POST'])
def addUser():
    request_data = json.loads(request.get_data())
    if 'first_name' in request_data and 'last_name' in request_data \
    and 'password' in request_data and 'mail' in request_data and 'pseudo' in request_data:
        user = User.query.filter_by(mail=request_data['mail']).first()
        if not user:
            try:
                first_name = request_data['first_name']
                last_name = request_data['last_name']
                password = request_data['password']
                mail = request_data['mail']
                pseudo = request_data['pseudo']
                user = User(first_name, last_name, password, mail, pseudo)
                db_session.add(user)
                db_session.commit()
                auth_token = user.encode_auth_token(user.user_id)
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered',
                    'status_code': '201',
                    'auth_token': User.decode_auth_token(auth_token)
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                print(e)
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occured . Please try again',
                    'status_code': '401',
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please login',
                'status_code': '409',
            }
            return make_response(jsonify(responseObject)), 409
    else:
        responseObject = {
                'status': 'fail',
                'message': 'Bad request. Please try again',
                'status_code': '401',
            }
        return make_response(jsonify(responseObject)), 401

@app.route('/user/login', methods=['POST'])
def login():
    request_data = json.loads(request.get_data())
    if 'mail' in request_data and 'password' in request_data:
        user = User.query.filter_by(login=request_data['mail'], password=request_data['password']).first()
        if user!=None:
            return jsonify(user.to_dict())
        else:
            return Response(status=403)
    else:
        return Response(status=400)

@app.route('/user/validPseudo/<pseudo>', methods=['GET'])
def validPseudo(pseudo):
    if User.query.filter_by(pseudo = pseudo).first() is not None:
        Response = app.response_class(
            response=json.dumps({ 
            "result": False,
            }),
            status=200,
            mimetype="application/json"
        )
        return Response
    else:
        Response = app.response_class(
            response=json.dumps({ 
            "result": True
            }),
            status=200,
            mimetype="application/json"
        )
        return Response