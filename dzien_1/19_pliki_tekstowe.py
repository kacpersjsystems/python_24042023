# Umieść napis "Hello World" w pliku o nazwie "hello_world.txt"
#
# a - append, dodajemy nową treść do pliku
# w - write, usuwamy całą wartość pliku i dodajemy do niego nową treść
# r - read, odczyt pliku
# Znak końca pliku \n

# Opcja 1 open i close
file = open('hello_world.txt', 'w')
file.write('Hello World\n')
file.write('Hello\n')
file.write('World\n')
file.close()

# Open 2 Context Manager
with open('hello_world.txt', 'a') as file:
    file.write('hello World\n')
    file.write('hello\n')
    file.write('World\n')

# with open('hello_world.txt', 'r') as file:
#     for line in file:
# Wszystkie litery zapisane jako wielkie
# print(line.strip().upper())

# Wszystkie litery zapisane jako małe
# print(line.strip().lower())

# Każda pierwsza litera słowa jest wielka
# print(line.strip().title())

# odwołanie do konkretnej linii tekstu
with open('hello_world.txt', 'r') as file:
    # Cała zawartość pliku ląduje w pamięci
    lines = file.readlines()
    # w nawiasach kwadratowych wskazuje konkretne indeksy
    # interesujących mnie linii. Indeksy numerowane są od 0
    # natomiast jeżeli chcę pobierać wartości od końca to mogę
    # używać indeksów ujemnych.
    print(lines[0].strip().replace('World', 'Kacper'))
    #print(lines[-1].strip())



