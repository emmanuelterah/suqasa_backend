from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD

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
=======
from sqlalchemy_serializer import SerializerMixin
from models.dbmodels import db

class Tenant(db.Model, SerializerMixin):
    __tablename__ = 'tenants'

    TenantID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    ContactInfo = db.Column(db.String)
    Occupation = db.Column(db.String)
    CurrentAddr = db.Column(db.String)
    PrevAddr = db.Column(db.String)
    EmergencyCnt = db.Column(db.String)

    leases = db.relationship("LeaseAgreement", back_populates="tenant")
    payments = db.relationship("Payment", back_populates="tenant")
>>>>>>> origin/Derrick
