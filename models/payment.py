from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
# from models.dbmodels import db
from dbmodels import db

class Payment(db.Model, SerializerMixin):
    __tablename__ = 'payments'

    PaymentID = db.Column(db.Integer, primary_key=True)
    LeaseID = db.Column(db.Integer, db.ForeignKey('lease_agreements.LeaseID'))
    TenantID = db.Column(db.Integer, db.ForeignKey('tenants.TenantID'))
    PaymentDate = db.Column(db.Date)
    PaymentAmount = db.Column(db.Float)
    PaymentMethod = db.Column(db.String)
    PaymentStatus = db.Column(db.String)

    tenant = db.relationship("Tenant", back_populates="payments")
    lease = db.relationship("LeaseAgreement", back_populates="payments")