from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from models.dbmodels import db

class Payment(db.models, SerializerMixin):
    __tablename__ = 'payment'

    PaymentID = db.Column(db.Integer, primary_key=True)
    LeaseID = db.Column(db.Integer, db.ForeignKey('lease_agreement.LeaseID'))
    TenantID = db.Column(db.Integer, db.ForeignKey('tenant.TenantID'))
    PaymentDate = db.Column(db.Date)
    PaymentAmount = db.Column(db.Float)
    PaymentMethod = db.Column(db.String)
    PaymentStatus = db.Column(db.String)

    tenant = db.relationship("Tenant", back_populates="payments")
    lease = db.relationship("LeaseAgreement", back_populates="payments")