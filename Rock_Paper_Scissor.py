import random 
def game(comp,you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True

print("Computer Turn: Rock(r), Paper(p) or Scissor(s):")
randNo = random.randint(1,3)
if randNo ==1 :
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your turn: Rock(r), Paper(p) or Scissor(s): ")
a = game(comp,you)
print("Computer choose", comp)
print("You choose", you)

if a == None:
    print("Game is a tie!")
elif a:
    print("You win")
else:
    print("You loose")
