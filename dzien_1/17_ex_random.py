# Napisz program który będzie dodawał kolejne losowe wartości z zakresu
# od 1 do 10 do zmiennej suma, tak dlugo az suma nie osiagnie wartosci
# wiekszej od wartosci podanej przez uzytkownik

# from random import randint
# randint()

import random


maximum = int(input('Podaj wartość maksymalną: '))
total = 0

while total <= maximum:
    value = random.randint(1, 10)
    print(value)
    total += value

print(f'Koniec programu, total wynosi {total}')