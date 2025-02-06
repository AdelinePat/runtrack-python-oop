class Rectangle():
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_perimeter(self):
        return (self.__length + self.__width) * 2
    
    def get_area(self):
        return self.__length * self.__width
    
    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width
    
    def set_length(self, new_length):
        self.__length = new_length

    def set_width(self, new_width):
        self.__width = new_width

class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.__height = height
    
    def get_volume(self):
        return self.get_width() * self.get_length() * self.get_height()

    def get_height(self):
        return self.__height 

my_rectangle = Rectangle(3,4)
print("=== RECTANGLE ==")
print(f"longueur : {my_rectangle.get_length()}\
      \nlargeur : {my_rectangle.get_width()}\
      \npérimètre : {my_rectangle.get_perimeter()}\
      \naire : {my_rectangle.get_area()}\n")
my_rectangle.set_length(5)
my_rectangle.set_width(3)

print(f"longueur : {my_rectangle.get_length()}\
      \nlargeur : {my_rectangle.get_width()}\
      \npérimètre : {my_rectangle.get_perimeter()}\
      \naire : {my_rectangle.get_area()}\n")

my_parallelepiped = Parallelepiped(4,3,2)

print("\n=== PARALLELEPIPEDE ===")
print(f"longueur : {my_parallelepiped.get_length()}\
      \nlargeur : {my_parallelepiped.get_width()}\
      \npérimètre : {my_parallelepiped.get_perimeter()}\
      \naire : {my_parallelepiped.get_area()}\
      \nvolume : {my_parallelepiped.get_volume()}\n")

my_parallelepiped.set_length(5)
my_parallelepiped.set_width(4)

print(f"longueur : {my_parallelepiped.get_length()}\
      \nlargeur : {my_parallelepiped.get_width()}\
      \npérimètre : {my_parallelepiped.get_perimeter()}\
      \naire : {my_parallelepiped.get_area()}\
      \nvolume : {my_parallelepiped.get_volume()}")