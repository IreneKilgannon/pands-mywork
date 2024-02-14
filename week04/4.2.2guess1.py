# Prompts the user to guess a number
# Keeps prompting until the user gets it right
# Author: Irene Kilgannon

number_to_guess = 30

guess = int(input("Please guess a number: "))

while guess != number_to_guess:
    print(("wrong"))
    guess = int(input("Please guess again: "))

print(f'Well done. The number was {number_to_guess}')