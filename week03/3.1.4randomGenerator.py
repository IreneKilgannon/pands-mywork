# program that prints out a random number between 1 and 10

import random

number = random.randint(1,10)
print("Here is a random number {}".format(number))

# newer method of formatting
print(f"Here is a random number {number}")

# modify the program so the user inputs the range
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

range = random.randint(number1, number2)
print(f"Here is a random number in {range}")
