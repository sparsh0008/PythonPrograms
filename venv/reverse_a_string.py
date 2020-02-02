def myString(str):
    length = len(str)
    for i in range(length-1,-1,-1):
        yield str[i]

def main():
    a = (myString("hello"))
    for i in a:
        print(i)

if __name__ == '__main__':
    main()