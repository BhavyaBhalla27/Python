def mySum(n):
    mySum = 0
    for i in range(n):
        mySum = mySum + (i+1)
    return mySum
s = mySum(89)
print(s)