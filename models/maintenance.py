# # # from flask_sqlalchemy import SQLAlchemy
# # # from sqlalchemy_serializer import SerializerMixin
# # # from models.dbmodels import db

# # # <<<<<<< HEAD
# # # db = SQLAlchemy()
# # # from dbmodels import db
# # # =======
# # # class MaintenanceRequest(db.Model, SerializerMixin):
# # #     __tablename__ = 'maintenance_requests'
# # # >>>>>>> origin

# # #     RequestID = db.Column(db.Integer, primary_key=True)
# # #     PropertyID = db.Column(db.Integer, db.ForeignKey('properties.id'))
# # #     Description = db.Column(db.String)
# # #     RequestDate = db.Column(db.Date)
# # #     RequestedBy = db.Column(db.String)
# # #     Status = db.Column(db.String)
# # #     AssignedStaff = db.Column(db.String)
# # #     CompletionDate = db.Column(db.Date)

# # #     property = db.relationship("Property", back_populates="maintenance_requests")

# # from flask_sqlalchemy import SQLAlchemy
# # from sqlalchemy_serializer import SerializerMixin
# # from .dbmodels import db

# # class MaintenanceRequest(db.Model, SerializerMixin):
# #     __tablename__ = 'maintenance_requests'

# #     RequestID = db.Column(db.Integer, primary_key=True)
# #     PropertyID = db.Column(db.Integer, db.ForeignKey('properties.id'))
# #     Description = db.Column(db.String)
# #     RequestDate = db.Column(db.Date)
# #     RequestedBy = db.Column(db.String)
# #     Status = db.Column(db.String)
# #     AssignedStaff = db.Column(db.String)
# #     CompletionDate = db.Column(db.Date)

# #     property = db.relationship("Property", back_populates="maintenance_requests")

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMixin

# db = SQLAlchemy()

# class MaintenanceRequest(db.Model, SerializerMixin):
#     __tablename__ = 'maintenance_requests'

#     RequestID = db.Column(db.Integer, primary_key=True)
#     PropertyID = db.Column(db.Integer, db.ForeignKey('properties.id'))
#     Description = db.Column(db.String)
#     RequestDate = db.Column(db.Date)
#     RequestedBy = db.Column(db.String)
#     Status = db.Column(db.String)
#     AssignedStaff = db.Column(db.String)
#     CompletionDate = db.Column(db.Date)

#     property = db.relationship("Property", back_populates="maintenance_requests")


from .dbmodels import db
from sqlalchemy_serializer import SerializerMixin

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

