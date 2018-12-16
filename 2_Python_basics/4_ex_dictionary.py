pins = {"Mike":1234, "Joe":1111, "Jack":2222}

print(pins["Mike"]) # 1234
print(pins.keys()) # ['Mike', 'Joe', 'Jack']
print(pins.values()) # [1234, 1111, 2222]

person97 = {"name":"Jack", "surname":"Smith" ,"age":"29" }
person97.pop("name") 
print(person97) # {'age': '29', 'surname': 'Smith'}
person97["name"]="Jack"
print(person97) # {'age': '29', 'surname': 'Smith', 'name': 'Jack'}
person97["age"] = 30
print(person97) # {'age': 30, 'surname': 'Smith', 'name': 'Jack'}

# mapping two lists to a dictionary
keys = ["a","b","c"]
values = [1,2,3]
mydict = dict(zip(keys,values)) 
print(mydict)

