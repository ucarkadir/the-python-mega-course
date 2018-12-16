myfile = open("fruits.txt")

content = myfile.read()
content = content.splitlines()
myfile.close()

for i in content:
    print(len(i))


file = open("fruits.txt")
content = file.readlines()
content = [line.strip() for line in content]
print (content)
file.close()

for i in content:
    print(i)