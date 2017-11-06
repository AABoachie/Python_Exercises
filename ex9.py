import random

print("The Guessing Game!")
stop = 'n'
while stop == 'n':
    num = random.randint(1, 9)
    pick = -1
    while pick != num:
        pick = int(input("Enter a number from 1-9 inclusive: "))
        if pick < num:
            print("Too Low! Try again.")
        if pick > num:
            print("Too High! Try again.")
        if pick == num:
            print("You got it right!")
            break
    stop = input("Would you like to stop playing? y/n: ")
