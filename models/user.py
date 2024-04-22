from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from .dbmodels import db

# def get_uuid():
#     return uuid4().hex

class User(db.Model):
    tablename = 'user'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable =False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True)
    user_type = db.Column(db.String(50))
    password = db.Column(db.Text, nullable=False)
        

   

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)