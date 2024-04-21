from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# from dbmodels import db
class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    contact_information = db.Column(db.String(100))
    role = db.Column(db.String(50))