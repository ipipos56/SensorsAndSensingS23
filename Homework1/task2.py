import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Generate noisy data points with a nonlinear relationship
x = np.linspace(0, 10, 50)
y = 2 * x**3 + 5 * x**2 - 4 * x + 8 + np.random.normal(0, 4, 50)

# Define the polynomial function to fit
def polynomial_func(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

# Use curve_fit to fit the polynomial function to the data
params, covariance = curve_fit(polynomial_func, x, y)

# Extract the optimized parameters
a, b, c, d = params

# Plot the original data and the fitted function
plt.scatter(x, y, label="Original data")
plt.plot(x, polynomial_func(x, a, b, c, d), label="Fitted function")
plt.legend()
plt.show()
