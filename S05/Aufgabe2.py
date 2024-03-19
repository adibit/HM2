import numpy as np
import matplotlib.pyplot as plt

#mit wenig Punkten testen für Prüfung! z.B: 2-4 Punkte

#Input
x = np.array([4.,6,8,10])
y = np.array([6.,3,9,0])
#x = np.array([4.,6,8])
#y = np.array([6.,3,9])
xx = np.linspace(4, 10)

def check_size(x, y):
    if x.size != y.size:
        raise ValueError("x and y must have the same size")
    else :return True

def show_plot(x, y, xx, yy):
    plt.scatter(x, y)
    plt.plot(xx, yy)
    plt.grid()
    plt.show()

#natural spline
def aufg2_spline(x,y,xx):
    check_size(x,y)

    #init a
    a = y[:-1]
    #init h
    h = x[1:] - x[:-1]
    #init c
    c = np.zeros(x.shape)
    #Ac = z
    if x.size > 2:
        A = np.diag(2 * (h[:-1] + h[1:]))\
            + np.diag(h[1:-1], -1)\
            + np.diag(h[1:-1], 1)
        z = (3 * (y[2:] - y[1:-1]) / h[1:] - 3 * (y[1:-1] - y[:-2]) / h[:-1])
        c[1:-1] = np.linalg.solve(A, z)
    #init b
    b = ((y[1:] - y[:-1]) / h) \
        - (c[1:] + 2 * c[:-1]) * h / 3
    #init d
    d = (c[1:] - c[:-1]) / h / 3

    #eval
    yy = np.zeros(xx.shape)
    for k in range(x.size - 1):
        idx, = np.nonzero((xx >= x[k]) & (xx <= x[k + 1]))
        dx = xx[idx] - x[k]
        yy[idx] = a[k] + b[k] * dx + c[k] * dx ** 2 + d[k] * dx ** 3

    print('a: ', a)
    print('b: ', b)
    print('c: ', c)
    print('d: ', d)

    return yy


if __name__=='__main__':
    yy = aufg2_spline(x, y, xx)
    show_plot(x, y, xx, yy)
    print('yy: ', yy)