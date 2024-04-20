# # # # # # # # # # # from flask_sqlalchemy import SQLAlchemy
# # # # # # # # # # # from sqlalchemy_serializer import SerializerMixin
# # # # # # # # # # # from models.dbmodels import db

# # # # # # # # # # # <<<<<<< HEAD
# # # # # # # # # # # db = SQLAlchemy()
# # # # # # # # # # # from dbmodels import db
# # # # # # # # # # # class Property(db.Model):
# # # # # # # # # # # =======
# # # # # # # # # # # class Property (db.Model, SerializerMixin):
# # # # # # # # # # #     __tablename__ = 'properties'
    
# # # # # # # # # # #     serialize_only = ('id', 'name', 'image')
    
# # # # # # # # # # # >>>>>>> origin
# # # # # # # # # # #     id = db.Column(db.Integer, primary_key=True)
# # # # # # # # # # #     name = db.Column(db.String)
# # # # # # # # # # #     address = db.Column(db.String)
# # # # # # # # # # #     description =db.Column(db.String)
# # # # # # # # # # #     Bedrooms = db.Column(db.Integer)
# # # # # # # # # # #     image = db.Column(db.VARCHAR)
# # # # # # # # # # #     Size = db.Column(db.Float)
# # # # # # # # # # #     RentAmount = db.Column(db.Float)
# # # # # # # # # # #     Status = db.Column(db.String)

# # # # # # # # # # #     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
# # # # # # # # # # #     landlord = db.relationship("Landlord", back_populates="properties")
# # # # # # # # # # #     leases = db.relationship("LeaseAgreement", back_populates="property")
# # # # # # # # # # #     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
    
# # # # # # # # # # #     def __repr__(self):
# # # # # # # # # # #         return f'<Property {self.id}, {self.name}, {self.image}>'

    


# # # # # # # # # # from flask_sqlalchemy import SQLAlchemy
# # # # # # # # # # from sqlalchemy_serializer import SerializerMixin
# # # # # # # # # # from .dbmodels import db

# # # # # # # # # # class Property (db.Model, SerializerMixin):
# # # # # # # # # #     __tablename__ = 'properties'
    
# # # # # # # # # #     serialize_only = ('id', 'name', 'image')
    
# # # # # # # # # #     id = db.Column(db.Integer, primary_key=True)
# # # # # # # # # #     name = db.Column(db.String)
# # # # # # # # # #     address = db.Column(db.String)
# # # # # # # # # #     description =db.Column(db.String)
# # # # # # # # # #     Bedrooms = db.Column(db.Integer)
# # # # # # # # # #     image = db.Column(db.VARCHAR)
# # # # # # # # # #     Size = db.Column(db.Float)
# # # # # # # # # #     RentAmount = db.Column(db.Float)
# # # # # # # # # #     Status = db.Column(db.String)

# # # # # # # # # #     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
# # # # # # # # # #     landlord = db.relationship("Landlord", back_populates="properties")
# # # # # # # # # #     leases = db.relationship("LeaseAgreement", back_populates="property")
# # # # # # # # # #     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
    
# # # # # # # # # #     def __repr__(self):
# # # # # # # # # #         return f'<Property {self.id}, {self.name}, {self.image}>'

    

# # # # # # # # # from .dbmodels import db
# # # # # # # # # from sqlalchemy_serializer import SerializerMixin

# # # # # # # # # class Property(db.Model, SerializerMixin):
# # # # # # # # #     __tablename__ = 'properties'
    
# # # # # # # # #     serialize_only = ('id', 'name', 'image')
    
# # # # # # # # #     id = db.Column(db.Integer, primary_key=True)
# # # # # # # # #     name = db.Column(db.String)
# # # # # # # # #     address = db.Column(db.String)
# # # # # # # # #     description = db.Column(db.String)
# # # # # # # # #     Bedrooms = db.Column(db.Integer)
# # # # # # # # #     image = db.Column(db.String)  # Changed from db.VARCHAR to db.String
# # # # # # # # #     Size = db.Column(db.Float)
# # # # # # # # #     RentAmount = db.Column(db.Float)
# # # # # # # # #     Status = db.Column(db.String)

