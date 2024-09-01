# import flast module
from flask import Flask

# instance of flask application
app = Flask(__name__)


from app.controllers import payments