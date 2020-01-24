print("enter a string")
char = input()
vowels = [ char[i] for i in range(len(char)) if (char[i] == 'a' or char[i] == 'e'or char[i] == 'i'or  char[i] == 'o'or  char[i] == 'u')]
print(vowels)