#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5

def check_value(a, b):
    if a == b == 5:
        return True
    elif a + b == 5:
        return True
    elif a - b == 5:
        return True
    else:
        return False

print(check_value(10,5))
print(check_value(3,2))
print(check_value(10,8))

