# Prompts the user to guess a number
# Tells the user if the number is too high or too low
# Keeps prompting until the user gets it right
# Author: Irene Kilgannon

number_to_guess = 30

guess = int(input("Please guess a number: "))

while guess != number_to_guess:
    if guess < number_to_guess:
        print("Too low")
    elif guess > number_to_guess:   # the solution has else statement.
        print("Too high")
    guess = int(input("Please guess again: "))

print(f'Well done. Yes, the number was {number_to_guess}.')