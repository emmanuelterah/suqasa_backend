from flask_sqlalchemy import SQLAlchemy

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