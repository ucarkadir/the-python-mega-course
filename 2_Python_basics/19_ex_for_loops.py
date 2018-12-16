a = [1,2,3]
# print(a[0])
# print(a[1])
# print(a[2])

for item in a:
    print(item)

a= "Hello"
for item in a: # hello string dizi haline döndürüyor.
    print(item)


a= ["Hello","Hello2"] # burada dizinin içinde bulunan bir nesne olarak değerlendiriyor.
for item in a:
    print(item)


# dictionaries
pins = {"Mike":1234, "Joe":1111, "Jack":2222}

# for item in pins:
for item in pins.keys(): # her iki yazım da aynı sonucu verir
    print(item)


myfile = open("sample.txt")
c = myfile.read()
c = c.splitlines()
myfile.close()

for i in c:
    print(i)


