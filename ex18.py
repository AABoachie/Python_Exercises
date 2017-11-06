import random

def get_rand_int():
    return random.randint(0, 10)


rand_num = [get_rand_int(), get_rand_int(), get_rand_int(), get_rand_int()]

def parse_num(num):
    return [int(x) for x in str(num)]

def get_num():
    return int(input(">>>: "))

def get_cows():
    cows = 0
    for i in range(0, len(rand_num)):
        if rand_num[i] == input_num[i]:
            cows += 1        
    return cows

def get_bulls():
    bulls = 0
    for i in range(0, len(rand_num)):
        if rand_num[i] != input_num[i] and rand_num[i] in input_num:
            bulls += 1
    return bulls

print("Welcome to the Cows and Bulls Game!")
print("Enter a four digit number: ")

while(True):
    input_num = parse_num(get_num())
    
    print("%d cow(s), %d bull(s)" % (get_cows(), get_bulls()))
    if get_cows() == 4:
        print("You win!")
        break

