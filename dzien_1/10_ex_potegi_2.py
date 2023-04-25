# • Wyświetl 20 kolejnych potęg liczby 2
# 2 ** 1, 2**2... 2**20

for power in range(1, 21):
    print(f'2 do potęgi {power} wynosi {2 ** power}')
    print(f'2 do potęgi {power} wynosi {pow(2, power)}')
    print('--' * 30)