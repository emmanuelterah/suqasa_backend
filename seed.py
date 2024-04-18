from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.property import Property
from models.landlord import Landlord
from models.tenant import Tenant
from models.lease_agreement import LeaseAgreement
from models.maintenance import MaintenanceRequest
from models.payment import Payment
from datetime import datetime

# Create engine and session
# engine = create_engine('sqlite:///app.db')
# Session = sessionmaker(bind=engine)
# session = Session()

# # Seed data for landlords
# landlord1 = Landlord(Name="Derrick Ndinya", ContactInfo="derrick@example.com", BankAcctInfo="1234567890", Address="123 Main St")
# landlord2 = Landlord(Name="Immanuel Nyaanga", ContactInfo="immanuel@example.com", BankAcctInfo="1234567890", Address="124 Main St")
# landlord3 = Landlord(Name="Joseph", ContactInfo="joseph@example.com", BankAcctInfo="1234567890", Address="124 Main St")
# landlord4 = Landlord(Name="Mary", ContactInfo="mary@example.com", BankAcctInfo="1234567890", Address="124 Main St")
# landlord5 = Landlord(Name="Felo", ContactInfo="felo@example.com", BankAcctInfo="1234567890", Address="124 Main St")
# landlord6 = Landlord(Name="Ericko", ContactInfo="ericko@example.com", BankAcctInfo="1234567890", Address="124 Main St")
# landlord7 = Landlord(Name="Sharon", ContactInfo="sharon@example.com", BankAcctInfo="1234567890", Address="124 Main St")
# landlord8 = Landlord(Name="Nakumicha", ContactInfo="nakumicha@example.com", BankAcctInfo="1234567890", Address="124 Main St")
# landlord9 = Landlord(Name="Sakaja", ContactInfo="sakaja@example.com", BankAcctInfo="1234567890", Address="124 Main St")
# landlord10 = Landlord(Name="Sifuna", ContactInfo="sifuna@example.com", BankAcctInfo="1234567890", Address="124 Main St")
# session.add_all([landlord1, landlord2, landlord3, landlord4, landlord5, landlord6, landlord7, landlord8, landlord9, landlord10])


            
# # Seed data for properties
# property1 = Property(name="Apartment 101", address="456 Elm St", description="Cozy apartment in downtown", Bedrooms=2, image="/home/tyreek/Development/apartments/pexels-eye4dtail-129494.jpg", Size=800, RentAmount=8500, Status="Available", landlord=landlord1)
# property2 = Property(name="Apartment 102", address="45 Githurai", description="Studio apartment in downtown", Bedrooms=1, image="/home/tyreek/Development/apartments/Parliament-Tower.jpg", Size=200, RentAmount=7500, Status="Available", landlord=landlord2)
# property3 = Property(name="Apartment 103", address="125 Rongai", description="Three bedroom villa in downtown", Bedrooms=3, image="/home/tyreek/Development/apartments/digital-marketing-agency-ntwrk-g39p1kDjvSY-unsplash.jpg.jpg", Size=1000, RentAmount=50000, Status="Available", landlord=landlord3)
# property4 = Property(name="Apartment 104", address="8 kibera", description="apartment in uptown", Bedrooms=2, image="/home/tyreek/Development/apartments/GTC-Apartment.jpg", Size=800, RentAmount=30000, Status="Available", landlord=landlord10)
# property5 = Property(name="Apartment 105", address="12 Githunguri", description="Villa in uptown", Bedrooms=4, image="/home/tyreek/Development/apartments/dillon-kydd-2keCPb73aQY-unsplash.jpg", Size=1400, RentAmount=60000, Status="Available", landlord=landlord4)
# property6 = Property(name="Apartment 106", address="60 kilimani", description="Studio apartment in downtown", Bedrooms=3, image="/home/tyreek/Development/apartments/Britam-Tower.jpg", Size=1000, RentAmount=25000, Status="Available", landlord=landlord5)
# property7 = Property(name="Apartment 107", address="98 Gigiri ", description="cozy apartment in downtown", Bedrooms=3, image="/home/tyreek/Development/apartments/k8-9brIbLCo950-unsplash.jpg", Size=1000, RentAmount=35000, Status="Available", landlord=landlord6)
# property8 = Property(name="Apartment 108", address="134 karen", description="Houses in downtown", Bedrooms=4, image="/home/tyreek/Development/apartments/john-fornander-y3_AHHrxUBY-unsplash.jpg", Size=1400, RentAmount=70000, Status="Available", landlord=landlord7)
# property9 = Property(name="Apartment 109", address="150 kitengela", description="cozy apartment in downtown", Bedrooms=1, image="/home/tyreek/Development/apartments/saru-robert-9rP3mxf8qWI-unsplash.jpg", Size=200, RentAmount=20000, Status="Available", landlord=landlord8)
# property10 = Property(name="Apartment 1010", address="16 imara Daima", description="Cozy apartment in downtown", Bedrooms=2, image="/home/tyreek/Development/apartments/jason-grant-SZ0Rwvu3MX0-unsplash.jpg", Size=800, RentAmount=25000, Status="Available", landlord=landlord9)
# session.add_all([property1, property2, property3, property4, property5, property6, property7, property8, property9, property10])

