from flask import Flask

application = Flask(__name__)


@application.route('/')
def index():
    return '<h1>Hello World</h1>'


@application.route('/hello/<first_name>')
def hello(first_name):
    return f'Dzień dobry! Cześć {first_name.title()}!'
