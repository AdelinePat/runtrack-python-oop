class Car():
    def __init__(self, brand, model, year, mileage, running=False, tank=50):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__running = running
        self.__tank = tank

    def get_running(self):
        return self.__running
    
    def get_tank(self):
        return self.__tank

    def start_running(self):
        if self.__check_tank() > 5:
            self.__running = True
            self.__tank = self.__reduce_gas()
        else:
            print("Vous n'avez pas assez d'essence pour démarrer")
        return self.__running
    
    def stop_running(self):
        self.__running = False
        return self.__running

    def __check_tank(self):
        return self.__tank
    
    def __reduce_gas(self):
        if self.__running:
            self.__tank -= 5
        return self.__tank

my_car = Car("Toyota", "Yaris", 1999, 20000)
print(my_car.get_running())
print(my_car.get_tank())
my_car.start_running()
print(my_car.get_running())
my_car.stop_running()
print(my_car.get_running())
print(my_car.get_tank())

