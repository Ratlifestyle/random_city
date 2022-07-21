from mimetypes import init
from flask import Flask
from flask_cors import CORS
from random_city.database import db_session, init_db

app = Flask(__name__)
CORS(app)
init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

import random_city.routes.UserController
import random_city.routes.SessionController
import random_city.routes.VilleController