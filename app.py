
# # # # # from flask import Flask
# # # # # from flask_sqlalchemy import SQLAlchemy
# # # # # from models.expense import Expense
# # # # # from models.staff import Staff
# # # # # from models.lease_agreement import LeaseAgreementg
# # # # # from models.maintenance import MaintenanceRequest
# # # # # from models.payment import Payment
# # # # # from models.property import Property
# # # # # from models.tenant import Tenant
# # # # # from flask_migrate import Migrate
# # # # # from flask import Flask, request, jsonify, session
# # # # # from flask_bcrypt import Bcrypt
# # # # # from flask_cors import CORS
# # # # # from models.user import db, User
# # # # # from dotenv import load_dotenv
# # # # # load_dotenv()
# # # # # import os
# # # # # from sqlalchemy.exc import IntegrityError

# # # # # app = Flask(__name__)
# # # # # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
# # # # # app.config['SECRET_KEY'] = 'micasa-suqasa'
# # # # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # # # # app.config['SQLALCHEMY_ECHO'] = True
# # # # # # app.json.compact = False
# # # # # app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True 

# # # # # migrate = Migrate(app, db)

# # # # # # Initialize extensions
# # # # # db.init_app(app)
# # # # # bcrypt = Bcrypt(app)
# # # # # CORS(app, supports_credentials=True)

# # # # # @app.route('/')
# # # # # def home():
# # # # #     return '<h1>Property management</h1>'

# # # # # @app.route('/properties', methods=['GET'])
# # # # # def get_properties():
# # # # #     properties = Property.query.all()
# # # # #     return jsonify([property.to_dict() for property in properties])



# # # # # @app.route("/signup", methods=["POST"])
# # # # # def signup():
# # # # #     email = request.json.get("email")
# # # # #     password = request.json.get("password")

# # # # #     if not email or not password:
# # # # #         return jsonify({"error": "Email and password are required"}), 400

# # # # #     user_exists = User.query.filter_by(email=email).first()

# # # # #     if user_exists:
# # # # #         return jsonify({"error": "Email already exists"}), 409

# # # # #     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
# # # # #     new_user = User(email=email, password=hashed_password)
# # # # #     db.session.add(new_user)
# # # # #     db.session.commit()

# # # # #     return jsonify({
# # # # #         "id": new_user.id,
# # # # #         "email": new_user.email
# # # # #     })

# # # # # @app.route("/login", methods=["POST"])
# # # # # def login_user():
# # # # #     email = request.json.get("email")
# # # # #     password = request.json.get("password")

# # # # #     if not email or not password:
# # # # #         return jsonify({"error": "Email and password are required"}), 400

# # # # #     user = User.query.filter_by(email=email).first()

# # # # #     if user is None:
# # # # #         return jsonify({"error": "User not found"}), 404

# # # # #     if not bcrypt.check_password_hash(user.password, password):
# # # # #         return jsonify({"error": "Incorrect password"}), 401

# # # # #     return jsonify({
# # # # #         "id": user.id,
# # # # #         "email": user.email
# # # # #     })

# # # # # if __name__ == '__main__':
# # # # #     with app.app_context():
# # # # #         db.create_all()
# # # # #     app.run(port=5555, debug=True)


# # # from flask import Flask
# # # from flask_sqlalchemy import SQLAlchemy
# # # from models.expense import Expense
# # # from models.staff import Staff
# # # from models.lease_agreement import LeaseAgreement
# # # from models.maintenance import MaintenanceRequest
# # # from models.payment import Payment
# # # from models.property import Property
# # # from models.tenant import Tenant
# # # from flask_migrate import Migrate
# # # from flask import Flask, request, jsonify, session
# # # from flask_bcrypt import Bcrypt
# # # from flask_cors import CORS
# # # from models.user import db, User
# # # from models.passwordresettoken import passwordresettoken
# # # from dotenv import load_dotenv
# # # from cloudinary.uploader
# # # from flasgger import Swagger
# # # from datetime import datetime,timedelta
# # # import jwt
# # # import base64
# # # import werkzeug.security import generate_password_harsh, check_password_harsh
# # # load_dotenv()
# # # import os
# # # from sqlalchemy.exc import IntegrityError
# # # from utils import cloudconfig


# # # # Load environment variables
# # # load_dotenv()

# # # app = Flask(__name__)
# # # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
# # # app.config['SECRET_KEY'] = 'micasa-suqasa'
# # # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # # app.config['SQLALCHEMY_ECHO'] = True
# # # app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# # # # Initialize extensions
# # # db.init_app(app)
# # # bcrypt = Bcrypt(app)
# # # CORS(app, supports_credentials=True)
# # # migrate = Migrate(app, db)

