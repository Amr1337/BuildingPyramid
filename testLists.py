d = {
    "January": 2200,
    "February": 2350,
    "March": 2600,
    "April": 2130,
    "May": 2190
}


l = list(d.items())
print(l)
print(l[1][1] - l[0][1])

#extracting the values from the dic into a list
myList = list(d.values())
print(myList)
extraDollars = myList[1]-myList[0]
print(extraDollars)
sum_first_quarter=0

#expense of first three months
for i in range(3):
    sum_first_quarter += myList[i]
print(sum_first_quarter)
#checking if there is a month with 2000$ exactly

months= list(d.keys())
print(months)
for i in myList:
    if i == 2000:
        print("The Month where we spent 2000 exactly is: ",months[i])
else:
        print("There isn't any months with exactly 2000$")

#adding June
myNewList = list(d.items())
l.append(("June", 1980))
print(myNewList)
print(l)
#applying refund to april

l.pop(3)
newApril = ("April", 1980)

l.insert(3 ,newApril)
print(l)