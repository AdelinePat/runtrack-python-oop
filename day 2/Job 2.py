class Book():
    def __init__(self, title, author, pages_number):
        self.__title = title
        self.__author = author
        self.__pages_number = pages_number
    
    def set_title(self, new_title):
        self.__title = new_title

    def set_author(self, new_author):
        self.__author = new_author

    def set_pages_number(self, new_pages_number):
        if new_pages_number is int and new_pages_number > 0:
            self.__pages_number = new_pages_number
        else:
            print("Vous ne pouvez ajouter que des nombres entier positif au nombre de pages !!")
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_pages_number(self):
        return self.__pages_number
    
    def __str__(self):
        return f"Titre : {self.__title}\
            \nAuteur : {self.__author}\
            \nPages : {self.__pages_number}"

my_book = Book("1984", "Georges Orwell", 482)
# print(my_book)

title = my_book.get_title()
author = my_book.get_author()
pages = my_book.get_pages_number()
string = f"Titre : {title}\
            \nAuteur : {author}\
            \nPages : {pages}\n"
print(string)

my_book.set_author("Isaac Asimov")
my_book.set_title("Fondation")
my_book.set_pages_number("256")

print(f"Titre : {my_book.get_author()}\
\nAuteur : {my_book.get_title()}\
\nPages : {my_book.get_pages_number()}\n")

my_book.set_pages_number(-12)
print(f"Titre : {my_book.get_author()}\
\nAuteur : {my_book.get_title()}\
\nPages : {my_book.get_pages_number()}\n")

my_book.set_pages_number(256)
print(f"Titre : {my_book.get_author()}\
\nAuteur : {my_book.get_title()}\
\nPages : {my_book.get_pages_number()}\n")
