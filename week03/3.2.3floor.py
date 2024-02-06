# A program that takes in a float and outputs an int rounded down, math.floor() needed

import math

number_to_round = float(input("Enter a number:"))

rounded_down = math.floor(number_to_round)

print(f"{number_to_round} rounds down to {rounded_down}")

# Solution has the variable names as number_to_floor and floored_number hich are better descriptors.