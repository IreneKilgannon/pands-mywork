# Make a pie chart of a list of counties

import numpy as np
import matplotlib.pyplot as plt

list_counties = ["Galway", "Mayo", "Leitrim", "Kerry", "Sligo"]

counties = np.random.choice(list_counties, p = [0.1, 0.3, 0.2, 0.12, 0.28], size = (100))

unique, counts = np.unique(counties, return_counts= True)

#plt.pie(counts, labels = unique)
plt.bar(unique, counts)
plt.show()