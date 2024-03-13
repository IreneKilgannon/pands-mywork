# Write a program that makes a list, called salaries that has say 10 random numbers(20000 - 80000)
# Author Irene Kilgannon

import numpy as np

min_salary = 20000
max_salary = 80000

number_of_entries = 10

salaries = np.random.randint(min_salary, max_salary, number_of_entries)

print(salaries)
