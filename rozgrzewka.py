# 0. Napisz program, który pobierze od użytkownika dowolny ciąg znaków i wypisze go na ekranie w odwrotnej kolejności
# bez spacji, przecinka oraz kropki.
#
# Input: Ala ma kota.
# Output: atokamalA

# sentence = input('Podaj zdanie: ')
sentence = 'Ala ma kota.'
for char in '. ,':
    sentence = sentence.replace(char, '')

print(sentence[::-1])

#
# 1. Z podanej listy imion o różnej długości wyświetl tylko te które są dłuższe niż 5 znaków.
# Długość imienia sprawdź funkcją len()
#   * Zmień ten program do postaci listy składanej (list comprehension)
#   * Za pomocą .title() upewnij się, że zawsze zaczynamy z wielkiej litery

names = ['asia', 'Kasia', 'zofia', 'Adelajda', 'michalina']
longer_names = []
for name in names:
    if len(name) > 5:
        longer_names.append(name.title())

longer_names = [name.title() for name in names if len(name) > 5]
print(longer_names)
#
# 2. “12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek”
# policzyć ile łącznie razem ważą zakupione produktu. (spacje przed kilogramami muszą być :)
# a) split i rozbij wyrażenie po spacjach
# b) iteruj po każdym wyrażeniu i dodawaj do siebie te, które wyglądają jak liczby .isnumeric()
#
#
# 3. Napisz program, który odbierze od użytkownika liczbę całkowitą, a następnie wyświetli na ekranie wszystkie liczby
# parzyste od 2 do tej liczby. Wyświetl wszystkie te liczby oddzielone przecinkami.
# a) załaduj wszystkie te liczby do listy
# b) połącz elementy listy przecinkami ','.join(lista)
#
#
# 4. Napisz program, w którym odbierzesz od użytkownika imiona oraz nazwiska rozdzielone przecinkami,
# w odpowiedzi powinny wyświetlić się poprawnie zapisane imiona bez powtórzeń posortowaną w kolejności Z-A.
# IN: Adam Mickiewicz, Adam Asnyk, Zbigniew Nienacki
# OUT: Zbigniew, Adam
#
# a) Rozbij imiona i nazwiska po przecinkach
# b) Rozbij każde imie i nazwisko po spacji
# c) Dodaj imię do nowej listy jeżeli jeszcze go tam nie było
# d) Wyświetl odwrotnie posortowaną listę sorted(lista, reverse=True)
