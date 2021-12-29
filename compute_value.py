# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#input 5, answer should be 615

n=input("Write an input of n: ")

n1=n+n
n1=int(n1)

n2=n+n+n
n2=int(n2)

n=int(n)
result=n+n1+n2
print(result)