def remove_and_strip(string, word):
    newString = string.replace(word, "")
    return newString.strip()
a = "     Bhavya is a good coder      "
b= remove_and_strip(a,"Bhavya")
print(b)