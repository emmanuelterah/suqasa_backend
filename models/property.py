from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from dbmodels import db
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    description = db.Column(db.Text)
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    size = db.Column(db.Float)
    rent_amount = db.Column(db.Float)
    status = db.Column(db.String(50))