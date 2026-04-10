# Car Class
# Samuel Renneke, 4/10/2026
class Car:
    def __init__(self, year_model, make):
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed

def function():

    car = Car(2015, "Ford")

    print("Accelerating")

    for i in range(5):
        car.accelerate()
        print(car.get_speed())

    print("Braking")

    for i in range(5):
        car.brake()
        print(car.get_speed())

function()
