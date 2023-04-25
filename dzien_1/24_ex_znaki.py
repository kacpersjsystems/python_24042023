number_of_lines = 0
number_of_small_letters = 0
number_of_capital_letters = 0
number_of_spaces = 0

with open('24_ex_znaki.txt', 'r', encoding='utf8') as file:
    for line in file:
        number_of_lines += 1
        for char in line:
            if char.islower():
                number_of_small_letters += 1

            if char.isupper():
                number_of_capital_letters += 1

            if char.isspace():
                number_of_spaces += 1

print(f'''Ilość linii {number_of_lines}
Ilość małych liter: {number_of_small_letters}
Ilość wielkich liter: {number_of_capital_letters}
Ilość spacji: {number_of_spaces}
''')

