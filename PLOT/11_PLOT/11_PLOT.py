from matplotlib import pyplot as plt
from matplotlib.ticker import (AutoMinorLocator)

fig, ax = plt.subplots()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 8, 9, 12]
y = [1, 11, 8, 6, 17, 15, 16, 9, 11, 14, 10, 7, 6, 5]

plt.plot(x, y)

ax.grid(which="major", linewidth=1)
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

plt.savefig('11_PLOT')

plt.show()