myDict = {"Fast":"Quickly", "Bhavya":"Coder", "Marks": "[1,2,3]", "anotherDict":{'bhavya':'player'}}
# Keys in the form of list
print(myDict.keys())
# Values in the form of list
print(myDict.values())
# Key-value pair in form of tuple
print(myDict.items())
# Updating the Dictionary
updateDict= {"Bhavya":"Dancer", "Nasty":"Unpleasent"}
myDict.update(updateDict)
print(myDict)
# Get 
print(myDict.get("Bhavya"))     # Prints value associated with Bhavya that is Dancer
print(myDict.get("Bhavya2"))    # Gives none as it is not present in the dictionary
print(myDict["Bhavya2"])        # Throws error as it is not present in the dictionary