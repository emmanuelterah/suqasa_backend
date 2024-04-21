from flask import request, Response, jsonify
from app import app
from models.dbmodels import db
from models.landlord import Landlord
from models.property import Property
from models.tenant import Tenant
from models.lease_agreement import LeaseAgreement
from models.payment import Payment
from models.maintenance import MaintenanceRequest
from datetime import datetime


# Welcome route
@app.route("/")
def index():
    return "<h1>Welcome to the Property Management App!</h1>"

# Routes for Landlord
@app.route("/landlords", methods=['GET'])
def get_landlords():
    landlords = Landlord.query.all()
    landlord_data = [
        {
            "LandlordID": landlord.LandlordID,
            "Name": landlord.Name,
            "ContactInfo": landlord.ContactInfo,
            "BankAcctInfo": landlord.BankAcctInfo,
            "Address": landlord.Address
        }
        for landlord in landlords
    ]
    return jsonify(landlord_data), 200

@app.route("/landlords/<int:id>", methods=['GET'])
def get_landlord_by_id(id):
    landlord = Landlord.query.get_or_404(id)
    return jsonify({
        "LandlordID": landlord.LandlordID,
        "Name": landlord.Name,
        "ContactInfo": landlord.ContactInfo,
        "BankAcctInfo": landlord.BankAcctInfo,
        "Address": landlord.Address
    }), 200

@app.route('/landlords/<int:id>', methods=['DELETE'])
def delete_landlord(id):
    landlord = Landlord.query.get(id)
    if landlord:
        db.session.delete(landlord)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Landlord not found"}), 404
    
@app.route("/landlords", methods=['POST'])
def create_landlord():
    data = request.get_json()
    new_landlord = Landlord(**data)
    db.session.add(new_landlord)
    db.session.commit()
    return jsonify({
        "LandlordID": new_landlord.LandlordID,
        "Name": new_landlord.Name,
        "ContactInfo": new_landlord.ContactInfo,
        "BankAcctInfo": new_landlord.BankAcctInfo,
        "Address": new_landlord.Address
    }), 201 

# @app.route("/landlords/<int:id>", methods=['GET'])
# def get_landlord(id):
#     landlord = Landlord.query.get_or_404(id)
#     return jsonify(landlord.serialize()), 200

# @app.route("/landlords", methods=['POST'])
# def create_landlord():
#     data = request.json
#     landlord = Landlord(**data)
#     db.session.add(landlord)
#     db.session.commit()
#     return jsonify({'message': 'Landlord created successfully'}), 201

# @app.route("/landlords/<int:id>", methods=['PUT'])
# def update_landlord(id):
#     data = request.json
#     landlord = Landlord.query.get_or_404(id)
#     for key, value in data.items():
#         setattr(landlord, key, value)
#     db.session.commit()
#     return jsonify({'message': 'Landlord updated successfully'}), 200

# @app.route("/landlords/<int:id>", methods=['DELETE'])
# def delete_landlord(id):
#     landlord = Landlord.query.get_or_404(id)
#     db.session.delete(landlord)
#     db.session.commit()
#     return jsonify({'message': 'Landlord deleted successfully'}), 200

# Routes for Property
@app.route("/properties", methods=['GET'])
def get_properties():
    properties = Property.query.all()
    property_data = [
        {
            "id": property.id,
            "name": property.name,
            "address": property.address,
            # Add other fields as needed
        }
        for property in properties
    ]
    return jsonify(property_data), 200

@app.route("/properties/<int:id>", methods=['GET'])
def get_property_by_id(id):
    property = Property.query.get_or_404(id)
    return jsonify({
        "id": property.id,
        "name": property.name,
        "address": property.address,
        "description": property.description,
        "Bedrooms": property.Bedrooms,
        "Size": property.Size,
        "RentAmount": property.RentAmount,
        "Status": property.Status,
        "LandlordID": property.LandlordID
    }), 200

@app.route("/properties", methods=['POST'])
def create_property():
    data = request.get_json()
    new_property = Property(**data)
    db.session.add(new_property)
    db.session.commit()
    return jsonify({
        "id": new_property.id,
        "name": new_property.name,
        "address": new_property.address,
        "description": new_property.description,
        "Bedrooms": new_property.Bedrooms,
        "Size": new_property.Size,
        "RentAmount": new_property.RentAmount,
        "Status": new_property.Status,
        "LandlordID": new_property.LandlordID
    }), 201

