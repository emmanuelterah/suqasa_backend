# # # from flask import Flask, jsonify, request
# # # from flask_sqlalchemy import SQLAlchemy
# # # from datetime import datetime

# # # app = Flask(__name__)
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# # # db = SQLAlchemy(app)

# # # # Import models
# # # from models.property import Property
# # # from models.landlord import Landlord
# # # from models.tenant import Tenant
# # # from models.lease_agreement import LeaseAgreement
# # # from models.maintenance import MaintenanceRequest
# # # from models.payment import Payment

# # # # Routes for CRUD operations

# # # # Create
# # # @app.route('/property', methods=['POST'])
# # # def create_property():
# # #     data = request.json
# # #     property = Property(**data)
# # #     db.session.add(property)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Property created successfully'}), 201

# # # # Read
# # # @app.route('/property/<int:id>', methods=['GET'])
# # # def get_property(id):
# # #     property = Property.query.get_or_404(id)
# # #     return jsonify(property.serialize()), 200

# # # # Update
# # # @app.route('/property/<int:id>', methods=['PUT'])
# # # def update_property(id):
# # #     data = request.json
# # #     property = Property.query.get_or_404(id)
# # #     for key, value in data.items():
# # #         setattr(property, key, value)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Property updated successfully'}), 200

# # # # Delete
# # # @app.route('/property/<int:id>', methods=['DELETE'])
# # # def delete_property(id):
# # #     property = Property.query.get_or_404(id)
# # #     db.session.delete(property)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Property deleted successfully'}), 200

# # # # Create Landlord
# # # @app.route('/landlord', methods=['POST'])
# # # def create_landlord():
# # #     data = request.json
# # #     landlord = Landlord(**data)
# # #     db.session.add(landlord)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Landlord created successfully'}), 201

# # # # Read Landlord
# # # @app.route('/landlord/<int:id>', methods=['GET'])
# # # def get_landlord(id):
# # #     landlord = Landlord.query.get_or_404(id)
# # #     return jsonify(landlord.serialize()), 200

# # # # Update Landlord
# # # @app.route('/landlord/<int:id>', methods=['PUT'])
# # # def update_landlord(id):
# # #     data = request.json
# # #     landlord = Landlord.query.get_or_404(id)
# # #     for key, value in data.items():
# # #         setattr(landlord, key, value)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Landlord updated successfully'}), 200

# # # # Delete Landlord
# # # @app.route('/landlord/<int:id>', methods=['DELETE'])
# # # def delete_landlord(id):
# # #     landlord = Landlord.query.get_or_404(id)
# # #     db.session.delete(landlord)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Landlord deleted successfully'}), 200

# # # # Similarly, you can create routes for Tenant, LeaseAgreement, Payment, and MaintenanceRequest entities
# # # # Create Tenant
# # # @app.route('/tenant', methods=['POST'])
# # # def create_tenant():
# # #     data = request.json
# # #     tenant = Tenant(**data)
# # #     db.session.add(tenant)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Tenant created successfully'}), 201

# # # # Read Tenant
# # # @app.route('/tenant/<int:id>', methods=['GET'])
# # # def get_tenant(id):
# # #     tenant = Tenant.query.get_or_404(id)
# # #     return jsonify(tenant.serialize()), 200

# # # # Update Tenant
# # # @app.route('/tenant/<int:id>', methods=['PUT'])
# # # def update_tenant(id):
# # #     data = request.json
# # #     tenant = Tenant.query.get_or_404(id)
# # #     for key, value in data.items():
# # #         setattr(tenant, key, value)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Tenant updated successfully'}), 200

# # # # Delete Tenant
# # # @app.route('/tenant/<int:id>', methods=['DELETE'])
# # # def delete_tenant(id):
# # #     tenant = Tenant.query.get_or_404(id)
# # #     db.session.delete(tenant)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Tenant deleted successfully'}), 200

