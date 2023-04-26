from datetime import datetime, timedelta

day = input('Podaj datę w formacie (d.m.Y): ')
# strFtime -> formatujemy obiekt daty do postaci stringa
# strPtime -> parsujemy datę, ze stringa do obiektu daty
# date.today() -> zwraca bieżącą datę
# datetime.now() -> zwraca bieżącą datę i godzinę

# To jest data dzisiejsza
today = datetime.now()
# To jest data jutrzejsza
tomorrow = datetime.now() + timedelta(days=1)
# To jest data wczorajsza
yesterday = datetime.now() - timedelta(days=1)
print(yesterday)
yesterday = datetime.now() + timedelta(days=-1)
print(yesterday)

day = datetime.strptime(day, '%d.%m.%Y')
# print(day, type(day))

if today > day:
    print('Ale to już było...')
else:
    print('Kiedyś ten dzień nadejdzie :-)')