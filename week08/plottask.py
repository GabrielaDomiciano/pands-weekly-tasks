#Gabriela Domiciano

import numpy as np
import matplotlib.pyplot as plt
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, 
#Generate 1000 random values from a normal distribution with mean of 5 and standard deviation of 2

randomNumbers = np.random.normal(loc=5, scale=2, size=1000)
print (randomNumbers)


linex = randomNumbers
liney = linex ** 3



#plt.plot(xpoints, ypoints)
# plt.plot(linex, liney, label="Histogram of Normal Distribution and Plot of h(x)=x^3", color="red")
plt.scatter(linex, liney, label="Histogram of Normal Distribution and Plot of h(x)=x^3", color="red")
plt.xlabel('Values')
plt.legend()


plt.show()

