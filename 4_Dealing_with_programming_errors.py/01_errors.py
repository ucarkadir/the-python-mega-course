#Syntax Error

print(1)
int(9)
int(9) # int 9 - SyntaxError: invalid syntax
print(2)
print(3) # print 3 - SyntaxError: Missing parentheses in call to 'print'. Did you mean print(3)

# Exceptions

a = 1
b = "2"
print(int(2.5)) # 2
print(a + float(b)) # 3.0
print(str(a) + b) # 12
c = 3
print(c) # print(c) - NameError: name 'c' is not defined
print(c/0) # ZeroDivisionError: integer division or modulo by zero


# mydict = ["name":"John", "surname":"Smith"] - SyntaxError: invalid syntax
mydict = {"name":"John", "surname":"Smith"} 
print(mydict) 

a = [1,2,3] # a = [1, 2, 3} - SyntaxError: invalid syntax

print("John") # print(John) - NameError: name 'Kadir' is not defined

mylist = ["John", "Jack", "Jim"] # mylist = [John, Jack, Jim] - NameError: name 'John' is not defined 
print(mylist) 