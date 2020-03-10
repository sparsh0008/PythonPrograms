a  =[1,2,3,4,5]

lg = len(a)
comma = ", "

for i in range(lg):
    if a[i] == lg:
        comma = ""
    print(a[i],end=comma)