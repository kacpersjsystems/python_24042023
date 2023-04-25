# Korzystając z list składanych wygeneruj listę zawierajaca 10 kolejnych poteg 2

result = [2 ** n for n in range(1, 11)]
print(result)

# Korzystając z list składanych wygeneruj listę 10 elementow której każdy element również
# będzie listą. Pierwszy element tej podlisty to numer potegi, a drugi to wartosc tej potegi dla
# liczby 2

result = [[n, 2 ** n] for n in range(1, 11)]
print(result)
