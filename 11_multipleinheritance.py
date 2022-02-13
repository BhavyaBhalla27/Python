class Employee:
    company = "Micromax"
class FreeLancer:
    company = "Google"
    level = 0
    def upgradeLevel(self):
        self.level = self.level + 1
class Programmer(Employee, FreeLancer):
    name = "Bhavya"

p = Programmer()
print(p.company)                  # Inherits common part that is company from the upper defined parameter in Programmer class .
p.upgradeLevel()                   
print(p.level)
p.upgradeLevel()
print(p.level)