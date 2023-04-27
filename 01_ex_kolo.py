# Zaimplementuj klasę Circle, która w metodzie init powinna odebrać promień koło.
# Klasa ta powinna posiadać dwie metody liczące pole koła, a także obwód koła.

# (r lub radius)
# field, circumference
# pi = 3.14, #from math import pi

from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_field(self):
        return pi * self.radius ** 2

    def calculate_circumference(self):
        return 2 * pi * self.radius


radius = float(input('Podaj mi promień koła: '))
circle = Circle(radius)
print('Pole koła wynosi', round(circle.calculate_field(), 2))
print('Obwód koła wynosi', round(circle.calculate_circumference(), 2))