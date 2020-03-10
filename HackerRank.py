def count_substring(string, sub_string):
    j = 0
    count = 0
    for i in range(len(string)):
       if(string[i] == sub_string[j]):

           if(j == len(sub_string) - 1):
               count = count + 1
               j = 0
               if(string[i] == sub_string[j]):
                    j = j + 1
               continue

           j = j + 1
       else:
           j = 0

    return count

if __name__ == '__main__':
    a = input("Enter a String")
    b = input("Enter a Sub String")
    c = count_substring(a,b)
    print(c)

'''
ThIsisCoNfUsInG
WoW!ItSCoOWoWW
'''