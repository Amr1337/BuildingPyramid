#Write a Python program to check whether a file exists.

my_file = open("NewOOP.py")

try:
    my_file.close()
    print("file Exists")
except FileNotFoundError:
    print("file not found")

