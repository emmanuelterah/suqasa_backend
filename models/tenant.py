from .dbmodels import db
from sqlalchemy_serializer import SerializerMixin

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
