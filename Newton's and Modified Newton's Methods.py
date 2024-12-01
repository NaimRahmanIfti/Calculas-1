import sympy as sp

# Define symbolic variable and function
x = sp.symbols('x')
f = sp.exp(2 * sp.sin(x)) - 2 * x - 1
f_prime = sp.diff(f, x)  # First derivative

# Fix Newton's methods for the small initial value
def newtons_method_numeric_fixed(f, f_prime, x0, tol=1e-6, max_iter=100):
    """Standard Newton's method with numerical evaluation, adjusted for edge cases."""
    for _ in range(max_iter):
        f_x = float(f.subs(x, x0))
        f_prime_x = float(f_prime.subs(x, x0))
        if abs(f_x) < tol:
            return x0
        if abs(f_prime_x) < tol:  # Avoid division by very small values
            raise ValueError("Derivative near zero. Method may not converge.")
        x0 -= f_x / f_prime_x
    return x0

def modified_newtons_method_numeric_fixed(f, f_prime, x0, tol=1e-6, max_iter=100):
    """Modified Newton's method with numerical evaluation, adjusted for edge cases."""
    for _ in range(max_iter):
        f_x = float(f.subs(x, x0))
        f_prime_x = float(f_prime.subs(x, x0))
        if abs(f_x) < tol:
            return x0
        if abs(f_prime_x) < tol:  # Avoid division by very small values
            raise ValueError("Derivative near zero. Method may not converge.")
        x0 -= 2 * f_x / f_prime_x
    return x0

# Initial value
x0_small = 0.01
# Recompute roots with fixed methods
try:
    newtons_root_numeric_fixed = newtons_method_numeric_fixed(f, f_prime, x0_small)
    modified_newtons_root_numeric_fixed = modified_newtons_method_numeric_fixed(f, f_prime, x0_small)

    print("newtons_root_numeric_fixed: ", newtons_root_numeric_fixed,"modified_newtons_root_numeric_fixed: ", modified_newtons_root_numeric_fixed)
except ValueError as e:
    str(e)
