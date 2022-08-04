from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from random_city import db
from datetime import date

class GameSession(db.Model):
    __tablename__ = 'GameSession'
    game_session_id = Column(Integer, primary_key=True)
    is_active = Column(Integer)
    dateStart = Column(Text)
    duree = Column(Text)
    result = Column(Integer)
    fk_user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)
    user = relationship("User", back_populates="game_sessions")
    villes = relationship("Ville", back_populates="game_session")

    def __init__(self, fk_user_id, is_active=0, dateStart=date.today(), duree="0", result=0):
        self.is_active = is_active
        self.dateStart = dateStart
        self.duree = duree
        self.result = result
        self.fk_user_id = fk_user_id

    def to_dict(self):
        return {
            "game_session_id": self.game_session_id,
            "is_active": self.is_active,
            "date": self.dateStart,
            "duree": self.duree,
            "result": self.result,
            "user": self.fk_user_id,
            "ville": [ville.to_dict() for ville in self.villes]
        }
