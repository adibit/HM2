import matplotlib.pyplot as plt
import numpy as np

c = 1

w = lambda x, t: np.sin(x + c * t)
v = lambda x, t: np.sin(x + c * t) + np.cos(2 * x + 2 * c * t)

[x, y] = np.meshgrid(np.linspace(0, 5), np.linspace(0,5))
z = v(x, y)

fig = plt.figure(1)
ax = fig.add_subplot(projection='3d')
ax.plot_wireframe(x, y, z)

plt.title('Wireframe')
# ax.set_xlabel(xlabel)
# ax.set_ylabel(ylabel)
# ax.set_zlabel(zlabel)
plt.show()