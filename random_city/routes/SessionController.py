from socketserver import UDPServer
from requests import request
from random_city import app
from random_city.models.Session import Session
from random_city.database import db_session, init_db
from flask import jsonify, Response

@app.route('/session', methods=['GET'])
def getSessions():
    sessions = Session.query.all()
    return jsonify(result = [session.to_dict() for session in sessions])

@app.route('/session', methods=['POST'])
def addSession():
    if 'user_id' in request.form:
        session = Session(request.form['user_id'])
        db_session.add(session)
        db_session.commit()
        status = Response(status_code=201)
        return status
    else:
        status = Response(status_code=500)
        return status