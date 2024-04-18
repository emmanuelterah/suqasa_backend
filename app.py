
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.expense import Expense
from models.staff import Staff
from models.lease_agreement import LeaseAgreement
from models.maintenance import MaintenanceRequest
from models.payment import Payment
from models.property import Property
from models.tenant import Tenant
from flask_migrate import Migrate
from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from models.user import db, User
from dotenv import load_dotenv
load_dotenv()
import os
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SECRET_KEY'] = 'micasa-suqasa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# app.json.compact = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True 

migrate = Migrate(app, db)

# Initialize extensions
db.init_app(app)
bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)

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

    return jsonify({
        "id": user.id,
        "email": user.email
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)


