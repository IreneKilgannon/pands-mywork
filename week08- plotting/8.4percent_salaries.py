# Write a program that makes a list, called salaries that has say 10 random numbers(20000 - 80000)
# Modify the program so that 5% is added to each salary
# Author Irene Kilgannon

import numpy as np

min_salary = 20000
max_salary = 80000


number_of_entries = 10

np.random.seed(2233433)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)

salaries_percent = salaries * 1.05

print(salaries_percent.astype(int))   # astype(int) converts the float values to an integer