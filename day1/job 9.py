print("\n=== JOB 9 ===")
"""
Job 9
"""
class Product():
    def __init__(self, name, priceExludeTaxes, VAT):
        self.name = name
        self.priceExludeTaxes = priceExludeTaxes
        self.VAT = VAT / 100
        self.price = self.calculate_full_price()

    def calculate_full_price(self):
        full_price = self.priceExludeTaxes + (self.priceExludeTaxes * self.VAT) 
        return full_price
    
    def change_name(self, new_name):
        self.name = new_name

    def change_priceExludeTaxes(self, new_price):
        self.priceExludeTaxes = new_price
        self.price = self.calculate_full_price()

    def change_PriceWithTaxes(self, new_price):
        self.price = new_price
        self.priceExludeTaxes = self.calculate_priceExcludeTaxes()

    def calculate_priceExcludeTaxes(self):
        priceExludeTaxes = self.price / (1+ self.VAT)
        return priceExludeTaxes

    def display_info(self):
        self.__str__() 

    def __str__(self):
        return f"Nom : {self.name}\
              \nPrix HT : {self.priceExludeTaxes}\
              \nTVA : {int(self.VAT * 100)}%\
              \nPrix TTC : {self.price}"

chips = Product("chips", 5, 20)
café = Product("café", 3, 15)

# chips.display_info()
print(chips)
chips.change_priceExludeTaxes(10)
print("\n")
# café.display_info()
print(café)
print("\n")
café.change_name("Mocha")
café.change_PriceWithTaxes(8)

# chips.display_info()
print(chips)
print("\n")
# café.display_info()
print(café)