# # # # # # # # #     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
# # # # # # # # #     landlord = db.relationship("Landlord", back_populates="properties")
# # # # # # # # #     leases = db.relationship("LeaseAgreement", back_populates="property")
# # # # # # # # #     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
# # # # # # # # #     def __repr__(self):
# # # # # # # # #         return f'<Property {self.id}, {self.name}, {self.image}>'

# # # # # # # # from flask_sqlalchemy import SQLAlchemy
# # # # # # # # from sqlalchemy_serializer import SerializerMixin

# # # # # # # # db = SQLAlchemy()

# # # # # # # # class Property(db.Model, SerializerMixin):
# # # # # # # #     __tablename__ = 'properties'
    
# # # # # # # #     serialize_only = ('id', 'name', 'image')
    
# # # # # # # #     id = db.Column(db.Integer, primary_key=True)
# # # # # # # #     name = db.Column(db.String)
# # # # # # # #     address = db.Column(db.String)
# # # # # # # #     description = db.Column(db.String)
# # # # # # # #     Bedrooms = db.Column(db.Integer)
# # # # # # # #     image = db.Column(db.String)  # Changed from db.VARCHAR to db.String
# # # # # # # #     Size = db.Column(db.Float)
# # # # # # # #     RentAmount = db.Column(db.Float)
# # # # # # # #     Status = db.Column(db.String)

# # # # # # # #     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
# # # # # # # #     landlord = db.relationship("Landlord", back_populates="properties")
# # # # # # # #     leases = db.relationship("LeaseAgreement", back_populates="property")
# # # # # # # #     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
# # # # # # # #     def __repr__(self):
# # # # # # # #         return f'<Property {self.id}, {self.name}, {self.image}>'

# # # # # # from models.dbmodels import db
# # # # # # from sqlalchemy_serializer import SerializerMixin

# # # # # # class Property(db.Model, SerializerMixin):
# # # # # #     __tablename__ = 'properties'
    
# # # # # #     serialize_only = ('id', 'name', 'image')
    
# # # # # #     id = db.Column(db.Integer, primary_key=True)
# # # # # #     name = db.Column(db.String)
# # # # # #     address = db.Column(db.String)
# # # # # #     description = db.Column(db.String)
# # # # # #     Bedrooms = db.Column(db.Integer)
# # # # # #     image = db.Column(db.String)  # Changed from db.VARCHAR to db.String
# # # # # #     Size = db.Column(db.Float)
# # # # # #     RentAmount = db.Column(db.Float)
# # # # # #     Status = db.Column(db.String)

# # # # # #     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
# # # # # #     landlord = db.relationship("Landlord", back_populates="properties")
# # # # # #     leases = db.relationship("LeaseAgreement", back_populates="property")
# # # # # #     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
# # # # # #     def __repr__(self):
# # # # # #         return f'<Property {self.id}, {self.name}, {self.image}>'

# # # # # # property.py

# # # # # from models.dbmodels import db
# # # # # from sqlalchemy_serializer import SerializerMixin

# # # # # class Property(db.Model, SerializerMixin):
# # # # #     __tablename__ = 'properties'
    
# # # # #     serialize_only = ('id', 'name', 'image')
    
# # # # #     id = db.Column(db.Integer, primary_key=True)
# # # # #     name = db.Column(db.String)
# # # # #     address = db.Column(db.String)
# # # # #     description = db.Column(db.String)
# # # # #     Bedrooms = db.Column(db.Integer)
# # # # #     image = db.Column(db.String)  # Changed from db.VARCHAR to db.String
# # # # #     Size = db.Column(db.Float)
# # # # #     RentAmount = db.Column(db.Float)
# # # # #     Status = db.Column(db.String)

# # # # #     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
# # # # #     landlord = db.relationship("Landlord", back_populates="properties")
# # # # #     lease_agreements = db.relationship("LeaseAgreement", back_populates="property")
# # # # #     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
# # # # #     def __repr__(self):
# # # # #         return f'<Property {self.id}, {self.name}, {self.image}>'

# # # # from models.dbmodels import db
# # # # from sqlalchemy_serializer import SerializerMixin

# # # # class Property(db.Model, SerializerMixin):
# # # #     __tablename__ = 'properties'
    
# # # #     serialize_only = ('id', 'name', 'image')
    
