# Napisz program który będzie od uzytkownika przyjmowal nazwę pliku z kodem pythona.
# Program ma wyświetlić wszystkie linie które nie są w całości komentarzami wraz z numerami tych
# linii w pliku

# 1. Otwieramy plik do odczytu
# 2. Przechodzimy po pliku linia po linii
# 3. Jeżeli linia zaczyna się od # to jej nie wyświetlaj
#    line.startswith('#')
# 4. Jeżeli hash nie jest z przodu to wyświetl tę linię

# 11:03 -> 11:13
with open('04_ex_szukaj_w_pliku.py', encoding='utf8') as file:
    for line in file:
        if not line.startswith('#') and len(line.strip()) > 0:
            print(line.strip())
        # if line.startswith('#') or len(line.strip()) == 0:
        #     pass
        # else:
        #     print(line.strip())
