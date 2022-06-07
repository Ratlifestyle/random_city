import code


class Ville:
    def __init__(self, nom, latitude, longitude, distance, codePostal):
        self.nom = nom
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
        self.codePostal = codePostal

    def __str__(self) -> str:
        return "nom : " + str(self.nom) + " latitude : " + str(self.latitude) + " longitude : " + str(self.longitude) 

    def __repr__(self) -> str:
        return str(self)

    def to_dic(self):
        return {
            "nom" : self.nom,
            "distance" : self.distance/1000,
            "latitude" : self.latitude,
            "longitude" : self.longitude,
            "codePostal" : self.codePostal
        }