f = open('log.txt','r')
t = f.read().lower()
if 'python' in t:
    print("python is present")
else:
    print("python is not present")
f.close()

