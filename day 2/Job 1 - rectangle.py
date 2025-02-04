class Rectangle():
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    
    def set_length(self, new_length):
        self.__length = new_length
    
    def get_length(self):
        return self.__length

    def set_width(self, new_width):
        self.__width = new_width
    
    def get_width(self):
        return self.__width


my_rectangle = Rectangle(10, 5)
print(f"Longueur : {my_rectangle.get_length()} \nLargeur : {my_rectangle.get_width()}\n")
my_rectangle.set_length(12)
my_rectangle.set_width(8)
print(f"Longueur : {my_rectangle.get_length()} \nLargeur : {my_rectangle.get_width()}")
