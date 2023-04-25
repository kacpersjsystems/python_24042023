a = [1, 3, 5, 7, 9]
b = [2, 6, 8, 10, 12]

c = a + b
print(c)

print('APPEND')
a.append(b)
print(a)

print('EXTEND')
a = [1, 3, 5, 7, 9]
a.extend(b)
print(a)