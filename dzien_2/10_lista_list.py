# Korzystajac z petli stworz liste zawierajaca elementy same bedace listami. Kazdy taki
# element ma zawierac numer potegi oraz wartosc tej potegi dla liczby 2.
#
# [
#     numer_potegi, wartość po podnieniu do tej potęgi
#     [1, 2],
#     [2, 4],
#     [3, 8]
#     ...
# ]
#
#  Podpowiedź co dodawać do listy
#  mylist = []
#  mylist.append([a, 2 ** a])

values = []
for p in range(1, 11):
    # pow(2, p)
    values.append([p, 2 ** p])

for value in values:
    print(value)
