from random_city import db
from flask import Blueprint, jsonify, request, make_response
from random_city.randomCityGenerator import getRandomCity, getRandomStreet
from random_city.exceptions.BadRequestException import BadRequestException


villeBluePrint = Blueprint('VilleBluePrint', __name__)


@villeBluePrint.route('/ville', methods=['GET'])
def getVille():
    if 'game_session_id' in request.args and 'latitude' in request.args and 'longitude' in request.args:
        latitude = float(request.args['latitude'])
        longitude = float(request.args['longitude'])
        if 'distance' in request.args:
            distance = float(request.args['distance'])
        else:   
            distance = 50
        ville = getRandomCity(latitude, longitude, distance)
        ville.fk_session_id = request.args['game_session_id']
        ville.street = getRandomStreet(ville)['properties']['label']
        db.session.add(ville)
        db.session.commit()
        responseObject = {
            'status' : 'success',
            'result' : ville.to_dict(),
            'status_code' : 200
        } 
        return make_response(jsonify(responseObject)), 200
    raise BadRequestException()