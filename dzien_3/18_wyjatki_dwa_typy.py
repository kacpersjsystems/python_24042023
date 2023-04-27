
try:
    my_list = []
    my_dict = {}

    # print(my_list[1])
    print(my_dict['pies'])
except (IndexError, KeyError) as error:
    print('Taki klucz lub indeks nie istnieje')
    print(type(error))
    print(error)