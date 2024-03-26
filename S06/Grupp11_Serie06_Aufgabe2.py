import numpy as np
import matplotlib.pyplot as plt
import HM2_Serie06_Aufg2_Daten as daten


mch_org = daten.data[:, 4:5].copy()
print('mch: ', mch_org)

A = daten.data.copy()
A[:, 4:5] = np.ones(daten.data[:, 4:5].shape)
print('A: ', A)

Q, R = np.linalg.qr(A)
lamQR = np.linalg.solve(R, Q.T @ mch_org)
y = A @ lamQR

x = np.arange(0, 32, 1)

plt.scatter(x, mch_org, color="orange", label="Gemessen")
plt.plot(x, y, label="Gefittet")
plt.grid()
plt.legend()
plt.show()
