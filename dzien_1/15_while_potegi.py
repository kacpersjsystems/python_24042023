# Napisz korzystajac z petli while program który wyświetli
# 10 kolejnych potęg liczby 2.
#
# n = 1
# while n <= 10:
#     print(2 ** n)
#     n += 1

# Napisz pętlę while która będzie wyświetlała kolejne potęgi liczby 2 aż wartość potęgi nie przekroczy wartości
# podanej przez użytkownika

maximum = int(input('Podaj mi wartość maksymalną dla potęgi liczby 2')) # 1000
# n = 2
# p = 1
#
# while 2 ** p <= maximum:
#     n = 2 ** p
#     print(n)
#     p += 1

# break - kończy działanie pętli
# continue - przechodzi do kolejnej iteracji (kolejny przebieg pętli)

p = 1
while True:
    if 2 ** p <= maximum:
        print(2 ** p)
    else:
        break

    p += 1
