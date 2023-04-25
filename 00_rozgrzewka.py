# Rozgrzewka
#
# 1. Zapytaj użytkownika o potrzebne dane i policz pole trapezu. (a+b)* h /2
#    * wymuś na użytkowniku by podane dane były liczbami
# a = None
# b = None
# h = None
a, b, h = None, None, None
#
# while a is None or not a.isnumeric():
#     a = input('Podaj długość podstawy 1: ')
#
# while b is None or not b.isnumeric():
#     b = input('Podaj długość podstawy 2: ')
#
# while h is None or not h.isnumeric():
#     h = input('Podaj długość wysokości: ')
#
# field = (float(a) + float(b)) * float(h) / 2
# print(f'Pole takiego trapezu wynosi {field:.2f}')


# 2. Napisz program, który zapyta użytkownika o temperaturę.
# Jeśli będzie 10 stopni lub zimniej wypisz “zostań w domu”
# Jeśli będzie więcej niż 10, ale mniej niż 20 wypisz “weź kurtkę!”
# W każdym innym przypadku wypisz “Baw się dobrze”

# temperature = float(input('Ile dziś jest stopni? '))
#
# if temperature <= 10:
#     print('Zostań w domu!')
# elif temperature >= 20:
#     print('Baw się dobrze!')
# else:
#     print('Weź kurtkę!')
#
# if temperature <= 10:
#     print('Zostań w domu!')
# elif 10 < temperature < 20:
#     print('Weź kurtkę')
# else:
#     print('Baw się dobrze')


# 3. Umieszczając pętle for w drugiej pętli for wyświetl trójkąt jak w przykładzie:
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# 1
# 1 2
# 1 2 3
# 1 2 3 4

for row in range(1, 5):
    for col in range(1, 6 - row):
        print(col, end=' ')
    print()


# 4. Napisz program generujące bardzo “silne” hasła.
# Zamień każdą literę “a” na @ oraz każdą literę s na $.

password = input('Podaj hasło: ')
password = password.replace('a', '@')
password = password.replace('s', '$')
print(password)


