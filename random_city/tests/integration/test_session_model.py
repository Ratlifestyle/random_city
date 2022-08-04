import json
import unittest
from random_city.tests.integration.Base import BaseTestCase
from random_city.models.User import User

class BaseTestSession(BaseTestCase):
    def register_user(self, user : User):
        return self.client.post(
            '/user/register',
            data=json.dumps(user.to_dict()),
            content_type='application/json',
        )
    def validPseudo(self, pseudo):
        return self.client.get('/user/validPseudo/'+pseudo)
    
    def login_user(self, email, password):
        return self.client.post(
            '/user/login',
            data=json.dumps(dict(
            mail=email,
            password=password
            )),
            content_type='application/json',
        )
    def startSession(self, user : User):
        return self.client.get(\
            '/game_session/start',
            headers=dict(
                Authorization=user.encode_auth_token()
            ),
            content_type='application/json'
        )

    def populate_user(self) -> User:
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        self.register_user(user)
        return User.query.filter_by(pseudo='ratata').first()

class TestSession(BaseTestSession):
    def test_start_session(self):
        user = self.populate_user()
        response = self.startSession(user)