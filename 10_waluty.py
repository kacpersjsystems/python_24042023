# urllib - wbudowana biblioteka w Pythona
# requests - trzeba doinstalować

from requests import get

URL = 'http://api.nbp.pl/api/exchangerates/tables/A/'
FILTERS = ['EUR', 'USD', 'NOK']

with get(URL) as request:
    response = request.json()
    for rate in response[0]['rates']:
        if rate['code'] in FILTERS:
            print(rate['currency'], rate['mid'])

