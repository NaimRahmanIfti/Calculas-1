import sympy as sp

# Define the function
x = sp.symbols('x')
f = sp.exp(2 * sp.sin(x)) - 2 * x - 1

# Compute derivatives
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)

# Evaluate at x = 0
f_at_0 = f.subs(x, 0)
f_prime_at_0 = f_prime.subs(x, 0)
f_double_prime_at_0 = f_double_prime.subs(x, 0)

print("f at 0 :", f_at_0, "\nf Prime at 0 :", f_prime_at_0, "\nf Double Prime at 0 :", f_double_prime_at_0)
