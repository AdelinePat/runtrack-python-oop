import random

class Command():
    number_id = random.randrange(0, 100)

    dishes_dict = {
        "porc au caramel" : 12.50,
        "nems" : 6,
        "katsutori" : 15,
        "poulet au curry": 13.50,
        "poulet terriyaki": 12.50,
        "pizza": 14,
        "lasagne": 16.50,
        "pâtes au pesto": 14,
        "gyoza": 8,
        "ravioli": 10,
        "burger": 15,
        "beignets d'aubergine": 9,
        "tenders et frites": 13
    }

    def __init__(self):
        self.__dish_list = []
        self.__status = ""
        self.__command_id = Command.number_id
        self.__vat = 20 / 100

    def add_dish(self, new_dish):
        if new_dish in Command.dishes_dict:
            self.__dish_list.append(new_dish)
            self.__status = "in progress"
        else:
            print("vous ne pouvez pas commander ce plat")
    def set_vat(self, new_vat):
        self.__vat = new_vat / 100

    def cancel_command(self):
        self.__dish_list = []
        self.__status = "canceled"
    
    def edit_command_id(self, new_id):
        self.__command_id += new_id

    def get_command_id(self):
        return self.__command_id
    
    def get_status(self):
        return self.__status
    
    def __calculate_price(self):
        if len(self.__dish_list) > 0:
            price = 0
            for each_dish in self.__dish_list:
                price += self.dishes_dict[each_dish]
                self.__status = "done"
        else:
            price = 0
            print("Vous n'avez encore rien commandé")
        return price
    
    def get_priceWithTaxes(self):
        if self.__status == "canceled":
            priceWithTaxes = 0
        else:
            priceWithTaxes = self.__calculate_price()
        return priceWithTaxes

    def get_priceWithoutTaxes(self):
        price = self.__calculate_price()
        if price:
            priceExludeTaxes = price / (1 + self.__vat)
        else:
            priceExludeTaxes = 0

        return priceExludeTaxes

    def get_all_dishes_with_price(self):
        pass

    def display_command(self):
        all_dish_displayed = ""
        for dish in self.__dish_list:
            all_dish_displayed += "-" + dish + " " + str(Command.dishes_dict[dish]) + "€" + "\n"

        return f"=== COMMAND n°{self.get_command_id()- int(Command.number_id) +1} ===\
            \ncommand_id : {self.get_command_id()}\
            \n{all_dish_displayed}\
            \nPrice without taxes : {round(self.get_priceWithoutTaxes(), 2)} €\
            \nPrice with taxes : {round(self.get_priceWithTaxes(), 2)} €\
            \ncommand status : {self.get_status()}\n\n"

def main():
    first_command = Command()
    second_command = Command()
    third_command = Command()

    command_list = [first_command, second_command, third_command]

    for index in range(len(command_list)):
        command_list[index].edit_command_id(index)
    
    first_command.add_dish("poulet au curry")
    first_command.add_dish("ravioli")
    first_command.add_dish("ravioli")
    print(f"first command status {first_command.get_status()}")
    first_command.add_dish("lasagne")
    first_command.add_dish("burger")

    first_command.set_vat(10)
    
    second_command.add_dish("tenders et frites")
    second_command.add_dish("pizza 4 fromages")
    second_command.add_dish("katsutori")
    print(f"second command status {second_command.get_status()}")
    second_command.cancel_command()
    print(f"second command status {second_command.get_status()}\n")

    third_command.add_dish("pâtes au pesto")
    third_command.add_dish("lasagne")
    third_command.add_dish("beignets d'aubergine")

    for command in command_list:
        print(command.display_command())
main()

# e = [1,2,3]
# new_e = 2*e #immuable
# new_e_bis = e
# print(e)
# print(new_e)
# print(new_e_bis)
# new_e.append(4)
# for item in new_e_bis:
#     new_e_bis.pop()

# for item in new_e:
#     new_e.pop()

# new_e.append("mdr")
# print("\n")
# print(e)
# print(new_e)
# print(new_e_bis)
