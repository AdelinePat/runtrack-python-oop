class BankAccount():
    def __init__(self, lastname, firstname, account_number, balance):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__account_number = account_number
        self.__balance = balance
        self.__overdraft = True
    
    def display_info(self):
        return f"{self.get_lastname()} {self.get_firstname()}\
            \nN° de compte : {self.get_account_number()}\
            \nSolde : {self.get_balance()}"
    
    def display_balance(self):
        return self.get_balance()
    
    def add_to_balance(self, payment):
        self.__balance = self.get_balance() + payment

    def withdrawal(self, widthdrawal_amount):
        if self.get_balance() - widthdrawal_amount >= 0:
            self.__balance = self.get_balance() - widthdrawal_amount
        else:
            if self.__overdraft == False:
                print("Arretez de dépenser l'argent que vous n'avez pas : allez travailler !")
            else:
                self.__balance = self.get_balance() - widthdrawal_amount + self.agios(widthdrawal_amount)
            
    def agios(self, widthdrawal_amount):
        agios = (self.get_balance() - widthdrawal_amount) * 12/100
        return agios

    def bank_transfer(self, beneficiary, payment):
        if self.get_balance() - payment >= 0:
            self.__balance = self.get_balance() - payment
            beneficiary.__balance += payment
        else:
            if self.__overdraft == False:
                print("Arretez de dépenser l'argent que vous n'avez pas : allez travailler !")
            else:
                self.__balance = self.get_balance() - payment + self.agios(payment)
                beneficiary.__balance += payment

    def get_lastname(self):
        return self.__lastname
    def get_firstname(self):
        return self.__firstname
    def get_account_number(self):
        return self.__account_number
    def get_balance(self):
        return self.__balance
    
sari = BankAccount("Sari", "Norumai", 1234, 100)
print(sari.display_info())

print(sari.display_balance())

malia = BankAccount("Malia", "Jodeli", 5678, -50)
print(malia.display_info())
sari.bank_transfer(malia, 70)

print(f"Solde Sari : {sari.display_balance()}\
      \nSolde Malia :{malia.display_balance()}\n")

malia.bank_transfer(sari, 10)

print(f"Solde Sari : {sari.display_balance()}\
      \nSolde Malia : {malia.display_balance()}\n")

sari.add_to_balance(200)
sari.withdrawal(50)
malia.add_to_balance(1000)
malia.bank_transfer(sari, 300)
malia.withdrawal(800)

print(f"Solde Sari : {sari.display_balance()}\
      \nSolde Malia : {malia.display_balance()}\n")


    