# # # #     id = db.Column(db.Integer, primary_key=True)
# # # #     name = db.Column(db.String)
# # # #     address = db.Column(db.String)
# # # #     description = db.Column(db.String)
# # # #     Bedrooms = db.Column(db.Integer)
# # # #     image = db.Column(db.String)  # Changed from db.VARCHAR to db.String
# # # #     SquareFootage = db.Column(db.Float)  # New attribute
# # # #     RentAmount = db.Column(db.Float)
# # # #     Status = db.Column(db.String)

# # # #     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
# # # #     landlord = db.relationship("Landlord", back_populates="properties")
# # # #     lease_agreements = db.relationship("LeaseAgreement", back_populates="property")
# # # #     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
# # # #     def __repr__(self):
# # # #         return f'<Property {self.id}, {self.name}, {self.image}>'

# # # from models.dbmodels import db
# # # from sqlalchemy_serializer import SerializerMixin
# # # from models.lease_agreement import LeaseAgreement
# # # class Property(db.Model, SerializerMixin):
# # #     __tablename__ = 'properties'
    
# # #     serialize_only = ('id', 'name', 'image')
    
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     name = db.Column(db.String)
# # #     address = db.Column(db.String)
# # #     description = db.Column(db.String)
# # #     Bedrooms = db.Column(db.Integer)
# # #     image = db.Column(db.String)  # Changed from db.VARCHAR to db.String
# # #     SquareFootage = db.Column(db.Float)  # Optional addition
# # #     RentAmount = db.Column(db.Float)
# # #     Status = db.Column(db.String)

# # #     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
# # #     landlord = db.relationship("Landlord", back_populates="properties")

# # #     # Fix warning: Add overlaps parameter
# # #     leases = db.relationship(LeaseAgreement, backref='property', overlaps="lease_agreements") 

# # #     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
# # #     def __repr__(self):
# # #         return f'<Property {self.id}, {self.name}, {self.image}>'


# # from flask_sqlalchemy import SQLAlchemy
# # from sqlalchemy_serializer import SerializerMixin

# # db = SQLAlchemy()

# # class Property(db.Model, SerializerMixin):
# #     __tablename__ = 'properties'
    
# #     serialize_only = ('id', 'name', 'image')
    
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String)
# #     address = db.Column(db.String)
# #     description = db.Column(db.String)
# #     Bedrooms = db.Column(db.Integer)
# #     image = db.Column(db.String)  # Changed from db.VARCHAR to db.String
# #     Size = db.Column(db.Float)
# #     RentAmount = db.Column(db.Float)
# #     Status = db.Column(db.String)

# #     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
# #     landlord = db.relationship("Landlord", back_populates="properties")
# #     leases = db.relationship("LeaseAgreement", back_populates="property")
# #     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
# #     def __repr__(self):
# #         return f'<Property {self.id}, {self.name}, {self.image}>'

# from .dbmodels import db
# from sqlalchemy_serializer import SerializerMixin

# class Property(db.Model, SerializerMixin):
#     __tablename__ = 'properties'
    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     address = db.Column(db.String)
#     description = db.Column(db.String)
#     Bedrooms = db.Column(db.Integer)
#     image = db.Column(db.String)
#     Size = db.Column(db.Float)
#     RentAmount = db.Column(db.Float)
#     Status = db.Column(db.String)

#     # Define the relationship with Landlord using actual column names
#     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
#     landlord = db.relationship("Landlord", backref="properties", foreign_keys="[Property.LandlordID]", primaryjoin="Landlord.LandlordID == Property.LandlordID")

#     leases = db.relationship("LeaseAgreement", back_populates="property")
#     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
#     def __repr__(self):
#         return f'<Property {self.name}>'

from .dbmodels import db
from sqlalchemy_serializer import SerializerMixin

class Property(db.Model, SerializerMixin):
    __tablename__ = 'properties'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    description = db.Column(db.String)
    Bedrooms = db.Column(db.Integer)
    image = db.Column(db.String)
    Size = db.Column(db.Float)
    RentAmount = db.Column(db.Float)
    Status = db.Column(db.String)

    LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
    landlord = db.relationship("Landlord", back_populates="properties")

    leases = db.relationship("LeaseAgreement", back_populates="property")
    maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")

