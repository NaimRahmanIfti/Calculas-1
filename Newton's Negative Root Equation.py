import numpy as np
import pandas as pd

# Define the function \( f(x) = e^x - 4 + x^2 \) and its derivative
def f(x):
    return np.exp(x) - 4 + x**2

def df(x):
    return np.exp(x) + 2*x

# Newton's method with detailed iteration tracking
def newtons_method(x0, tol, max_iter=100):
    x = x0
    iterations = []
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            break  # Prevent division by zero
        next_x = x - fx / dfx
        iterations.append((i, x, fx, dfx))
        if abs(next_x - x) < tol:
            iterations.append((i+1, next_x, f(next_x), df(next_x)))
            break
        x = next_x
    return iterations

# Parameters
x0 = -1.5  # Initial guess for the negative root
tolerance = 1e-6

# Perform Newton's method
result = newtons_method(x0, tolerance)

# Create DataFrame with descriptive column names using mathematical notation
cols = ['Iteration', 'x_n (Root Estimate)', 'f(x) (Function Value at x_n)', 'f\'(x) (Derivative at x_n)']
iteration_data = pd.DataFrame(result, columns=cols)

# Save to CSV for Excel plotting
iteration_data.to_csv('newtons_method_detail.csv', index=False)

print("Data saved to 'newtons_method_detail.csv'. Here's a preview:")
print(iteration_data.head())
