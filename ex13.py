aList = [0, 1]

def get_int(prompt):
    return int(input(prompt))

num = get_int("Enter how many Fibonacci Numbers you would like to generate: ")

for i in range(2, num):
    aList.append(aList[i - 1] + aList[i - 2])

print(aList[:num])
