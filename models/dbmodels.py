from flask_sqlalchemy import SQLAlchemy
from .user import db

# db = SQLAlchemy()

from models.property import Property
from models.landlord import Landlord
from models.tenant import Tenant
from models.lease_agreement import LeaseAgreement
from models.maintenance import MaintenanceRequest
from models.payment import Payment
