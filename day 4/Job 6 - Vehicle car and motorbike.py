class Vehicle():
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    
    def __str__(self):
        return f"Marque : {self.brand}\
            \nModèle : {self.model}\
            \nAnnée : {self.year}\
            \nPrix : {self.price} €"
    

class Car(Vehicle):
    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.car_door = 4

    def __str__(self):
        return super().__str__() + f"\nPortes : {self.car_door}"

    def set_door(self, new_door_number):
        self.car_door = new_door_number

class Motorbike(Vehicle):
    def __init__(self,brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.wheel = 2

    def __str__(self):
        return super().__str__() + f"\nRoues : {self.wheel}"


car = Car("Toyota", "Yaris", 1999, 20000)
moto = Motorbike("Yamaha", "R1M", 2024, 27999)
car.set_door(3)
print(car)
print("\n")
print(moto)