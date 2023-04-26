# Kamil Stoch - urodzony 25 maja 1987 roku.
# Dawid Kubacki - urodzony 12 marca 1990 roku.
# Piotr Żyła - urodzony 16 czerwca 1987 roku.

from datetime import date
from math import floor

people = [
    {
        'first_name': 'Kamil',
        'last_name': 'Stoch',
        'birth_date': date(1987, 5, 25)
    }, {
        'first_name': 'Dawid',
        'last_name': 'Kubacki',
        'birth_date': date(1990, 3, 12)
    }, {
        'first_name': 'Piotr',
        'last_name': 'Żyła',
        'birth_date': date(1987, 6, 16)
    }
]

today = date.today()

for person in people:
    print(f"Imię: {person.get('first_name')}")
    print(f"Nazwisko: {person.get('last_name')}")

    birth_date = person.get('birth_date')
    difference = today - birth_date
    age = floor(difference.days / 365)
    print(f"Data urodzenia: {birth_date.strftime('%d.%m.%Y')}r.")
    print(f'Wiek: {age}')
    print('---' * 10)

# 13:03