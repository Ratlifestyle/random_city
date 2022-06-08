from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from random_city.database import Base

class Session(Base):
    __tablename__ = 'Session'
    session_id = Column(Integer, primary_key= True)
    is_active = Column(Integer)
    duree = Column(Text)
    result = Column(Integer)
    fk_user_id = Column(Integer, ForeignKey("User.user_id"), nullable=False)
    user = relationship("User", back_populates="sessions")
    villes = relationship("Ville", back_populates="sessions")

    def __init__(self, fk_user_id, is_active=0, duree = "0", result=0):
        self.is_active = is_active
        self.duree = duree
        self.result = result
        self.fk_user_id = fk_user_id

    def to_dict(self):
        return {
            "session_id" : self.session_id,
            "is_active" : self.is_active,
            "duree" : self.duree,
            "result" : self.result,
            "user" : self.fk_user_id,
            "ville" : [ville.to_dict() for ville in self.villes]
        }