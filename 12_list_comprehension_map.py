# brands = ['audi', 'fiat', 'kia', 'lada', 'toyota']

# Za pomocą pętli for stwórz nową listę correct_brand_names
# Gdzie nazwy marek samochodów zapisane są z wielkiej litery .title()
#
# 1. Zdefiniuj pustą listę correct_brand_names = []
# 2. Za pomocą pętli for przejdź po elementach listy
# 3. Każdy jeden elemnt zamieniaj np. element.title() i dodawaj do listy
#    correct_brand_names
# 4. Wyświetl listę i sprawdź czy nazwy zapisane są prawidłowo

# Podejście klasyczne
# correct_brand_names = []
# for brand in brands:
#     correct_brand_names.append(brand.title())
#
# print(correct_brand_names)

# List comprehension (lista składana)
#                      z czego tworzę     pętla for
#                        nową listę
# correct_brand_names = [brand.title() for brand in brands]
# print(correct_brand_names)


names = ['Karolina', 'Adam', 'Wojciech', 'Alina', 'Patryk']
#     jeżeli imię kończy się na literę a to dodaj "Pani" w przeciwnym razie "Pan"
#     ['Pani Karolina', 'Pan Adam', 'Pan Wojciech', 'Pani Alina', 'Pan Patryk']
#
#     b. spróbuj zapisać to za pomocą skróconego if'a

proper_names = []
for name in names:
    # 0. Najdłużej
    # if name.endswith('a'):
    #     proper_names.append(f'Pani {name}')
    # else:
    #     proper_names.append(f'Pan {name}')

    # 1. Dodatkowa zmienna
    # proper_name = f'Pani {name}' if name.endswith('a') else f'Pan {name}'
    # proper_names.append(proper_name)

    # 2. Usuwamy tę zmienną
    proper_names.append(
        f'Pani {name}' if name.endswith('a') else f'Pan {name}'
    )

proper_names = [f'Pani {name}' if name.endswith('a') else f'Pan {name}' for name in names]
print(proper_names)

