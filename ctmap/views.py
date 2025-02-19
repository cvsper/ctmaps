from flask import Blueprint, render_template, url_for, redirect, request
import csv
from lists import searching

views = Blueprint(__name__, "views")

gas_file = 'gas.csv'
no_gas_file = 'no_gas.csv'
masscap = 'https://www.masscap.org/category/service-areas/'


@views.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'GET':
		return render_template('index.html')

	elif request.method == 'POST':
		city = request.form['city']
		tech = searching(city)
		return render_template('thankyou.html', tech=tech)

		
				




	