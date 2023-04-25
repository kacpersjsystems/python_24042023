# Wydrukuj liczby w zakresie 1-100 wypisujac obok czy dana liczba jest parzysta czy nieparzysta
# BONUS: skrócenie if'a do jednolinijkowej postaci

# for value in range(1, 101):
#     if value % 2 == 0:
#         print(value, 'jest parzysta')
#     else:
#         print(value, 'jest nieparzysta')
z = 1
for value in range(1, 101):
    print(z, value, 'jest parzysta' if value % 2 == 0 else 'jest nieparzysta')
    z = z + 1

# codewars.com


# for value in range(1, 101):
#     print(value, end=' ')
#     if value % 2 == 0:
#         print('jest parzysta')
#     else:
#         print('jest nieparzysta')
