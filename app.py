from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import calc_income_minus_expenditure

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
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
