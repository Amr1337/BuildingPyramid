
def checkString(s):
    if len(s)>=2 and s[:2] =="Is":
        return s
    else:
        return "Is" + s

print(checkString("IsEmpty"))
print(checkString("Array"))