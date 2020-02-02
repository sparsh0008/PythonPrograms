def mygen():
    n = 0
    print("Value for n is : {0}".format(n))
    yield n

    n = n + 1
    print("Value foe n is : {0}".format(n))
    yield n

    n = n + 1
    print("Value foe n is : {0}".format(n))
    yield n

def main():
    res = mygen()

    next(res)
    next(res)
    next(res)

if __name__ == '__main__':
    main()
