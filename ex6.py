from sys import exit
string = input("Enter a string: ")

mid = (len(string) // 2)


for i in range(0, mid):
    if string[i].capitalize() != string[-1 * (i + 1)].capitalize():
        print("Not a palindrome!")
        exit(0)
print("%s happens to be a palindrome." % string)
    
