from random_city.tests.integration.Base import BaseTestCase
from random_city.models.User import User
import json
import unittest

class BaseTestVille(BaseTestCase):
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
        return self.client.get(
            '/game_session/start',
            headers=dict(
                Authorization=user.encode_auth_token()
            ),
            content_type='application/json'
        )

    def endSession(self, session):
        return self.client.get(
            'game_session/end?game_session_id='+str(session['game_session_id']),
            content_type='application/json'
        )


    def populate_user(self) -> User:
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        self.register_user(user)
        return User.query.filter_by(pseudo='ratata').first()


    def getVille(self, session_id, latitude, longitude, distance='50') :
        return self.client.get(
            '/ville?game_session_id='+session_id+'&latitude='+latitude+'&longitude='+longitude+'&distance='+distance,
            content_type='application/json'
        )


    def setUp(self):
        super().setUp()
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        self.register_user(user)

class TestVille(BaseTestVille):
    def testGetVille(self):
        user = User.query.filter_by(pseudo='ratata').first()
        response = self.startSession(user)
        self.assert200(response)
        data = json.loads(response.data.decode())
        response = self.getVille(str(data['result']['game_session_id']), '48.73', '2.26')
        print(response)

