# Stwórz plik ustawienia.txt i umieść w nim poniższe dane
# encoding;utf-8
# timezone;-2
# color;black
# Następnie wczytaj dane do słownika w ten sposób by pierwsza kolumna stanowila klucze a
# druga przypisane do nich wartości. Przeiteruj po słowniku i wypisz klucze oraz przypisane
# do nich wartości
#
# { 'encoding': 'utf-8', 'timezone': '-2', 'color': 'black' }
#
# 1. Otwórz plik i wyświetl z niego wszystkie linie
# 2. Rozbij linie po średniu
# 3. Przypisz do osobnych zmiennych klucze, wartości (wewnątrz pętli)
# 4. Zdefiniuj pusty słownik nad pętlą
# 5. Wewnątrz pętli przypisz do słownika klucz i wartość o tak to_jest_slownik[to_jest_klucz]=to_jest_wartosc

with open('12_ex_file_to_dictionary.txt', encoding='utf8') as file:
    settings = {}
    for line in file:
        key, value = line.strip().split(';')
        settings[key] = value

    print(settings)

for key, value in settings.items():
    print(f'{key}: {value}')
