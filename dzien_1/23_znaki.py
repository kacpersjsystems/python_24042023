text = 'Kup 3 chleby!'

for char in text:
    print(char)
    print('Litera lub cyfra', char.isalnum())
    print('Litera', char.isalpha())
    print('Cyfra', char.isnumeric())
    print('Wielka litera', char.isupper())
    print('Mała litera', char.islower())
    print('Czy jest to spacja', char.isspace())
    print('Tablica ASCII', ord(char))
    print('---' * 10)

# 24_ex_znaki.txt
#
# Napisz program który zliczy ilość wystąpień małej lub dużej
# wersji ciagu tekstowego podanego przez użytkownika w pliku
# którego nazwę również poda użytkownik.

# Ala ma kota
# kot ma Alę

# małych liter:  x
# wielkich liter: x
# spacji: x
# linii: x

