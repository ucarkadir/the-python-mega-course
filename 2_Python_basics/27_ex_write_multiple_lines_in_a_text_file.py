numbers = [1,2,3]
myfile = open("mynumbers.txt","w")
for n in numbers:
    myfile.write(str(n) + "\n")
myfile.close()

