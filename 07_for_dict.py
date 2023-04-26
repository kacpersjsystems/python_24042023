person = {
    'first_name': 'Adam',
    'last_name': 'Małysz',
    'age': 45
}

# Przechodzimy po słowniku
for x in person:
    print(x, person[x], person.get(x))

print('---' * 10)
# Przechodzimy po słowniku biorąc klucz i wartość
for key, value in person.items():
    print(key, value)

print('---' * 10)
for key in person.keys():
    print(key)

print('---' * 10)
for value in person.values():
    print(value)