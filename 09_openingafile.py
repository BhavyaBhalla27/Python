# We will use open function to open the file
a = open('bhavya.txt','r')
# data = a.read(5)             # Reads only first five characters from the file
data = a.read()              # Reads all the characters 
print(data) 
a.close()                  # Closing a file
  