import matplotlib.pyplot as plt
import numpy as np

# Antwort 1a) grössste Distanz bei 45Grad

G = 9.81
R = 8.31


def wire(x, y, z, xlabel, ylabel, zlabel):
    fig = plt.figure(2)
    ax = fig.add_subplot(projection='3d')
    ax.plot_wireframe(x, y, z)

    plt.title('Wireframe')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)


def surface(x, y, z, xlabel, ylabel, zlabel):
    fig = plt.figure(3)
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x, y, z)

    plt.title('Surface')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)


def contour(x, y, z, xlabel, ylabel):
    plt.figure(4)
    plt.contour(x, y, z)
    plt.title('Höhelinie')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


def a():
    w = lambda v0, a: (v0 ** 2 * np.sin(2 * a)) / G
    [v0, a] = np.meshgrid(np.linspace(0, 100), np.linspace(0, 90) / 180 * np.pi)
    z = w(v0, a)
    wire(v0, a, z, 'Wurfgesch.', 'Winkel in Rad', 'Wurfweite')
    surface(v0, a, z, 'Wurfgesch.', 'Winkel in Rad', 'Wurfweite')
    contour(v0, a, z, 'Wurfgesch.', 'Winkel in Rad')

    plt.show()


def bp():
    p = lambda v, t: R * t / v
    [v, t] = np.meshgrid(np.linspace(0.000000001, 0.2), np.linspace(0, 1e4))
    z = p(v, t)
    wire(v, t, z, 'Volumen', 'Temp K', 'Druck')
    surface(v, t, z, 'Volumen', 'Temp K', 'Druck')
    contour(v, t, z, 'Volumen', 'Temp K')
    plt.show()

def bv():
    v = lambda p, t: R * t / p
    [p, t] = np.meshgrid(np.linspace(1e4,1e5), np.linspace(0, 1e4))
    z = v(p, t)
    wire(p, t, z, 'Druck', 'Temp K', 'Volumen')
    surface(p, t, z, 'Druck', 'Temp K', 'Volumen')
    contour(p, t, z, 'Druck', 'Temp K')
    plt.show()

def bt():
    t = lambda p, v: p * v / R
    [p, v] = np.meshgrid(np.linspace(1e4, 1e6), np.linspace(0, 10))
    z = t(p, v)
    wire(p, v, z, 'Druck', 'Volumen', 'Temp K')
    surface(p, v, z, 'Druck', 'Volumen', 'Temp K')
    contour(p, v, z, 'Druck', 'Volumen')
    plt.show()


def b():
    bt()



b()