# # Seed data for tenants
# tenant1 = Tenant(Name="Alice Smith", ContactInfo="alice.smith@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Bob Smith")
# tenant2 = Tenant(Name="Jonte", ContactInfo="jonte@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Kevo")
# tenant3 = Tenant(Name="Efjeniah", ContactInfo="efjeniah@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Kevo")
# tenant4 = Tenant(Name="Enoch", ContactInfo="enoch@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Kevo")
# tenant5 = Tenant(Name="Edith", ContactInfo="edith@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Kevo")
# tenant6 = Tenant(Name="Davies", ContactInfo="davies@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Kevo")
# session.add(tenant1, tenant2 )
# session.add(tenant3, tenant4 )
# session.add(tenant5, tenant6 )

# # Seed data for lease agreements
# lease1 = LeaseAgreement(PropertyID=1, TenantID=1, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
# lease2 = LeaseAgreement(PropertyID=2, TenantID=2, StartDate=datetime(2024, 2, 1), EndDate=datetime(2025, 2, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
# lease3 = LeaseAgreement(PropertyID=3, TenantID=3, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
# lease4 = LeaseAgreement(PropertyID=4, TenantID=4, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
# lease5 = LeaseAgreement(PropertyID=5, TenantID=5, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
# lease6 = LeaseAgreement(PropertyID=6, TenantID=6, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
# session.add(lease1, lease2 )
# session.add(lease3, lease4 )
# session.add(lease5, lease6 )

# # Seed data for payments
# payment1 = Payment(LeaseID=1, TenantID=1, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Credit Card", PaymentStatus="Paid")
# payment2 = Payment(LeaseID=2, TenantID=2, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Credit Card", PaymentStatus="Paid")
# payment3 = Payment(LeaseID=3, TenantID=3, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Mpesa", PaymentStatus="Paid")
# payment4 = Payment(LeaseID=4, TenantID=4, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Cash", PaymentStatus="Paid")
# payment5 = Payment(LeaseID=5, TenantID=5, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Mpesa", PaymentStatus="Paid")
# payment6 = Payment(LeaseID=6, TenantID=6, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Mpesa", PaymentStatus="Paid")
# session.add(payment1, payment2 )
# session.add(payment3, payment4 )
# session.add(payment5, payment6 )

# # Seed data for maintenance requests
# request1 = MaintenanceRequest(PropertyID=1, Description="Leaky faucet", RequestDate=datetime(2024, 4, 1), RequestedBy="Alice Smith", Status="Pending")
# request2 = MaintenanceRequest(PropertyID=2, Description="paint", RequestDate=datetime(2024, 4, 1), RequestedBy="Immanuel Nyaanga", Status="Pending")
# request3 = MaintenanceRequest(PropertyID=3, Description="Broken windows", RequestDate=datetime(2024, 4, 1), RequestedBy="Efjeniah Ssaru", Status="Pending")
# request4 = MaintenanceRequest(PropertyID=4, Description="Broken door", RequestDate=datetime(2024, 4, 1), RequestedBy="Enoch Kibet", Status="Pending")
# request5 = MaintenanceRequest(PropertyID=5, Description="Power shortage", RequestDate=datetime(2024, 4, 1), RequestedBy="Edith Chelangat", Status="Pending")
# request6 = MaintenanceRequest(PropertyID=6, Description="Internet shortage", RequestDate=datetime(2024, 4, 1), RequestedBy="Davis Clement", Status="Done")
# session.add(request1, request2 )
# session.add(request3, request4 )
# session.add(request5, request6 )

# # Commit changes and close session
# session.commit()
# session.close()

# Create engine and session
engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

