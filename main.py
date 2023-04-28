from dotenv import load_dotenv
from flask import Flask, render_template
import requests

from dao import get_products, get_product_by_id

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
    return render_template('products.html', products=get_products())


@application.route('/produkty/<int:product_id>')
def single_product(product_id: int):
    return render_template('single_product.html', product=get_product_by_id(product_id))
