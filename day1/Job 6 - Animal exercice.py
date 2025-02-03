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

    def __str__(self):
        return f"L'age de l'animal : {an_animal.age} an(s)\
                \nL'animal se nomme : {an_animal.name}\n"

an_animal = Animal()

print(an_animal)
an_animal.aging()
an_animal.naming("Booya")
print(an_animal)
