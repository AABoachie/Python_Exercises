string = input("Enter a string: ")

words = string.split(' ')
words.reverse()
string = ' '.join(words)

print(string)
