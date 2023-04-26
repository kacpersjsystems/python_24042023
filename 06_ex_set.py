# Wygeneruj dwa zestawy, dodaj do nich po 20 (w przypadku duplikatów lista może być
# mniejsza niż 20 elementów) losowych liczb z zakresu 1-40. Wyswietl ich sumę, różnicę i część
# wspólną
#
# 1. Stwórz dwie listy po 20 elementów z zakresu od 1 do 40
# 2. Zamień obie te listy na dwa zbiory
# 3. Wykonaj sumę(|), różnicę(-) i część wspólną (&)

from random import randint

set_a = set([randint(1, 40) for _ in range(20)])
set_b = set([randint(1, 40) for _ in range(20)])

print(set_a)
print(set_b)
print('--' * 30)
print(set_a | set_b)
print('--' * 30)
print(set_a - set_b)
print(set_b - set_a)
print('--' * 30)
print(set_a & set_b)