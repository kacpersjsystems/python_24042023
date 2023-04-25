# Napisz symulator splaty kredytu. Symulator ma przyjmowac przez zmienne:
# - kwotę kredytu
# - oprocentowanie w skali roku
# - wysokość spłacanej raty
# Symulator ma dla każdego miesiąca wypisać który to miesiąc i kwotę
# pozostala do splaty. Przy kazdym miesiacu doliczamy odsetki i odejmujemy
# ratę. Jeśli ostatnia rata jest wyższa niż pozostała do spłaty kwota,
# to zamiast odejmować całej raty należy wyzerować kwotę pozostałą.
# Na koniec działania programu wyświetl też ile w sumie zapłaciliśmy.

# 2%
# 1000
# 100
# 1. 1000 + 20 / 12
# 2. 920 + 920 * 2% / 12

# kwota kredytu: 10000,
# oprocentowanie 5 (5%)
# rata 500

# 14:44

total = 10000
borrowed = total
percentage = 0.05
amount = 500
month_number = 1
total_interest = 0
while total > 0:
    # wartość odsetek
    interest = total * percentage / 12
    total_interest += interest

    # całkowita wartość do spłaty wraz z odsetkami
    total += interest
    # jeżeli rata jest większa niż pozostała wartość kredytu to po prostu spłacam kredyt
    if total < amount:
        amount = total

    # odejmuję spłaconą ratę od kredytu
    total -= amount
    print(f'Miesiąc {month_number}, wartość odsetek {round(interest, 2)} pozostało do spłaty {round(total, 2)}')
    month_number += 1

print(f'Całkowity koszt kredytu {borrowed + total_interest}')