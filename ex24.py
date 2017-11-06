def print_dashes(mult = 1):
    print(" ---" * mult)
def print_bars(mult = 1):
    print("|   " * mult + "|")


size = int(input("How big do you want the board?: "))

for i in range(0, size):
    print_dashes(size)
    print_bars(size)
print_dashes(size)
