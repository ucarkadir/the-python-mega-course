print(type(10)) # <class 'int'>

# dir(__bulitins__)
int(10.5) # 10
int(10.6) # 10
float(10) # 10.0
int("100") # 100
int("100") + 100 # 200
float(100.10) # 100.1
str(10) # '10'
str (10.09) # '10.09'

help(len) 
print(len('kadir'))

address = ["Flat Floor Street", 18, "New York"]
print(len(address))

print("hello"[1]) # e
print("hello","hi") # ('hello', 'hi')
 
print(address[1] + 20) # 38
print(address[-2] + 20) # 38

# from 0 to 1 : ['Flat Floor Street', 18]
# ! son index dahil edilmiyor 
print(address[0:2]) 
print(address[0:])
print(address[:])
print(address[:2])

print(address[-2:])     # -2 index to son index'e git   -->> : [18, 'New York'] 
print(address[-2:-1])   # -2 index to -1 index'e git    -->> : [18]

name = "John"
print(name[2])

name = "John Smith"
print(name[2:4])

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-2])

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[-3:-1])

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(mylist[17])

