class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.string = year


car1 = Car('Ford', 'Camry', '2020')
print(car1.make, car1.model, car1.string)