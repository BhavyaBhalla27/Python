number = int(input("Enter your marks to get the grade:\n"))
if (number>=90):
    print("Your grade is Ex")
elif (number>=80 and number<90):
    print("Your grade is A")
elif (number>=70 and number <80):
    print("Your grade is B")
elif (number>=60 and number <70):
    print("Your grade is C")
elif (number>=50 and number <60):
    print("Your grade is D")
else:
    print("Your grade is F")