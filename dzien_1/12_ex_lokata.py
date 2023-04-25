# Napisz symulator lokaty. Symulator ma przyjmować przez zmienne:
# - kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakladamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc
# oraz ile mamy aktualnie zgromadzone na koncie po doliczeniu odsetek.
# Kapitalizacja comiesięczna

# Lokata -> 1000 na 10 miesięcy i 0.1 (to jest 10%)
# 1. 1000 + 0.1 * 1000 / 12
# 2. wartość z miesiąca 1 + 0.1 * wartość z miesiąca1 / 12
# 3. wartość z miesiąca 2 + 0.1 * wartość z miesiąca2 / 12
# ...

amount = int(input('Podaj wartość lokaty: '))
percent_per_year = float(input('Oprocentowanie w skali roku: '))
number_of_months = int(input('Ilość miesięcy: '))

for number_of_month in range(1, number_of_months + 1):
    # amount = amount + percent_per_year * amount / 12
    amount += percent_per_year * amount / 12
    print(f'Miesiąc {number_of_month}, Wartość: {amount:.2f}')

# 12:48 -> 13:20
#
# from math import pi
#
# print(round(pi))
# print(round(pi, 2))
#
# print(f'Liczba pi zaokr. do 2 miejsc to {pi:.2f}')
# print(f'Liczba pi zaokr. do 2 miejsc to {pi:.3f}')
