import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
number = np.random.normal(loc=5, scale=2, size=1000)

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = x ** 3

plt.hist(number)
plt.plot(y)
plt.show()