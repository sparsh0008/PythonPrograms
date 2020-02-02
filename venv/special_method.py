'''
operator overloading
'''
class Abc:
    def __init__(self, val1, val2):
        self.a = val1
        self.b = val2
    def __add__(self, sobj):
        a = self.a + sobj.a
        b = self.b + sobj.b
        return (a , b)

def main():
    obj1 = Abc(2,3)
    obj2 = Abc(4,5)

    print(obj1 + obj2)

if __name__ == '__main__':
    main()