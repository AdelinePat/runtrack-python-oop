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

    def __set_running(self, new_running):
        self.__running = new_running


    def start(self):
        if self.get_running():
            print("vous ne pouvez pas démarrer une voiture déjà en marche")
        else:
            if self.__check_tank() > 5:
                self.__set_running(True)
                self.__reduce_gas()
            else:
                print("Vous n'avez pas assez d'essence pour démarrer")
        return self.__running
    
    def stop(self):
        if not self.get_running():
            print("Vous ne pouvez pas arrêter une voiture déjà à l'arrêt")
        else:
            self.__set_running(False)
        return self.__running

    def __check_tank(self):
        return self.__tank
    
    def __reduce_gas(self):
        if self.get_running():
            self.__tank -= 5

my_car = Car("Toyota", "Yaris", 1999, 20000)
print(my_car.get_running())
print(my_car.get_tank())
my_car.start()
my_car.start()
print(my_car.get_running())
my_car.stop()
print(my_car.get_running())
print(my_car.get_tank())

