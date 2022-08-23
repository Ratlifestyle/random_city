from sqlalchemy import Column, Integer, Text, ForeignKey
from random_city import db

class DeviceLocation(db.Model):
    __tablename__ = "device_location"
    device_location_id = Column(Integer, primary_key=True)
    latitude = Column(Text)
    longitude = Column(Text)
    fk_game_session_id = Column(Integer, ForeignKey("GameSession.game_session_id"), nullable=False)
    #session = relationship("Session", backref=backref("device_location", use_list=False))

    def __init__(self, latitude, longitude, fk_session_id):
        self.latitude = latitude
        self.longitude = longitude
        self.fk_session_id = fk_session_id
    
    def to_dict(self):
        return {
            "device_location_id" : self.device_location_id,
            "latitude" : self.latitude,
            "longitude" : self.longitude,
            "fk_session_id" : self.fk_session_id
        }