from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# instance of flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:720horasgratis@localhost/inovafinance'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from app.controllers import payments
from app.models import payments