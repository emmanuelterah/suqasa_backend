from flask import Flask
from models.dbmodels import db
from models.property import Property
from models.landlord import Landlord
from models.lease_agreement import LeaseAgreement
from models.maintenance import MaintenanceRequest
from models.payment import Payment
from models.tenant import Tenant
from flask_migrate import Migrate
from dotenv import load_dotenv
load_dotenv()
import os 

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

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
