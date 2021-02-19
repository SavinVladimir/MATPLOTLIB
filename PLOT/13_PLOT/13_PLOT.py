import matplotlib.pyplot as plt
from random import randint

linear = list(range(1, 21))
wiggly = list(num + randint(-1, 1) for num in linear)

fig, plots = plt.subplots(nrows=1, ncols=3)

ticks = list(range(0, 21, 5))

for plot in plots:
    plot.set_xticks(ticks)
    plot.set_yticks(ticks)

plots[0].scatter(linear, wiggly, alpha=0.4)
plots[1].plot(linear, wiggly, color='red',)
plots[2].plot(linear, wiggly, 'o-')

plt.savefig('13_PLOT')

plt.show()
