# # # # from flask_sqlalchemy import SQLAlchemy
# # # # from sqlalchemy_serializer import SerializerMixin
# # # # from models.dbmodels import db

# # # # <<<<<<< HEAD
# # # # db = SQLAlchemy()
# # # # from dbmodels import db
# # # # =======
# # # # class Payment(db.Model, SerializerMixin):
# # # #     __tablename__ = 'payments'
# # # # >>>>>>> origin

# # # #     PaymentID = db.Column(db.Integer, primary_key=True)
# # # #     LeaseID = db.Column(db.Integer, db.ForeignKey('lease_agreements.LeaseID'))
# # # #     TenantID = db.Column(db.Integer, db.ForeignKey('tenants.TenantID'))
# # # #     PaymentDate = db.Column(db.Date)
# # # #     PaymentAmount = db.Column(db.Float)
# # # #     PaymentMethod = db.Column(db.String)
# # # #     PaymentStatus = db.Column(db.String)

# # # #     tenant = db.relationship("Tenant", back_populates="payments")
# # # #     lease = db.relationship("LeaseAgreement", back_populates="payments")

# # # from flask_sqlalchemy import SQLAlchemy
# # # from sqlalchemy_serializer import SerializerMixin
# # # from .dbmodels import db

# # # class Payment(db.Model, SerializerMixin):
# # #     __tablename__ = 'payments'

# # #     PaymentID = db.Column(db.Integer, primary_key=True)
# # #     LeaseID = db.Column(db.Integer, db.ForeignKey('lease_agreements.LeaseID'))
# # #     TenantID = db.Column(db.Integer, db.ForeignKey('tenants.TenantID'))
# # #     PaymentDate = db.Column(db.Date)
# # #     PaymentAmount = db.Column(db.Float)
# # #     PaymentMethod = db.Column(db.String)
# # #     PaymentStatus = db.Column(db.String)

# # #     tenant = db.relationship("Tenant", back_populates="payments")
# # #     lease = db.relationship("LeaseAgreement", back_populates="payments")

# # from flask_sqlalchemy import SQLAlchemy
# # from sqlalchemy_serializer import SerializerMixin

# # db = SQLAlchemy()

# # class Payment(db.Model, SerializerMixin):
# #     __tablename__ = 'payments'

# #     PaymentID = db.Column(db.Integer, primary_key=True)
# #     LeaseID = db.Column(db.Integer, db.ForeignKey('lease_agreements.LeaseID'))
# #     TenantID = db.Column(db.Integer, db.ForeignKey('tenants.TenantID'))
# #     PaymentDate = db.Column(db.Date)
# #     PaymentAmount = db.Column(db.Float)
# #     PaymentMethod = db.Column(db.String)
# #     PaymentStatus = db.Column(db.String)

# # from .dbmodels import db
# # from sqlalchemy_serializer import SerializerMixin

# # class Payment(db.Model, SerializerMixin):
# #     __tablename__ = 'payments'

# #     PaymentID = db.Column(db.Integer, primary_key=True)
# #     LeaseID = db.Column(db.Integer, db.ForeignKey('lease_agreements.LeaseID'))
# #     TenantID = db.Column(db.Integer, db.ForeignKey('tenants.TenantID'))
# #     PaymentDate = db.Column(db.Date)
# #     PaymentAmount = db.Column(db.Float)
# #     PaymentMethod = db.Column(db.String)
# #     PaymentStatus = db.Column(db.String)

# payment.py

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

    # Define relationship with LeaseAgreement
    lease = relationship("LeaseAgreement", backref="payments")

    # Define relationship with Tenant (assuming it exists in your model)
    tenant = relationship("Tenant", backref="payments")



