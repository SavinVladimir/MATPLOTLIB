import matplotlib.pyplot as plt

plt.plot([1, 1.1, 1, 1.1, 1], linestyle='-', linewidth=4)
plt.text(1.5, 1.3, "linestyle = '-' ", horizontalalignment='left', size='medium', color='C0', weight='semibold')

plt.plot([2, 2.1, 2, 2.1, 2], linestyle='--', linewidth=4)
plt.text(1.5, 2.3, "linestyle = '--' ", horizontalalignment='left', size='medium', color='C1', weight='semibold')

plt.plot([3, 3.1, 3, 3.1, 3], linestyle='-.', linewidth=4)
plt.text(1.5, 3.3, "linestyle = '-.' ", horizontalalignment='left', size='medium', color='C2', weight='semibold')

plt.plot([4, 4.1, 4, 4.1, 4], linestyle=':', linewidth=4)
plt.text(1.5, 4.3, "linestyle = ':' ", horizontalalignment='left', size='medium', color='C3', weight='semibold')

plt.axis('off')

plt.savefig("05_PLOT")

plt.show()