from flask import Flask
from models.dbmodels import db
from models.property import Property
from models.landlord import Landlord
from models.lease_agreement import LeaseAgreement
from models.maintenance import MaintenanceRequest
from models.payment import Payment
from models.tenant import Tenant
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://suqasa_backend_user:YUKcTzli9ZIfBwDpgdss7KH9FzmxMr8K@dpg-coifn7779t8c738g18ag-a.oregon-postgres.render.com/suqasa_backend?sslmode=require&sslrootcert=path/to/render_ssl_cert.pem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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


