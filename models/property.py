from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from models.dbmodels import db

class Property (db.model, SerializerMixin):
    __tablename__ = 'property'
    
    serialize_only = ('id')
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Colum(db.String)
    address = db.Column(db.String)
    description =db.Column(db.String)
    Bedrooms = db.Column(db.Integer)
    image = db.Column(db.VARCHAR)
    Size = db.Column(db.Float)
    RentAmount = db.Column(db.Float)
    Status = db.Column(db.String)

    LandlordID = db.Column(db.Integer, db.ForeignKey('landlord.LandlordID'))
    landlord = db.relationship("Landlord", back_populates="properties")
    leases = db.relationship("LeaseAgreement", back_populates="property")
    maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")

    

