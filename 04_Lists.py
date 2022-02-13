# Creating a list by enclosing it in square brackets
a = [2,4,'bhavya']
print(a)
# Access a particular index in a List
print(a[2])   # Prints bhavya
print(a[1])   # Prints 4
print(a[0:2]) # Prints index 0 and 1 that is 2,4 (List slicing)
# Changing a value in a list
b = [2,3,4,5,6,7,2.3,'bhavya','mitu']
b[2]=98
print(b)
print(b[0::4]) # Slicing having skip value=4 