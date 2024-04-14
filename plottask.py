# Author Gabriela Domiciano Avellar
# Weekly Task 08

# Write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
# and a plot of the function  h(x)=x3 in the range 0 to 10.


import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
number = np.random.normal(loc=5, scale=2, size=1000)

labelx = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
labely = labelx ** 3


plt.xlabel('Values')
plt.ylabel('Frequency / h(x)')
plt.title('Histogram of Normal Distribution and Plot of h(x)=x^3')

plt.hist(number)
plt.plot(labely)
plt.show()


