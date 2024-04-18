from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.dbmodels import Property, Landlord, Tenant, LeaseAgreement, Payment, MaintenanceRequest
from datetime import datetime

# Create engine and session
engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

# Seed data for landlords
landlord1 = Landlord(Name="John Doe", ContactInfo="john.doe@example.com", BankAcctInfo="1234567890", Address="123 Main St")
session.add(landlord1)

# Seed data for properties
property1 = Property(name="Apartment 101", address="456 Elm St", description="Cozy apartment in downtown", Bedrooms=2, image="/home/tyreek/Development/apartments/pexels-eye4dtail-129494.jpg", Size=800, RentAmount=1500, Status="Available", landlord=landlord1)
session.add(property1)

# Seed data for tenants
tenant1 = Tenant(Name="Alice Smith", ContactInfo="alice.smith@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Bob Smith")
session.add(tenant1)

# Seed data for lease agreements
lease1 = LeaseAgreement(PropertyID=1, TenantID=1, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
session.add(lease1)

# Seed data for payments
payment1 = Payment(LeaseID=1, TenantID=1, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Credit Card", PaymentStatus="Paid")
session.add(payment1)

# Seed data for maintenance requests
request1 = MaintenanceRequest(PropertyID=1, Description="Leaky faucet", RequestDate=datetime(2024, 4, 1), RequestedBy="Alice Smith", Status="Pending")
session.add(request1)

# Commit changes and close session
session.commit()
session.close()