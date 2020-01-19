'''
FILTER In Built Function

a = [1, 2, 3, 4, 5]
def even(a):
    if(a % 2 == 0):
        return a
b = list(filter(even, a))
print(b)
'''
'''
Using FILTER and LAMBDA function simultaneously
'''
a = [1, 2, 3, 4, 5]

c = list(filter(lambda a : a % 2 == 0,a))
print(c)
