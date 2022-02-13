class Employee:
    company = "Google"
    salary = 30000
    increment = 2000
    
    @property
    def totalSalary(self):
        return self.salary + self.increment
    @totalSalary.setter
    def totalSalary(self,val):
        self.incremet = val - self.salary

e = Employee()
e.totalSalary = 36000
print(e.totalSalary)
print(e.increment)
print(e.salary)

