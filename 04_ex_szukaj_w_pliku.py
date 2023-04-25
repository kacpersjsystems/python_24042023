# Napisz wyszukiwarkę plikową. Wyszukiwarka powinna odebrać od użytkownika
# poszukiwaną frazę, oraz nazwę pliku. Wyszukiwarka powinna wyświetlić
# linie w których znalazła poszukiwaną frazę wraz z numerem linii. Wyszukiwarka
# po odebraniu danych od uzyszkodnika powinna wyswietlic jakiej frazy
# i jakim pliku szuka. Wyszukiwarka powinna być nieczula na wielkosc liter.

# Podpowiedź: Porównuj linię pliku zamienioną na małe litery z poszukiwaną frazą
#             też zapisaną małymi literami




search_for = 'Python'
filename = '04_ex_szukaj_w_pliku.txt'

# 1. Otwórz plik o nazwie "04_ex_szukaj_w_pliku.txt" do odczytu
with open(filename, 'r', encoding='utf8') as file:
# 2. Przejść po tym pliku linia po linii i zamieniać linie na małe litery
    for line_number, line in enumerate(file, start=1):
# 3. Sprawdzać czy szukana wartość również zamieniona na małe litery znajduje się w tym pliku
        if search_for.lower() in line.lower():
# 4. Jeżeli wartość się znajduje to chcemy ją wyświetlić wraz z numerami linii
            print(line_number, line.strip())

print(f'Szukałem treści {search_for} wewnątrz pliku {filename}.')