class Number:
    def __init__(self,num1):
        self.num1 = num1
    
    def __add__(self,num2):
        
        print("lets add")
        return self.num1 + num2.num1

    def __mul__(self,num2):
        
        print("lets multiply")
        return self.num1 * num2.num1

num1 = Number(4)
num2 = Number(6)
sum = num1 + num2
mul = num1 * num2 
print(sum)
print(mul)
    