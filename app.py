# # # from flask import Flask
# # # from flask_sqlalchemy import SQLAlchemy
# # # from models.dbmodels import db


# # # app = Flask(__name__)
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Adjust as per your database setup
# # # db = SQLAlchemy(app)

# # from models.expense import Expense
# # from models.staff import Staff
# # from models.lease_agreement import LeaseAgreement
# # from models.maintenance import MaintenanceRequest
# # from models.payment import Payment
# # from models.property import Property
# # from models.tenant import Tenant
# # from models.dbmodels import db

# # # # Define routes and other application 

# # # if __name__ == '__main__':
# # #     # Create the database tables
# # #     db.create_all()
# # #     app.run(debug=True)



# # from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from models.dbmodels import db

# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# # db = SQLAlchemy(app)

# # # Define your routes and other application logic here

# # if __name__ == '__main__':
# #     with app.app_context():
# #         db.create_all()
# #     app.run(debug=True)


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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'micasa-suqasa'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Initialize extensions
db.init_app(app)
bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)

@app.route("/")
def hello_world():
    return "Hello, World!"

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
    app.run(debug=True)

