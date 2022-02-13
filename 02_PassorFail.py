sub1 = eval(input("Enter the marks of your first subject: "))
sub2 = eval(input("Enter the marks of your second subject: "))
sub3 = eval(input("Enter the marks of your third subject: "))
avg = (sub1 + sub2 + sub3)/3

if (sub1<33 or sub2<33 or sub3<33):
    print("You are failed due to less percentage in atleast any one of the subjects")
elif (avg<40):
    print("You are failed due to less overall percentage that is less than 40% ")
else:
    print("Congrats! You are passed")