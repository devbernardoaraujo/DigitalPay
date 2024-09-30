from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import config_local
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# instance of flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config_local.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = 'bernardogustavoifc'

# instance of database and bcrypt
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# migrations
migrate = Migrate(app, db)

from app.controllers import payments, users, decorators
from app.models import payments, users

# instance of flask login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return users.Users.query.get(int(user_id))