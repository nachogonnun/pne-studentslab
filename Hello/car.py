class Car:
    def __init__(self, brand , speed):
        self.brand = brand
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def get_nationality(self):
        if self.brand == "Renault":
            return "France"
        if self.brand == "Ferrari":
            return "Italy"


my_car = Car("Renault", 80)
my_car.set_speed(80)
print(my_car.get_speed())
print(my_car.get_nationality())

your_car = Car("Ferrari", 250)
print(your_car.get_speed())
print(your_car.get_nationality())