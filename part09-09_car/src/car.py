# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__litres = 0
        self.__km = 0

    def fill_up(self):
        self.__litres = 60

    def drive(self, km:int):
        if km > self.__litres:
            self.__litres = 0
            self.__km += self.__litres
        else:
            self.__litres -= km
            self.__km += km

    def __str__(self):
        return f"Car: odometer reading {self.__km} km, petrol remaining {self.__litres} litres"


if __name__ == "__main__":
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