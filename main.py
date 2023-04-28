from dotenv import load_dotenv
from flask import Flask, render_template, abort
import requests

from dao import get_products, get_product_by_id

application = Flask(__name__)
load_dotenv()


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/hello/<first_name>')
def hello(first_name):
    # return f'Dzien dobry! Czesc {first_name}'
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
    product = get_product_by_id(product_id)
    if product is None:
        return abort(404)
    else:
        product_id, product_name, unit_price, units_in_stock, supplier_name, category_name = product
        return render_template('single_product.html', product={
            'product_id': product_id,
            'product_name': product_name,
            'unit_price': unit_price,
            'units_in_stock': units_in_stock,
            'supplier_name': supplier_name,
            'category_name': category_name,
        })


@application.route('/produkty/<int:product_id>/wydarzenia')
def create_event(product_id):
    return render_template('create_event.html', product_id=product_id)