'''
MAP function
'''
a = [1, 2, 3, 4, 5]
def sqrt (a):
    return a ** 2
b = list(map(sqrt, a))
print(b)
'''
using MAP function and LAMBDA function 
'''
a = [1, 2, 3, 4, 5]
b = list(map(lambda a : a**2 ,a))
print(b)