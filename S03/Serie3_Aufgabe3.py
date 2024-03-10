import numpy as np
import sympy as sy

sy.init_printing()
x, y, z = sy.symbols('x y z')

""" INPUT """
f1 = x + y ** 2 - z ** 2 - 13
f2 = sy.log(y / 4) + sy.exp(0.5 * z - 1) - 1
f3 = (y - 3) ** 2 - z ** 3 + 7
x0 = np.array([[1.5], [3], [2.5]])
eps = 10 ** -5

""" INPUT """


def newton_damped(f, x0):
    x, y, z = sy.symbols('x y z')
    Df = f.jacobian([x, y, z])

    Df = sy.lambdify([([x], [y], [z])], Df, 'numpy')
    fl = sy.lambdify([([x], [y], [z])], f, 'numpy')
    x = [x0]
    k = 0
    while np.linalg.norm(fl(x[k]), 2) >= eps:
        d = np.linalg.solve(Df(x[k]), -fl(x[k]))
        i = 0
        # daempfung ausfuehren bis 2-norm
        while np.linalg.norm(fl(x[k] + d / (2 ** i)), 2) >= np.linalg.norm(fl(x[k]), 2):
            i += 1
        x.append(x[k] + d / (2 ** i))
        k += 1
    return x


f = sy.Matrix([f1, f2, f3])
print("f: ", f)
print("x0 = ", x0)

xn = newton_damped(f, x0)

for k in range(1, len(xn)):
    print(k, " x = ", xn[k].T)