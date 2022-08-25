from sqlalchemy import Column, Integer, Text, ForeignKey, relationship
from random_city import db

class DeviceLocation(db.Model):
    __tablename__ = "device_location"
    device_location_id = Column(Integer, primary_key=True)
    latitude = Column(Text)
    longitude = Column(Text)
    fk_game_session_id = Column(Integer, ForeignKey("GameSession.game_session_id"), nullable=False)
    recorded_on = Column(Text)
    game_session = relationship("Session", back_populates='device_location')

    def __init__(self, latitude, longitude, fk_session_id, recorded_on):
        self.latitude = latitude
        self.longitude = longitude
        self.recorded_on = recorded_on
        self.fk_session_id = fk_session_id
    
    def to_dict(self):
        return {
            "device_location_id" : self.device_location_id,
            "latitude" : self.latitude,
            "longitude" : self.longitude,
            "recorded_on" : self.recorded_on,
            "fk_session_id" : self.fk_session_id
        }