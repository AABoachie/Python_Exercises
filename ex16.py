import random
import string

print("Password Generator!")
aList = ['Addae', 'Amofa', 'Boachie', 'Osei', 'Kyeiwaa']
strngth = input("Enter if you want a [strong] or [weak] password: ")

def pick_letter():
    return random.choice(string.ascii_letters)
def pick_digit():
    return str(random.randint(0, 10))
def pick_name():
    if strngth == 'strong':
        return random.choice(aList)
    return ''
funcs = {'d' : pick_digit, 'l' : pick_letter, 'n' : pick_name}

password = []

for i in range(0, random.randint(3, 10)):
    determine = random.choice(['d', 'l', 'n'])
    password.append(funcs[determine]())
    
print(''.join(password))
