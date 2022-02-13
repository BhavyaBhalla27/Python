def factorial(n):
    if n ==1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter the number: "))
print("The factorial of the entered number is", factorial(n))