# # # # Similar routes for LeaseAgreement
# # # # Create Lease Agreement
# # # @app.route('/lease', methods=['POST'])
# # # def create_lease_agreement():
# # #     data = request.json
# # #     lease_agreement = LeaseAgreement(**data)
# # #     db.session.add(lease_agreement)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Lease Agreement created successfully'}), 201

# # # # Read Lease Agreement
# # # @app.route('/lease/<int:id>', methods=['GET'])
# # # def get_lease_agreement(id):
# # #     lease_agreement = LeaseAgreement.query.get_or_404(id)
# # #     return jsonify(lease_agreement.serialize()), 200

# # # # Update Lease Agreement
# # # @app.route('/lease/<int:id>', methods=['PUT'])
# # # def update_lease_agreement(id):
# # #     data = request.json
# # #     lease_agreement = LeaseAgreement.query.get_or_404(id)
# # #     for key, value in data.items():
# # #         setattr(lease_agreement, key, value)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Lease Agreement updated successfully'}), 200

# # # # Delete Lease Agreement
# # # @app.route('/lease/<int:id>', methods=['DELETE'])
# # # def delete_lease_agreement(id):
# # #     lease_agreement = LeaseAgreement.query.get_or_404(id)
# # #     db.session.delete(lease_agreement)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Lease Agreement deleted successfully'}), 200

# # # # Similar routes for Payment and MaintenanceRequest entities
# # # # Create Payment
# # # @app.route('/payment', methods=['POST'])
# # # def create_payment():
# # #     data = request.json
# # #     payment = Payment(**data)
# # #     db.session.add(payment)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Payment created successfully'}), 201

# # # # Read Payment
# # # @app.route('/payment/<int:id>', methods=['GET'])
# # # def get_payment(id):
# # #     payment = Payment.query.get_or_404(id)
# # #     return jsonify(payment.serialize()), 200

# # # # Update Payment
# # # @app.route('/payment/<int:id>', methods=['PUT'])
# # # def update_payment(id):
# # #     data = request.json
# # #     payment = Payment.query.get_or_404(id)
# # #     for key, value in data.items():
# # #         setattr(payment, key, value)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Payment updated successfully'}), 200

# # # # Delete Payment
# # # @app.route('/payment/<int:id>', methods=['DELETE'])
# # # def delete_payment(id):
# # #     payment = Payment.query.get_or_404(id)
# # #     db.session.delete(payment)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Payment deleted successfully'}), 200

# # # # Create Maintenance Request
# # # @app.route('/maintenance', methods=['POST'])
# # # def create_maintenance_request():
# # #     data = request.json
# # #     maintenance_request = MaintenanceRequest(**data)
# # #     db.session.add(maintenance_request)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Maintenance Request created successfully'}), 201

# # # # Read Maintenance Request
# # # @app.route('/maintenance/<int:id>', methods=['GET'])
# # # def get_maintenance_request(id):
# # #     maintenance_request = MaintenanceRequest.query.get_or_404(id)
# # #     return jsonify(maintenance_request.serialize()), 200

# # # # Update Maintenance Request
# # # @app.route('/maintenance/<int:id>', methods=['PUT'])
# # # def update_maintenance_request(id):
# # #     data = request.json
# # #     maintenance_request = MaintenanceRequest.query.get_or_404(id)
# # #     for key, value in data.items():
# # #         setattr(maintenance_request, key, value)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Maintenance Request updated successfully'}), 200

# # # # Delete Maintenance Request
# # # @app.route('/maintenance/<int:id>', methods=['DELETE'])
# # # def delete_maintenance_request(id):
# # #     maintenance_request = MaintenanceRequest.query.get_or_404(id)
# # #     db.session.delete(maintenance_request)
# # #     db.session.commit()
# # #     return jsonify({'message': 'Maintenance Request deleted successfully'}), 200
# # # #
# # # if __name__ == '__main__':
# # #     app.run(debug=True)


# # # if __name__ == '__main__':
# # #     app.run(debug=True)


