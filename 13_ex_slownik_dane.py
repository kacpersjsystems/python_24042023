# Wczytaj do słownika dane z pliku 13_ex_slownik_dane.txt tak by kluczem było imię sklejone z nazwiskiem
# rozdzielone spacja, a pozostałe dane znalazły się w wartości
# jako krotka lub lista. Przeiteruj po slowniku i wyswietl jego zawartość.

# { 'JanKowalski': { "wzost": 150, "waga": 49 }, "ZofiaNowak": [160,56] }

people = {}
with open('13_ex_slownik_dane', encoding='utf8') as file:
    for line in file:
        first_name, last_name, height, weight = line.strip().split(',')

        people[first_name + last_name] = [weight, height]
        #people[first_name + last_name] = {'weight': weight, 'height': height}

print(people)
# 14:44