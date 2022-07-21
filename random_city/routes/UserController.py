import json

from sqlalchemy import exists
from random_city import app
from random_city.models.User import User
from random_city.database import db_session, init_db
from flask import jsonify, Response, request


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
    print("ajout d user")
    request_data = json.loads(request.get_data())
    print(request_data)

    if 'first_name' in request_data and 'last_name' in request_data and 'login' in request_data \
    and 'password' in request_data and 'mail' in request_data and 'pseudo' in request_data:
        first_name = request_data['first_name']
        last_name = request_data['last_name']
        login = request_data['login']
        password = request_data['password']
        mail = request_data['mail']
        pseudo = request_data['pseudo']
        user = User(first_name, last_name, login, password, mail, pseudo)
        db_session.add(user)
        db_session.commit()
        status_code = Response(status=201)
        return status_code
    else:
        status_code = Response(status=500)
        return status_code

@app.route('/user/login', methods=['POST'])
def login():
    request_data = request.get_json()
    if 'login' in request_data and 'password' in request:
        user = User.query.filter_by(login=request_data['login'], password=request_data['password']).first()
        if user!=None:
            return jsonify(user.to_dict())
        else:
            return Response(status_code=400)

@app.route('/user/validPseudo/<pseudo>', methods=['GET'])
def validPseudo(pseudo):
    if User.query.filter_by(pseudo = pseudo).first() is not None:
        Response = app.response_class(
            response=json.dumps({ 
            "result": "aaa",
            "TEST": 'OK' 
            }),
            status=200,
            mimetype="application/json"
        )
        return Response
    else:
        Response = app.response_class(
            response=json.dumps({ 
            "result": "aaa",
            "TEST": 'OK' 
            }),
            status=200,
            mimetype="application/json"
        )
        return Response