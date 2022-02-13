class Employee:
    company = "Google"
    salary = 10000
    salarybonus = 5000

    @property
    def totalsalary(self):
        return self.salary + self.salarybonus
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalsalary)
e.totalsalary = 12000
print(e.salary)
print(e.salarybonus)