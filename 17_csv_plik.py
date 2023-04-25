# Napisz program który z pliku dane.txt wyświetli
# powiekszone imiona i nazwiska oraz wzrost i masę

# Otwórz plik do odczytu
# Przejdź po pliku linia po linii
# Każdą linię rozbij na podstawie ,
# Każdy element przypisz do osobnej zmiennej
# Imię i nazwisko zamień na wielkie litery
# Wszystkie informacje wyświetl na ekranie (każdą osobę w jednym wierszu)

with open('17_csv_plik.txt', encoding='utf8') as file:
    for line in file:
        #              Jan,Kowalski,150,49 \n
        # .strip()     Jan,Kowalski,150,49
        # .split(',')  ['Jan', 'Kowalski', 150, 49]
        first_name, last_name, height, weight = line.strip().split(',')
        print(first_name.upper(), last_name.upper(), height, weight)