# Write a program that plots the function y = x^2
# Author Irene Kilgannon

import numpy as np
import matplotlib.pyplot as plt

x_points = np.array(range(1, 101))
y_points = x_points * x_points

plt.plot(x_points, y_points)
plt.show()
