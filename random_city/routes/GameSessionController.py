from random_city import app, db
from random_city.models.GameSession import GameSession
from flask import Blueprint, jsonify, Response, request


gameSessionBluePrint = Blueprint('GameSessionBluePrint', __name__)


@gameSessionBluePrint.route('/game_session', methods=['GET'])
def getSessions():
    sessions = GameSession.query.all()
    return jsonify(result = [session.to_dict() for session in sessions])

@gameSessionBluePrint.route('/game_session/start', methods=['GET'])
def addSession():
    auth_token = request.headers.get('Authorization')
    if auth_token:
        

    if 'user_id' in request.args:
        session = GameSession(request.args['user_id'])
        db.add(session)
        db.commit()
        return session.to_dict()
    else:
        status = Response(status_code=400)
        return status

@gameSessionBluePrint.route('/game_session/end', methods=['GET'])
def endSession():
    if 'game_session_id' in request.args:
        session = GameSession.query.get(request.args['game_session_id'])
        session.is_active = 0
        db.update(session)
        return session.to_dict()
    else:
        status = Response(status_code = 400)
        return status
