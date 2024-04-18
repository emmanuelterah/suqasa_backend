from flask import Flask, request, make_response, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from models.dbmodels import db, Property, Landlord, Tenant,  MaintenanceRequest, Payment

from dotenv import load_dotenv
load_dotenv()
import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# DATABASE = os.environ.get(
#     "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True 

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Property management</h1>'

@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    return jsonify([property.to_dict() for property in properties])


if __name__ == '__main__':
    app.run(port=5555, debug=True)