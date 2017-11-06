import random

a = [random.randint(0,10) for i in range(0, random.randint(0, 20))]
print(a)

b = []
c = set(a)
[b.append(x) for x in a if x not in b]



print(b)
print(c)


