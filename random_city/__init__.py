import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

os.environ['SECRET_KEY'] = str(os.urandom(24))

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
CORS(app)

engine_options = {
    'echo': True
}
db = SQLAlchemy(app, engine_options=engine_options)
#db = SQLAlchemy(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


from random_city.routes.GameSessionController import gameSessionBluePrint

app.register_blueprint(gameSessionBluePrint)

from random_city.routes.UserController import userBluePrint

app.register_blueprint(userBluePrint)

from random_city.routes.VilleController import villeBluePrint

app.register_blueprint(villeBluePrint)

import random_city.errorsHandler.UserControllerErrorsHandler

