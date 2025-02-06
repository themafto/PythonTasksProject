class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

electric_car1 = ElectricCar('Tesla', 'Models S', 2022, 100)
print(electric_car1.make, electric_car1.model, electric_car1.year, electric_car1.battery_size)
