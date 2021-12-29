from functools import reduce

def func(a, b):
    return a * b


result = lambda a, b: a * b
#print(result(3, 5))

def isEven(n):
    return n % 2 == 0

nums=[3, 2, 5, 6, 4, 2, 18]

eN = list(filter(lambda n : n % 2 == 0, nums))
print(eN)

doubles = list(map(lambda n : n * 2, nums))
print(doubles)
doubles = list(map(lambda n : n * 2, nums))
print(doubles)

addOne = map(lambda a : a+1, nums)
print(list(addOne))

sum = reduce(lambda a, b: a + b, nums)
print(sum)