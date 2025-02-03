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