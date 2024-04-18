from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD

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
=======
from sqlalchemy_serializer import SerializerMixin
from models.dbmodels import db

class MaintenanceRequest(db.Model, SerializerMixin):
    __tablename__ = 'maintenance_requests'

    RequestID = db.Column(db.Integer, primary_key=True)
    PropertyID = db.Column(db.Integer, db.ForeignKey('properties.id'))
    Description = db.Column(db.String)
    RequestDate = db.Column(db.Date)
    RequestedBy = db.Column(db.String)
    Status = db.Column(db.String)
    AssignedStaff = db.Column(db.String)
    CompletionDate = db.Column(db.Date)

    property = db.relationship("Property", back_populates="maintenance_requests")
>>>>>>> origin/Derrick
