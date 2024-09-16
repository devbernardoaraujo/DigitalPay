from app import app, db, bcrypt

class Marketplaces(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_key = db.Column(db.String(80), unique=True, nullable=False)
    private_key = db.Column(db.String(80), unique=True, nullable=False)
    external_id = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    domain = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Marketplace %r>' % self.name

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    marketplace_id = db.Column(db.Integer, db.ForeignKey('marketplaces.id'))

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password.encode('utf-8'))

    def __repr__(self):
        return '<User %r>' % self.name

