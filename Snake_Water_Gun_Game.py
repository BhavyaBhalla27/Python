import random
def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False 
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False 
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False 

print("Computer turn: Snake(s), Water(w) or Gun(g): ")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your turn: Snake(s), Water(w) or Gun(g): ")
a = gameWin(comp,you)

print("Computer choose ", comp)
print("You choose ", you)

if a == None:
    print("Game is a tie!")
elif a:
    print("You won")
else:
    print("You lose")
