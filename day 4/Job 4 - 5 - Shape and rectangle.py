class Shape():
    def get_area():
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return self.radius ** 2 * 3.14
    
    
a_rectangle = Rectangle(5,6)
a_circle = Circle(8)
print(f"RECTANGLE : {a_rectangle.get_area()}")
print(f"CIRCLE : {a_circle.get_area()}")