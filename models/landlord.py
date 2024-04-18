from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from models.dbmodels import db

class Landlord(db.Model, SerializerMixin):
    __tablename__ = 'landlords'

    LandlordID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    ContactInfo = db.Column(db.String)
    BankAcctInfo = db.Column(db.String)
    Address = db.Column(db.String)

    properties = db.relationship("Property", back_populates="landlord")