# # # # Decorator functions for authorization
# # # def tenant_required(f):
# # #     @wraps(f)
# # #     def decorated(*args, **kwargs):
# # #         token = request.headers.get('Authorization', '').split(" ")[1]

# # #         try:
# # #             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
# # #             user_id = data['user_id']
# # #             role = data['role']
# # #             if role == 'tenant':
# # #                 return f(user_id, *args, **kwargs)
# # #             else:
# # #                 return jsonify({'message': 'Unauthorized access'}), 403
# # #         except jwt.ExpiredSignatureError:
# # #             return jsonify({'message': 'Token has expired'}), 401
# # #         except jwt.InvalidTokenError:
# # #             return jsonify({'message': 'Invalid token'}), 401

# # #     return decorated

# # # def landlord_required(f):
# # #     @wraps(f)
# # #     def decorated(*args, **kwargs):
# # #         token = request.headers.get('Authorization', '').split(" ")[1]

# # #         try:
# # #             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
# # #             user_id = data['user_id']
# # #             role = data['role']
# # #             if role == 'landlord':
# # #                 return f(user_id, *args, **kwargs)
# # #             else:
# # #                 return jsonify({'message': 'Unauthorized access'}), 403
# # #         except jwt.ExpiredSignatureError:
# # #             return jsonify({'message': 'Token has expired'}), 401
# # #         except jwt.InvalidTokenError:
# # #             return jsonify({'message': 'Invalid token'}), 401

# # #     return decorated

# # # # Routes
# # # @app.route('/')
# # # def home():
# # #     return '<h1>Property management</h1>'

# # # @app.route('/properties', methods=['GET'])
# # # def get_properties():
# # #     properties = Property.query.all()
# # #     return jsonify([property.to_dict() for property in properties])

# # # @app.route("/signup", methods=["POST"])
# # # def signup():
# # #     email = request.json.get("email")
# # #     password = request.json.get("password")

# # #     if not email or not password:
# # #         return jsonify({"error": "Email and password are required"}), 400

# # #     user_exists = User.query.filter_by(email=email).first()

# # #     if user_exists:
# # #         return jsonify({"error": "Email already exists"}), 409

# # #     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
# # #     new_user = User(email=email, password=hashed_password)
# # #     db.session.add(new_user)
# # #     db.session.commit()

# # #     return jsonify({
# # #         "id": new_user.id,
# # #         "email": new_user.email
# # #     })

# # # @app.route("/login", methods=["POST"])
# # # def login_user():
# # #     email = request.json.get("email")
# # #     password = request.json.get("password")

# # #     if not email or not password:
# # #         return jsonify({"error": "Email and password are required"}), 400

# # #     user = User.query.filter_by(email=email).first()

# # #     if user is None:
# # #         return jsonify({"error": "User not found"}), 404

# # #     if not bcrypt.check_password_hash(user.password, password):
# # #         return jsonify({"error": "Incorrect password"}), 401

# # #     # Determine the user's role
# # #     role = 'tenant' if isinstance(user, Tenant) else 'landlord'

# # #     # Generate JWT token with user ID and role
# # #     token_payload = {
# # #         'user_id': user.id,
# # #         'role': role
# # #     }
# # #     token = jwt.encode(token_payload, app.config['SECRET_KEY'], algorithm='HS256')

# # #     return jsonify({
# # #         "id": user.id,
# # #         "email": user.email,
# # #         "token": token.decode('UTF-8')
# # #     })

# # # @app.route('/tenant-data', methods=['GET'])
# # # @tenant_required
# # # def get_tenant_data(user_id):
# # #     # Fetch tenant-specific data based on the user_id
# # #     tenant_data = Tenant.query.filter_by(user_id=user_id).first()
# # #     if tenant_data:
# # #         return jsonify(tenant_data.serialize()), 200
# # #     else:
# # #         return jsonify({'message': 'Tenant data not found'}), 404

# # # @app.route('/landlord-data', methods=['GET'])
# # # @landlord_required
# # # def get_landlord_data(user_id):
# # #     # Fetch landlord-specific data based on the user_id
# # #     landlord_data = Landlord.query.filter_by(user_id=user_id).first()
# # #     if landlord_data:
# # #         return jsonify(landlord_data.serialize()), 200
# # #     else:
# # #         return jsonify({'message': 'Landlord data not found'}), 404

# # # if __name__ == '__main__':
# # #     with app.app_context():
# # #         db.create_all()
# # #     app.run(port=5555, debug=True)


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from models.expense import Expense
# from models.staff import Staff
# from models.lease_agreement import LeaseAgreement
# from models.maintenance import MaintenanceRequest
# from models.payment import Payment
# from models.property import Property
# from models.tenant import Tenant
# from flask_migrate import Migrate
# from flask import Flask, request, jsonify, session
# from flask_bcrypt import Bcrypt
# from flask_cors import CORS
# from models.user import db, User
# from dotenv import load_dotenv
# load_dotenv()
# import os
# from sqlalchemy.exc import IntegrityError

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
# app.config['SECRET_KEY'] = 'micasa-suqasa'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True
# # app.json.compact = False
# app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True 

