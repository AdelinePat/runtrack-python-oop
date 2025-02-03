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
        self.__str__()

    def __str__(self):
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