import random
#a = [1, 1, 2, 3, 5, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13]

a = []
b = []

for i in range(0, random.randint(0, 100)):
    a.append(random.randint(0, 100))
for i in range(0, random.randint(0, 100)):
    b.append(random.randint(0, 100))    

c = []
[c.append(x) for x in a if x in b and x not in c]

print(c)