# migrate = Migrate(app, db)

# # Initialize extensions
# db.init_app(app)
# bcrypt = Bcrypt(app)
# CORS(app, supports_credentials=True)

# @app.route('/')
# def home():
#     return '<h1>Property management</h1>'

# @app.route('/properties', methods=['GET'])
# def get_properties():
#     properties = Property.query.all()
#     return jsonify([property.to_dict() for property in properties])



# @app.route("/signup", methods=["POST"])
# def signup():
#     email = request.json.get("email")
#     password = request.json.get("password")

#     if not email or not password:
#         return jsonify({"error": "Email and password are required"}), 400

#     user_exists = User.query.filter_by(email=email).first()

#     if user_exists:
#         return jsonify({"error": "Email already exists"}), 409

#     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
#     new_user = User(email=email, password=hashed_password)
#     db.session.add(new_user)
#     db.session.commit()

#     return jsonify({
#         "id": new_user.id,
#         "email": new_user.email
#     })

# @app.route("/login", methods=["POST"])
# def login_user():
#     email = request.json.get("email")
#     password = request.json.get("password")

#     if not email or not password:
#         return jsonify({"error": "Email and password are required"}), 400

#     user = User.query.filter_by(email=email).first()

#     if user is None:
#         return jsonify({"error": "User not found"}), 404

#     if not bcrypt.check_password_hash(user.password, password):
#         return jsonify({"error": "Incorrect password"}), 401

#     return jsonify({
#         "id": user.id,
#         "email": user.email
#     })

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(port=5555, debug=True)


# # from flask import Flask, request, jsonify
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_migrate import Migrate
# # from flask_bcrypt import Bcrypt
# # from flask_cors import CORS
# # from functools import wraps
# # from dotenv import load_dotenv
# # from models.user import db, User
# # from models.tenant import Tenant
# # from models.landlord import Landlord
# # from models.property import Property

# # import jwt
# # import os

# # # Load environment variables
# # load_dotenv()

# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
# # app.config['SECRET_KEY'] = 'micasa-suqasa'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.config['SQLALCHEMY_ECHO'] = True
# # app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# # # Initialize extensions
# # db.init_app(app)
# # bcrypt = Bcrypt(app)
# # CORS(app, supports_credentials=True)
# # migrate = Migrate(app, db)

# # # Decorator functions for authorization
# # def tenant_required(f):
# #     @wraps(f)
# #     def decorated(*args, **kwargs):
# #         token = request.headers.get('Authorization', '').split(" ")[1]

# #         try:
# #             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
# #             user_id = data['user_id']
# #             role = data['role']
# #             if role == 'tenant':
# #                 return f(user_id, *args, **kwargs)
# #             else:
# #                 return jsonify({'message': 'Unauthorized access'}), 403
# #         except jwt.ExpiredSignatureError:
# #             return jsonify({'message': 'Token has expired'}), 401
# #         except jwt.InvalidTokenError:
# #             return jsonify({'message': 'Invalid token'}), 401

# #     return decorated

# # def landlord_required(f):
# #     @wraps(f)
# #     def decorated(*args, **kwargs):
# #         token = request.headers.get('Authorization', '').split(" ")[1]

# #         try:
# #             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
# #             user_id = data['user_id']
# #             role = data['role']
# #             if role == 'landlord':
# #                 return f(user_id, *args, **kwargs)
# #             else:
# #                 return jsonify({'message': 'Unauthorized access'}), 403
# #         except jwt.ExpiredSignatureError:
# #             return jsonify({'message': 'Token has expired'}), 401
# #         except jwt.InvalidTokenError:
# #             return jsonify({'message': 'Invalid token'}), 401

# #     return decorated

# # # Routes
# # @app.route('/')
# # def home():
# #     return '<h1>Property management</h1>'

# # @app.route('/properties', methods=['GET'])
# # def get_properties():
# #     properties = Property.query.all()
# #     return jsonify([property.to_dict() for property in properties])

# # @app.route("/signup", methods=["POST"])
# # def signup():
# #     email = request.json.get("email")
# #     password = request.json.get("password")

# #     if not email or not password:
# #         return jsonify({"error": "Email and password are required"}), 400

# #     user_exists = User.query.filter_by(email=email).first()

# #     if user_exists:
# #         return jsonify({"error": "Email already exists"}), 409

# #     hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
# #     new_user = User(email=email, password=hashed_password)
# #     db.session.add(new_user)
# #     db.session.commit()

