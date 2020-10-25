import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('AFLT.csv')

x_1 = df['Дата'].iloc[0:5]
y1_1 = df['Цена открытия'].iloc[0:5]
y1_2 = df['Цена закрытия'].iloc[0:5]

x_2 = df['Дата'].iloc[4:10]
y2_1 = df['Цена открытия'].iloc[4:10]
y2_2 = df['Цена закрытия'].iloc[4:10]

x_3 = df['Дата'].iloc[9:15]
y3_1 = df['Цена открытия'].iloc[9:15]
y3_2 = df['Цена закрытия'].iloc[9:15]

x_4 = df['Дата'].iloc[14:20]
y4_1 = df['Цена открытия'].iloc[14:20]
y4_2 = df['Цена закрытия'].iloc[14:20]

x_5 = df['Дата'].iloc[19:25]
y5_1 = df['Цена открытия'].iloc[19:25]
y5_2 = df['Цена закрытия'].iloc[19:25]

x_6 = df['Дата'].iloc[24:30]
y6_1 = df['Цена открытия'].iloc[24:30]
y6_2 = df['Цена закрытия'].iloc[24:30]

fig = plt.figure()

ax_1 = fig.add_subplot(3, 2, 1)

ax_1.plot(x_1, y1_1, label='Open')
ax_1.plot(x_1, y1_2, label='Close')

ax_2 = fig.add_subplot(3, 2, 2)

ax_2.plot(x_2, y2_1, label='Open')
ax_2.plot(x_2, y2_2, label='Close')

ax_3 = fig.add_subplot(3, 2, 3)

ax_3.plot(x_3, y3_1, label='Open')
ax_3.plot(x_3, y3_2, label='Close')

ax_4 = fig.add_subplot(3, 2, 4)

ax_4.plot(x_4, y4_1, label='Open')
ax_4.plot(x_4, y4_2, label='Close')

ax_5 = fig.add_subplot(3, 2, 5)

ax_5.plot(x_5, y5_1, label='Open')
ax_5.plot(x_5, y5_2, label='Close')

ax_6 = fig.add_subplot(3, 2, 6)

ax_6.plot(x_6, y6_1, label='Open')
ax_6.plot(x_6, y6_2, label='Close')


ax_1.set(title='ax_1', xticks=[], yticks=[])
ax_1.legend()

ax_2.set(title='ax_2', xticks=[], yticks=[])
ax_2.legend()

ax_3.set(title='ax_3', xticks=[], yticks=[])
ax_3.legend()

ax_4.set(title='ax_4', xticks=[], yticks=[])
ax_4.legend()

ax_5.set(title='ax_5', xticks=[], yticks=[])
ax_5.legend()

ax_6.set(title='ax_6', xticks=[], yticks=[])
ax_6.legend()

plt.savefig("08_PLOT")

plt.show()