import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [11, 8, 6, 17, 15, 16, 9, 11, 14, 10]

plt.plot(x, y, linestyle='--')

plt.xlabel('Ось X')
plt.ylabel('Ось Y')

plt.grid(True)

plt.savefig("04_PLOT")

plt.show()