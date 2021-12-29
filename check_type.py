#Write a Python program to add two objects if both objects are an integer type.

def add_object(a, b):
    if type(a) == type(b) == int:
        return  a+b
    else:
        return "not integer"


print(add_object(2,5))
print(add_object(2,7))
print(add_object(2,5.5))
print(add_object("a","1"))