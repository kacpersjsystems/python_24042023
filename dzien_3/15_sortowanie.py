fruits = ['mango', 'lmn', 'apple', 'peach', 'raspberry']
print('Posortowane alfabetycznie')
print(sorted(fruits))

print('Posortowane według długości')
#      [5, 3, 5, 5, 9]
#      [3, 5, 5, 5, 9]
print(sorted(fruits, key=len))


people = [
    ('Cecylia', 'Siekawska'),
    ('Adam', 'Żasnyk'),
    ('Beata', 'Rzonda'),
]
print('Posortowane tuple')
print(sorted(people))


def get_second_element(collection: tuple):
    return collection[1]


print('Posortowane tuple według nazwisk')
print(sorted(people, key=get_second_element, reverse=True))