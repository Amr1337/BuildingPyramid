#Write a Python program to concatenate all elements in a list into a string and return it.

def newString(listElements):
    elements=""
    for i in listElements:
        elements+=i
    return elements

print(newString(['a','b','c','d']))
newList=['Tommy','Lee','Jones']
print(newList)
print(newString(newList))