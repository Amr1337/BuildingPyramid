#Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return three times of their sum

#def num_calc(a,b,c):

#    if a ==b & b==c:
 #       return 3*(a+b+c)
  #  else:
   #     return a+b+c

#print(num_calc(1,2,3))
#print(num_calc(3,3,3))

def num_calc1(a,b,c):
    sum=a+b+c
    if a==b==c:
        sum=3*sum
    return sum
  #  else:
      #  return sum

print(num_calc1(3,3,3))
print(num_calc1(1,2,3))
