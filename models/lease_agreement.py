# # # # # # # # # from flask_sqlalchemy import SQLAlchemy
# # # # # # # # # from sqlalchemy_serializer import SerializerMixin
# # # # # # # # # from models.dbmodels import db

# # # # # # # # # <<<<<<< HEAD
# # # # # # # # # db = SQLAlchemy()
# # # # # # # # # from dbmodels import db
# # # # # # # # # =======
# # # # # # # # # class LeaseAgreement(db.Model, SerializerMixin):
# # # # # # # # #     __tablename__ = 'lease_agreements'
# # # # # # # # # >>>>>>> origin

# # # # # # # # #     LeaseID = db.Column(db.Integer, primary_key=True)
# # # # # # # # #     PropertyID = db.Column(db.Integer, db.ForeignKey('properties.id'))
# # # # # # # # #     TenantID = db.Column(db.Integer, db.ForeignKey('tenants.TenantID'))
# # # # # # # # #     StartDate = db.Column(db.Date)
# # # # # # # # #     EndDate = db.Column(db.Date)
# # # # # # # # #     RentAmount = db.Column(db.Float)
# # # # # # # # #     PaymentSchedule = db.Column(db.String)
# # # # # # # # #     DepositAmount = db.Column(db.Float)

# # # # # # # # #     property = db.relationship("Property", back_populates="leases")
# # # # # # # # #     tenant = db.relationship("Tenant", back_populates="leases")
# # # # # # # # #     payments = db.relationship("Payment", back_populates="lease")

# # # # # # # # from flask_sqlalchemy import SQLAlchemy
# # # # # # # # from sqlalchemy_serializer import SerializerMixin
# # # # # # # # from .dbmodels import db

# # # # # # # # class LeaseAgreement(db.Model, SerializerMixin):
# # # # # # # #     __tablename__ = 'lease_agreements'

# # # # # # # #     LeaseID = db.Column(db.Integer, primary_key=True)
# # # # # # # #     PropertyID = db.Column(db.Integer, db.ForeignKey('properties.id'))
# # # # # # # #     TenantID = db.Column(db.Integer, db.ForeignKey('tenants.TenantID'))
# # # # # # # #     StartDate = db.Column(db.Date)
# # # # # # # #     EndDate = db.Column(db.Date)
# # # # # # # #     RentAmount = db.Column(db.Float)
# # # # # # # #     PaymentSchedule = db.Column(db.String)
# # # # # # # #     DepositAmount = db.Column(db.Float)

# # # # # # # #     property = db.relationship("Property", back_populates="leases")
# # # # # # # #     tenant = db.relationship("Tenant", back_populates="leases")
# # # # # # # #     payments = db.relationship("Payment", back_populates="lease")

# # from flask_sqlalchemy import SQLAlchemy
# # from sqlalchemy_serializer import SerializerMixin

# # db = SQLAlchemy()

# # class LeaseAgreement(db.Model, SerializerMixin):
# #     __tablename__ = 'lease_agreements'

# #     LeaseID = db.Column(db.Integer, primary_key=True)
# #     PropertyID = db.Column(db.Integer, db.ForeignKey('properties.id'))
# #     TenantID = db.Column(db.Integer, db.ForeignKey('tenants.TenantID'))
# #     StartDate = db.Column(db.Date)
# #     EndDate = db.Column(db.Date)
# #     RentAmount = db.Column(db.Float)
# #     PaymentSchedule = db.Column(db.String)
# #     DepositAmount = db.Column(db.Float)

# #     property = db.relationship("Property", back_populates="leases")
# #     tenant = db.relationship("Tenant", back_populates="leases")
# #     payments = db.relationship("Payment", back_populates="lease")


# from .dbmodels import db
# from sqlalchemy_serializer import SerializerMixin

# class LeaseAgreement(db.Model, SerializerMixin):
#     __tablename__ = 'lease_agreements'

#     LeaseID = db.Column(db.Integer, primary_key=True)
#     PropertyID = db.Column(db.Integer, db.ForeignKey('properties.id'))
#     TenantID = db.Column(db.Integer, db.ForeignKey('tenants.TenantID'))
#     StartDate = db.Column(db.Date)
#     EndDate = db.Column(db.Date)
#     RentAmount = db.Column(db.Float)
#     PaymentSchedule = db.Column(db.String)
#     DepositAmount = db.Column(db.Float)

#     property = db.relationship("Property", back_populates="leases")
#     tenant = db.relationship("Tenant", back_populates="leases")
#     payments = db.relationship("Payment", back_populates="lease")


# # # # # # lease_agreement.py

# # # # # from sqlalchemy import ForeignKey
# # # # # from sqlalchemy.orm import relationship
# # # # # from .dbmodels import db

