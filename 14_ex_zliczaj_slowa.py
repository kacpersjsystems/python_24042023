# Napisz program, który otworzy plik o nazwie 14_ex_zliczaj_slowa.txt zawierający
# tekst. Plik może zawierać dowolną ilość linii. Zadaniem programu jest zliczenie
# Jak często w pliku występuje każdy z wyrazów

# Posortuj słowa na podstawie ilości wystąpień

# 1. Otwórz plik i analizuj go linia po linia
# 2. Rozbij każdą linię po spacji
# 3. Oczyść każdą linię z kropek, przecinków i  ( oraz )
# 3. Sprawdź czy słowo już było w słowniku, jeżeli tak to zwiększ licznik
#    a jeżeli nie, to ustaw ilość 1 dla tego słowa.
# >>> a = {'a': 1, 'b': 2}
# >>> 'a' in a
# True

# a = 'a,.,;b,.,.c'
#
# for char in '.,;':
#     a = a.replace(char, '')
SPECIAL_CHARS = ',.()-–'

with open('14_ex_zliczaj_slowa.txt', encoding='utf8') as file:
    counter = {}
    for line in file:
        for char in SPECIAL_CHARS:
            line = line.replace(char, '').strip()

        for word in line.split(' '):
            counter[word] = counter.get(word, 0) + 1

print(counter)