@app.route('/properties/<int:id>', methods=['DELETE'])
def delete_property(id):
    property = Property.query.get(id)
    if property:
        db.session.delete(property)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Property not found"}), 404

# @app.route("/properties/<int:id>", methods=['PUT'])
# def update_property(id):
#     data = request.json
#     property = Property.query.get_or_404(id)
#     for key, value in data.items():
#         setattr(property, key, value)
#     db.session.commit()
#     return jsonify({'message': 'Property updated successfully'}), 200

# @app.route("/properties/<int:id>", methods=['DELETE'])
# def delete_property(id):
#     property = Property.query.get_or_404(id)
#     db.session.delete(property)
#     db.session.commit()
#     return jsonify({'message': 'Property deleted successfully'}), 200

# Routes for Tenant
@app.route("/tenants", methods=['GET'])
def get_tenants():
    tenants = Tenant.query.all()
    tenant_data = [
        {
            "TenantID": tenant.TenantID,
            "Name": tenant.Name,
            "ContactInfo": tenant.ContactInfo,
            "Occupation": tenant.Occupation,
            "CurrentAddr": tenant.CurrentAddr,
            "PrevAddr": tenant.PrevAddr,
            "EmergencyCnt": tenant.EmergencyCnt
        }
        for tenant in tenants
    ]
    return jsonify(tenant_data), 200

@app.route("/tenants/<int:id>", methods=['GET'])
def get_tenant(id):
    tenant = Tenant.query.get_or_404(id)
    return jsonify(tenant.serialize()), 200

@app.route("/tenants", methods=['POST'])
def create_tenant():
    data = request.get_json()
    new_tenant = Tenant(**data)
    db.session.add(new_tenant)
    db.session.commit()
    return jsonify({
        "TenantID": new_tenant.TenantID,
        "Name": new_tenant.Name,
        "ContactInfo": new_tenant.ContactInfo,
        "Occupation": new_tenant.Occupation,
        "CurrentAddr": new_tenant.CurrentAddr,
        "PrevAddr": new_tenant.PrevAddr,
        "EmergencyCnt": new_tenant.EmergencyCnt
    }), 201

@app.route("/tenants/<int:id>", methods=['GET'])
def get_tenant_by_id(id):
    tenant = Tenant.query.get_or_404(id)
    return jsonify({
        "TenantID": tenant.TenantID,
        "Name": tenant.Name,
        "ContactInfo": tenant.ContactInfo,
        "Occupation": tenant.Occupation,
        "CurrentAddr": tenant.CurrentAddr,
        "PrevAddr": tenant.PrevAddr,
        "EmergencyCnt": tenant.EmergencyCnt
    }), 200

@app.route("/tenants/<int:id>", methods=['DELETE'])
def delete_tenant(id):
    tenant = Tenant.query.get_or_404(id)
    db.session.delete(tenant)
    db.session.commit()
    return jsonify({'message': 'Tenant deleted successfully'}), 200

