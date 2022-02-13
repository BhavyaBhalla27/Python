class Employee:                            # Defining a class first
    company = "google"                     # Giving class attribute in the form of company
    salary = "700000"                      # Giving class attribute in the form of salary         

bhavya = Employee()                        # Object instantiation
mitu = Employee()
print(bhavya.company)
print(mitu.company)
print(bhavya.salary)
print(mitu.salary)
Employee.company = "YouTube"               # Changing Class Attribute
Employee.salary = "60000"                  # Changing Class Attribute

print(bhavya.company)
print(mitu.company)
print(bhavya.salary)
print(mitu.salary)

