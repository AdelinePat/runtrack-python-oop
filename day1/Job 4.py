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
