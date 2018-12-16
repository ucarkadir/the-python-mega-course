mylist = [1,2,3,4,5]

for i in mylist:
    print(i)


mylist = ["Terribly Tricky"] 
for word in mylist:
    # print(word) # Terribly Tricky   
    # word = word.splitlines()  
    for letter in word[-6:]:
        print(letter)