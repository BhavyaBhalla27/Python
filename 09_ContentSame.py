file1 = "bhavya.txt"
file2 = "copybhavya.txt"

with open('bhavya.txt', 'r') as f:
    content1 = f.read()
with open('copybhavya.txt', 'r') as g:
    content2 = g.read()

if content1 == content2:
    print("The contents are same")
else:
    print("Contents are not same")
