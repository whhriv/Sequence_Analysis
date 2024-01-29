from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)


login = LoginManager(app)
login.login_view = 'login'
login.init_app(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)



# from app.blueprints.api import api
# app.register_bluepriint(api)

from . import routes, models