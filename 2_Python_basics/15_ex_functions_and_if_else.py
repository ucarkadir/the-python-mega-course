def string_length(mystring):
     if type(mystring) == int:
         return "Sorry, integers don't have length"
     elif type(mystring) == float:
         return "Sorry, floats don't have length"
     else:
         return len(mystring)

print(string_length(10))        # Sorry integers don't have length
print(string_length("1.0"))     # 2

print(string_length(10.00))     # Sorry floats don't have length
print(string_length("10.00"))   # 25