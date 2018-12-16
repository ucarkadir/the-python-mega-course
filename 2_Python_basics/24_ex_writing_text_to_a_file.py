myfile = open("employees.txt", "w")
myfile.write("mike")
myfile.close()

myfile = open("employees.txt","w")
myfile.write("Mike\nJoe\nJack")
myfile.close()

myfile = open("employees2.txt", "w")
myfile.write("Mike")
myfile.write("\nJoe")
myfile.close()
