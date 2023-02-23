import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x1)
x2 = np.linspace(0, 2 * np.pi, 100)
y2 = np.cos(x2)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.ylim(-1.1, 1.1)
plt.grid()
plt.show()
