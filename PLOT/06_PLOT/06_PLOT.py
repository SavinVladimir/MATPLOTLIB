import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [8, 3, 5, 7, 4]
y2 = [4, 5, 8, 4, 5]

plt.subplot(2, 1, 1)
plt.plot(x, y1, color='orange', marker='o', linewidth=0.7, markersize=3)

plt.subplot(2, 1, 2)
plt.plot(x, y2, color='green', marker='o', linewidth=0.7, markersize=3)

plt.savefig("06_PLOT")

plt.show()