# # from flask import Flask, jsonify, request
# # # from models.dbmodels import db
# # # from models.property import Property
# # # from models.tenant import Tenant
# # # from models.lease_agreement import LeaseAgreement
# # # from models.maintenance import MaintenanceRequest
# # # from models.payment import Payment

# # # # # Create Flask app
# # # # app = Flask(__name__)
# # # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# # # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # # # Initialize SQLAlchemy
# # # # db.init_app(app)

# # from models.dbmodels import db
# # from models.landlord import Landlord
# # from models.property import Property
# # from models.tenant import Tenant
# # from models.lease_agreement import LeaseAgreement
# # from models.maintenance import MaintenanceRequest
# # from models.payment import Payment
# # from datetime import datetime
# # from app import app
# # # app = Flask(__name__)
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # # db.init_app(app)

# # # if __name__ == "__main__":
# # #     with app.app_context():
# # #         db.create_all()

# # #         # Seed data...


# # # Routes
# # @app.route('/')
# # def index():
# #     return 'Welcome to the Suqasa Backend!'

# # # Properties CRUD operations
# # @app.route('/properties', methods=['GET'])
# # def get_properties():
# #     properties = Property.query.all()
# #     return jsonify([property.serialize() for property in properties])

# # @app.route('/properties/<int:id>', methods=['GET'])
# # def get_property(id):
# #     property = Property.query.get_or_404(id)
# #     return jsonify(property.serialize())

# # @app.route('/properties', methods=['POST'])
# # def create_property():
# #     data = request.json
# #     property = Property(**data)
# #     db.session.add(property)
# #     db.session.commit()
# #     return jsonify(property.serialize()), 201

# # @app.route('/properties/<int:id>', methods=['PUT'])
# # def update_property(id):
# #     property = Property.query.get_or_404(id)
# #     data = request.json
# #     for key, value in data.items():
# #         setattr(property, key, value)
# #     db.session.commit()
# #     return jsonify(property.serialize())

# # @app.route('/properties/<int:id>', methods=['DELETE'])
# # def delete_property(id):
# #     property = Property.query.get_or_404(id)
# #     db.session.delete(property)
# #     db.session.commit()
# #     return '', 204

# # # Tenants CRUD operations
# # @app.route('/tenants', methods=['GET'])
# # def get_tenants():
# #     tenants = Tenant.query.all()
# #     return jsonify([tenant.serialize() for tenant in tenants])

# # @app.route('/tenants/<int:id>', methods=['GET'])
# # def get_tenant(id):
# #     tenant = Tenant.query.get_or_404(id)
# #     return jsonify(tenant.serialize())

# # @app.route('/tenants', methods=['POST'])
# # def create_tenant():
# #     data = request.json
# #     tenant = Tenant(**data)
# #     db.session.add(tenant)
# #     db.session.commit()
# #     return jsonify(tenant.serialize()), 201

# # @app.route('/tenants/<int:id>', methods=['PUT'])
# # def update_tenant(id):
# #     tenant = Tenant.query.get_or_404(id)
# #     data = request.json
# #     for key, value in data.items():
# #         setattr(tenant, key, value)
# #     db.session.commit()
# #     return jsonify(tenant.serialize())

# # @app.route('/tenants/<int:id>', methods=['DELETE'])
# # def delete_tenant(id):
# #     tenant = Tenant.query.get_or_404(id)
# #     db.session.delete(tenant)
# #     db.session.commit()
# #     return '', 204

# # # Lease agreements CRUD operations
# # @app.route('/lease_agreements', methods=['GET'])
# # def get_lease_agreements():
# #     lease_agreements = LeaseAgreement.query.all()
# #     return jsonify([lease_agreement.serialize() for lease_agreement in lease_agreements])

# # # Add routes for other CRUD operations for LeaseAgreement here

# # # Maintenance requests CRUD operations
# # @app.route('/maintenance_requests', methods=['GET'])
# # def get_maintenance_requests():
# #     maintenance_requests = MaintenanceRequest.query.all()
# #     return jsonify([request.serialize() for request in maintenance_requests])

