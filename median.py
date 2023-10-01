"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

# sort the list
numbers.sort()

if len(numbers) % 2 != 0:
    print(numbers[len(numbers)// 2])
else:
    # first value = round down 
    first_value = numbers[len(numbers) // 2 - 1]
    # second value = round up
    second_value = numbers[len(numbers) // 2]
    print((first_value + second_value) / 2)