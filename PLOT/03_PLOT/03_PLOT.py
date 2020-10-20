from matplotlib import pyplot as plt

year = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(year, gdp, color='green', marker='o')

plt.title('Номинальный ВВП')

plt.xlabel('Год')
plt.ylabel('Млрд $')

plt.savefig("03_PLOT")

plt.show()