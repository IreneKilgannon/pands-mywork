# Program that reads in numbers until the user enters a 0
# appends each number into a list
# Prrint out each number entered
# Gets the average them

numbers = []  #Create an empty list

number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input("Enter another (0 to quit): "))    # Had an error here as forgot to use 'int'

for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)
print(f'The average of {average}')
