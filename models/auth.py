from flask import jsonify
import jwt
import datetime
import bcrypt

SECRET_KEY = 'your_secret_key'  # Change this to your desired secret key

users = []

def generate_token(username):
    token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
    return token.decode('UTF-8')

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def verify_password(hashed_password, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def login(username, password):
    for user in users:
        if user['username'] == username and verify_password(user['password'], password):
            return generate_token(username)
    return None

def signup(username, password):
    if any(user['username'] == username for user in users):
        return jsonify({'message': 'Username already exists!'}), 400

    hashed_password = hash_password(password)
    users.append({'username': username, 'password': hashed_password})
    return jsonify({'message': 'User registered successfully!'}), 201

def verify_token(token):
    try:
        data = jwt.decode(token, SECRET_KEY)
        return data['user']
    except:
        return None