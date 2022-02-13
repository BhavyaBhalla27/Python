with open('bhavya.txt', 'r') as f:
    a = f.read()

with open('copybhavya.txt', 'w') as f:
    f.write(a)
