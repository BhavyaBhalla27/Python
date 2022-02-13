class Employee:
    company = ""
    def getsalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")

bhavya = Employee()
bhavya.company = "Google"
bhavya.salary = "150000"
bhavya.getsalary()           # Employee.getsalary(bhavya)