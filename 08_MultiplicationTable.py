def table(num):
    for i in range(1,11):
         print(str(num) + "X" + str(i) + "=" + str(num*i))
num = int(input("Enter the number: "))
print("The multiplication table of the given number is below: ")
table(num)