# Write a program that makes a list, called salaries that has say 10 random numbers(20000 - 80000)
# Make a histogram of the results
# Author Irene Kilgannon

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000

number_of_entries = 10

np.random.seed(343434)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
plt.xlabel("Salaries in euro")
plt.title("Distribution of salaries")
plt.hist(salaries)
plt.show()