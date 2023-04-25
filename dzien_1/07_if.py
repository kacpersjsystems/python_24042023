# age = 19
#
# if age >= 18:
#     print('Jesteś dorosły!')
# else:
#     print('Według prawa jestes dzieckiem.')
#     wait_for_years = 18 - age
#     print(f'Musisz zaczekać jeszcze lat: {wait_for_years}.')
#
# print('Koniec programu.')

# Wartość < 10 premia wynosi 0.1
# Wartość >= 10 oraz wartość <= 15 0.2
# Wartość > 15 to premia wynosi     0.3

working_years = 12

# if working_years < 10:
#     bonus = 0.1
# else:
#     if working_years > 15:
#         bonus = 0.3
#     else:
#         bonus = 0.2

if working_years < 10:
    bonus = 0.1
elif working_years > 15:
    bonus = 0.3
else:
    bonus = 0.2

# and - koniunkcja - oraz
# zwraca prawdę jeżeli wszystkie wyrażenia są prawdziwe

# or  - alternatywa - lub
# zwraca prawdę jeżeli przynajmniej jedno wyrażenie jest prawdziwe

# Wartość < 10 premia wynosi 0.1
# Wartość >= 10 oraz wartość <= 15 0.2
# Wartość > 15 to premia wynosi     0.3

if working_years < 10:
    bonus = 0.1
# elif working_years >= 10 and working_years <= 15:
elif 10 <= working_years <= 15:
    bonus = 0.2
else:
    bonus = 0.3
