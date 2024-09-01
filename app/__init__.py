from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import config_local

# instance of flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config_local.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.controllers import payments
from app.models import payments