#Write a Python program to test whether a passed letter is a vowel or not

def checkLetter(l):
    vowels="aeiouy"
    for i in vowels:
        if i==l:
            return "This letter is a vowel"
        else:
            return "this letter is not a vowel"

print(checkLetter("a"))
print(checkLetter("y"))
print(checkLetter("L"))