# Write a program that make a list called ages with the same ramdom values as salaries (range 21-65)
# Make a scatter plot
# Add a line that shows y = x^2 in a different colour
# Add legend, title, and axis labels

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000

number_of_entries = 10

np.random.seed(343434)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)

ages = np.random.randint(low = 21, high = 65, size = number_of_entries)

plt.scatter(ages, salaries)

x_points = np.array(range(1, 101))
y_points = x_points * x_points

plt.plot(x_points, y_points, color = "red", label = "x squared")

plt.ylabel("Salaries in euro")
plt.xlabel("ages")
plt.title("Random plot")
plt.legend()
plt.savefig("prettier-plot.png")
plt.show()