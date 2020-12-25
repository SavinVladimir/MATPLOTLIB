import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 8)
y = np.random.randint(1, 20, size = 7)

fig, ax = plt.subplots()

ax.bar(x, y)

ax.set_facecolor('white')
fig.set_facecolor('white')

fig.set_figwidth(8)
fig.set_figheight(6)

plt.savefig("01_BAR")

plt.show()