# Generate a random number to guess
# Author: Irene Kilgannon

import random

number_to_guess = random.randint(0, 100)

guess = int(input("Please guess a number: "))

while guess != number_to_guess:
    if guess < number_to_guess:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Please guess again: "))

print(f'Well done. Yes, the number was {number_to_guess}.')