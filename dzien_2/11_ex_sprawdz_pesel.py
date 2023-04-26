# Napisz program, który sprawdzi, czy podany przez użytkownika PESEL jest prawidłowy.
# Aby policzyć sumę kontrolną należy kolejne cyfry numeru PESEL mnożyć w następujący sposób:

# 1 2 3 4 5 6 7 8 9  10 11   kolejna pozycja cyfry
# 1 8 2 1 0 1 7 7 9   1 5    przykładowy pesel
# 1 3 7 9 1 3 7 9 1   3 1    cyfry przez które musimy mnożyć

# 1 x 1 + 8 x 3 + 2 x 7 + 1 x 9 ..... 9 x 1 = 1230
# jeżeli reszta z dzielenia sumy tych iloczynów wynosi zero to znak, że PESEL jest prawidłowy
# ostania cyfra - sprawdzamy liczbę jako str() lub sprawdzamy czy modulo 10 jest = 0

# 1. Zdefniuj sobie zmienną z peselem możesz użyć wartości 99010124415, 18210177915
# 2. Zdefiniuj pesel_check = '13791379131'
# 3*. Zamień pesele na listy
# 4. Nad pętlą zdefiniuj nową zmienną control_sum
# 4. Iteruj za pomocą zipa po obu listach (pesel oraz pesel_check)
# 5. mnóż poszczególne wartości przez siebie i zapisuj ich sumę do zmiennej control_sum
# 6. Po zakończeniu pętli sprawdź czy suma jest podzielna przez 10, jeżeli tak to pesel jest prawidłowy

pesel = '99010124415'
pesel_check = '13791379131'

control_sum = 0
for pesel_value, pesel_check_value in zip(pesel, pesel_check):
    # control_sum = control_sum + int(pesel_value) * int(pesel_check_value)
    control_sum += int(pesel_value) * int(pesel_check_value)

if control_sum % 10 == 0:
    print('Pesel jest prawidłowy')
else:
    print('Pesel jest niepoprawny')






