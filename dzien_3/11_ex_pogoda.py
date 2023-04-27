# Korzystając z api dostarczonego przez
# imgw odpowiedz jaka jest temperatura, ciśnienie i wilgotność
# na Kasprowym Wierchu

# https://danepubliczne.imgw.pl/api/data/synop/

from requests import get

with get('https://danepubliczne.imgw.pl/api/data/synop/') as request:
    response = request.json()
    for row in response:
        if row['stacja'] == 'Kasprowy Wierch':
            print(row)

# API: metaweather, wolnelektury,