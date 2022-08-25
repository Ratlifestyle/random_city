from flask import Blueprint, jsonify, request, make_response
from datetime import datetime
from random_city.models.DeviceLocation import DeviceLocation
from random_city.exceptions.BadRequestException import BadRequestException
from random_city.models.DeviceLocationHistory import DeviceLocationHistory
from random_city import db
from random_city.checkPosition import isInTown, isInStreet
from random_city.models.Ville import Ville

deviceLocationBluePrint = Blueprint('DeviceLocationBluePrint', __name__)

@deviceLocationBluePrint.route('/device_location/add')
def addDeviceLocation():
    if 'game_session_id' in request.args and 'latitude' in request.args and 'longitude' in request.args:
        deviceLocation = DeviceLocation.query.filter_by(fk_game_session_id=request.args['game_session_id']).first()
        if deviceLocation:
            deviceLocationHistory = DeviceLocationHistory(deviceLocation.latitude, deviceLocation.longitude, request.args['game_session_id'], deviceLocation.recorded_on)
            db.session.add(deviceLocationHistory)
        deviceLocation.longitude = request['longitude']
        deviceLocation.latitude = request['latitude']
        deviceLocation.recorded_on = datetime.now()
        db.session.commit()
        responseObject = {
            'status': 'success',
            'result': deviceLocation.to_dict()
        }
        return make_response(jsonify(responseObject)), 200
    else:
        raise BadRequestException()

@deviceLocationBluePrint.route('/device_location/checkPositionCity')
def addDeviceLocation():
    if 'game_session_id' in request.args and 'latitude' in request.args and 'longitude' in request.args:
        deviceLocation = DeviceLocation.query.filter_by(fk_game_session_id=request.args['game_session_id'])
        if deviceLocation:
            city = Ville.query.filter_by(fk_game_session_id=request.args['game_session_id']).first()   
            if isInTown(request.args['latitude'], request.args['longitude'], city):
                responseObject = {
                'status': 'success',
                'result': True
                }
            else:
                responseObject = {
                'status': 'success',
                'result': False
                }                
            return make_response(jsonify(responseObject)), 200
    raise BadRequestException()

@deviceLocationBluePrint.route('/device_location/checkPositionRoad')
def addDeviceLocation():
    if 'game_session_id' in request.args and 'latitude' in request.args and 'longitude' in request.args:
        deviceLocation = DeviceLocation.query.filter_by(fk_game_session_id=request.args['game_session_id'])
        if deviceLocation:
            city = Ville.query.filter_by(fk_game_session_id=request.args['game_session_id']).first()   
            if isInStreet(request.args['latitude'], request.args['longitude'], city):
                responseObject = {
                'status': 'success',
                'result': True
                }
            else:
                responseObject = {
                'status': 'success',
                'result': False
                }                
            return make_response(jsonify(responseObject)), 200
    raise BadRequestException()