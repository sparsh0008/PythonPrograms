class Parrot:

    def __init__(self, name):
        self.name = name
        #self.age = age


    def sing(self, song):
        print("{0} sings {1} song".format(self.name, song))
        return 0


    def dance(self):
        print("{0} is now dancing".format(self.name))
        return 0

def main():
    MithuObj = Parrot("Mithu")
    GudduObj = Parrot("Guddu")

    MithuObj.sing('Happiness')
    GudduObj.sing('Perfect')

    MithuObj.dance()
    GudduObj.dance()

if __name__ == "__main__":
    main()