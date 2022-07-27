import json
import unittest
from random_city.tests.integration.Base import BaseTestCase


def login_user(self, email, password):
    return self.client.post(
        '/user/login',
        data=json.dumps(dict(
            email=email,
            password=password
        )),
        content_type='application/json',
    )


class TestUser(BaseTestCase):
    def register_user(self, email, password):
        return self.client.post(
            '/user/register',
            data=json.dumps(dict(
                email=email,
                password=password
            )),
            content_type='application/json',
        )

    def test_registration(self):
        response = self.register_user('ratata@test', 'test')
        print(response)
        data = json.loads(response.data.decode())
        print(data)


if __name__ == '__main__':
    unittest.main()
