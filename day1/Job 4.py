print("\n=== JOB 4 ===")
"""
Job 4
"""
class Person():
    def __init__(self, firstname="", lastname="", age=""):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age

    def present_yourself(self):
        self.lastname = input("Entrez votre nom : ")
        self.firstname = input("Entrez votre prénom :")
        self.age = input("entrez votre âge : ")
        # self.__str__()

    def __str__(self):
        return f"Bonjour, je m'appelle {self.firstname} {self.lastname} et j'ai {self.age} ans."

person1 = Person("Sari", "Norumai", 20)
person2 = Person("Irahan", "Shuxi", 22)
person3 = Person("Malia", "Jodeli", 18)
person4 = Person("Naku", "Atsona", 18)
person5 = Person("Hashegin", "Ogin", 30)

person6 = Person()
person6.present_yourself()

print(person1)
print(person2)
print(person3)
print(person4)
print(person5)
print(person6)
