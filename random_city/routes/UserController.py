from requests import request
from random_city import app
from random_city.models.User import User
from random_city.database import db_session, init_db
from flask import jsonify, Response

@app.route("/user", methods=['GET'])
def getAllUsers():
    users = User.query.all()
    return jsonify(result = [user.to_dict() for user in users])

@app.route('/user/<id>', methods=['GET'])
def getUserById(id):
    user = User.query.get(id)        
    return jsonify(user.to_dict())

@app.route('/user', methods=['POST'])
def addUser():
    if 'first_name' in request.form and 'last_name' in request.form and 'login' in request.form and 'password' in request.form:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        login = request.form['login']
        password = request.form['password']
        user = User(first_name, last_name, login, password)
        db_session.add(user)
        db_session.commit()
        status_code = Response(status=201)
        return status_code
    else:
        status_code = Response(status=500)
        return status_code

@app.route('/user/login', methods=['POST'])
def login():
    if 'login' in request.form and 'password' in request.form:
        user = User.query.filter_by(login=request.form['login'], password=request.form['password']).first()
        if user!=None:
            return jsonify(user.to_dict())
        else:
            return Response(status_code=400)