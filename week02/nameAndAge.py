# nameAndAge.py
# Reads in a name and age and outputs "Hello Andrew, your age is 21"
# Author: Irene Kilgannon

name = input('Enter your name: ')

# As age is an integer, need to conver the input to an integer
age = int(input('Enter your age: '))

print(f'Hello {name}, your age is {age}')

# Modifying the program so that it has a tab after name
#\t for a tab

print(f'Hello {name}, \tyour age is {age}')