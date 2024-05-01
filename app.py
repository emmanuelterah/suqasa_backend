from flask import Flask, request, Response, jsonify
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
# from models.passwordresettoken import PasswordResetToken
from models.dbmodels import db
from models.property import Property
from models.landlord import Landlord
from models.lease_agreement import LeaseAgreement
from models.maintenance import MaintenanceRequest
from models.payment import Payment
from models.tenant import Tenant
from flask_migrate import Migrate
from datetime import datetime
from models.user import User
import base64
import random
import string
# from flasgger import Swagger
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()


import os 
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import sqlite3
import psycopg2
import traceback


app = Flask(
    __name__,
    static_url_path='',
    # static_folder='../client/build',
    # template_folder='../client/build'
)
CORS(app)

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATABASE = os.environ.get(
#     "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://admin:QUnioSOEHitFALuT3ACdSYyxLNYx0MGu@dpg-coj6of0cmk4c73afdirg-a.oregon-postgres.render.com/property_elk4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

secret_key = base64.b64encode(os.urandom(24)).decode('utf-8')
print(secret_key)
# Initialize the database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)


users = {
    "tenant1": {
        "password": generate_password_hash("password1"),
        "type": "tenant"
    },
    "landlord1": {
        "password": generate_password_hash("password2"),
        "type": "landlord"
    }
}


def token_required(user_type):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization')

            if not token:
                return jsonify({'message': 'Token is missing'}), 401

            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
                current_user = data['username']
                if users[current_user]['type'] != user_type:
                    raise Exception("Unauthorized access")
            except Exception as e:
                return jsonify({'message': str(e)}), 401

            return f(current_user, *args, **kwargs)

        return decorated
    return decorator

# # Connect to your database
# def connect_db():
#     conn = sqlite3.connect('app.db')
#     return conn

# def connect_db():
#     conn = psycopg2.connect(
#         dbname='property_management_285e',
#         user='property_management_285e_user',
#         password='236h6am7uok3sE85JlzrPBH6OLQL9KYO',
#         host='localhost',
#         port='5432'
#     )
#     return conn



@app.route('/register', methods=['POST'])
def register():

    data = request.get_json()

    # Check if required fields are present
    if not all(key in data for key in ('username', 'email', 'password', 'user_type')):
        return jsonify({'message': 'Missing required fields'}), 400

    # Extract data from JSON
    username = data['username']
    email = data['email']
    password = data['password']
    user_type = data['user_type']

    # Check if username already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 409

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create a new user instance
    new_user = User(username=username, email=email, password=hashed_password, user_type=user_type)

    # Add user to the database
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error registering user: {}'.format(str(e))}), 500
    finally:
        db.session.close()


# @app.route('/login', methods=['POST'])
# def login():
#     try:
#         data = request.get_json()
#         username = data.get('username')
#         password = data.get('password')

#         if not username or not password:
#             return jsonify({'message': 'Missing username or password'}), 400

#         user = User.query.filter_by(username=username).first()

#         if not user or not check_password_hash(user.password, password):
#             return jsonify({'message': 'Invalid username or password'}), 401

#         expiration_time = datetime.utcnow() + timedelta(hours=1)
#         token = jwt.encode({'user_id': user.id, 'exp': expiration_time}, secret_key, algorithm='HS256')

#         return jsonify({'message': 'Login successful', 'token': token})
#     except Exception as e:
#         print(f"Login error: {e}")
#         traceback.print_exc()  # Print traceback for detailed error information
#         return jsonify({'message': 'Internal server error'}), 500

	
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid username or password'}), 401

    expiration_time = datetime.utcnow() + timedelta(hours=1)
    token = jwt.encode({'user_id': user.id, 'user_type': user.user_type, 'exp': expiration_time}, secret_key, algorithm='HS256')

    return jsonify({'message': 'Login successful', 'token': token, 'user_type': user.user_type})
except Exception as e:
    print(f"Login error: {e}")
    traceback.print_exc()  # Print traceback for detailed error information
    return jsonify({'message': 'Internal server error'}), 500

# jj

def decode_token(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return 'Token has expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
    except jwt.JWTException as e:
        print(f"Token decoding error: {e}")
        return 'Invalid token.'



@app.route('/protected', methods=['GET'])
def protected_route():
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({'message': 'Token is missing'}), 401

    token = token.split(' ')[1]  # Extract the token from the 'Authorization' header

    # Decode the token
    payload = decode_token(token)

    if isinstance(payload, str):
        return jsonify({'message': payload}), 401

    user_id = payload.get('user_id')

    # Now you have the user ID, and you can perform further authorization logic
    # Check if the user has the necessary permissions, etc.
    # the process 
    return jsonify({'message': 'Access granted'}), 200



# @app.route('/forgot-password', methods=['POST'])
# def forgot_password():
#     data = request.get_json()
#     username = data.get('username')

#     user = User.query.filter_by(username=username).first()

#     if user:
#         # Generate a random token
#         token = ''.join(random.choices(string.ascii_letters + string.digits, k=20))

#         # Set token expiration time (e.g., 1 hour)
#         expiration = datetime.now() + timedelta(hours=1)
#         print(token)
#         print(expiration)
#         # Create a new reset token
#         reset_token = PasswordResetToken(user_id=user.id, token=token, expiration=expiration)
#         db.session.add(reset_token)
#         db.session.commit()

       

#         return jsonify({'message': 'Password reset token generated successfully'})

#     return jsonify({'message': 'User not found'}), 404

# @app.route('/reset-password/<token>', methods=['POST'])
# def reset_password(token):
#     data = request.get_json()
#     new_password = data.get('new_password')

#     reset_token = PasswordResetToken.query.filter_by(token=token).first()

#     if reset_token and reset_token.expiration > datetime.now():
#         user = User.query.filter_by(id=reset_token.user_id).first()
#         hashed_password = generate_password_hash(new_password, method='sha256')
#         user.password = hashed_password

#         db.session.delete(reset_token)
#         db.session.commit()

#         return jsonify({'message': 'Password reset successful'})

#     return jsonify({'message': 'Invalid or expired reset token'}), 400


# Protected route example for tenants
@app.route('/protected/tenant', methods=['GET'])
@token_required('tenant')
def protected_tenant(current_user):
    return jsonify({'message': 'Hello, {}! This is a protected tenant route.'.format(current_user)}), 200

# Protected route example for landlords
@app.route('/protected/landlord', methods=['GET'])
@token_required('landlord')
def protected_landlord(current_user):
    return jsonify({'message': 'Hello, {}! This is a protected landlord route.'.format(current_user)}), 200












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

@app.route("/landlords/<int:id>", methods=['PUT'])
def update_landlord_by_id(id):
    try:
        landlord = Landlord.query.get(id)
        if landlord:
            data = request.json
            landlord.Name = data.get('Name', landlord.Name)
            landlord.ContactInfo = data.get('ContactInfo', landlord.ContactInfo)
            landlord.BankAcctInfo = data.get('BankAcctInfo', landlord.BankAcctInfo)
            landlord.Address = data.get('Address', landlord.Address)
            db.session.commit()
            return jsonify({'message': 'Landlord updated successfully'}), 200
        else:
            return jsonify({"error": "Landlord not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/properties", methods=['GET'])
def get_properties():
    properties = Property.query.all()
    property_data = [
        {
            "id": property.id,
            "name": property.name,
            "address": property.address,
            "description": property.description,
            "Bedrooms": property.Bedrooms,
            "image": property.image,
            "Size": property.Size,
            "RentAmount": property.RentAmount,
            "Status": property.Status,
            "LandlordID": property.LandlordID,
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
        "image": property.image,  # Include image field
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
    
from flask import request, jsonify

@app.route("/properties/<int:property_id>", methods=['PUT'])
def update_property(property_id):
    property = Property.query.get(property_id)
    
    if property is None:
        return jsonify({"error": "Property not found"}), 404
    
    data = request.json
    
    # Update property fields if provided in the request
    if 'name' in data:
        property.name = data['name']
    if 'address' in data:
        property.address = data['address']
    if 'description' in data:
        property.description = data['description']
    if 'Bedrooms' in data:
        property.Bedrooms = data['Bedrooms'] 
    if 'image' in data:
        property.image = data['image']
    if 'Size' in data:
        property.Size = data['Size']
    if 'RentAmount' in data:
        property.RentAmount = data['RentAmount']
    if 'Status' in data:
        property.Status = data['Status']
    if 'LandlordID' in data:
        property.LandlordID = data['LandlordID']
    
    # Commit changes to the database
    db.session.commit()
    
    return jsonify({"message": "Property updated successfully"}), 200

@app.route('/tenants', methods=['GET'])
def get_tenants():
    try:
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
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

@app.route("/lease_agreements/<int:id>", methods=['PUT'])
def update_lease_agreement(id):
    try:
        lease_agreement = LeaseAgreement.query.get_or_404(id)
        data = request.json
        
        # Convert date strings to Python date objects
        start_date = datetime.strptime(data.get('StartDate'), '%Y-%m-%d').date()
        end_date = datetime.strptime(data.get('EndDate'), '%Y-%m-%d').date()
        
        # Update lease agreement fields with data from the request
        lease_agreement.PropertyID = data.get('PropertyID', lease_agreement.PropertyID)
        lease_agreement.TenantID = data.get('TenantID', lease_agreement.TenantID)
        lease_agreement.StartDate = start_date
        lease_agreement.EndDate = end_date
        lease_agreement.RentAmount = data.get('RentAmount', lease_agreement.RentAmount)
        lease_agreement.PaymentSchedule = data.get('PaymentSchedule', lease_agreement.PaymentSchedule)
        lease_agreement.DepositAmount = data.get('DepositAmount', lease_agreement.DepositAmount)
        
        db.session.commit()
        
        return jsonify({'message': 'Lease agreement updated successfully'}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/lease_agreements', methods=['POST'])
def create_lease_agreement():
    data = request.json  # Assuming JSON data is sent in the request
    if not data:
        return jsonify({'message': 'No input data provided'}), 400

    # Extracting data from JSON
    property_id = data.get('PropertyID')
    tenant_id = data.get('TenantID')
    start_date_str = data.get('StartDate')
    end_date_str = data.get('EndDate')
    rent_amount = data.get('RentAmount')
    payment_schedule = data.get('PaymentSchedule')
    deposit_amount = data.get('DepositAmount')

    # Convert date strings to Python date objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

    # Create a new lease agreement instance
    new_lease = LeaseAgreement(
        PropertyID=property_id,
        TenantID=tenant_id,
        StartDate=start_date,
        EndDate=end_date,
        RentAmount=rent_amount,
        PaymentSchedule=payment_schedule,
        DepositAmount=deposit_amount
    )

    # Add and commit the new lease agreement to the database
    db.session.add(new_lease)
    db.session.commit()

    response_data = {
        "LeaseID": new_lease.LeaseID,
        "PropertyID": new_lease.PropertyID,
        "TenantID": new_lease.TenantID,
        "StartDate": str(new_lease.StartDate),
        "EndDate": str(new_lease.EndDate),
        "RentAmount": new_lease.RentAmount,
        "PaymentSchedule": new_lease.PaymentSchedule,
        "DepositAmount": new_lease.DepositAmount
    }

    return jsonify(response_data), 201


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
    

    
@app.route("/maintenance_requests/<int:id>", methods=['PUT'])
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
            completion_date = data.get('CompletionDate')
            if completion_date:
                maintenance_request.CompletionDate = datetime.strptime(completion_date, "%Y-%m-%d")
            else:
                maintenance_request.CompletionDate = None
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


@app.route("/maintenance_requests", methods=['POST'])
def create_maintenance_request():
    data = request.get_json()

    # Convert date string to Python date object
    request_date = datetime.strptime(data['RequestDate'], '%Y-%m-%d').date()

    # Check if CompletionDate is provided
    completion_date = None
    if 'CompletionDate' in data and data['CompletionDate']:
        completion_date = datetime.strptime(data['CompletionDate'], '%Y-%m-%d').date()

    new_maintenance_request = MaintenanceRequest(
        PropertyID=data['PropertyID'],
        Description=data['Description'],
        RequestDate=request_date,
        RequestedBy=data['RequestedBy'],
        Status=data['Status'],
        AssignedStaff=data['AssignedStaff'],
        CompletionDate=completion_date
    )

    db.session.add(new_maintenance_request)
    db.session.commit()

    response_data = {
        "RequestID": new_maintenance_request.RequestID,
        "PropertyID": new_maintenance_request.PropertyID,
        "Description": new_maintenance_request.Description,
        "RequestDate": new_maintenance_request.RequestDate.strftime("%Y-%m-%d"),
        "RequestedBy": new_maintenance_request.RequestedBy,
        "Status": new_maintenance_request.Status,
        "AssignedStaff": new_maintenance_request.AssignedStaff,
        "CompletionDate": new_maintenance_request.CompletionDate.strftime("%Y-%m-%d") if new_maintenance_request.CompletionDate else None
    }

    return jsonify(response_data), 201

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
    

@app.route("/payments", methods=['POST'])
def create_payment():
    data = request.get_json()

    # Convert date string to Python date object
    payment_date = datetime.strptime(data['PaymentDate'], '%Y-%m-%d').date()

    new_payment = Payment(
        LeaseID=data['LeaseID'],
        TenantID=data['TenantID'],
        PaymentDate=payment_date,
        PaymentAmount=data['PaymentAmount'],
        PaymentMethod=data['PaymentMethod'],
        PaymentStatus=data['PaymentStatus']
    )

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({
        "PaymentID": new_payment.PaymentID,
        "LeaseID": new_payment.LeaseID,
        "TenantID": new_payment.TenantID,
        "PaymentDate": new_payment.PaymentDate.strftime("%Y-%m-%d"),
        "PaymentAmount": new_payment.PaymentAmount,
        "PaymentMethod": new_payment.PaymentMethod,
        "PaymentStatus": new_payment.PaymentStatus
    }), 201


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




if __name__ == "__main__":
    
    app.run(port=5555, debug=True)
