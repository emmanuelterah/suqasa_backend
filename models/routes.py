from flask import Blueprint, request, jsonify
from auth import login, signup, verify_token

routes = Blueprint('routes', __name__)

@routes.route('/login', methods=['POST'])
def user_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')  # Add role parameter

    token = login(username, password, role)  # Pass role to the login function
    if token:
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid username, password, or role'}), 401

@routes.route('/signup', methods=['POST'])
def user_signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')  # Add role parameter

    return signup(username, password, role)  # Pass role to the signup function

@routes.route('/protected', methods=['GET'])
def protected_route():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'message': 'Token is missing!'}), 401

    username = verify_token(token)
    if not username:
        return jsonify({'message': 'Token is invalid!'}), 401

    return jsonify({'message': 'You are authenticated!'})
