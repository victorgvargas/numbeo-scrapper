from flask import Flask, request, jsonify
from utils import calc_income_minus_expenditure

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_income_data():
    city = request.args.get('city')
    income = float(request.args.get('income'))
    city_centre = request.args.get('city_centre') == 'true'
    outskirts = request.args.get('outskirts') == 'true'

    result = calc_income_minus_expenditure(city, income, {"city_centre": city_centre, "outskirts": outskirts})
    
    return jsonify({"result": result})