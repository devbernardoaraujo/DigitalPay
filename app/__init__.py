# import flast module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# instance of flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

from app.controllers import payments