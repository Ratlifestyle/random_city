

import pytest
from random_city.app import createApp
from config import TestingConfig

@pytest.fixture
def client():
    app = createApp(TestingConfig)
    with app.test_client() as client:
        yield client