cities_a = {'Gdynia', 'Warszawa', 'Zabrze'}
cities_b = set(['Warszawa', 'Kraków', 'Gniezno'])

print('Zbiór A', cities_a)
print('Zbiór B', cities_b)
print('--' * 10)

print('Suma', cities_a | cities_b)

print('A-B', cities_a - cities_b)
print('---' * 10)
print('Iloczyn', cities_a & cities_b)
print(cities_a.intersection(cities_b))
print('---' * 10)
print('Różnica', cities_a ^ cities_b)
