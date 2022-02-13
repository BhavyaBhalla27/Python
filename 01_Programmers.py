class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,post):
        self.name = name 
        self.salary = salary
        self.post = post
        print(f"{self.name} is working at {self.company} and he is earning {self.salary} per month. His post is {self.post}")

bhavya = Programmer("Bhavya","200000", "Senior SE")
mitu = Programmer("Mitu","150000","SE")
harry = Programmer("Harry","100000","Consultant")