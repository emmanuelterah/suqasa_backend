from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .dbmodels import db

class Payment(db.Model):
    __tablename__ = 'payments'

    PaymentID = db.Column(db.Integer, primary_key=True)
    LeaseID = db.Column(db.Integer, ForeignKey('lease_agreements.LeaseID'))
    TenantID = db.Column(db.Integer, ForeignKey('tenants.TenantID'))
    PaymentDate = db.Column(db.Date)
    PaymentAmount = db.Column(db.Float)
    PaymentMethod = db.Column(db.String)
    PaymentStatus = db.Column(db.String)

    lease = relationship("LeaseAgreement", back_populates="payments")
    tenant = relationship("Tenant", back_populates="payments")
