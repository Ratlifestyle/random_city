import datetime
import jwt
import os
from enum import unique
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from random_city import db
from random_city.models.Session import Session

class User(db.Model):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    password = Column(Text)
    mail = Column(Text, unique=True)
    pseudo = Column(Text, unique=True)
    sessions = relationship("Session", back_populates="user")

    def __init__(self, first_name=None, last_name=None, password=None, mail=None, pseudo=None, user_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.user_id = user_id
        self.mail = mail
        self.pseudo = pseudo

    def __repr__(self) -> str:
        return f'<User {self.first_name!r}, {self.last_name!r}, {self.mail!r}>'

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                os.getenv('SECRET_KEY'),  # a modifier dans un fichier de config
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, os.getenv('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again'

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "mail": self.mail,
            "pseudo": self.pseudo,
            "sessions": [session.to_dict() for session in self.sessions]
        }
