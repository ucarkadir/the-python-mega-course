correct_password = "python123"

name = input("Enter a name: ")
surname = input("Enter Surname: ")
password = input("Enter password: ")

while correct_password != password:
    password = input("Wrong password! Enter again: ")

 # virgüler ile stringler tanımlanabiliyor.
print("Hi", name, "you are logged in")

# % yüzde işareti ile stringler tanımlanabiliyor.
# " " çift tırnak arasına yayzılan string ifade satır sonuna ilave ediliyor
massage = "Hi %s you are logged in" % name
print(massage) 

massage ="Hi %s %s , you are logged in " % (name, surname)
print(massage)
