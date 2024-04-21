from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# from dbmodels import db
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    description = db.Column(db.Text)
    amount = db.Column(db.Float)
    expense_date = db.Column(db.Date)
    expense_type = db.Column(db.String(50))