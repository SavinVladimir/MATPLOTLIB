from matplotlib import pyplot as plt
import pandas as pd

dataframe = pd.read_csv('AFLT.csv')

x = dataframe['Дата'].iloc[0:71]

y1 = dataframe['Цена открытия'].iloc[0:71]
y2 = dataframe['Цена закрытия'].iloc[0:71]


plt.subplot(2, 1, 1)
plt.title('Цена открытия')
plt.plot(x, y1, color='#0000CD',linestyle='--',  marker='o', markersize=3)
plt.grid()

frame = plt.gca()
frame.axes.get_xaxis().set_ticks([0, 10, 20, 30, 40, 50, 60, 70])


plt.subplot(2, 1, 2)
plt.title('Цена закрытия')
plt.plot(x, y2, color='#FF4500', linestyle='--', marker='o', markersize=3)
plt.grid()

frame = plt.gca()
frame.axes.get_xaxis().set_ticks([0, 10, 20, 30, 40, 50, 60, 70])


plt.show()