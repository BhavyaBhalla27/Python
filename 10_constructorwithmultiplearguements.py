class Employee:
    company = "Google"
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print(f"The employee is created by the name {self.name} and the salary of employee is {self.salary}\nHe will be working in the subunit {self.subunit}.")

        

harry = Employee("Harry", 100000, "YouTube") 
print("\n") 
bhavya = Employee("Bhavya", 1000000, "Google")
