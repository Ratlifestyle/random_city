import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

os.environ['SECRET_KEY'] = str(os.urandom(24))

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
CORS(app)

db = SQLAlchemy(app)

import random_city.models.User

db.create_all()
db.session.commit()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


from random_city.routes.UserController import userBluePrint

app.register_blueprint(userBluePrint)

from random_city.routes.VilleController import villeBluePrint

app.register_blueprint(villeBluePrint)

import random_city.errorsHandler.UserControllerErrorsHandler

