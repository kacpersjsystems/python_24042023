# Przefiltruj miasta zaczynające się na konkretną literę
cities = ['Gdynia', 'Augustów', 'Grudziądz', 'Warszawa', 'Wałbrzych', 'Poznań', 'Jarocin', 'Opole']
starts_with = 'G'

# 0. zdefiniuj pustą listę filtered_cities
# 1. przejdź po miastach
# 2. sprawdź czy miasto zaczyna się na odpowiednią literę
# 3. jeśli tak to dodaj je do nowej listy z punktu 0.
# 4. wyświetl przefiltrowane miasta

# filtered_cities = []
# for city in cities:
#     if city.startswith(starts_with):
#         filtered_cities.append(city)
#
# print(filtered_cities)
                #   Co                        Filtrowanie
                # w liście                   danych
filtered_cities = [city for city in cities if city.startswith(starts_with)]
print(filtered_cities)


# new_list = [ city  if city.startswith(starts_with) for city in cities]
# [f'Pani {name}' if name.endswith('a') else f'Pan {name}' for name in names]


#[ CO W NOWEJ LIŚCIE  for element in lista FILTROWANIE]