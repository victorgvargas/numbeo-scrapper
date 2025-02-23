from flask import Blueprint, request, jsonify
from app.models.budget import Budget

budget_bp = Blueprint('budget_bp', __name__)

@budget_bp.route('/', methods=['POST'])
def create_budget():
    data = request.json
    Budget.create(data['user_id'], data['income'], data['net_budget'], data['currency'], data['region'], data['family_size'], data['city'])
    return jsonify({"message": "Budget created successfully"}), 201

@budget_bp.route('/<int:user_id>', methods=['GET'])
def get_budget(user_id):
    budgets = Budget.get(user_id)
    return jsonify(budgets)

@budget_bp.route('/all', methods=['GET'])
def get_all_budgets():
    budgets = Budget.get_all()
    return jsonify(budgets)

@budget_bp.route('/<int:id>', methods=['PUT'])
def update_budget(id):
    data = request.json
    Budget.update(id, data['user_id'], data['income'], data['net_budget'], data['currency'], data['region'], data['family_size'], data['city'])
    return jsonify({"message": "Budget updated successfully"})

@budget_bp.route('/<int:id>', methods=['DELETE'])
def delete_budget(id):
    user_id = request.json['user_id']
    Budget.delete(id, user_id)
    return jsonify({"message": "Budget deleted successfully"})