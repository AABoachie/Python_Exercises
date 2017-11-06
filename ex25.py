start = 0
end = 100

print("Pick a number in your head between 0 and 100 inclusive. ")

count = 0

while(True):
    guess = start + (end - start) // 2
    count += 1
    ans = input("Is your number %d?(y/n): " % guess)
    if ans == 'y':
        break;
    else:
        ans = input("(h)igher or (l)ower: ")
        if ans == 'h':
            start = guess
        elif ans == 'l':
            end = guess

print("It took %d guesses." % count)
