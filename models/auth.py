from flask import jsonify
import jwt
import datetime

SECRET_KEY = 'your_secret_key'  # Change this to your desired secret key

users = []

def generate_token(username):
    token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
    return token.decode('UTF-8')

def login(username, password):
    if username == 'username' and password == 'password':
        return generate_token(username)
    return None

def signup(username, password):
    if any(user['username'] == username for user in users):
        return jsonify({'message': 'Username already exists!'}), 400

    users.append({'username': username, 'password': password})
    return jsonify({'message': 'User registered successfully!'}), 201

def verify_token(token):
    try:
        data = jwt.decode(token, SECRET_KEY)
        return data['user']
    except:
        return None
