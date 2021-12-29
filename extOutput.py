#Write a Python program to accept a filename from the user and print the extension of that

name=input("Enter file name: ")
f_ext= name.split(".")
print ("The extension of the file is : " + repr(f_ext[-1]))