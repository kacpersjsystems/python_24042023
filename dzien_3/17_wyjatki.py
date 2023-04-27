# ValueError oraz ZeroDivisionError

try:
    a = int(input('Podaj liczbę A: '))
    b = int(input('Podaj liczbę B: '))

    try:
        result = a / b
    except ZeroDivisionError:
        result = 'Błąd'

    print(f'Wynik wynosi {result}')

except ValueError:
    print('Podane dane są nieprawidłowe')
# except ZeroDivisionError:
#     print('Nie dzielimy przez zero!')