from flask import Flask
from models.dbmodels import db
from models.property import Property
from models.landlord import Landlord
from models.lease_agreement import LeaseAgreement
from models.maintenance import MaintenanceRequest
from models.payment import Payment
from models.tenant import Tenant
from flask_migrate import Migrate

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# # # Create the database tables
# with app.app_context():
#     db.create_all()

if __name__ == "__main__":
    from routes import *
    app.run(debug=True)


# # # from flask import Flask
# # # from models.dbmodels import db
# # # from routes import *

# # # app = Flask(__name__)
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # db.init_app(app)

# # # if __name__ == "__main__":
# # #     app.run(debug=True)


# # from flask import Flask
# # from models.dbmodels import db
# # from flask_migrate import Migrate
# # from routes import *

# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # # Initialize the database
# # db.init_app(app)

# # # Initialize Flask-Migrate
# # migrate = Migrate(app, db)
# # if __name__ == "__main__":
# #     app.run(debug=True)


# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db = SQLAlchemy(app)

# class Landlord(db.Model):
#     __tablename__ = 'landlords'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     properties = db.relationship('Property', backref='landlord', lazy=True)

#     def __repr__(self):
#         return f'Landlord(id={self.id}, name={self.name})'

# class Property(db.Model):
#     __tablename__ = 'properties'

#     id = db.Column(db.Integer, primary_key=True)
#     address = db.Column(db.String(255), nullable=False)
#     landlord_id = db.Column(db.Integer, db.ForeignKey('landlords.id'), nullable=False)

#     def __repr__(self):
#         return f'Property(id={self.id}, address={self.address}, landlord_id={self.landlord_id})'

# @app.route('/landlords', methods=['GET'])
# def get_landlords():
#     landlords = Landlord.query.all()
#     return jsonify([landlord.__dict__ for landlord in landlords])

# @app.route('/properties', methods=['GET'])
# def get_properties():
#     properties = Property.query.all()
#     return jsonify([property.__dict__ for property in properties])

# @app.route('/landlords', methods=['POST'])
# def create_landlord():
#     data = request.json
#     new_landlord = Landlord(name=data['name'])
#     db.session.add(new_landlord)
#     db.session.commit()
#     return jsonify(new_landlord.__dict__), 201

# @app.route('/properties', methods=['POST'])
# def create_property():
#     data = request.json
#     new_property = Property(address=data['address'], landlord_id=data['landlord_id'])
#     db.session.add(new_property)
#     db.session.commit()
#     return jsonify(new_property.__dict__), 201

# if __name__ == '__main__':
#     db.create_all()
#     app.run(debug=True)
