class Employee:
    company = "Microsoft"

    def showDetails(self):
        print("This is an employee of Microsoft")

class Programmer(Employee):
    language = "Python"
    
    def getLang(self):
        print(f"This programmer know {self.language}")

    def showDetails(self):                               # Overwriting 
        print("This is an employee of Google")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
p.getLang()

    