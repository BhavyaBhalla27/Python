import random
num1 = random.randint(1,100)
guessByUser = 0
guess = 0

while guessByUser != num1:
    guessByUser = int(input("Enter your guess:\n"))
    
    if guessByUser == num1:
        print("Perfect Guess!")
    elif (guessByUser>num1):
        print("Try Again and Enter a lower number")
    elif (guessByUser<num1):
        print("Try Again and Enter a bigger number")
    guess = guess + 1

print("You guessed it right in ", guess , "turns")
