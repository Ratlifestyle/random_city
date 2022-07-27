from crypt import methods
from requests import request
from random_city import app, db
from random_city.models.Session import Session
from flask import jsonify, Response

@app.route('/session', methods=['GET'])
def getSessions():
    sessions = Session.query.all()
    return jsonify(result = [session.to_dict() for session in sessions])

@app.route('/session/start', methods=['GET'])
def addSession():
    if 'user_id' in request.args:
        session = Session(request.args['user_id'])
        db.add(session)
        db.commit()
        return session.to_dict()
    else:
        status = Response(status_code=400)
        return status

@app.route('/session/end', methods=['GET'])
def endSession():
    if 'session_id' in request.args:
        session = Session.query.get(request.args['session_id'])
        session.is_active = 0;
        db.update(session)
        return session.to_dict()
    else:
        status = Response(status_code = 400)
        return status
