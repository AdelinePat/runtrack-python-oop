class Animal():
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} se déplace")

class Dog(Animal):
    def __init__(self, name, race):
        super().__init__(name)
        self.race = race

    def move(self):
        print(f"Le chien {self.name} court !")
    
    def noise(self):
        print("Le chien aboie")

class Bird(Animal):
    def __init__(self, name, race, color, wings=2):
        super().__init__(name)
        self.race = race
        self.color = color
        self.wings = wings

    def move(self):
        print(f"L'oiseau {self.name} vole !")

class Parrot(Bird):
    def __init__(self, name, race, color):
        super().__init__(name, race, color, 4)

a_bird = Bird("Pip", "perroquet", "vert")
a_dog = Dog("Wow", "labrador")
a_parrot = Parrot("Pipo", "perroquet", "blue")

a_bird.move()
a_dog.move()
a_dog.noise()

a_parrot.move()

print(a_parrot.wings)