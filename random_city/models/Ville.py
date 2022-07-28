from sqlalchemy import Column, ForeignKey, Integer, Numeric, Text
from sqlalchemy.orm import relationship
from random_city import db


class Ville(db.Model):

    __tablename__ = "Ville"
    ville_id = Column(Integer, primary_key=True)
    name = Column(Text)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    distance = Column(Numeric)
    codePostal = Column(Integer)
    street = Column(Text)
    fk_session_id = Column(Integer, ForeignKey("Session.session_id"))
    session = relationship("Session", back_populates="villes")

    def __init__(self, name, latitude, longitude, distance, codePostal, fk_session_id, street=None):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
        self.codePostal = codePostal
        self.fk_session_id = fk_session_id
        self.street = street

    def __str__(self) -> str:
        return "name : " + str(self.name) + " latitude : " + str(self.latitude) + " longitude : " + str(self.longitude) + " steet : " + str(self.street)

    def __repr__(self) -> str:
        return str(self)

    def to_dict(self):
        return {
            "name" : self.name,
            "distance" : self.distance/1000,
            "latitude" : self.latitude,
            "longitude" : self.longitude,
            "codePostal" : self.codePostal,
            "steet" : self.street
        }