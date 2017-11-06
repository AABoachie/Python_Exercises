a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = list(filter(lambda x: True if x % 2 == 0 else False, a))
c = [x for x in a if x % 2 == 0 ]
print(b)
print(c)
