with open('four.txt' , 'r') as f:
    content = f.read()
content = content.replace("Donkey", "######")
with open('four.txt' , 'w') as f:
    f.write(content)

