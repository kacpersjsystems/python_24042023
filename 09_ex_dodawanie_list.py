# Stwórz dwie listy. Każda z list ma zawierać 10 liczb losowych z zakresu 1-10.
# Połącz te dwie listy do jednej i wyswietl na konsoli (zarówno za pomocą dodawania, jak i extend)

# 1. Zaimportuj from random import randint
# 2. Nad pętlą zdefiniuj dwie puste listy
# 3. Napisz pętle for która wywoła się 10 razy
# 4. W każdym przebiegu pętli dodawaj do listy nowe wartości (wylosowane od 1 do 10)
# 5. Dodaj te dwie listy do siebie

from random import randint

values1 = []
values2 = []

for _ in range(11):
    values1.append(randint(1, 10))
    values2.append(randint(1, 10))


print('Za pomocą plusa')
print(values1 + values2)

# print('Za pomocą extend')
# values1.extend(values2)
# print(values1)

# first_name, _, age, _ = 'Kacper', 'Sieradziński', 35, 12121
# print(_)

# 6*. zip() i dodawanie kolejnych wartości do siebie
#  [  list1[0] + list2[0], list1[1], list2[1]  ]

new_list = []
for value1, value2 in zip(values1, values2):
    new_list.append(value1 + value2)

print('----' * 5)
print(values1)
print(values2)
print(new_list)
print('----' * 5)
print('SUM', sum(new_list))
print('LEN', len(new_list))
print('AVG', sum(new_list) / len(new_list))