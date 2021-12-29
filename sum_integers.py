# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def sum(a, b, c):
    if a == b or b == c or a == c:
        sum = 0
    else:
        sum = a + b + c
    print("Sum of 3 intergers is: ", sum)

sum(1,3,5)
sum(2,2,5)
sum(1,2,1)