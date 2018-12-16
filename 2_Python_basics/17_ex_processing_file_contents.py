myfile = open("sample.txt")
fruits = myfile.read()
fruits = fruits.splitlines() # fruitst nesnesine dizi haline dönüştürür
print("Fruits: \n" , fruits) # print(r"Fruits\n", fruits)

print("Hello\nWorld")
'''
Hello
Wordl
'''
print(r"\nHello\nWorld") # Hello\nWorld
print("Hello\nWorld\nHere".splitlines()) # ['Hello', 'Wordl', 'Here']
print("Here" in ['Hello', 'Wordl', 'Here']) # True