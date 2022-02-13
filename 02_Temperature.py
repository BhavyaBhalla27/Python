def conversion(c):
    f = (9*c)/5 + 32
    return f 
c = int(input("Enter the temp: "))
conversion(c)
print("The temperature in farh is", conversion(c))
    