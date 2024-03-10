import sympy as sp
from sympy import symbols, Matrix, ln, exp

x1, x2, x3 = symbols('x1 x2 x3')
# Define the function f(x1, x2, x3) as a matrix using the expressions provided
f_c = Matrix([
    [x1 + x2**2 - x3**2 - 13],
    [ln(x2/4) + exp(0.5*x3-1) - 1],
    [(x2 - 3)**2 - x3**3 + 7]
])

J = f_c.jacobian([x1, x2, x3])

x0 = Matrix([1.5, 3, 2.5]).T

Jx0 = J.subs({x1: x0[0], x2: x0[1], x3: x0[2]})
fx0 = f_c.subs({x1: x0[0], x2: x0[1], x3: x0[2]})
gx = fx0 + Jx0 * Matrix([x1-1.5, x2-3, x3-2.5])
print(gx.evalf())
