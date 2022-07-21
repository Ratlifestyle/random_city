from enum import unique
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from random_city.database import Base

class User(Base):

    __tablename__ = 'User'
    user_id = Column(Integer, primary_key= True)
    first_name = Column(Text)
    last_name = Column(Text)
    login = Column(Text, unique=True)
    password = Column(Text)
    mail = Column(Text)
    pseudo = Column(Text, unique=True)
    sessions = relationship("Session", back_populates="user")

    def __init__(self, first_name=None, last_name=None, login=None, password=None, mail=None, pseudo=None, user_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.user_id = user_id
        self.mail = mail
        self.pseudo = pseudo
        
    def __repr__(self) -> str:
        return f'<User {self.first_name!r}, {self.last_name!r}, {self.login!r}>'
    
    def to_dict(self):
        return {
            "user_id" : self.user_id,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "login" : self.login,
            "mail" : self.mail,
            "pseudo" : self.pseudo,
            "sessions" : [session.to_dict() for session in self.sessions]
        }