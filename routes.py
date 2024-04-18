from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

# Import models
from models.property import Property
from models.landlord import Landlord
from models.tenant import Tenant
from models.lease_agreement import LeaseAgreement
from models.maintenance import MaintenanceRequest
from models.payment import Payment

# Routes for CRUD operations

# Create
@app.route('/property', methods=['POST'])
def create_property():
    data = request.json
    property = Property(**data)
    db.session.add(property)
    db.session.commit()
    return jsonify({'message': 'Property created successfully'}), 201

# Read
@app.route('/property/<int:id>', methods=['GET'])
def get_property(id):
    property = Property.query.get_or_404(id)
    return jsonify(property.serialize()), 200

# Update
@app.route('/property/<int:id>', methods=['PUT'])
def update_property(id):
    data = request.json
    property = Property.query.get_or_404(id)
    for key, value in data.items():
        setattr(property, key, value)
    db.session.commit()
    return jsonify({'message': 'Property updated successfully'}), 200

# Delete
@app.route('/property/<int:id>', methods=['DELETE'])
def delete_property(id):
    property = Property.query.get_or_404(id)
    db.session.delete(property)
    db.session.commit()
    return jsonify({'message': 'Property deleted successfully'}), 200

# Create Landlord
@app.route('/landlord', methods=['POST'])
def create_landlord():
    data = request.json
    landlord = Landlord(**data)
    db.session.add(landlord)
    db.session.commit()
    return jsonify({'message': 'Landlord created successfully'}), 201

# Read Landlord
@app.route('/landlord/<int:id>', methods=['GET'])
def get_landlord(id):
    landlord = Landlord.query.get_or_404(id)
    return jsonify(landlord.serialize()), 200

# Update Landlord
@app.route('/landlord/<int:id>', methods=['PUT'])
def update_landlord(id):
    data = request.json
    landlord = Landlord.query.get_or_404(id)
    for key, value in data.items():
        setattr(landlord, key, value)
    db.session.commit()
    return jsonify({'message': 'Landlord updated successfully'}), 200

# Delete Landlord
@app.route('/landlord/<int:id>', methods=['DELETE'])
def delete_landlord(id):
    landlord = Landlord.query.get_or_404(id)
    db.session.delete(landlord)
    db.session.commit()
    return jsonify({'message': 'Landlord deleted successfully'}), 200

# Similarly, you can create routes for Tenant, LeaseAgreement, Payment, and MaintenanceRequest entities
# Create Tenant
@app.route('/tenant', methods=['POST'])
def create_tenant():
    data = request.json
    tenant = Tenant(**data)
    db.session.add(tenant)
    db.session.commit()
    return jsonify({'message': 'Tenant created successfully'}), 201

# Read Tenant
@app.route('/tenant/<int:id>', methods=['GET'])
def get_tenant(id):
    tenant = Tenant.query.get_or_404(id)
    return jsonify(tenant.serialize()), 200

# Update Tenant
@app.route('/tenant/<int:id>', methods=['PUT'])
def update_tenant(id):
    data = request.json
    tenant = Tenant.query.get_or_404(id)
    for key, value in data.items():
        setattr(tenant, key, value)
    db.session.commit()
    return jsonify({'message': 'Tenant updated successfully'}), 200

# Delete Tenant
@app.route('/tenant/<int:id>', methods=['DELETE'])
def delete_tenant(id):
    tenant = Tenant.query.get_or_404(id)
    db.session.delete(tenant)
    db.session.commit()
    return jsonify({'message': 'Tenant deleted successfully'}), 200

# Similar routes for LeaseAgreement
# Create Lease Agreement
@app.route('/lease', methods=['POST'])
def create_lease_agreement():
    data = request.json
    lease_agreement = LeaseAgreement(**data)
    db.session.add(lease_agreement)
    db.session.commit()
    return jsonify({'message': 'Lease Agreement created successfully'}), 201

# Read Lease Agreement
@app.route('/lease/<int:id>', methods=['GET'])
def get_lease_agreement(id):
    lease_agreement = LeaseAgreement.query.get_or_404(id)
    return jsonify(lease_agreement.serialize()), 200

# Update Lease Agreement
@app.route('/lease/<int:id>', methods=['PUT'])
def update_lease_agreement(id):
    data = request.json
    lease_agreement = LeaseAgreement.query.get_or_404(id)
    for key, value in data.items():
        setattr(lease_agreement, key, value)
    db.session.commit()
    return jsonify({'message': 'Lease Agreement updated successfully'}), 200

# Delete Lease Agreement
@app.route('/lease/<int:id>', methods=['DELETE'])
def delete_lease_agreement(id):
    lease_agreement = LeaseAgreement.query.get_or_404(id)
    db.session.delete(lease_agreement)
    db.session.commit()
    return jsonify({'message': 'Lease Agreement deleted successfully'}), 200

# Similar routes for Payment and MaintenanceRequest entities
# Create Payment
@app.route('/payment', methods=['POST'])
def create_payment():
    data = request.json
    payment = Payment(**data)
    db.session.add(payment)
    db.session.commit()
    return jsonify({'message': 'Payment created successfully'}), 201

# Read Payment
@app.route('/payment/<int:id>', methods=['GET'])
def get_payment(id):
    payment = Payment.query.get_or_404(id)
    return jsonify(payment.serialize()), 200

# Update Payment
@app.route('/payment/<int:id>', methods=['PUT'])
def update_payment(id):
    data = request.json
    payment = Payment.query.get_or_404(id)
    for key, value in data.items():
        setattr(payment, key, value)
    db.session.commit()
    return jsonify({'message': 'Payment updated successfully'}), 200

# Delete Payment
@app.route('/payment/<int:id>', methods=['DELETE'])
def delete_payment(id):
    payment = Payment.query.get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    return jsonify({'message': 'Payment deleted successfully'}), 200

# Create Maintenance Request
@app.route('/maintenance', methods=['POST'])
def create_maintenance_request():
    data = request.json
    maintenance_request = MaintenanceRequest(**data)
    db.session.add(maintenance_request)
    db.session.commit()
    return jsonify({'message': 'Maintenance Request created successfully'}), 201

# Read Maintenance Request
@app.route('/maintenance/<int:id>', methods=['GET'])
def get_maintenance_request(id):
    maintenance_request = MaintenanceRequest.query.get_or_404(id)
    return jsonify(maintenance_request.serialize()), 200

# Update Maintenance Request
@app.route('/maintenance/<int:id>', methods=['PUT'])
def update_maintenance_request(id):
    data = request.json
    maintenance_request = MaintenanceRequest.query.get_or_404(id)
    for key, value in data.items():
        setattr(maintenance_request, key, value)
    db.session.commit()
    return jsonify({'message': 'Maintenance Request updated successfully'}), 200

# Delete Maintenance Request
@app.route('/maintenance/<int:id>', methods=['DELETE'])
def delete_maintenance_request(id):
    maintenance_request = MaintenanceRequest.query.get_or_404(id)
    db.session.delete(maintenance_request)
    db.session.commit()
    return jsonify({'message': 'Maintenance Request deleted successfully'}), 200
#
if __name__ == '__main__':
    app.run(debug=True)


