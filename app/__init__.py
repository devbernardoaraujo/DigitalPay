from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import config_local
from flask_bcrypt import Bcrypt


# instance of flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config_local.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = 'bernardogustavoifc'

# instance of database and bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# migrations
migrate = Migrate(app, db)

from app.controllers import payments
from app.models import payments