import requests


def getTown(latitude, longitude):
    query = {'latitude': latitude, 'longitude': longitude, 'format': 'json'}
    response = requests.get('https://nominatim.openstreetmap.org/reverse', params=query)
    return response.json()

def isInTown(latitude, longitude, city):
    cityName = city.name
    result = getTown(latitude=latitude, longitude=longitude)
    return result['address']['town'].upper() == cityName.upper()

def isInStreet(latitude, longitude, city):
    if isInTown:
        town = getTown(latitude, longitude)
        street = city.street
        return town['address']['road'] == street
    else:
        return False