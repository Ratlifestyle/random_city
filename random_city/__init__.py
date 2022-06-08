from mimetypes import init
from flask import Flask
from random_city.database import db_session, init_db

app = Flask(__name__)
init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

import random_city.routes.routes
import random_city.routes.UserController
import random_city.routes.SessionController