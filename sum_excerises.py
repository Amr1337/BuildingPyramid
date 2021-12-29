#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

def sum(a, b):
    if a+b>15 and a+b <20:
        return 20
    else:
        sum = a+b
        return sum

print(sum(4,5))
print(sum(10,6))
print(sum(10,5))
