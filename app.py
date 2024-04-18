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


app = Flask(__name__)
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
