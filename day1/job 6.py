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
