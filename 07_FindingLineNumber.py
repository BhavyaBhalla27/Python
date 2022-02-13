content = True
i = 1
with open('log.txt','r') as f:
    while content:
        content = f.readline()
        if 'python' in content:
            print(content)
            print("Yes python is present in line number", str(i))
            i = i + 1
