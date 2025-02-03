print("\n=== JOB 9 ===")
"""
Job 9
"""
class Product():
    def __init__(self, name, priceExludeTaxes, VAT):
        self.name = name
        self.priceExludeTaxes = priceExludeTaxes
        self.VAT = VAT
        self.price = self.calculate_full_price()

    def calculate_full_price(self):
        full_price = self.priceExludeTaxes + (self.priceExludeTaxes / 100) * self.VAT
        return full_price
    
    def change_name(self, new_name):
        self.name = new_name

    def change_priceExludeTaxes(self, new_price):
        self.priceExludeTaxes = new_price

    def display_info(self):
        self.__str__()

    def __str__(self):
        print(f"Nom : {self.name}\
              \nPrix HT : {self.priceExludeTaxes}\
              \nTVA : {self.VAT}\
              \nPrix TTC : {self.price}")

chips = Product("chips", 5, 20)
café = Product("chips", 3, 15)

chips.display_info()
chips.change_priceExludeTaxes(10)

café.display_info()
café.change_name("Mocha")

chips.display_info()
café.display_info()