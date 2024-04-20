# # # # # from flask_sqlalchemy import SQLAlchemy
# # # # # from sqlalchemy_serializer import SerializerMixin
# # # # # from .dbmodels import db

# # # # # class Landlord(db.Model, SerializerMixin):
# # # # #     __tablename__ = 'landlords'

# # # # #     LandlordID = db.Column(db.Integer, primary_key=True)
# # # # #     Name = db.Column(db.String)
# # # # #     ContactInfo = db.Column(db.String)
# # # # #     BankAcctInfo = db.Column(db.String)
# # # # #     Address = db.Column(db.String)

# # # # #     properties = db.relationship("Property", back_populates="landlord")

# # # from flask_sqlalchemy import SQLAlchemy
# # # from sqlalchemy_serializer import SerializerMixin
# # # from .dbmodels import db
# # # from models.property import Property


# # # db = SQLAlchemy()

# # # class Landlord(db.Model, SerializerMixin):
# # #     __tablename__ = 'landlords'

# # #     LandlordID = db.Column(db.Integer, primary_key=True)
# # #     Name = db.Column(db.String)
# # #     ContactInfo = db.Column(db.String)
# # #     BankAcctInfo = db.Column(db.String)
# # #     Address = db.Column(db.String)

# # #     # Define the relationship with Property using actual column names
# # #     properties = db.relationship("Property", backref="landlord", foreign_keys="[Property.LandlordID]", primaryjoin="Landlord.LandlordID == Property.LandlordID")

# # #     def __repr__(self):
# # #         return f'<Landlord {self.Name}>'


# # # from .dbmodels import db

# # # class Landlord(db.Model):
# # #     __tablename__ = 'landlords'

# # #     LandlordID = db.Column(db.Integer, primary_key=True)
# # #     Name = db.Column(db.String)
# # #     ContactInfo = db.Column(db.String)
# # #     BankAcctInfo = db.Column(db.String)
# # #     Address = db.Column(db.String)

# # #     # Define the relationship with Property using a string-based relationship definition
# # #     properties = db.relationship("Property", backref="landlord", foreign_keys="[Property.LandlordID]")

# # #     def __repr__(self):
# # #         return f'<Landlord {self.Name}>'


# # from .dbmodels import db

# # class Landlord(db.Model):
# #     __tablename__ = 'landlords'

# #     LandlordID = db.Column(db.Integer, primary_key=True)
# #     Name = db.Column(db.String)
# #     ContactInfo = db.Column(db.String)
# #     BankAcctInfo = db.Column(db.String)
# #     Address = db.Column(db.String)

# #     # Define the relationship with Property using a string-based relationship definition
# #     properties = db.relationship("Property", backref="landlords", foreign_keys="[Property.LandlordID]")

# #     def __repr__(self):
# #         return f'<Landlord {self.Name}>'


# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMixin
# from models.dbmodels import db

# class Landlord(db.Model, SerializerMixin):
#     __tablename__ = 'landlords'

#     LandlordID = db.Column(db.Integer, primary_key=True)
#     Name = db.Column(db.String)
#     ContactInfo = db.Column(db.String)
#     BankAcctInfo = db.Column(db.String)
#     Address = db.Column(db.String)

#     properties = db.relationship("Property", back_populates="landlord")


from .dbmodels import db
from sqlalchemy_serializer import SerializerMixin

class Landlord(db.Model, SerializerMixin):
    __tablename__ = 'landlords'

    LandlordID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String)
    ContactInfo = db.Column(db.String)
    BankAcctInfo = db.Column(db.String)
    Address = db.Column(db.String)

    properties = db.relationship("Property", back_populates="landlord")
