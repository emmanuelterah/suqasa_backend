from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# from dbmodels import db

class MaintenanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    description = db.Column(db.Text)
    request_date = db.Column(db.Date)
    requested_by = db.Column(db.String(50))
    status = db.Column(db.String(50))
    assigned_staff = db.Column(db.String(100))
    completion_date = db.Column(db.Date)