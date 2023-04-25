# Napisz program który przyjmie od użyszkodnika ciąg tekstowy
# a następnie usunie z niego znaki ,.!? i wyświetli powiększony
# do dużych liter na konsoli

# Podpowiedzi:
# 1. możesz korzystać z replace i usuwać wymienione znaki zamieniając je na
#    pusty string
# 2. możesz interować po napisie znak po znaku i dodawać tylko te znaki,
#    które nie są ,.!?
# 3. Powiększone litery .upper()

# Ala ma kota, a kot ma Alę! Czy są szczęśliwi? Tak.
# ALA MA KOTA A KOT MA ALĘ CZY SĄ SZCZĘŚLIWI TAK

string = 'Ala ma kota, a kot ma Alę! Czy są szczęśliwi? Tak.'
for special_char in ',.!?':
    string = string.replace(special_char, '')
print(string.upper())

string = 'Ala ma kota, a kot ma Alę! Czy są szczęśliwi? Tak.'
new_string = ''
for char in string:
    if char not in ',.!?':
        new_string += char

print(new_string.upper())