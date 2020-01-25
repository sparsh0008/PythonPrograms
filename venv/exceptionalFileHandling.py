try:
    num = input("Enter a number: ")
    print(num/0)
except Exception as exp:
    print("Error is {0} ".format(exp))
