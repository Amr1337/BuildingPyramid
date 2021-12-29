#Write a Python program to find whether a given number (accept from the user)#
# is even or odd, print out an appropriate message to the user.

userInput =eval(input("Please Enter a random number: "))

if userInput % 2 == 0:
    print("the given number "+str(userInput)+" is even")
else:
    print("The given number "+str(userInput)+" is odd")