@app.route("/tenants/<int:id>", methods=['PUT'])
def update_tenant(id):
    try:
        tenant = Tenant.query.get(id)
        if tenant:
            data = request.json
            tenant.Name = data.get('Name', tenant.Name)
            tenant.ContactInfo = data.get('ContactInfo', tenant.ContactInfo)
            tenant.Occupation = data.get('Occupation', tenant.Occupation)
            tenant.CurrentAddr = data.get('CurrentAddr', tenant.CurrentAddr)
            tenant.PrevAddr = data.get('PrevAddr', tenant.PrevAddr)
            tenant.EmergencyCnt = data.get('EmergencyCnt', tenant.EmergencyCnt)
            # Add other fields as needed
            
            db.session.commit()
            return jsonify({'message': 'Tenant updated successfully'}), 200
        else:
            return jsonify({"error": "Tenant not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# # Routes for Lease Agreement
# @app.route("/lease_agreements", methods=['GET'])
# def get_lease_agreements():
#     lease_agreements = LeaseAgreement.query.all()
#     lease_agreement_data = [lease_agreement.serialize() for lease_agreement in lease_agreements]
#     return jsonify(lease_agreement_data), 200

# @app.route("/lease_agreements/<int:id>", methods=['GET'])
# def get_lease_agreement(id):
#     lease_agreement = LeaseAgreement.query.get_or_404(id)
#     return jsonify(lease_agreement.serialize()), 200

# @app.route("/lease_agreements", methods=['POST'])
# def create_lease_agreement():
#     data = request.json
#     lease_agreement = LeaseAgreement(**data)
#     db.session.add(lease_agreement)
#     db.session.commit()
#     return jsonify({'message': 'Lease Agreement created successfully'}), 201

# @app.route("/lease_agreements/<int:id>", methods=['PUT'])
# def update_lease_agreement(id):
#     data = request.json
#     lease_agreement = LeaseAgreement.query.get_or_404(id)
#     for key, value in data.items():
#         setattr(lease_agreement, key, value)
#     db.session.commit()
#     return jsonify({'message': 'Lease Agreement updated successfully'}), 200

# @app.route("/lease_agreements/<int:id>", methods=['DELETE'])
# def delete_lease_agreement(id):
#     lease_agreement = LeaseAgreement.query.get_or_404(id)
#     db.session.delete(lease_agreement)
#     db.session.commit()
#     return jsonify({'message': 'Lease Agreement deleted successfully'}), 200

# # Routes for Payment
# @app.route("/payments", methods=['GET'])
# def get_payments():
#     payments = Payment.query.all()
#     payment_data = [payment.serialize() for payment in payments]
#     return jsonify(payment_data), 200

# @app.route("/payments/<int:id>", methods=['GET'])
# def get_payment(id):
#     payment = Payment.query.get_or_404(id)
#     return jsonify(payment.serialize()), 200

# @app.route("/payments", methods=['POST'])
# def create_payment():
#     data = request.json
#     payment = Payment(**data)
#     db.session.add(payment)
#     db.session.commit()
#     return jsonify({'message': 'Payment created successfully'}), 201

# @app.route("/payments/<int:id>", methods=['PUT'])
# def update_payment(id):
#     data = request.json
#     payment = Payment.query.get_or_404(id)
#     for key, value in data.items():
#         setattr(payment, key, value)
#     db.session.commit()
#     return jsonify({'message': 'Payment updated successfully'}), 200

# @app.route("/payments/<int:id>", methods=['DELETE'])
# def delete_payment(id):
#     payment = Payment.query.get_or_404(id)
#     db.session.delete(payment)
#     db.session.commit()
#     return jsonify({'message': 'Payment deleted successfully'}), 200

# # Routes for Maintenance Requests
# @app.route("/maintenance_requests", methods=['GET'])
# def get_maintenance_requests():
#     maintenance_requests = MaintenanceRequest.query.all()
#     maintenance_request_data = [maintenance_request.serialize() for maintenance_request in maintenance_requests]
#     return jsonify(maintenance_request_data), 200

# @app.route("/maintenance_requests/<int:id>", methods=['GET'])
# def get_maintenance_request(id):
#     maintenance_request = MaintenanceRequest.query.get_or_404(id)
#     return jsonify(maintenance_request.serialize()), 200

# @app.route("/maintenance_requests", methods=['POST'])
# def create_maintenance_request():
#     data = request.json
#     if not data:
#         return jsonify({'message': 'Missing maintenance request data'}), 400

#     maintenance_request = MaintenanceRequest(**data)
#     db.session.add(maintenance_request)
#     db.session.commit()
#     return jsonify({'message': 'Maintenance Request created successfully'}), 201

# @app.route("/maintenance_requests/<int:id>", methods=['PUT'])
# def update_maintenance_request(id):
#     data = request.json
#     if not data:
#         return jsonify({'message': 'Missing maintenance request data'}), 400

#     maintenance_request = MaintenanceRequest.query.get_or_404(id)
#     for key, value in data.items():
#         setattr(maintenance_request, key, value)
#     db.session.commit()
#     return jsonify({'message': 'Maintenance Request updated successfully'}), 200

# @app.route("/maintenance_requests/<int:id>", methods=['DELETE'])
# def delete_maintenance_request(id):
#     maintenance_request = MaintenanceRequest.query.get_or_404(id)
#     db.session.delete(maintenance_request)
#     db.session.commit()
#     return jsonify({'message': 'Maintenance Request deleted successfully'}), 200


@app.route("/lease_agreements", methods=['GET'])
def get_lease_agreements():
    lease_agreements = LeaseAgreement.query.all()
    lease_agreement_data = [
        {
            "LeaseID": lease.LeaseID,
            "PropertyID": lease.PropertyID,
            "TenantID": lease.TenantID,
            "StartDate": lease.StartDate.strftime("%Y-%m-%d"),  # Convert date to string
            "EndDate": lease.EndDate.strftime("%Y-%m-%d"),      # Convert date to string
            "RentAmount": lease.RentAmount,
            "PaymentSchedule": lease.PaymentSchedule,
            "DepositAmount": lease.DepositAmount
        }
        for lease in lease_agreements
    ]
    return jsonify(lease_agreement_data), 200
@app.route("/lease_agreements/<int:id>", methods=['GET'])
def get_lease_agreement_by_id(id):
    lease_agreement = LeaseAgreement.query.get_or_404(id)
    return jsonify({
        "LeaseID": lease_agreement.LeaseID,
        "PropertyID": lease_agreement.PropertyID,
        "TenantID": lease_agreement.TenantID,
        "StartDate": lease_agreement.StartDate.strftime("%Y-%m-%d"),
        "EndDate": lease_agreement.EndDate.strftime("%Y-%m-%d"),
        "RentAmount": lease_agreement.RentAmount,
        "PaymentSchedule": lease_agreement.PaymentSchedule,
        "DepositAmount": lease_agreement.DepositAmount
    }), 200

@app.route("/maintenance_requests", methods=['GET'])
def get_maintenance_requests():
    maintenance_requests = MaintenanceRequest.query.all()
    maintenance_request_data = [
        {
            "RequestID": request.RequestID,
            "PropertyID": request.PropertyID,
            "Description": request.Description,
            "RequestDate": request.RequestDate.strftime("%Y-%m-%d"),  # Convert date to string
            "RequestedBy": request.RequestedBy,
            "Status": request.Status,
            "AssignedStaff": request.AssignedStaff,
            "CompletionDate": request.CompletionDate.strftime("%Y-%m-%d") if request.CompletionDate else None,  # Convert date to string or None
        }
        for request in maintenance_requests
    ]
    return jsonify(maintenance_request_data), 200

@app.route("/maintenance_requests/<int:id>", methods=['GET'])
def get_maintenance_request_by_id(id):
    maintenance_request = MaintenanceRequest.query.get_or_404(id)
    return jsonify({
        "RequestID": maintenance_request.RequestID,
        "PropertyID": maintenance_request.PropertyID,
        "Description": maintenance_request.Description,
        "RequestDate": maintenance_request.RequestDate.strftime("%Y-%m-%d"),
        "RequestedBy": maintenance_request.RequestedBy,
        "Status": maintenance_request.Status,
        "AssignedStaff": maintenance_request.AssignedStaff,
        "CompletionDate": maintenance_request.CompletionDate.strftime("%Y-%m-%d") if maintenance_request.CompletionDate else None
    }), 200

@app.route('/maintenance_requests/<int:id>', methods=['DELETE'])
def delete_maintenance_request(id):
    maintenance_request = MaintenanceRequest.query.get(id)
    if maintenance_request:
        db.session.delete(maintenance_request)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Maintenance Request not found"}), 404
    
@app.route("/maintenance_request/<int:id>", methods=['PUT'])
def update_maintenance_request_by_id(id):
    try:
        maintenance_request = MaintenanceRequest.query.get(id)
        if maintenance_request:
            data = request.json
            maintenance_request.PropertyID = data.get('PropertyID', maintenance_request.PropertyID)
            maintenance_request.Description = data.get('Description', maintenance_request.Description)
            maintenance_request.RequestDate = datetime.strptime(data.get('RequestDate', maintenance_request.RequestDate), "%Y-%m-%d")
            maintenance_request.RequestedBy = data.get('RequestedBy', maintenance_request.RequestedBy)
            maintenance_request.Status = data.get('Status', maintenance_request.Status)
            maintenance_request.AssignedStaff = data.get('AssignedStaff', maintenance_request.AssignedStaff)
            maintenance_request.CompletionDate = datetime.strptime(data.get('CompletionDate', maintenance_request.CompletionDate), "%Y-%m-%d")
            db.session.commit()
            return jsonify({'message': 'Maintenance request updated successfully'}), 200
        else:
            return jsonify({"error": "Maintenance request not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/payments", methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    payment_data = [
        {
            "PaymentID": payment.PaymentID,
            "LeaseID": payment.LeaseID,
            "TenantID": payment.TenantID,
            "PaymentDate": payment.PaymentDate.strftime("%Y-%m-%d"),  # Convert date to string
            "PaymentAmount": payment.PaymentAmount,
            "PaymentMethod": payment.PaymentMethod,
            "PaymentStatus": payment.PaymentStatus,
        }
        for payment in payments
    ]
    return jsonify(payment_data), 200
@app.route("/payments/<int:id>", methods=['GET'])
def get_payment_by_id(id):
    payment = Payment.query.get_or_404(id)
    return jsonify({
        "PaymentID": payment.PaymentID,
        "LeaseID": payment.LeaseID,
        "TenantID": payment.TenantID,
        "PaymentDate": payment.PaymentDate.strftime("%Y-%m-%d"),
        "PaymentAmount": payment.PaymentAmount,
        "PaymentMethod": payment.PaymentMethod,
        "PaymentStatus": payment.PaymentStatus
    }), 200

@app.route('/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):
    payment = Payment.query.get(id)
    if payment:
        db.session.delete(payment)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Payment not found"}), 404

# @app.route('/payments/<int:id>', methods=['PUT'])
# def update_payment(id):
#     try:
#         payment = Payment.query.get(id)
#         if payment:
#             data = request.json
#             payment.amount = data.get('amount', payment.amount)
#             payment.date = data.get('date', payment.date)

#             # Update other fields as needed
            
#             db.session.commit()
#             return jsonify({'message': 'Payment updated successfully'}), 200
#         else:
#             return jsonify({"error": "Payment not found"}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# @app.route('/payments/<int:id>', methods=['PUT'])
# def update_payment(id):
#     try:
#         payment = Payment.query.get(id)
#         if payment:
#             data = request.json
#             payment.PaymentID = data.get('PaymentID', payment.PaymentID)
#             payment.LeaseID = data.get('LeaseID', payment.LeaseID)
#             payment.TenantID = data.get('TenantID', payment.TenantID)
#             payment.PaymentDate = data.get('PaymentDate', payment.PaymentDate)
#             payment.PaymentAmount = data.get('PaymentAmount', payment.PaymentAmount)
#             payment.PaymentMethod = data.get('PaymentMethod', payment.PaymentMethod)
#             payment.PaymentStatus = data.get('PaymentStatus', payment.PaymentStatus)
#             db.session.commit()
#             return jsonify({'message': 'Payment updated successfully'}), 200
#         else:
#             return jsonify({"error": "Payment not found"}), 404
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
@app.route("/payments/<int:id>", methods=['PUT'])
def update_payment_by_id(id):
    try:
        payment = Payment.query.get(id)
        if payment:
            data = request.json
            payment.PaymentID = data.get('PaymentID', payment.PaymentID)
            payment.LeaseID = data.get('LeaseID', payment.LeaseID)
            payment.TenantID = data.get('TenantID', payment.TenantID)
            payment.PaymentDate = datetime.strptime(data.get('PaymentDate', payment.PaymentDate), "%Y-%m-%d")
            payment.PaymentAmount = data.get('PaymentAmount', payment.PaymentAmount)
            payment.PaymentMethod = data.get('PaymentMethod', payment.PaymentMethod)
            payment.PaymentStatus = data.get('PaymentStatus', payment.PaymentStatus)
            db.session.commit()
            return jsonify({'message': 'Payment updated successfully'}), 200
        else:
            return jsonify({"error": "Payment not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

