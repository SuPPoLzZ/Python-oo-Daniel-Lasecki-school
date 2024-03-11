class Car:
    def __init__(self):
        self.__petrol = 0
        self.__odometer = 0

    def fill_up(self):
        self.__petrol = min(60, self.__petrol + (60 - self.__petrol))
        
    def drive(self, km):
        fuel_needed = km
        if fuel_needed > self.__petrol:
            fuel_needed = self.__petrol
        self.__odometer += fuel_needed
        self.__petrol -= fuel_needed

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"

car = Car()
print(car)
car.fill_up()
print(car)
car.drive(20)
print(car)
car.drive(50)
print(car)
car.drive(10)
print(car)
car.fill_up()
car.fill_up()
print(car)
