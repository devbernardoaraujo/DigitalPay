from app import app, db

class Marketplaces(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    public_key = db.Column(db.String(80), unique=True, nullable=False)
    private_key = db.Column(db.String(80), unique=True, nullable=False)
    external_id = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    domain = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Marketplace %r>' % self.name

# class User(db.Model):
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     password = db.Column(db.String(80), nullable=False)
#     login = db.Column(db.String(80), unique=True, nullable=False)
#     marketplace_id = db.Column(db.Integer, db.foreignKey('marketplace.id'))
#
#     def __repr__(self):
#         return '<User %r>' % self.name