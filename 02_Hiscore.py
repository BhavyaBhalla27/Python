import random

def game():
    a = random.randint(1,100)
    return a

score = game()
with open('Hiscore.txt', 'r') as f:
    hiscore = f.read()

if hiscore == '':
    with open('Hiscore.txt', 'w') as f:
        f.write(str(score))
    
elif int(hiscore)<score:
    with open('Hiscore.txt', 'w') as f:
        f.write(str(score))
    
