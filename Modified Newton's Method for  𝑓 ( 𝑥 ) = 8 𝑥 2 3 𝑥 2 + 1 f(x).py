import sympy as sp

# Define symbolic variable and function for part (c)
x = sp.symbols('x')
f_c = (8 * x**2) / (3 * x**2 + 1)
f_c_prime = sp.diff(f_c, x)  # First derivative of f_c(x)

# Newton's method
def newtons_method_numeric(f, f_prime, x0, tol=1e-6, max_iter=100):
    """Standard Newton's method with numerical evaluation."""
    for _ in range(max_iter):
        f_x = float(f.subs(x, x0))
        f_prime_x = float(f_prime.subs(x, x0))
        if abs(f_x) < tol:
            return x0
        if abs(f_prime_x) < tol:  # Avoid division by very small values
            raise ValueError("Derivative near zero. Method may not converge.")
        x0 -= f_x / f_prime_x
    return x0

# Modified Newton's method
def modified_newtons_method_numeric(f, f_prime, x0, tol=1e-6, max_iter=100):
    """Modified Newton's method with numerical evaluation."""
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
x0_c = 0.15

# Apply Newton's Method
newtons_root_c = newtons_method_numeric(f_c, f_c_prime, x0_c)

# Apply Modified Newton's Method
modified_newtons_root_c = modified_newtons_method_numeric(f_c, f_c_prime, x0_c)

# Output results
print("Part (c):")
print("Newton's method root for f_c(x) (starting at x0 = 0.15):", newtons_root_c)
print("Modified Newton's method root for f_c(x) (starting at x0 = 0.15):", modified_newtons_root_c)
