from flask import Blueprint, make_response, request, jsonify
from flask_login import login_user

from app.models.user import User

login_bp = Blueprint('login_bp', __name__)

@login_bp.route('/login', methods=['POST'])
def login():
    from flask_bcrypt import Bcrypt
    bcrypt = Bcrypt()
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.get_by_email(email)

    if user and bcrypt.check_password_hash(user.password, password):
        login_user(user)
        res = make_response()
        res.set_cookie('session', user.get_session_token(), httponly=True, secure=True)
        return jsonify({"message": "Logged in successfully"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
    