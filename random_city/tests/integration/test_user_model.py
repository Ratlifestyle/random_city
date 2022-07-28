import json
import unittest
from random_city.tests.integration.Base import BaseTestCase
from random_city.models.User import User


class BaseTestUser(BaseTestCase):
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

class TestUserRegistration(BaseTestUser):
    def test_registration(self):
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        response = self.register_user(user)
        data = json.loads(response.data.decode())
        self.assertEqual(data['status_code'], '201')

    def test_registration_same_mail(self):
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        response = self.register_user(user)
        data = json.loads(response.data.decode())
        self.assertEqual(data['status_code'], '201')        
        user = User('testFN2', 'testLN2', 'testPass2', 'test@mail.fr', 'ratata2')
        response = self.register_user(user)
        data = json.loads(response.data.decode())
        self.assertEqual(data['status_code'], '409')

    def test_registration_same_pseudo(self):
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        response = self.register_user(user)
        data = json.loads(response.data.decode())
        self.assertEqual(data['status_code'], '201')        
        user = User('testFN2', 'testLN2', 'testPass2', 'test2@mail.fr', 'ratata')
        response = self.register_user(user)
        data = json.loads(response.data.decode())
        self.assertEqual(data['status_code'], '409')

    def test_registration_same_pseudo_same_mail(self):
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        response = self.register_user(user)
        data = json.loads(response.data.decode())
        self.assertEqual(data['status_code'], '201')        
        user = User('testFN2', 'testLN2', 'testPass2', 'test@mail.fr', 'ratata')
        response = self.register_user(user)
        data = json.loads(response.data.decode())
        self.assertEqual(data['status_code'], '409')

    def test_valid_pseudo(self):
        pseudo = 'ratata'
        response = self.validPseudo(pseudo)
        data = json.loads(response.data.decode())
        self.assertTrue(data['result'])
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        response = self.register_user(user)
        data = json.loads(response.data.decode())
        response = self.validPseudo(pseudo)
        data = json.loads(response.data.decode())
        self.assertFalse(data['result'])

class TestUserLogin(BaseTestUser):
    def test_login(self):
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        self.register_user(user)
        response = self.login_user('test@mail.fr', 'testPass')
        self.assert200(response)

    def test_login_bad_credentials(self):
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        self.register_user(user)
        response = self.login_user('test@mail.fr', 'testPass2')
        self.assert401(response)
        response = self.login_user('test2@mail.fr', 'testPass')
        self.assert401(response)

class TestUserJWT(BaseTestUser):
    def test_encode_auth_token(self):
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        self.register_user(user)
        user = User.query.filter_by(pseudo='ratata').first()
        auth_token = user.encode_auth_token()
        self.assertTrue(isinstance(auth_token, str))

    def test_decode_auth_token(self):
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        self.register_user(user)
        user = User.query.filter_by(pseudo='ratata').first()
        auth_token = user.encode_auth_token()
        self.assertEqual(User.decode_auth_token(auth_token), 1)
    
    def test_get_token_register(self):
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        response = self.register_user(user)
        data = json.loads(response.data.decode())
        self.assertEqual(User.decode_auth_token(data['auth_token']), 1)

    def test_get_token_login(self):
        user = User('testFN', 'testLN', 'testPass', 'test@mail.fr', 'ratata')
        self.register_user(user)
        response = self.login_user('test@mail.fr', 'testPass')
        data = json.loads(response.data.decode())
        self.assertEqual(User.decode_auth_token(data['auth_token']), 1)

if __name__ == '__main__':
    unittest.main()
