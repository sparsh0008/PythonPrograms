a = [1,2,3,4]
# i = iter(a)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
class Abc:
    def __init__(self, mylist):
        self.mylist = mylist

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if(self.index <= len(self.mylist)):
            print(self.mylist[self.index] ** 2)
            self.index = self.index + 1

def main():
    obj = Abc(a)
    i = iter(obj)
    next(i)
    next(i)
    next(i)
    next(i)

if __name__ == '__main__':
    main()
