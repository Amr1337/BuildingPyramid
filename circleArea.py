import math
#taking input from user
userInput=eval(input("Please enter the radius of the circle: "))

print("r= ",userInput)

#powering input with 2
inputPow= pow(userInput, 2)

#calculating the circle area
circleArea= inputPow*3.14
print("Area= ",circleArea)