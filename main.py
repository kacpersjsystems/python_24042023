from dotenv import load_dotenv
from flask import Flask, render_template
from os import getenv
import psycopg2
import requests

application = Flask(__name__)
load_dotenv()


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/hello/<first_name>')
def hello(first_name):
    # return f'Dzień dobry! Cześć {first_name.title()}!'

    return render_template('hello.html', first_name=first_name)


@application.route('/pogoda')
def weather():
    with requests.get('https://danepubliczne.imgw.pl/api/data/synop') as response:
        return render_template('weather.html', stations=response.json())


@application.route('/produkty')
def products():


        return render_template('products.html', products = cursor.fetchall())