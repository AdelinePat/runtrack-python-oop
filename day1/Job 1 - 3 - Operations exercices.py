print("\n=== JOB 1 à 3 ===")

class Operation_job1():
    def __init__(self, number1=12, number2=3):
        self.number1 = number1
        self.number2 = number2
    
an_operation = Operation_job1()
print(an_operation)
print(an_operation.number1)
print(an_operation.number2)

"""
Job 1 to 3
"""
class Operation():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        self.operator = ""
        self.result = ""

    # Job 3
    def addition(self):
        self.result = self.number1 + self.number2
        self.operator = "+"
        
    def soustraction(self):
        self.result = self.number1 - self.number2
        self.operator = "-"
    
    def multiply(self):
        self.result = self.number1 * self.number2
        self.operator = "*"
    
    def division(self):
        try:
            if self.number2 == 0:
                self.result = "IMPOSSIBLE"
                self.operator = "/"
                raise ZeroDivisionError("la division par 0 est impossible")
            else:
                self.result = self.number1 / self.number2
                self.operator = "/"
        except ZeroDivisionError as message:
            print(message)

    # Job 1 & Job 2
    def calculate(self, operator):
        self.operator = operator

        try:
            match operator:
                case "+":
                    self.result = self.number1 + self.number2
                case "-":
                    self.result = self.number1 - self.number2
                case "/":
                    if self.number2 == 0:
                        self.result = "IMPOSSIBLE"
                        raise ZeroDivisionError("La division par 0 est impossible")
                    else:
                      self.result = self.number1 / self.number2
                case "*":
                    self.result = self.number1 * self.number2
        except ZeroDivisionError as message:
            print(message)

    def __str__(self): 
        return f"{self.number1} {self.operator} {self.number2} = {self.result}"

operation = Operation(8, 0)
operation.calculate("/")
print(operation)

other_operation = Operation(8,2)
other_operation.multiply()
print(other_operation)