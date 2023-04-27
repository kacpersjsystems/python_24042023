class Box:
    def __init__(self, height: int, length:int, width:int):
        self.height = height
        self.length = length
        self.width = width

    def __str__(self):
        # Dotyczy wyświetlania obiektu lub zamiany obiektu na str str(a)
        return f'Pudełko(wysokość:{self.height}, długość: {self.length}, szerokość: {self.width})'

    def __repr__(self):
        # Dotyczy wyświetlania obiektu w liście
        return f'{self.height} x {self.length} x {self.width}'

    def __add__(self, other):
        # Pozwala na zdefiniowanie sposobu dodawania obiektów do siebie
        return Box(
            self.height + other.height,
            self.length + other.length,
            self.width + other.width
        )

    def __lt__(self, other):
        return self.calculate_volume() < other.calculate_volume()

    def calculate_volume(self):
        return self.height * self.length * self.width


a = Box(10, 20, 30)
b = Box(40, 50, 60)
c = Box(80, 100, 120)

print(str(a))

boxes = [c, a, b]
# usuwanie elemntu z listy
del boxes[1]
print(sorted(boxes, reverse=True))

print(a + b)

boxes = [c, a, b]

print('--' * 50)
# Zdejmuje ostatnią wartość z listy
print('przed', boxes)
last = boxes.pop()
print('po', boxes)
print('ostatni', last)
