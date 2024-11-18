class Publication:
    def __init__(self,name):
        self.name = name

class Book(Publication):
    def __init__(self,name, author,page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        print(f'{self.name} (author {self.author},page count {self.page_count} pages)')

class Magazine(Publication):
    def __init__(self,name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print(f'{self.name} (chief editor {self.chief_editor})')

publications = []
publications.append(Magazine('Donald Duck','Aki Hyyppä'))
publications.append(Book('Compartment No. 6','Rosa Liksom',192))

for b in publications:
    b.print_information()


import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.traveled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.traveled_distance += self.current_speed * hours




class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed,battery):
        super().__init__(registration_number, maximum_speed)

        self.battery = battery
    def print_information(self):
        print(f'{self.registration_number}, {self.maximum_speed}, {self.battery},{self.traveled_distance} km traveled')


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed,tank):
        super().__init__(registration_number, maximum_speed)

        self.tank = tank

    def print_information(self):
        print(f'{self.registration_number}, {self.maximum_speed}, {self.tank},{self.traveled_distance} km traveled')

cars = []
cars.append(ElectricCar('ABC-15', 180 , 52.5))
cars.append(GasolineCar('ACD-123', 165, 32.3))

for c in cars:
    c.accelerate(random.randint(-10, 15))
    c.drive(3)


for c in cars:
    c.print_information()