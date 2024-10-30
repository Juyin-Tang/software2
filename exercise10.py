class Elevator:
    def __init__(self,numbers_of_bottom,numbers_of_top):
        self.numbers_of_bottom=numbers_of_bottom
        self.numbers_of_top=numbers_of_top
        self.start_floor = self.numbers_of_bottom

    def floor_up(self):
        self.start_floor += 1
        print(f'The elevator is in {self.start_floor}')

    def floor_down(self):
        self.start_floor -= 1
        print(f'The elevator is in {self.start_floor}')

    def goto_floor(self,target_floor):
        while self.start_floor != target_floor:
            if target_floor < self.start_floor:
                self.floor_down()
            elif target_floor > self.start_floor:
                self.floor_up()

    def back(self):
        self.start_floor = self.numbers_of_bottom
        print(f'The elevator is back to {self.start_floor}')

class Building:
    def __init__(self,numbers_of_bottom,numbers_of_top,numbers_of_elevators):
        self.numbers_of_bottom=numbers_of_bottom
        self.numbers_of_top=numbers_of_top
        self.elevators = []
        for i in range(numbers_of_elevators):
            self.elevators.append(Elevator(numbers_of_bottom,numbers_of_top))


    def run_elevator(self,numbers_of_elevators,target_floor):
        print(f'The elevator_{numbers_of_elevators + 1} move to {target_floor}')
        self.elevators[numbers_of_elevators].goto_floor(target_floor)

    def fire_alarm(self):
        print('all elevators to the bottom floor🔥')
        for elevator in self.elevators:
            elevator.goto_floor(self.numbers_of_bottom)



elevator1 = Elevator(0,9)
elevator1.goto_floor(9)
elevator1.back()
building1 = Building(0,9,3)

building1.fire_alarm()

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

class Race:
    def __init__(self,name,distance,cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hours_pass(self):
        for car in self.cars:
            speed_change = random.randint(-10,15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Car':<15}{'Max Speed':<15}{'Current Speed':<15}{'Distance Traveled':<20}")
        print('_'* 65 )
        for car in self.cars:
            print(f'{car.registration_number:<15}{car.maximum_speed:<15}{car.current_speed:<15}{car.traveled_distance:<20.1f}')

    def race_finished(self):
        for car in self.cars:
            if car.traveled_distance >= self.distance:
                return True
        return False

def main():
    cars = []
    for i in range(10):
        registration_number = f'ABC-{i+1}'
        max_speed = random.randint(100, 200)
        cars.append(Car(registration_number, max_speed))

    race = Race('The race',8000,cars)
    hours = 0

    while not race.race_finished():
        race.hours_pass()
        hours += 1

        if hours % 10 == 0:
            print(f'\nStatus after {hours} hours')
            race.print_status()
    print('\nFinished status:')
    race.print_status()


main()