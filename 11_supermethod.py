class Person():
    company = "Google"
    country = "India"
    def __init__(self):
        print("Intialising Person\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"
    salary = "300000"
    def __init__(self):
        super().__init__()
        print("Intialising Employee\n")
        
    def getSalary(self):
        print(f"The salary is {self.salary}")
    def takeBreath(self):
        super().takeBreath()
        print("I am an employee and I am breathing...")

class Programmer(Employee):
    company = "Fiverr"
    def __init__(self):
        super().__init__()
        print("Intialising Programmer")
    def getSalary(self):
        print("no salary to them.")
    def takeBreath(self):
        super().takeBreath()
        print("I am a programmer and I am breathing...")

p = Person()
e = Employee()
pr = Programmer()

p.takeBreath()
e.takeBreath()
pr.takeBreath()
