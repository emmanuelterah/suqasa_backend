from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD

db = SQLAlchemy()
# from dbmodels import db

class LeaseAgreement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    tenant_id = db.Column(db.Integer, db.ForeignKey('tenant.id'))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    rent_amount = db.Column(db.Float)
    payment_schedule = db.Column(db.String(50))
    lease_duration = db.Column(db.Integer)
    deposit_amount = db.Column(db.Float)
=======
from sqlalchemy_serializer import SerializerMixin
from models.dbmodels import db

class LeaseAgreement(db.Model, SerializerMixin):
    __tablename__ = 'lease_agreements'

    LeaseID = db.Column(db.Integer, primary_key=True)
    PropertyID = db.Column(db.Integer, db.ForeignKey('properties.id'))
    TenantID = db.Column(db.Integer, db.ForeignKey('tenants.TenantID'))
    StartDate = db.Column(db.Date)
    EndDate = db.Column(db.Date)
    RentAmount = db.Column(db.Float)
    PaymentSchedule = db.Column(db.String)
    DepositAmount = db.Column(db.Float)

    property = db.relationship("Property", back_populates="leases")
    tenant = db.relationship("Tenant", back_populates="leases")
    payments = db.relationship("Payment", back_populates="lease")
>>>>>>> origin/Derrick
