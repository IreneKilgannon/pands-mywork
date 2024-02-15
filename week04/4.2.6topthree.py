# A program that generates 10 random numbers from 0 to 100
# Prints them all out
# Then prints the top three


import random

generated_numbers = []

for num in range(0, 10):
    num = random.randint(0, 100)
    generated_numbers.append(num)
print(f'10 random numbers\t{generated_numbers}')

generated_numbers.sort()
print(f'The top 3 are\t\t{generated_numbers[-3:]}')


''' The solution is given as import random
# I programming the general case
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeto = 100
numbers = []
for i in range(0,howMany):
numbers.append(random.randint(rangeFrom,rangeto))
print (f"{howMany} random numbers\t {numbers}")
# I am keeping the original list maybe I don't need to
topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {topHowMany} are \t\t {topOnes[0:topHowMany]}")'''

