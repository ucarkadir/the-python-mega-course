myfile = open("example.txt","w")
myfile.write("Something")
myfile.close()

# bu şekilde yazım de senin için dosyayı açar ve kapatır.
with open("example.txt","w") as myfile:
    myfile.write("something2")