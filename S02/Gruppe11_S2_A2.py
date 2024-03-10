import sympy as sp

from sympy import symbols, Matrix

# Define the symbols
x1, x2, x3 = symbols('x1 x2 x3')

f = Matrix([[5*x1*x2], [x1**2 * x2**2 + x1 + 2*x2]])

print(f.jacobian([x1, x2]))

f2 = Matrix([[sp.ln(x1**2 + x2**2)+x3**2], [sp.exp(x2**2 + x3**2)+x1**2], [(1/(x3**2+x1**2))+x2**2]])

print(f2.jacobian([x1, x2, x3]))