# # # # # class LeaseAgreement(db.Model):
# # # # #     __tablename__ = 'lease_agreements'

# # # # #     LeaseID = db.Column(db.Integer, primary_key=True)
# # # # #     PropertyID = db.Column(db.Integer, ForeignKey('properties.id'))
# # # # #     TenantID = db.Column(db.Integer, ForeignKey('tenants.TenantID'))
# # # # #     StartDate = db.Column(db.Date)
# # # # #     EndDate = db.Column(db.Date)
# # # # #     RentAmount = db.Column(db.Float)
# # # # #     PaymentSchedule = db.Column(db.String)
# # # # #     DepositAmount = db.Column(db.Float)

# # # # #     # Define relationship with Property
# # # # #     property = relationship("Property", backref="leases")

# # # # #     # Define relationship with Tenant
# # # # #     tenant = relationship("Tenant", backref="leases")

# # # # # lease_agreement.py

# # # # from sqlalchemy import ForeignKey
# # # # from sqlalchemy.orm import relationship
# # # # from .dbmodels import db

# # # # class LeaseAgreement(db.Model):
# # # #     __tablename__ = 'lease_agreements'

# # # #     LeaseID = db.Column(db.Integer, primary_key=True)
# # # #     PropertyID = db.Column(db.Integer, ForeignKey('properties.id'))
# # # #     TenantID = db.Column(db.Integer, ForeignKey('tenants.TenantID'))
# # # #     StartDate = db.Column(db.Date)
# # # #     EndDate = db.Column(db.Date)
# # # #     RentAmount = db.Column(db.Float)
# # # #     PaymentSchedule = db.Column(db.String)
# # # #     DepositAmount = db.Column(db.Float)

# # # #     # Define relationship with Property
# # # #     property_lease = relationship("Property", backref="lease_agreements")

# # # #     # Define relationship with Tenant
# # # #     tenant = relationship("Tenant", backref="lease_agreements")

# # # # lease_agreement.py

# # # from sqlalchemy import ForeignKey
# # # from sqlalchemy.orm import relationship
# # # from .dbmodels import db

# # # class LeaseAgreement(db.Model):
# # #     __tablename__ = 'lease_agreements'

# # #     LeaseID = db.Column(db.Integer, primary_key=True)
# # #     PropertyID = db.Column(db.Integer, ForeignKey('properties.id'))
# # #     TenantID = db.Column(db.Integer, ForeignKey('tenants.TenantID'))
# # #     StartDate = db.Column(db.Date)
# # #     EndDate = db.Column(db.Date)
# # #     RentAmount = db.Column(db.Float)
# # #     PaymentSchedule = db.Column(db.String)
# # #     DepositAmount = db.Column(db.Float)

# # #     # Define relationship with Property
# # #     property = relationship("Property", backref="leases")

# # #     # Define relationship with Tenant
# # #     tenant = relationship("Tenant", backref="leases")

# # from sqlalchemy import ForeignKey
# # from sqlalchemy.orm import relationship
# # from .dbmodels import db

# # class LeaseAgreement(db.Model):
# #     __tablename__ = 'lease_agreements'

# #     LeaseID = db.Column(db.Integer, primary_key=True)  # New attribute
# #     PropertyID = db.Column(db.Integer, ForeignKey('properties.id'))
# #     TenantID = db.Column(db.Integer, ForeignKey('tenants.TenantID'))
# #     StartDate = db.Column(db.Date)
# #     EndDate = db.Column(db.Date)
# #     RentAmount = db.Column(db.Float)
# #     PaymentSchedule = db.Column(db.String)
# #     DepositAmount = db.Column(db.Float)

# #     # Define relationship with Property
# #     property = relationship("Property", backref="leases")

# #     # Define relationship with Tenant
# #     tenant = relationship("Tenant", backref="leases")

# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
# from .dbmodels import db
# from models.tenant import Tenant

# class LeaseAgreement(db.Model):
#     __tablename__ = 'lease_agreements'

#     LeaseID = db.Column(db.Integer, primary_key=True)  # Optional addition
#     PropertyID = db.Column(db.Integer, ForeignKey('properties.id'))
#     TenantID = db.Column(db.Integer, ForeignKey('tenants.TenantID'))
#     StartDate = db.Column(db.Date)
#     EndDate = db.Column(db.Date)
#     RentAmount = db.Column(db.Float)
#     PaymentSchedule = db.Column(db.String)
#     DepositAmount = db.Column(db.Float)

#     # Define relationship with Property
#     property = relationship("Property", backref="property@lease")

#     # Fix error: Rename backref
#     tenant = relationship(Tenant, backref='tenant_lease')  # Or 'lease'


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

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
