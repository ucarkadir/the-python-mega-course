myfile = open("fruits.txt")
fruits = myfile.read()
myfile.close()

print(fruits)
fruits = fruits.splitlines()
print(fruits[0])

f = "orange"
if f in fruits:
    print(f)