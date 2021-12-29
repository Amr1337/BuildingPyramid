# Write a Python program to sum of the first n positive integers.

def sum(n):
    sum=0
    for i in range(n+1):
        sum+= i
    return sum
print(sum(8))
print(sum(2))