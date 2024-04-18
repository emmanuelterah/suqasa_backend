from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from models.dbmodels import db

class LeaseAgreement(db.models, SerializerMixin):
    __tablename__ = 'lease_agreements'

    LeaseID = db.Column(db.Integer, primary_key=True)
    PropertyID = db.Column(db.Integer, db.ForeignKey('property.PropertyID'))
    TenantID = db.Column(db.Integer, db.ForeignKey('tenant.TenantID'))
    StartDate = db.Column(db.Date)
    EndDate = db.Column(db.Date)
    RentAmount = db.Column(db.Float)
    PaymentSchedule = db.Column(db.String)
    DepositAmount = db.Column(db.Float)

    property = db.relationship("Property", back_populates="leases")
    tenant = db.relationship("Tenant", back_populates="leases")
    payments = db.relationship("Payment", back_populates="lease")