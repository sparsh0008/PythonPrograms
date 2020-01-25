password = 1234
choose = int(input("enter password : "))
if(choose == password):
    with open("E://try.txt","r") as file:
        print(file.read())
        file.close()