# Author Gabriela Domiciano Avellar
# Weekly Task 08

# Write a program called plottask.py that displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2
# and a plot of the function  h(x)=x3 in the range 0 to 10.


import numpy as np
import matplotlib.pyplot as plt

#  random number generation 
np.random.seed(1)
number = np.random.normal(loc=5, scale=2, size=1000)

# creates an array labelx containing numbers from 1 to 10.
labelx = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
labely = labelx ** 3
# cube of each number in labelx and stores the results in labely.

plt.xlabel('Values')
plt.ylabel('Frequency / h(x)')
plt.title('Histogram of Normal Distribution and Plot of h(x)=x^3')

# creates a histogram of the numbers stored in the number variable.
plt.hist(number)
plt.plot(labely)
plt.show()
# displays the plot with both the histogram and the curve.

