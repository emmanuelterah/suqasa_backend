
from app import app
from models.dbmodels import db, Property, Landlord, Tenant, LeaseAgreement, MaintenanceRequest, Payment

if __name__ == '__main__':
    with app.app_context():
        import ipdb; ipdb.set_trace()