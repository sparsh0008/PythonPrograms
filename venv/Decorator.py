def validate(func):
    def inner(a,b):
        if(b == 0):
            print("Cannot divide by zero")
            return
        else:
            return func(a,b)
    return inner

@validate
def divide(a, b):
    c = a/b
    return c

result = divide(10,0)
if result:
    print(result)