# #     return jsonify({
# #         "id": new_user.id,
# #         "email": new_user.email
# #     })

# # @app.route("/login", methods=["POST"])
# # def login_user():
# #     email = request.json.get("email")
# #     password = request.json.get("password")

# #     if not email or not password:
# #         return jsonify({"error": "Email and password are required"}), 400

# #     user = User.query.filter_by(email=email).first()

# #     if user is None:
# #         return jsonify({"error": "User not found"}), 404

# #     if not bcrypt.check_password_hash(user.password, password):
# #         return jsonify({"error": "Incorrect password"}), 401

# #     # Determine the user's role
# #     role = 'tenant' if isinstance(user, tenant) else 'landlord'

# #     # Generate JWT token with user ID and role
# #     token_payload = {
# #         'user_id': user.id,
# #         'role': role
# #     }
# #     token = jwt.encode(token_payload, app.config['SECRET_KEY'], algorithm='HS256')

# #     return jsonify({
# #         "id": user.id,
# #         "email": user.email,
# #         "token": token.decode('UTF-8')
# #     })

# # @app.route('/tenant-data', methods=['GET'])
# # @tenant_required
# # def get_tenant_data(user_id):
# #     # Fetch tenant-specific data based on the user_id
# #     tenant_data = Tenant.query.filter_by(user_id=user_id).first()
# #     if tenant_data:
# #         return jsonify(tenant_data.serialize()), 200
# #     else:
# #         return jsonify({'message': 'Tenant data not found'}), 404

# # @app.route('/landlord-data', methods=['GET'])
# # @landlord_required
# # def get_landlord_data(user_id):
# #     # Fetch landlord-specific data based on the user_id
# #     landlord_data = Landlord.query.filter_by(user_id=user_id).first()
# #     if landlord_data:
# #         return jsonify(landlord_data.serialize()), 200
# #     else:
# #         return jsonify({'message': 'Landlord data not found'}), 404

# # if __name__ == '__main__':
# #     with app.app_context():
# #         db.create_all()
# #     app.run(port=5555, debug=True)



from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from functools import wraps
from dotenv import load_dotenv
from models.user import db, User
# from models.dbmodels import db
from models.tenant import Tenant
from models.property import Property
from models.landlord import Landlord
from models.payment import Payment
from models.lease_agreement import LeaseAgreement
from models.maintenance import MaintenanceRequest
import jwt
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SECRET_KEY'] = 'micasa-suqasa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Initialize extensions
db.init_app(app)
bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)
migrate = Migrate(app, db)

# Decorator functions for authorization
def tenant_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').split(" ")[1]

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            user_id = data['user_id']
            role = data['role']
            if role == 'tenant':
                return f(user_id, *args, **kwargs)
            else:
                return jsonify({'message': 'Unauthorized access'}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

    return decorated

def landlord_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').split(" ")[1]

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            user_id = data['user_id']
            role = data['role']
            if role == 'landlord':
                return f(user_id, *args, **kwargs)
            else:
                return jsonify({'message': 'Unauthorized access'}), 403
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

    return decorated

# Routes
@app.route('/')
def home():
    return '<h1>Property management</h1>'

@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    return jsonify([property.to_dict() for property in properties])

@app.route("/signup", methods=["POST"])
def signup():
    email = request.json.get("email")
    password = request.json.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user_exists = User.query.filter_by(email=email).first()

    if user_exists:
        return jsonify({"error": "Email already exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "id": new_user.id,
        "email": new_user.email
    })

@app.route("/login", methods=["POST"])
def login_user():
    email = request.json.get("email")
    password = request.json.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error": "User not found"}), 404

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Incorrect password"}), 401

    # Determine the user's role
    role = 'tenant' if isinstance(user, Tenant) else 'landlord'

    # Generate JWT token with user ID and role
    token_payload = {
        'user_id': user.id,
        'role': role
    }
    token = jwt.encode(token_payload, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({
        "id": user.id,
        "email": user.email,
        "token": token.decode('UTF-8')
    })

@app.route('/tenant-data', methods=['GET'])
@tenant_required
def get_tenant_data(user_id):
    # Fetch tenant-specific data based on the user_id
    tenant_data = Tenant.query.filter_by(user_id=user_id).first()
    if tenant_data:
        return jsonify(tenant_data.serialize()), 200
    else:
        return jsonify({'message': 'Tenant data not found'}), 404

@app.route('/landlord-data', methods=['GET'])
@landlord_required
def get_landlord_data(user_id):
    # Fetch landlord-specific data based on the user_id
    landlord_data = Landlord.query.filter_by(user_id=user_id).first()
    if landlord_data:
        return jsonify(landlord_data.serialize()), 200
    else:
        return jsonify({'message': 'Landlord data not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
