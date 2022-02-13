# Dictionary is created by enclosing the key-value pairs inside the curly brackets
myDict = {"Fast":"Quickly", "Bhavya":"Coder", "Marks": "[1,2,3]", "anotherDict":{'bhavya':'player'}}
print(myDict["Fast"])
print(myDict["Bhavya"])
myDict['Marks'] = [45,98]    # Dictionaries are mutable 
print(myDict["Marks"])
print(myDict["anotherDict"]['bhavya'])