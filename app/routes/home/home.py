from flask import Blueprint, request, jsonify
from app.utils import calc_income_minus_expenditure, calc_costs


home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=['GET'])
def get_income_data():
    city = request.args.get('city')
    income = float(request.args.get('income'))
    currency = request.args.get('currency')
    city_centre = request.args.get('city_centre') == 'true'
    outskirts = request.args.get('outskirts') == 'true'
    three_bedroom_outskirts = request.args.get(
        'three_bedroom_outskirts') == 'true'
    three_bedroom_city_centre = request.args.get(
        'three_bedroom_city_centre') == 'true'

    result = calc_income_minus_expenditure(city, income, {"city_centre": city_centre, "outskirts": outskirts,
                                           "three_bedroom_city_centre": three_bedroom_city_centre, 
                                           "three_bedroom_outskirts": three_bedroom_outskirts,
                                           "currency": currency})

    return jsonify({"result": result})

@home_bp.route('/costs', methods=['GET'])
def get_costs():
    city = request.args.get('city')
    currency = request.args.get('currency')

    result = calc_costs(city, {"currency": currency})

    return jsonify(result)