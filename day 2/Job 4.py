class Student():
    def __init__(self, lastname, firstname, student_id, credits=0):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__student_id = student_id
        self.__credits = credits
        self.__level = self.__student_eval()

    def get_credits(self):
        return self.__credits
    
    def get_firstname(self):
        return self.__firstname
    
    def get_lastname(self):
        return self.__lastname
    
    def get_student_level(self):
        self.__level = self.__student_eval()
        return self.__level

    def add_credits(self, add_value):
        if type(add_value) is int and add_value > 0:
            self.__credits += add_value
        else:
            print("Vous devez entrer un nombre entier positif")
    
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        elif self.__credits < 60:
            return "Insuffisant"
    
    def student_info(self):
        return f"Nom : {self.__lastname}\
            \nPrénom : {self.__firstname}\
            \nid : {self.__student_id}\
            \nNiveau : {self.__level}"

a_student = Student("Doe", "John", 145)
a_student.add_credits(51)
a_student.add_credits(-1.9)
a_student.add_credits(7)
a_student.add_credits("test")
a_student.add_credits(23)

firstname = a_student.get_firstname()
lastname = a_student.get_lastname()
level = a_student.get_student_level()
print(f"Le nombre de crédits de {firstname} {lastname} est de {a_student.get_credits()} points, son niveau est {level}")


print(a_student.student_info())