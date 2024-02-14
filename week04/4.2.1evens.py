# A program that uses a while loop to print all the even numbers from 2 to 100
# Author: Irene Kilgannon

for num in range(2, 101):   # done with a for loop, not the question asked!
    if num % 2 == 0:
        print(f"{num}", end = ' ')


even_num= 2

number_to = 100

while even_num <= number_to:
    print(even_num)
    even_num += 2