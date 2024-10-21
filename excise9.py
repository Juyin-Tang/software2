import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.traveled_distance = 0

    def accelerate(self,speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0


    def drive(self,hours):
        self.traveled_distance += self.current_speed * hours

cars = []
for i in range(10):
    registration_number = f'ABC-{i+1}'
    max_speed = random.randint(100, 200)
    car = Car(registration_number, max_speed)
    cars.append(car)

race = 0
while race != 1:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

        if car.traveled_distance >= 10000:
            race = 1



car1 = Car("ABC-123",142)
print(f'registration number:{car1.registration_number}, maximum speed:{car1.maximum_speed}, current speed:{car1.current_speed}, traveled_distance:{car1.traveled_distance}')

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
car1.accelerate(-200)
car1.accelerate(60)

car1.drive(1.5)
print(f'The current speed is {car1.current_speed}')
print(f'The traveled distance is {car1.traveled_distance}')
for car in cars:
    print(f'car registration: {car.registration_number}, traveled_distance:{car.traveled_distance}.')

