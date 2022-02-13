f = open('bhavya.txt','r')
data = f.readline()
print(data,end="")           # Prints the first line that is Bhavya is a good boy
data = f.readline()
print(data)                  # Prints the second line that is he is the best
f.close()
