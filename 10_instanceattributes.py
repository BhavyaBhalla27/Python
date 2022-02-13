class Employee:
    company = "google"
    salary = 100

bhavya = Employee()
mitu = Employee()
bhavya.salary = 150000        # Instance attributes 
mitu.salary = 35000           # Instance attributes
print(bhavya.salary)
print(mitu.salary)
# print(mitu.address)           # This throws an error as address is not present in instance as well as class