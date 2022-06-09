from crypt import methods
from requests import request
from random_city import app
from random_city.models.Session import Session
from random_city.database import db_session
from flask import jsonify, Response
from random_city.randomCityGenerator import getRandomCity, getRandomStreet
from random_city.models import Ville

@app.route('/ville', methods=['GET'])
def getVille():
    if 'session_id' in request.args and 'latitude' in request.args and 'longitude' in request.args:
        latitude = float(request.args['latitude'])
        longitude = float(request.args['longitude'])
        if 'distance' in request.args:
            distance = float(request.args['distance'])
        else:   
            distance = 50
        ville = getRandomCity(latitude, longitude, distance).to_dic()
        ville.fk_session_id = request.args['session_id']
        ville.street = getRandomStreet(ville)
        db_session.add(ville)
        db_session.commit()
        return ville.to_dict()