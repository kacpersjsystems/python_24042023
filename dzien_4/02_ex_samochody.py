# 10:57
#
# Przygotuj klasę Car, która powinna przechowywać nazwę samochodu(name)
# oraz jego cenę(price) i maksymalną prędkość(v_max).
# Stwórz 5 samochodów, a następnie wyświetl je na ekranie w formie tabelki.
#
# Przed zadaniem z gwiazdką podnieś rękę :-)
# * posortuj samochody według maksymalnej prędkości
#

# Ferrari 488 GTB - cena około 700 000 USD, prędkość maksymalna 330 km/h
# Lamborghini Aventador SVJ - cena około 500 000 USD, prędkość maksymalna 350 km/h
# Porsche 911 GT2 RS - cena około 300 000 USD, prędkość maksymalna 340 km/h
# Bugatti Chiron - cena około 3 000 000 USD, prędkość maksymalna 420 km/h
# Koenigsegg Jesko - cena około 3 000 000 USD, prędkość maksymalna 482 km/h

from prettytable import PrettyTable


class Car:
    def __init__(self, name: str, price:float, v_max:float):
        self.name = name
        self.price = price
        self.v_max = v_max

    # To wykracza poza poziom kursu, metoda statyczna nie działa w kontekście obiektowym
    # nie ma dostępu do self i wywołujemy ją Car.get_v_max()
    # po prostu jest to funkcja zgrupowana wewnąrz klasy.
    @staticmethod
    def get_v_max(obj):
        return obj.v_max


cars = [
    Car('Ferrari 488 GTB', 700000, 330),
    Car('Lamborghini Aventador SVJ', 500000, 350),
    Car('Porsche 911 GT2 RS', 300000, 340),
    Car('Bugatti Chiron', 3000000, 420),
    Car('Koenigsegg Jesko', 3000000, 482),
]

# sorted(cars) -> zwraca nową listę
# cars.sort() -> sortuje tę samą listę

# def get_v_max(obj:Car) -> float:
#     return obj.v_max
#
#
# cars.sort(key=get_v_max, reverse=True)
# cars.sort(key=Car.get_v_max, reverse=True)
cars.sort(key=lambda x: x.v_max, reverse=True)
table = PrettyTable()
table.field_names = ['Nazwa', 'Cena', 'Prędkość maksymalna']
table.add_rows([[car.name, car.price, car.v_max] for car in cars])

print(table)