# # # Add routes for other CRUD operations for MaintenanceRequest here

# # # Payments CRUD operations
# # @app.route('/payments', methods=['GET'])
# # def get_payments():
# #     payments = Payment.query.all()
# #     return jsonify([payment.serialize() for payment in payments])

# # # Add routes for other CRUD operations for Payment here

# # if __name__ == "__main__":
# #     app.run(debug=True)

# from flask import jsonify, request
# from models.dbmodels import db
# from models.property import Property
# from models.tenant import Tenant
# from models.lease_agreement import LeaseAgreement
# from models.maintenance import MaintenanceRequest
# from models.payment import Payment

# def initialize_routes(app):
#     @app.route('/')
#     def index():
#         return 'Welcome to the Suqasa Backend!'

#     # Properties CRUD operations
#     @app.route('/properties', methods=['GET'])
#     def get_properties():
#         properties = Property.query.all()
#         return jsonify([property.serialize() for property in properties])

#     @app.route('/properties/<int:id>', methods=['GET'])
#     def get_property(id):
#         property = Property.query.get_or_404(id)
#         return jsonify(property.serialize())

#     @app.route('/properties', methods=['POST'])
#     def create_property():
#         data = request.json
#         property = Property(**data)
#         db.session.add(property)
#         db.session.commit()
#         return jsonify(property.serialize()), 201

#     @app.route('/properties/<int:id>', methods=['PUT'])
#     def update_property(id):
#         property = Property.query.get_or_404(id)
#         data = request.json
#         for key, value in data.items():
#             setattr(property, key, value)
#         db.session.commit()
#         return jsonify(property.serialize())

#     @app.route('/properties/<int:id>', methods=['DELETE'])
#     def delete_property(id):
#         property = Property.query.get_or_404(id)
#         db.session.delete(property)
#         db.session.commit()
#         return '', 204

#     # Tenants CRUD operations
#     @app.route('/tenants', methods=['GET'])
#     def get_tenants():
#         tenants = Tenant.query.all()
#         return jsonify([tenant.serialize() for tenant in tenants])

#     @app.route('/tenants/<int:id>', methods=['GET'])
#     def get_tenant(id):
#         tenant = Tenant.query.get_or_404(id)
#         return jsonify(tenant.serialize())

#     @app.route('/tenants', methods=['POST'])
#     def create_tenant():
#         data = request.json
#         tenant = Tenant(**data)
#         db.session.add(tenant)
#         db.session.commit()
#         return jsonify(tenant.serialize()), 201

#     @app.route('/tenants/<int:id>', methods=['PUT'])
#     def update_tenant(id):
#         tenant = Tenant.query.get_or_404(id)
#         data = request.json
#         for key, value in data.items():
#             setattr(tenant, key, value)
#         db.session.commit()
#         return jsonify(tenant.serialize())

#     @app.route('/tenants/<int:id>', methods=['DELETE'])
#     def delete_tenant(id):
#         tenant = Tenant.query.get_or_404(id)
#         db.session.delete(tenant)
#         db.session.commit()
#         return '', 204

#     # Lease agreements CRUD operations
#     @app.route('/lease_agreements', methods=['GET'])
#     def get_lease_agreements():
#         lease_agreements = LeaseAgreement.query.all()
#         return jsonify([lease_agreement.serialize() for lease_agreement in lease_agreements])

#     # Add routes for other CRUD operations for LeaseAgreement here

#     # Maintenance requests CRUD operations
#     @app.route('/maintenance_requests', methods=['GET'])
#     def get_maintenance_requests():
#         maintenance_requests = MaintenanceRequest.query.all()
#         return jsonify([request.serialize() for request in maintenance_requests])

#     # Add routes for other CRUD operations for MaintenanceRequest here

#     # Payments CRUD operations
#     @app.route('/payments', methods=['GET'])
#     def get_payments():
#         payments = Payment.query.all()
#         return jsonify([payment.serialize() for payment in payments])

#     # Add routes for other CRUD operations for Payment here
