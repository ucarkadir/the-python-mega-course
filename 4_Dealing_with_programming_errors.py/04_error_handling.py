# def divide(a,b):
#     try:
#         return a/b
#     except:
#         return "Zero devision is meaningless"


def divide(a,b):
    try:
         return a/b
    except ZeroDivisionError:
        return "Zero devision is meaningless"
    # except TypeError:
    #     return "write correct sytnax"

print(divide(1, 0))

