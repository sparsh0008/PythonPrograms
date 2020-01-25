char = input("enter a string : ")

vowels = [ char[i] for i in range(len(char)) if (char[i] in ('a','e','i','o','u') )]

print("No of Vowels in {0} is ".format(char))
print(len(vowels))
