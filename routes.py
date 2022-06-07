from flask import Flask, jsonify, request
from randomCityGenerator import getRandomCity, getRandomStreet

app = Flask(__name__)

@app.route("/city", methods=['GET'])
def city():
    if 'latitude' in request.args and 'longitude' in request.args:
        latitude = float(request.args['latitude'])
        longitude = float(request.args['longitude'])
        if 'distance' in request.args:
            distance = float(request.args['distance'])
        else:
            distance = 50
        return jsonify(getRandomCity(latitude, longitude, distance).to_dic())
    else:
        print("error /city")

@app.route("/street", methods=['GET'])
def street():
    if 'city' in request.args and 'postCode' in request.args:
        city = request.args['city']
        postCode = request.args['postCode']
        return jsonify(getRandomStreet(city=city, postCode=postCode))
    else:
        print("error /street")

if __name__ == "__main__":
    app.run(debug=True)