from sqlalchemy import Column, ForeignKey, Integer, Numeric, Text
from sqlalchemy.orm import relationship
from random_city.database import Base

class Ville(Base):

    ville_id = Column(Integer, primary_key=True)
    name = Column(Text)
    latitude = Column(Numeric)
    longitude = Column(Numeric)
    distance = Column(Numeric)
    codePostal = Column(Integer)
    fk_session_id = Column(Integer, ForeignKey("Session.session_id"))
    session = relationship("Session", back_populates="villes")

    def __init__(self, name, latitude, longitude, distance, codePostal, fk_session_id):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.distance = distance
        self.codePostal = codePostal
        self.fk_session_id = fk_session_id

    def __str__(self) -> str:
        return "name : " + str(self.name) + " latitude : " + str(self.latitude) + " longitude : " + str(self.longitude)

    def __repr__(self) -> str:
        return str(self)

    def to_dic(self):
        return {
            "name" : self.name,
            "distance" : self.distance/1000,
            "latitude" : self.latitude,
            "longitude" : self.longitude,
            "codePostal" : self.codePostal,
        }