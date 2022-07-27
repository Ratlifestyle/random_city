from flask_testing import TestCase

from random_city import app, db


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def setUp(self):
        print('aaaa')
        db.create_all()
        print('bbbbb')
        db.session.commit()

