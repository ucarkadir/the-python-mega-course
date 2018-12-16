# metin dosyasına ilave etmek ve okumak için "a+" modu kullanılır. 
myfile = open("employees2.txt","a+") 
myfile.read()

myfile.seek(0)
myfile.read()

myfile.write("John")
myfile.read()

myfile.close()