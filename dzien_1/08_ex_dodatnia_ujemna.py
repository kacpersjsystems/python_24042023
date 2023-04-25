# Niech użytkownik poda jakąś liczbę. Jeśli poda dodatnią to chcemy wyświetlić tę wartość z
# informacją "wartość dodatnia", jeśli zero to wyświetlamy z informacją "równe zero", jeśli ujemna
# to wyświetlamy "wartość ujemna".

value = int(input('Podaj liczbę'))

if value > 0:
    print('Wartość dodatnia.')
elif value <0:
    print('Wartość ujemna.')
else:
    print('Równa zero.')