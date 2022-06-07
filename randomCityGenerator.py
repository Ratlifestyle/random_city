import math
import random
import re
from select import select
import sqlite3

import requests
from Ville import Ville
from calculDistance import deg2rad, distanceGPS, dms2dd

def get_liste_villes(latA, longA, distance):
    conn = sqlite3.connect('data.sqlite')
    cursor = conn.execute("select ville_nom, ville_longitude_deg, ville_latitude_deg, ville_code_postal from villes_france_free")
    liste_villes = []
    for row in cursor:
        nom = row[0]
        longB = deg2rad(float(row[1]))
        latB = deg2rad(float(row[2]))
        codePostal = row[3]
        distanceGps = distanceGPS(latA, longA, latB, longB) 
        if distanceGps <=distance*1000:
            ville = Ville(nom, latB, latA, distanceGps, codePostal)
            liste_villes.append(ville)
    return liste_villes

def getRandomCity(latitude, longitude, distance):
    latitude = deg2rad(latitude)
    longitude = deg2rad(longitude)
    liste_villes = get_liste_villes(latitude, longitude, distance)
    return random.choice(liste_villes)

def getRandomStreet(city, postCode):
    query = {'q' : city, 'type' : 'street', 'limit' : 100, 'autocomplete' : 1, 'postcode' : postCode}
    response = requests.get("https://api-adresse.data.gouv.fr/search/", params=query)
    print(response.json())
    result = response.json()['features']
    return random.choice(result)