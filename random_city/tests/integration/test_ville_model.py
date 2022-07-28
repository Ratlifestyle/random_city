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
    def setUp(self):
        super().setUp()
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        self.register_user(user)

class TestVille(BaseTestVille):
    def testGetVille(self):
        user = User.query.filter_by(pseudo='ratata').first()
        auth_token = user.encode_auth_token()
        response = self.client.get(
            '/ville'+'?session_id=1&latitude=48.73&longitude=2.26',
            headers=dict(
                Authorization=auth_token
            )
        )
        print(response)

