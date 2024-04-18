from flask import Flask, request, make_response, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from models.dbmodels import db, Property, Landlord, Tenant, LeaseAgreement, MaintenanceRequest, Payment
from dotenv import load_dotenv
load_dotenv()
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Property management</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)