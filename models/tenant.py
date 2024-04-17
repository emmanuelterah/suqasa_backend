from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# from dbmodels import db

class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    contact_information = db.Column(db.String(100))
    occupation = db.Column(db.String(100))
    current_address = db.Column(db.String(200))
    previous_address = db.Column(db.String(200))
    emergency_contact = db.Column(db.String(100))