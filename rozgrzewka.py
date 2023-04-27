# 1. Przygotuj  mały QUIZ z języka angielskiego, w słowniku mamy 10 wyrazów po polsku i po angielsku.
# Pytaj użytkownika o tłumaczenie kolejnych wyrazów i zliczaj ilość punktów jakie uzyskał jeśli poda
# poprawne tłumaczenie.
# * spróbuj sprawić by za każdym razem pytał o słowa w innej kolejności.

from random import shuffle
# pomysł ze zbiorem!
#
# dictionary = {
#     'pies': 'dog',
#     'kot': 'cat',
#     'drzewo': 'tree',
#     'samochód': 'car',
#     'wieża': 'tower',
#     'droga': 'road'
# }
# polish_words = set(dictionary.keys())
# # shuffle(polish_words)
#
# points = 0
# for polish_word in polish_words:
#     english_word = dictionary[polish_word]
#     answer = input(f'Jak po angielsku powiesz "{polish_word}"? ')
#     if answer == english_word:
#         points += 1
#
# print(f'Zdobywasz {points} punktów.')

# 2. Napisz program, ze zdefiniowaną trzy elementową listą zawierającą słowniki
# z informacjami o trzech krajach (nazwa kraju, stolica, język urzędowy).
# Następnie dodaj do słownika nowy kraj i wyświetl cały słownik po dodaniu
# nowego elementu.
#
# *Przejdź po słowniku za pomocą drugiej pętli for, zamiast robić dictionary[‘capital’]

countries = [
    {'name': 'Brazylia', 'capital': 'Brasilia', 'language': 'portugalski'},
    {'name': 'Norwegia', 'capital': 'Oslo', 'language': 'norweski'},
    {'name': 'Polska', 'capital': 'Warszawa', 'language': 'polski'}
]

countries.append({
    'name': 'Egipt',
    'capital': 'Kair',
    'language': 'arabski'
})

for country in countries:
    for key, value in country.items():
        print(key, value)

    print('---' * 10)


# 3. • z usługi sieciowej http://jsystems.pl/Universe/samaTabelka.do pobierz informację o
# szkoleniach. na konsoli wyswietl tytuly, miasta i daty wszystkich szkolen które w tytule mają
# malymi badz duzymi literami "Python" i status terminu gwarantowanego (pole
# terminyGwarantowany=1)
# * Możesz skorzystać z PrettyTable (pip install PrettyTable)

# aby zamienić string na listy i obiekty używamy     from json import loads
# aby zamienić listy i obiekty na string używamy     from json import dumps

from prettytable import PrettyTable
import requests


with requests.get('http://jsystems.pl/Universe/samaTabelka.do') as response:
    table = PrettyTable()
    table.field_names = ['Tytuł', 'Miasto', 'Termin']
    for training in response.json():
        # Fałszem jest - False, 0, '', None, []
        if training['terminyGwarantowany']:
            table.add_row([
                training['tytul_szkolenia'], training['miasto'], training['termin']
            ])

    print(table)

