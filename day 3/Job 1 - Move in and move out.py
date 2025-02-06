class City():
    def __init__(self, name, inhabitants):
        self.__name = name
        self.__inhabitants = inhabitants
    
    def get_inhabitants(self):
        return self.__inhabitants
    
    def add_inhabitants(self):
        self.__inhabitants = self.get_inhabitants() + 1
    
    def remove_inhabitant(self):
        self.__inhabitants = self.get_inhabitants() - 1

    def get_name(self):
        return self.__name
    
    def __str__(self):
        return f"{self.get_name().upper()} : {self.get_inhabitants()} habitants"
    
class Person():
    def __init__(self, firstname, age, city):
        self.__firstname = firstname
        self.__age = age
        self.__city = self.add_inhabitant(city)

    def get_firstname(self):
        return self.__firstname
    
    def get_city_name(self):
        return self.__city.get_name()
    
    def add_inhabitant(self, city):
        city.add_inhabitants()
        return city

    def get_inhabitants(self):
        return self.__city.get_inhabitants()
    
    def move_away(self, new_city):
        self.__city.remove_inhabitant()
        self.__city = self.add_inhabitant(new_city)

    def __str__(self):
        return f"{self.get_firstname()} vivant à {self.get_city_name().upper()} peuplée {self.get_inhabitants()} : habitants"

a_city = City("Atlantide", 100)
castalla = City("Castalla", 10456)
print(a_city)
print(castalla)
a_person = Person("Mira", 30, a_city)
sari = Person("Sari", 20, castalla)
paris = City("Paris", 1000000)
marseille = City("Marseille", 861635)

print(paris)
print(marseille)

john = Person("John", 45, paris)
myrtille = Person("Myrtille", 4, paris)
chloe = Person("Chloé", 18, marseille)
myrtille.move_away(castalla)
john.move_away(paris)
print("\n")

print(john)
print(myrtille)
print(chloe)
print(sari)
print(a_person)
