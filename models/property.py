# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMixin
# from models.dbmodels import db

# <<<<<<< HEAD
# db = SQLAlchemy()
# from dbmodels import db
# class Property(db.Model):
# =======
# class Property (db.Model, SerializerMixin):
#     __tablename__ = 'properties'
    
#     serialize_only = ('id', 'name', 'image')
    
# >>>>>>> origin
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     address = db.Column(db.String)
#     description =db.Column(db.String)
#     Bedrooms = db.Column(db.Integer)
#     image = db.Column(db.VARCHAR)
#     Size = db.Column(db.Float)
#     RentAmount = db.Column(db.Float)
#     Status = db.Column(db.String)

#     LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
#     landlord = db.relationship("Landlord", back_populates="properties")
#     leases = db.relationship("LeaseAgreement", back_populates="property")
#     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
    
#     def __repr__(self):
#         return f'<Property {self.id}, {self.name}, {self.image}>'

    


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from models.dbmodels import db

class Property (db.Model, SerializerMixin):
    __tablename__ = 'properties'
    
    serialize_only = ('id', 'name', 'image')
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    description =db.Column(db.String)
    Bedrooms = db.Column(db.Integer)
    image = db.Column(db.VARCHAR)
    Size = db.Column(db.Float)
    RentAmount = db.Column(db.Float)
    Status = db.Column(db.String)

    LandlordID = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
    landlord = db.relationship("Landlord", back_populates="properties")
    leases = db.relationship("LeaseAgreement", back_populates="property")
    maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
    
    
    def __repr__(self):
        return f'<Property {self.id}, {self.name}, {self.image}>'

    