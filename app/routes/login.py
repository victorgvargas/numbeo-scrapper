from flask import Blueprint, request, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from app import bcrypt

from app.models.user import User

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')

    user = User.create(username, email, password)

    if user:
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"message": "User already exists"}), 400

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.get_by_email(username)

    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Logged in successfully"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
    
@main.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200