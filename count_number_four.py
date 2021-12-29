#Write a Python program to count the number 4 in a given list.

def lstCounter(lst):
    count=0
    for i in range(len(lst)):
        if lst[i]==4:
            count+=1
    return count

print(lstCounter([1,4,2,5,4]))
print(lstCounter([4,4,4,4,5,4]))




#lst=[4,3,2,4]
#count=0
#for i in range(len(lst)):
#    if lst[i]==4:
#        count+=1
#print(count)
