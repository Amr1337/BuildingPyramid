#Write a Python program to get the n (non-negative integer) copies of the first 2
#characters of a given string. Return the n copies of the whole string if the length is less than 2.

def charExt(str,n):
    newStr=str[0]+str[1]
    #for i in range(n):
    if len(str)<2:
            return str
    else:
        return newStr*n

print(charExt("abcde",5))
print(charExt("Amro",7))
print(charExt("ab",6))