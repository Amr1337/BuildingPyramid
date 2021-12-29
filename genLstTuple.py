#Write a Python program
# which accepts a sequence of comma-separated numbers from user
# and generate a list and a tuple with those numbers

values=input("Enter some comma-separated values: ")
lst=values.split(",")
tupl=tuple(lst)
print(lst)
print(tupl)