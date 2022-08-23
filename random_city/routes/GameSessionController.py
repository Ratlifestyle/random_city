from random_city import app, db
from random_city.models.User import User
from random_city.models.GameSession import GameSession
from flask import Blueprint, jsonify, Response, request, make_response
from random_city.exceptions.BadRequestException import BadRequestException

gameSessionBluePrint = Blueprint('GameSessionBluePrint', __name__)


@gameSessionBluePrint.route('/game_session', methods=['GET'])
def getSessions():
    sessions = GameSession.query.all()
    return jsonify(result = [session.to_dict() for session in sessions])

@gameSessionBluePrint.route('/game_session/start', methods=['GET'])
def addSession():
    auth_token = request.headers.get('Authorization')
    if auth_token:
        user_id = User.decode_auth_token(auth_token)
        user = User.query.get(user_id)
        session = GameSession(user_id, 1)
        db.session.add(session)
        db.session.commit()
        responseObject = {
            'status': 'success',
            'result': session.to_dict()
        }
        return make_response(jsonify(responseObject)), 200
    else:
        raise BadRequestException()

@gameSessionBluePrint.route('/game_session/end', methods=['GET'])
def endSession():
    if 'game_session_id' in request.args:
        session = GameSession.query.get(request.args['game_session_id'])
        session.is_active = 0
        db.session.commit()
        responseObject = {
            'status': 'success',
            'result' : session.to_dict()
        }
        return make_response(jsonify(responseObject)), 200
    else:
        raise BadRequestException()

@gameSessionBluePrint.route('/game_session/delete', methods=['DELETE'])
def deleteSession():
    if 'game_session_id' in request.args:
        session = GameSession.query.get(request.args['game_session_id'])
        if session:
            if session.is_active == 0:
                session.delete(synchronize_session=False)
            else:
                responseObject  = {
                    'status' : 'failed',
                    'result' : 'session is active',
                    'status_code': 403
                }
                return make_response(jsonify(responseObject)), 403
        else:
            responseObject = {
                'status' : 'success',
                'result': 'session doesnt exist',
                'status_code': 204
            }
            return make_response(jsonify(responseObject)), 204
    else:
        raise BadRequestException()