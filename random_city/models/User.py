import datetime
import jwt
import os
from sqlalchemy import Column, Text
from sqlalchemy.orm import relationship
from random_city import db
from sqlalchemy.types import INTEGER


class User(db.Model):
    __tablename__ = 'User'
    user_id = Column(INTEGER, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    password = Column(Text)
    mail = Column(Text, unique=True)
    pseudo = Column(Text, unique=True)
    game_sessions = relationship("GameSession", back_populates="user")

    def __init__(self, first_name=None, last_name=None, password=None, mail=None, pseudo=None, user_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.user_id = user_id
        self.mail = mail
        self.pseudo = pseudo

    def __repr__(self) -> str:
        return f'<User {self.first_name!r}, {self.last_name!r}, {self.mail!r}>'

    def encode_auth_token(self):
        if(self.user_id!=None):
            try:
                payload = {
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=3600), #definir un temps convenable genre 24h ou 1 semaine
                    'iat': datetime.datetime.utcnow(),
                    'sub': self.user_id
                }
                return jwt.encode(
                    payload,
                    os.getenv('SECRET_KEY'),  # a modifier dans un fichier de config
                    algorithm='HS256'
                )
            except Exception as e:
                return e
        return None

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, os.getenv('SECRET_KEY'), 'HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again'
        except jwt.InvalidTokenError as e:
            print(e)
            return 'Invalid token. Please log in again'

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "mail": self.mail,
            "pseudo": self.pseudo,
            'password': self.password,
            "sessions": [game_session.to_dict() for game_session in self.game_sessions]
        }
