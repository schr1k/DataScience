import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
ax.set(xlabel='Угол в Радианах', ylabel='Синус/Косинус', title='Графики синуса/косинуса')
x = np.linspace(0, 2 * np.pi, 7)
y = np.linspace(-1, 1, 9)
ax.set_xticks(x)
ax.set_yticks(y)
plt.axis([-0.4, 6.5, -1.1, 1.1])
plt.grid()
z = np.linspace(0, 2 * np.pi, 100)
ax.plot(z, np.sin(z))
ax.plot(z, np.cos(z))
plt.show()
