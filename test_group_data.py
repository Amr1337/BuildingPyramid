#Write a Python program to check whether a specified value is contained in a group of values.
#Test Data :
#3 -> [1, 5, 8, 3] : True
#-1 -> [1, 5, 8, 3] : False

def checkValue(num,lst):
    for i in range(len(lst)):
        if lst[i] ==num:
            return True
    else:
        return False

print(checkValue(3,[1,5,8,3]))
print(checkValue(-1,[1,5,8,3]))