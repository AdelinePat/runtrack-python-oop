class Book():
    def __init__(self, title, author, pages_number, available = True):
        self.__title = title
        self.__author = author
        self.__pages_number = pages_number
        self.__available = available
    
    def set_title(self, new_title):
        self.__title = new_title

    def set_author(self, new_author):
        self.__author = new_author

    def set_pages_number(self, new_pages_number):
        if type(new_pages_number) is int and new_pages_number > 0:
            self.__pages_number = new_pages_number
        else:
            print("Vous ne pouvez ajouter que des nombres entier positif au nombre de pages !!")
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_pages_number(self):
        return self.__pages_number
    
    def get_availability(self):
        return self.__available
    
    def check_availability(self):
        if self.__available:
            return True
        else:
            return False
        
    def rent_book(self):
        if self.check_availability():
            self.__available = False
            print(f"\nVous avez emprunté {self.__title} avec succès")
        else:
            print("\nVous ne pouvez pas emprunter ce livre, attendez qu'il soit rendu pour pouvoir l'emprunter")

    def return_book(self):
        if not self.check_availability():
            self.__available = True
            print(f"\nVous avez rendu {self.__title} avec succès")
        else:
            print("\nVous ne pouvez pas rendre un livre que vous n'avez pas emprunté")


my_book = Book("1984", "Georges Orwell", 482)

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

my_book.rent_book()
print(my_book.get_availability())

my_book.return_book()
print(my_book.get_availability())
