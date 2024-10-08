from flask import Blueprint, request, jsonify

from app.models.user import User

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register', methods=['POST'])
def register():
    from app import bcrypt
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')

    user = User.create(username, email, password)

    if user:
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"message": "User already exists"}), 400