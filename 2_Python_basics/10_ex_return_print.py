def returning():
    return 10

def printing():
    print(100)

returning()
printing()

print(returning() + 20)
# printing() + (20)
print(type(returning())) # int
print(type(printing())) # NoneType
