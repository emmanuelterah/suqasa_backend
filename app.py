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
from flask import Flask
from models.routes import routes


app = Flask(__name__)
app.register_blueprint(routes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
Migrate(app, db)
# Define your routes and other application logic here

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# from flask import Flask
# from models.dbmodels import db
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# db.init_app(app)

# # Import your models to create tables
# # import models.dbmodels



# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
from flask import Flask, request, make_response, jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from models.dbmodels import db, Property, Landlord, Tenant, LeaseAgreement, MaintenanceRequest, Payment
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