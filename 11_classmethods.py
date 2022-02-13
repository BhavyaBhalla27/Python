class Employee:
    company = "google"
    salary = 100
    location = "chandigarh"

    @classmethod                     # Changes the class attributes directly
    def changeSalary(cls , sal):        
        cls.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(300)
print(e.salary)

