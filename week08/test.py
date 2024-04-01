import matplotlib.pyplot as plt
import numpy as np

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
randomNumbers = np.random.normal(loc=5, scale=2, size=1000)

# Plot histogram
plt.hist(randomNumbers, bins=30, density=True, alpha=0.6, color='blue')

# Plot the function h(x) = x^3
# x = np.linspace(0, 10, 100)
# y = x ** 3
# plt.plot(x, y, 'r-', linewidth=2)

# Add labels and title
plt.xlabel('Values')
plt.ylabel('Frequency / h(x)')
plt.title('Histogram of Normal Distribution and Plot of h(x)=x^3')

# Show plot
plt.grid(True)
plt.show()