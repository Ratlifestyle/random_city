from random_city import app, db
from random_city.models.Session import Session
from flask import Blueprint, jsonify, Response, request
from random_city.randomCityGenerator import getRandomCity, getRandomStreet
from random_city.models import Ville

villeBluePrint = Blueprint('VilleBluePrint', __name__)

@villeBluePrint.route('/ville', methods=['GET'])
def getVille():
    auth_header = request.headers.get('Authorization')
    #ajout de verification du JWT
    if 'session_id' in request.args and 'latitude' in request.args and 'longitude' in request.args:
        latitude = float(request.args['latitude'])
        longitude = float(request.args['longitude'])
        if 'distance' in request.args:
            distance = float(request.args['distance'])
        else:   
            distance = 50
        ville = getRandomCity(latitude, longitude, distance).to_dict()
        ville.fk_session_id = request.args['session_id']
        ville.street = getRandomStreet(ville)
        db.add(ville)
        db.commit()
        return ville.to_dict()