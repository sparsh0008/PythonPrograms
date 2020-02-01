class Abc:
    def __repr__(self):
        return  "I'm in __repr__(self)"
    def __str__(self):
        return  "I'm in __str__(self)"
    def display(self):
        return "I'm in display(self)"

def main():
    obj = Abc()
    print ([obj])
    print(obj.display())

if __name__ == "__main__":
    main()