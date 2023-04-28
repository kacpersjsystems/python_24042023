class Student:
    def __init__(self, first_name, last_name):
        # Odbieram zmienne initializujące (zmienne z jakimi chcę stworzyć obiekt)
        # Możemy wykonać dowolny fragment kodu podczas tworzenia obiektu
        print(f'Tworzę studenta {first_name} {last_name}')
        self.first_name = first_name
        self.last_name = last_name

    # metoda - funkcja zdefiniowana wewnątrz klasy
    def say_hello(self):
        return f'Cześć! Nazywam się {self.first_name} {self.last_name}'


john = Student('John', 'Smith')
print(john)
print(type(john))
print(john.first_name, john.last_name)
print(john.say_hello())

barbara = Student('Barbara', 'Smith')
print(barbara)
print(type(barbara))
print(barbara.first_name, barbara.last_name)
print(barbara.say_hello())
print(john.say_hello())

print('--' * 30)

students = [
    john,
    barbara,
    Student('Barbara', 'Walkinson')
]

for student in students:
    print(student.say_hello())
