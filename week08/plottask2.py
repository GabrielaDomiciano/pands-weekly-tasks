import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean of 5 and standard deviation of 2
randomNumbers = np.random.normal(loc=5, scale=2, size=1000)

xpoints = randomNumbers
ypoints = xpoints ** 3

#x = np.linspace(0, 10, 100)
#y = x ** 3

plt.plot(xpoints, ypoints, label="Histogram of Normal Distribution and Plot of h(x)=x^3", color="red")
plt.xlabel('Values')
plt.legend()

plt.show()