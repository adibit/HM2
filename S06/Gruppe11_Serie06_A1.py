import numpy as np
import matplotlib.pyplot as plt

#temperature in degree Celsius
T = np.array([0,10,20,30,40,50,60,70,80,90,100])
#water density
y = np.array([999.9,999.7,998.2,995.7,992.2,988.1,983.2,977.8,971.8,965.3,958.4])
#x axis
x = np.arange(0, 101, 10)  # x = T
#define Matrix A
A = np.array([x ** 2, x, np.ones(x.shape)]).T


#Ausgleichsfuntkion
def aufgabe1a(A, y):
    return np.linalg.solve(A.T @ A, A.T @ y)

def aufgabe1a_qr(A, y):
    Q, R = np.linalg.qr(A)
    return np.linalg.solve(R, Q.T @ y)

#Kondition
def aufg1b(A):
    print("Cond A.T@A", np.linalg.cond(A.T @ A))
    Q, R = np.linalg.qr(A)
    print("Cond R    ", np.linalg.cond(R))
    """
    Cond A.T@A 147270642.55371314 <- viel höher, sprich schlechter konditioniert
    Cond R     12135.511631312149
    """

#Ausgleichsfunktion mit polyfit
def aufg1c(x,y):
    return np.polyfit(x, y, 2)

#Berechnung Fehlerfunktionale
def aufg1d_fehlerfnktionale(A, y, lam, qr, p):  # y = orginale Y, yy = lamdba a), yy_fit = lamdba c)
    print("2-Norm: E(lam)", np.linalg.norm((y - A @ lam)) ** 2)
    print("2-Norm: E(lam) QR", np.linalg.norm((y - A @ qr)) ** 2)
    print("2-Norm: E(lam) polyfit", np.linalg.norm((y - A @ p)) ** 2)




plt.scatter(x, y, color='orange')
xx = np.linspace(x.min(), x.max())
# a)
yy = aufgabe1a(A, y)
yy2 = aufgabe1a_qr(A, y)
plt.plot(xx, yy[0] * xx ** 2 + yy[1] * xx + yy[2], '-b')
plt.plot(xx, yy2[0] * xx ** 2 + yy2[1] * xx + yy2[2], '--r')

#c
p = aufg1c(x, y)
plt.plot(xx, np.polyval(p, xx), '-g')

#d Antwort: alle sind gleich gut, da die Fehlerfunktionale gleich sind
aufg1d_fehlerfnktionale(A, y, yy, yy2, p)

plt.grid()
plt.legend(["data-points", "solve", "QR", "Polyval"])
plt.show()
