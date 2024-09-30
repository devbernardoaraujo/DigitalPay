from app import db

class Marketplaces(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_key = db.Column(db.String(80), unique=True, nullable=False)
    private_key = db.Column(db.String(80), unique=True, nullable=False)
    external_id = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    domain = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Marketplace %r>' % self.name



