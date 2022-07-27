import os
from random_city.database import db_session, init_db
from random_city.app import createApp
from config import DevelopmentConfig
from flask import Flask
from flask_cors import CORS
from random_city.database import db_session, init_db
from flask_sqlalchemy import SQLAlchemy

app = createApp(DevelopmentConfig)
init_db()
app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS', 'config.DevelopmentConfig'))
CORS(app)

db = SQLAlchemy(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

import random_city.routes.UserController
import random_city.routes.SessionController
import random_city.routes.VilleController