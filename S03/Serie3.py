import numpy as np
import sympy as sy

#Aufgabe 1
sy.init_printing()
x, y = sy.symbols('x y')

f1 = 20 - 18 * x - 2 * y ** 2
f2 = -4 * y * (x - y ** 2)
x0 = np.array([[1.1], [0.9]])

def newton_normal(f, x0):
    x, y = sy.symbols('x y')
    Df = f.jacobian([x, y])

    Df = sy.lambdify([([x], [y])], Df, 'numpy')
    fl = sy.lambdify([([x], [y])], f, 'numpy')
    x = [x0]
    for k in range(0, 5):
        d = np.linalg.solve(Df(x[k]), -fl(x[k]))
        x.append(x[k] + d)
    return x

f = sy.Matrix([f1, f2])
fl = sy.lambdify([([x], [y])], f, 'numpy')
print("f: ", f)
print("x0 = ", x0)

xn = newton_normal(f, x0)

for k in range(1, len(xn)):
    print(k, " : ||f||2 = ", np.linalg.norm(fl(xn[k]), 2), " ||x||2 = ",
          np.linalg.norm(xn[k] - xn[k - 1], 2),
          " x = ", xn[k].T)