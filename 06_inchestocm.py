# 1 inch = 2.54 cm
from typing import ChainMap


def conversion(inch):
    p = inch*2.54 
    return p
inch = eval(input("Enter the dimension in inch: "))
print("The given dimension in cm is ", conversion(inch), "cm")