char = input("enter a string")

vowels = [ char[i] for i in range(len(char)) if (char[i] in ('a', 'e','i','o','u') )]

print("No of Vowels in the string is ")
print(len(vowels))
