myfile = open("files/sample.txt")

'''
type(myfile) # _io.TextIOWrapper
dir(myfile) # tüm özelliklerinin bilgisini bize verir
myfile.read() # 'apple\norange\nbanana\n'
myfile.seek(0)
'''

content = myfile.read()
myfile.close()

print(content)

