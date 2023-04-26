
fruits = ['mango', 'apple', 'lemon', 'peach']
print(fruits)
print(type(fruits))
fruits.append('watermelon')
fruits[1] = 'raspberry'
fruits.append('apple')
print(fruits)
print(len(fruits))

# lista owoców przemnożona razy 3
print(fruits * 3)

# dodawanie dwóch list do siebie
vege = ['carrot', 'tomato', 'onion']
print(fruits + vege)

# wyświetlanie elementów listy
print('Owoce i warzywa: ')
for item in fruits + vege:
    print(f' - {item}')

items = fruits + vege
print('Posortowane według sorted')
# sortowanie elementów alfabetyczne
# za pomocą sorted
for item in sorted(items, reverse=True):
    print(item)

print('-' * 30)
# modyfikacja listy - sortowanie
print('Posortowane według items.sort()')
items.sort()
for item in items:
    print(item)