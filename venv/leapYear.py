def main():
    year = 2012
    if(year%4 )== 0:
        if(year%100 == 0):
            if(year%400 == 0):
                print("It is leap year")
            else:
                print("not a leap year")
        else:
            print("Year you entered is a leap year")
    else:
        print("Year you entered is not a leap year")

if __name__ == '__main__':
    main()
