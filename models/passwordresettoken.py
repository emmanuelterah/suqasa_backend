from .dbmodels import db

class PasswordResetToken(db.Model):
    __tablename__ ='password_reset_token'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    token = db.Column(db.String(100), nullable=False)
    expiration = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', backref='reset_tokens', primaryjoin="User.id == foreign(PasswordResetToken.user_id)")