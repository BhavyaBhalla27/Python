name = input("Enter your name: ")
date= input("Enter today's date: ")
letter = '''Dear <|NAME|>
You are selected!
Date: <|DATE|>'''
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)