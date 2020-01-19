from functools import reduce
'''
REDUCE function 
'''
a = [1, 2, 3, 4, 5]

def red(num1, num2):
    return num1 + num2

b = reduce(red, a)
print(b)
'''
using REDUCE function and LAMBDA function 
'''
a = [1, 2, 3, 4, 5]
b = reduce(lambda num1, num2: num1 + num2, a )
print(b)