# Delete existing data
session.query(MaintenanceRequest).delete()
session.query(LeaseAgreement).delete()
session.query(Payment).delete()
session.query(Tenant).delete()
session.query(Property).delete()
session.query(Landlord).delete()

# Seed data for landlords
landlord1 = Landlord(Name="Derrick Ndinya", ContactInfo="derrick@example.com", BankAcctInfo="1234567890", Address="123 Main St")
landlord2 = Landlord(Name="Immanuel Nyaanga", ContactInfo="immanuel@example.com", BankAcctInfo="1234567890", Address="124 Main St")
landlord3 = Landlord(Name="Joseph", ContactInfo="joseph@example.com", BankAcctInfo="1234567890", Address="124 Main St")
landlord4 = Landlord(Name="Mary", ContactInfo="mary@example.com", BankAcctInfo="1234567890", Address="124 Main St")
landlord5 = Landlord(Name="Felo", ContactInfo="felo@example.com", BankAcctInfo="1234567890", Address="124 Main St")
landlord6 = Landlord(Name="Ericko", ContactInfo="ericko@example.com", BankAcctInfo="1234567890", Address="124 Main St")
landlord7 = Landlord(Name="Sharon", ContactInfo="sharon@example.com", BankAcctInfo="1234567890", Address="124 Main St")
landlord8 = Landlord(Name="Nakumicha", ContactInfo="nakumicha@example.com", BankAcctInfo="1234567890", Address="124 Main St")
landlord9 = Landlord(Name="Sakaja", ContactInfo="sakaja@example.com", BankAcctInfo="1234567890", Address="124 Main St")
landlord10 = Landlord(Name="Sifuna", ContactInfo="sifuna@example.com", BankAcctInfo="1234567890", Address="124 Main St")

# Add landlords to the session
session.add_all([landlord1, landlord2, landlord3, landlord4, landlord5, landlord6, landlord7, landlord8, landlord9, landlord10])

# Commit changes
session.commit()

# Seed data for properties
property1 = Property(name="Apartment 101", address="456 Elm St", description="Cozy apartment in downtown", Bedrooms=2, image="/home/tyreek/Development/apartments/pexels-eye4dtail-129494.jpg", Size=800, RentAmount=8500, Status="Available", landlord=landlord1)
property2 = Property(name="Apartment 102", address="45 Githurai", description="Studio apartment in downtown", Bedrooms=1, image="/home/tyreek/Development/apartments/Parliament-Tower.jpg", Size=200, RentAmount=7500, Status="Available", landlord=landlord2)
property3 = Property(name="Apartment 103", address="125 Rongai", description="Three bedroom villa in downtown", Bedrooms=3, image="/home/tyreek/Development/apartments/digital-marketing-agency-ntwrk-g39p1kDjvSY-unsplash.jpg.jpg", Size=1000, RentAmount=50000, Status="Available", landlord=landlord3)
property4 = Property(name="Apartment 104", address="8 kibera", description="apartment in uptown", Bedrooms=2, image="/home/tyreek/Development/apartments/GTC-Apartment.jpg", Size=800, RentAmount=30000, Status="Available", landlord=landlord2)
property5 = Property(name="Apartment 105", address="12 Githunguri", description="Villa in uptown", Bedrooms=4, image="/home/tyreek/Development/apartments/dillon-kydd-2keCPb73aQY-unsplash.jpg", Size=1400, RentAmount=60000, Status="Available", landlord=landlord4)
property6 = Property(name="Apartment 106", address="60 kilimani", description="Studio apartment in downtown", Bedrooms=3, image="/home/tyreek/Development/apartments/Britam-Tower.jpg", Size=1000, RentAmount=25000, Status="Available", landlord=landlord5)
property7 = Property(name="Apartment 107", address="98 Gigiri ", description="cozy apartment in downtown", Bedrooms=3, image="/home/tyreek/Development/apartments/k8-9brIbLCo950-unsplash.jpg", Size=1000, RentAmount=35000, Status="Available", landlord=landlord6)
property8 = Property(name="Apartment 108", address="134 karen", description="Houses in downtown", Bedrooms=4, image="/home/tyreek/Development/apartments/john-fornander-y3_AHHrxUBY-unsplash.jpg", Size=1400, RentAmount=70000, Status="Available", landlord=landlord7)
property9 = Property(name="Apartment 109", address="150 kitengela", description="cozy apartment in downtown", Bedrooms=1, image="/home/tyreek/Development/apartments/saru-robert-9rP3mxf8qWI-unsplash.jpg", Size=200, RentAmount=20000, Status="Available", landlord=landlord8)
property10 = Property(name="Apartment 1010", address="16 imara Daima", description="Cozy apartment in downtown", Bedrooms=2, image="/home/tyreek/Development/apartments/jason-grant-SZ0Rwvu3MX0-unsplash.jpg", Size=800, RentAmount=25000, Status="Available", landlord=landlord9)

