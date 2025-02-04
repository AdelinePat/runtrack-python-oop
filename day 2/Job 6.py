import random

class Command():
    number_id = random.randrange(0, 100)
    def __init__(self, dishes_dict):
        self.dishes_dict = dishes_dict
        self.__dish_list = []
        self.__status = ""
        self.__command_id = Command.number_id
        self.vat = (20/100)

    def add_dish(self, new_dish):
        if new_dish in self.dishes_dict:
            self.__dish_list.append(new_dish)
            self.__status = "in progress"
        else:
            print("vous ne pouvez pas commander ce plat")
    
    # def __set_command_id(self):
    #     self.__command_id = random.randrange(0, 100)
    #     return self.__command_id

    def cancel_command(self):
        self.__dish_list = []
        self.__status = "canceled"
        return self.__status
    
    def edit_command_id(self, new_id):
        self.__command_id += new_id

    def get_command_id(self):
        return self.__command_id
    
    def get_status(self):
        return self.__status
    
    def __calculate_price(self):
        if len(self.__dish_list) > 0:
            self.__price = 0
            for each_dish in self.__dish_list:
                self.__price += self.dishes_dict[each_dish]
                self.__status = "done"
            return self.__price
        else:
            self.__price = 0
            print("Vous n'avez encore rien commandé")
    
    def get_priceWithTaxes(self):
        if self.__status == "canceled":
            return 0
        else:
            self.__price = self.__calculate_price()
            return self.__price

    def get_priceWithoutTaxes(self):
        self.__price = self.__calculate_price()
        if self.__price:
            self.__priceExludeTaxes = self.__price / (1 + self.vat)
            return self.__priceExludeTaxes
        else:
            return 0

def main():
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

    my_command = Command(dishes_dict)
    other_command = Command(dishes_dict)
    third_command = Command(dishes_dict)

    command_list = [my_command, other_command, third_command]

    for index in range(len(command_list)):
        command_list[index].edit_command_id(index)
    
    my_command.add_dish("poulet au curry")
    my_command.add_dish("ravioli")
    my_command.add_dish("ravioli")
    print(f"first command status {my_command.get_status()}")
    my_command.add_dish("lasagne")
    my_command.add_dish("burger")
    
    other_command.add_dish("tenders et frites")
    other_command.add_dish("pizza 4 fromages")
    other_command.add_dish("katsutori")
    print(f"second command status {other_command.get_status()}")
    other_command.cancel_command()
    print(f"second command status {other_command.get_status()}\n")


    third_command.add_dish("pâtes au pesto")
    third_command.add_dish("lasagne")
    third_command.add_dish("beignets d'aubergine")

    for command in command_list:
        print(f"=== COMMAND n°{command.get_command_id()- int(Command.number_id) +1} ===\
            \nPrice with taxes : {command.get_priceWithTaxes()}\
            \nPrice without taxes : {command.get_priceWithoutTaxes()}\
            \ncommand_id : {command.get_command_id()}\
            \ncommand status : {command.get_status()}\n")
main()
