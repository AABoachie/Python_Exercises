from sys import exit

def ask_int(prompt):
    return int(input(prompt))

num = ask_int("Enter a number: ")

divisors = range(2, num)

for div in divisors:
    if num % div == 0:
        print("%d is not a prime." % num)
        exit(0)
        
print("%d is prime." % num)
