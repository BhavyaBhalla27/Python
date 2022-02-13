class Person():
    company = "Google"
    country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"
    salary = "300000"
    def getSalary(self):
        print(f"The salary is {self.salary}")
    def takeBreath(self):
        print("I am an employee and I am breathing...")

class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print("no salary to them.")

p = Person()
e = Employee()
pr = Programmer()
print("***** DETAILS OF PERSON *****")
p.takeBreath()
print(p.company)
print("***** DETAILS OF EMPLOYEE *****")
print(e.company)
e.getSalary()
e.takeBreath()
print("***** DETAILS OF PROGRAMMER *****")
print(pr.company)
pr.getSalary()
pr.takeBreath()
print(pr.country)  