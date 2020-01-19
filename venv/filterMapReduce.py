from functools import reduce
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(filter(lambda a : a %2 == 0, a))
c = list(map(lambda b : b ** 2, b))
d = reduce(lambda num1, num2: num1 + num2,c)
print("All the even numbeers are :")
print(b)
print("square of all even numbers are :")
print(c)
print("So the sum of all square of even numbers are :")
print(d)