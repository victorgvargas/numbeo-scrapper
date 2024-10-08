from flask import Blueprint, jsonify
from flask_login import login_required, logout_user

logout_bp = Blueprint('logout_bp', __name__)

@logout_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200