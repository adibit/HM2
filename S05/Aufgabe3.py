import numpy as np
import matplotlib.pyplot as plt
from Aufgabe2 import aufg2_spline
from scipy import interpolate

t = np.array([1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010])
pt = np.array([75.995, 91.972, 105.711, 123.203, 131.669, 150.697, 179.323, 203.212, 226.505, 249.633, 281.422, 308.745])
xx = np.linspace(1900, 2010, 200)

#b

cs = interpolate.CubicSpline(t, pt, bc_type='natural')
plt.plot(t, pt, 'o', label='data')
plt.plot(xx, cs(xx), label='cubicSpline')


#a

yy = aufg2_spline(t, pt, xx)
plt.plot(xx, yy,":" , label='natSpline')


#c

xt = np.polyfit(t-1900, pt, t.size - 1)
plt.plot(xx, np.polyval(xt, xx-1900), label='polyfit')

plt.grid()
plt.legend()
plt.show()
