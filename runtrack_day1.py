print("\n=== JOB 1 à 3 ===")
"""
Job 1 to 3
"""
class Operation():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        self.operator = ""
        self.result = ""

    # Job 3
    def addition(self):
        self.result = self.number1 + self.number2
        self.operator = "+"
        
    def soustraction(self):
        self.result = self.number1 - self.number2
        self.operator = "-"
    
    def multiply(self):
        self.result = self.number1 * self.number2
        self.operator = "*"
    
    def division(self):
        try:
            if self.number2 == 0:
                self.result = "IMPOSSIBLE"
                self.operator = "/"
                raise ZeroDivisionError("la division par 0 est impossible")
            else:
                self.result = self.number1 / self.number2
                self.operator = "/"
        except ZeroDivisionError as message:
            print(message)

    # Job 1 & Job 2
    def calculate(self, operator):
        self.operator = operator

        try:
            match operator:
                case "+":
                    self.result = self.number1 + self.number2
                case "-":
                    self.result = self.number1 - self.number2
                case "/":
                    if self.number2 == 0:
                        self.result = "IMPOSSIBLE"
                        raise ZeroDivisionError("La division par 0 est impossible")
                    else:
                      self.result = self.number1 / self.number2
                case "*":
                    self.result = self.number1 * self.number2
        except ZeroDivisionError as message:
            print(message)

    def __str__(self): 
        print(f"{self.number1} {self.operator} {self.number2} = {self.result}")

operation = Operation(8, 0)
operation.calculate("/")
operation.__str__()

other_operation = Operation(8,2)
other_operation.multiply()
other_operation.__str__()

print("\n=== JOB 4 ===")
"""
Job 4
"""
class Person():
    def __init__(self, firstname, lastname, age):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age

    def present_yourself(self):
        self.__str__()

    def __str__(self):
        print(f"Bonjour, je m'appelle {self.firstname} {self.lastname} et j'ai {self.age} ans.")

person1 = Person("Sari", "Norumai", 20)
person2 = Person("Irahan", "Shuxi", 22)
person3 = Person("Malia", "Jodeli", 18)
person4 = Person("Naku", "Atsona", 18)
person5 = Person("Hashegin", "Ogin", 30)

person1.present_yourself()
person2.present_yourself()
person3.present_yourself()
person4.present_yourself()
person5.present_yourself()

print("\n=== JOB 5 ===")
"""
Job 5
"""
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def display_points(self):
        print(f"le point x est à {self.x} sur l'axe horizontal \
              \nle point y est à {self.y} sur l'axe vertical")
    def display_x(self):
        print(f"le point x est à {self.x} sur l'axe horizontal")
    
    def display_y(self):
        print(f"le point y est à {self.y} sur l'axe vertical")

    def change_x(self, new_x):
        self.x = new_x
    
    def change_y(self, new_y):
        self.y = new_y

point = Point(12, 4)
point.display_points()
point.change_x(7)
point.display_x()

print("\n=== JOB 6 ===")
"""
Job 6
"""
class Animal():
    def __init__(self, age=0, name=""):
        self.age = age
        self.name = name
    
    def aging(self):
        self.age += 1
    
    def naming(self, new_name):
        self.name = new_name

an_animal = Animal()

print(f"L'age de l'animal : {an_animal.age} an(s)\
      \nL'animal se nomme : {an_animal.name}")
an_animal.aging()
an_animal.naming("Booya")
print(f"L'age de l'animal : {an_animal.age} an(s)\
      \nL'animal se nomme : {an_animal.name}")

print("\n=== JOB 7 ===")
"""
Job 7
"""
class Character():
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.sign = "X"

    def move_up(self, board):
        self.clear_previous_emplacement(board)
        if self.y > 0:
            self.y -= 1
        else: 
            print("vous ne pouvez pas monter plus haut")
    
    def move_down(self, board):
        self.clear_previous_emplacement(board)
        if self.y < len(board)-1:
            self.y += 1
        else:
            print("vous ne pouvez pas descendre plus bas")
    
    def move_left(self, board):
        self.clear_previous_emplacement(board)
        if self.x > 0:
            self.x -= 1
        else:
            print("vous ne pouvez pas aller sur la gauche")
    
    def move_right(self, board):
        self.clear_previous_emplacement(board)
        if self.x < len(board[0])-1:
            self.x += 1
        else:
            print("vous ne pouvez pas vous déplacer sur la droite")
    
    def clear_previous_emplacement(self, board):
        board[self.y][self.x] = ""
    
    def position(self):
        return (self.x, self.y)

little_one = Character(1, 0)
board = [["", "", ""],["", "", ""],["", "", ""]]
board[little_one.y][little_one.x] = little_one.sign
print(board)
little_one.move_down(board)
little_one.move_down(board)
little_one.move_right(board)
little_one.move_left(board)
little_one.move_left(board)
board[little_one.y][little_one.x] = little_one.sign
print(board)
print(little_one.position())

print("\n=== JOB 8 ===")
"""
Job 8
"""
class Circle():
    def __init__(self, radius):
        self.radius = radius
        self.diameter = self.get_diameter()
        self.circumference = self.get_circumference()
        self.area = self.get_area()
    
    def change_radius(self, new_radius):
        self.radius = new_radius
    
    def get_diameter(self):
        diameter = self.radius * 2
        return diameter

    def get_circumference(self):
        circumference = self.diameter * 3.14
        return circumference

    def get_area(self):
        area = self.radius ** 2 * 3.14
        return area

    def display_info(self):
        print(f"Le cercle fait {self.radius} de rayon\
              \nSa circonférence est de {self.circumference}\
              \nSon diamètre est de {self.circumference}\
              \nSon aire est de {self.area}")

circle1 = Circle(4)
circle1.display_info()
circle1.change_radius(8)
circle1.display_info()
circle2 = Circle(7)
circle2.display_info()

print("\n=== JOB 9 ===")
"""
Job 9
"""
class Product():
    def __init__(self, name, priceExludeTaxes, VAT):
        self.name = name
        self.priceExludeTaxes = priceExludeTaxes
        self.VAT = VAT
        self.price = self.calculate_full_price()

    def calculate_full_price(self):
        full_price = self.priceExludeTaxes + (self.priceExludeTaxes / 100) * self.VAT
        return full_price
    
    def change_name(self, new_name):
        self.name = new_name

    def change_priceExludeTaxes(self, new_price):
        self.priceExludeTaxes = new_price

    def display_info(self):
        print(f"Nom : {self.name}\
              \nPrix HT : {self.priceExludeTaxes}\
              \nTVA : {self.VAT}\
              \nPrix TTC : {self.price}")

chips = Product("chips", 5, 20)
café = Product("chips", 3, 15)

chips.display_info()
chips.change_priceExludeTaxes(10)

café.display_info()
café.change_name("Mocha")

chips.display_info()
café.display_info()