# Add properties to the session
session.add_all([property1, property2, property3, property4, property5, property6, property7, property8, property9, property10])

# Commit changes
session.commit()

# Seed data for tenants
tenant1 = Tenant(Name="Alice Smith", ContactInfo="alice.smith@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Bob Smith")
tenant2 = Tenant(Name="Jonte", ContactInfo="jonte@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Kevo")
tenant3 = Tenant(Name="Efjeniah", ContactInfo="efjeniah@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Kevo")
tenant4 = Tenant(Name="Enoch", ContactInfo="enoch@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Kevo")
tenant5 = Tenant(Name="Edith", ContactInfo="edith@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Kevo")
tenant6 = Tenant(Name="Davies", ContactInfo="davies@example.com", Occupation="Software Engineer", CurrentAddr="789 Oak St", PrevAddr="321 Maple St", EmergencyCnt="Kevo")

# Add tenants to the session
session.add_all([tenant1, tenant2, tenant3, tenant4, tenant5, tenant6])

# Commit changes
session.commit()

# Seed data for lease agreements
lease1 = LeaseAgreement(PropertyID=1, TenantID=1, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
lease2 = LeaseAgreement(PropertyID=2, TenantID=2, StartDate=datetime(2024, 2, 1), EndDate=datetime(2025, 2, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
lease3 = LeaseAgreement(PropertyID=3, TenantID=3, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
lease4 = LeaseAgreement(PropertyID=4, TenantID=4, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
lease5 = LeaseAgreement(PropertyID=5, TenantID=5, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)
lease6 = LeaseAgreement(PropertyID=6, TenantID=6, StartDate=datetime(2024, 1, 1), EndDate=datetime(2025, 1, 1), RentAmount=1500, PaymentSchedule="Monthly", DepositAmount=1500)

# Add lease agreements to the session
session.add_all([lease1, lease2, lease3, lease4, lease5, lease6])

# Commit changes
session.commit()

# Seed data for payments
payment1 = Payment(LeaseID=1, TenantID=1, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Credit Card", PaymentStatus="Paid")
payment2 = Payment(LeaseID=2, TenantID=2, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Credit Card", PaymentStatus="Paid")
payment3 = Payment(LeaseID=3, TenantID=3, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Mpesa", PaymentStatus="Paid")
payment4 = Payment(LeaseID=4, TenantID=4, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Cash", PaymentStatus="Paid")
payment5 = Payment(LeaseID=5, TenantID=5, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Mpesa", PaymentStatus="Paid")
payment6 = Payment(LeaseID=6, TenantID=6, PaymentDate=datetime(2024, 1, 1), PaymentAmount=1500, PaymentMethod="Mpesa", PaymentStatus="Paid")

# Add payments to the session
session.add_all([payment1, payment2, payment3, payment4, payment5, payment6])

# Commit changes
session.commit()

# Seed data for maintenance requests
request1 = MaintenanceRequest(PropertyID=1, Description="Leaky faucet", RequestDate=datetime(2024, 4, 1), RequestedBy="Alice Smith", Status="Pending")
request2 = MaintenanceRequest(PropertyID=2, Description="paint", RequestDate=datetime(2024, 4, 1), RequestedBy="Immanuel Nyaanga", Status="Pending")
request3 = MaintenanceRequest(PropertyID=3, Description="Broken windows", RequestDate=datetime(2024, 4, 1), RequestedBy="Efjeniah Ssaru", Status="Pending")
request4 = MaintenanceRequest(PropertyID=4, Description="Broken door", RequestDate=datetime(2024, 4, 1), RequestedBy="Enoch Kibet", Status="Pending")
request5 = MaintenanceRequest(PropertyID=5, Description="Power shortage", RequestDate=datetime(2024, 4, 1), RequestedBy="Edith Chelangat", Status="Pending")
request6 = MaintenanceRequest(PropertyID=6, Description="Internet shortage", RequestDate=datetime(2024, 4, 1), RequestedBy="Davis Clement", Status="Done")


# Add maintenance requests to the session
session.add_all([request1, request2, request3, request4, request5, request6])

# Commit changes
session.commit()

# Close session
session.close()