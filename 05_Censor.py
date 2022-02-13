words = ["Donkey","Lion","Monkey"]
with open('censor.txt' , 'r') as f:
        content = f.read()
for word in words:
    content = content.replace(word, "######")
with open('censor.txt' , 'w') as f:
    f.write(content)
