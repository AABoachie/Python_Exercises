numbers = input("Enter a list of numbers: ").split(" ")
numbers = [int(x) for x in numbers if x.isdigit()]

print(numbers)

number = int(input("Enter a number: "))

if number in numbers:
    print("True")
else:
    print("False")
