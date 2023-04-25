# a. Napisz program który z pliku dane.txt wyświetli
# powiekszone imiona i nazwiska oraz wzrost i masę

# b. Użyj listy składanej i z linii pliku stwórz listę zawierającą listy.
#    data = [
#       ['Jan', 'Kowalski', 150, 49]
#       ['Zofia','Nowak', 160, 56 ]
#    ]

with open('17_csv_plik.txt', encoding='utf8') as file:
    # a.
    # for line in file:
    #     #              Jan,Kowalski,150,49 \n
    #     # .strip()     Jan,Kowalski,150,49
    #     # .split(',')  ['Jan', 'Kowalski', 150, 49]
    #     first_name, last_name, height, weight = line.strip().split(',')
    #     print(first_name.upper(), last_name.upper(), height, weight)
    # b.
    # data = []
    # for line in file:
    #     data.append(line.strip().split(','))

    data = [[int(element) if element.isnumeric() else element for element in line.strip().split(',')] for line in file]


# row = ['Jan', 'Kowalski', '150', '49']
# new_row = [int(element) if element.isnumeric() else element for element in row]


