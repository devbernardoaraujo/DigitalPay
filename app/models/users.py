from app import db, bcrypt
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    marketplace_id = db.Column(db.Integer, db.ForeignKey('marketplaces.id'))
    seller_id = db.Column(db.String(32), unique=True, nullable=True)
    role = db.Column(db.String(50), nullable=True)

    def is_marketplace_admin(self):
        return self.role == 'marketplace_admin'

    def is_sys_admin(self):
        return self.role == 'sys_admin'

    def is_seller(self):
        return self.role == 'seller'

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password.encode('utf-8'))

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def __repr__(self):
        return '<User %r>' % self.name