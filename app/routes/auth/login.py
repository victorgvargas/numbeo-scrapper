from flask import Blueprint, request, jsonify
from flask_login import login_user

from app.models.user import User

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    from app import bcrypt
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.get_by_email(username)

    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        return jsonify({"message": "Logged in successfully"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
    