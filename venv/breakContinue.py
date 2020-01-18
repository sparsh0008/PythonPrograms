i = -1
a = "Hello world"
while(i < len(a)-1):
    i = i + 1
    if(a[i] == "o"):
        continue
    print(a[i])
print("Out of the while loop")
