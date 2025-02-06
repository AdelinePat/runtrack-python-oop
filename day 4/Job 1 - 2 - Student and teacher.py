class Person():
    def __init__(self, age=14):
        # self.name = name
        self.age = age

    def display_age(self):
        return f"{self.age} ans"
    
    def hello(self):
        return "Hello"
        # print(f"Hello, je suis {self.name}")
    
    def set_age(self, new_age):
        self.age = new_age

class Student(Person):
    def __init__(self):
        super().__init__()
    
    def go_to_school(self):
        return "Je vais en cours"

    def display_age(self):
        return f"J'ai {self.age} ans"

class Teacher(Person):
    def __init__(self, subject, age):
        super().__init__(age)
        self.__subject = subject

    def teaching(self):
        return f"Le cours de {self.get_subject()} va commencer"
    
    def get_subject(self):
        return self.__subject

a_person = Person()
a_student = Student()
a_teacher = Teacher("math", 40)

print(f"ELEVE : {a_student.display_age()}")

print(f"ELEVE : {a_student.hello()}")
print(f"ELEVE : {a_student.go_to_school()}")
a_student.set_age(15)
print(f"ELEVE : {a_student.display_age()}")

print(f"PROF : {a_teacher.display_age()}")
print(f"PROF : {a_teacher.hello()}")
print(f"PROF : {a_teacher.teaching()}")