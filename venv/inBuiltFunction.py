'''
FILTER function
'''
a = [0, 1, 2, 3, 4, 5]
def even(a):
    if(a % 2 == 0):
        return 1
b = list(filter(even, a))
print(b)

'''
Using FILTER and LAMBDA function simultaneously
'''

a = [0, 1, 2, 3, 4, 5]

c = list(filter(lambda a : a % 2 == 0,a))
print(c)

