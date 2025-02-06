class Shape():
    def get_area():
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.length * self.width
    
a_rectangle = Rectangle(5,6)

print(a_rectangle.get_area())