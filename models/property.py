from .dbmodels import db
from sqlalchemy_serializer import SerializerMixin

class Property(db.Model, SerializerMixin):
    __tablename__ = 'properties'
    serialize_only = ('id', 'name', 'address', 'description','Bedrooms','image','Size','RentAmount','Status', 'LandlordID')
    
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

# from .dbmodels import db
# from sqlalchemy_serializer import SerializerMixin
# class Property(db.Model, SerializerMixin):
#     __tablename__ = 'properties'
    
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     address = db.Column(db.String)
#     description = db.Column(db.String)
#     bedrooms = db.Column(db.Integer)
#     image = db.Column(db.String)
#     size = db.Column(db.Float)
#     rent_amount = db.Column(db.Float)
#     status = db.Column(db.String)

#     landlord_id = db.Column(db.Integer, db.ForeignKey('landlords.LandlordID'))
#     landlord = db.relationship("Landlord", back_populates="properties")

#     leases = db.relationship("LeaseAgreement", back_populates="property")
#     maintenance_requests = db.relationship("MaintenanceRequest", back_populates="property")
