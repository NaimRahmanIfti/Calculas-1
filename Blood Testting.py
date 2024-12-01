import numpy as np

N = 100
q = 0.95

def average_test(x):
    return N * ((1 - q**x) + (1 / x))

assume_x_value = np.linspace(1, 150, N)
average_test_values = [average_test(x) for x in assume_x_value]

min_index = np.argmin(average_test_values)
optimal_value = assume_x_value[min_index]

min_test = assume_x_value[min_index]

print("Optimal value:", optimal_value)
print("minimum average test value:", min_test)