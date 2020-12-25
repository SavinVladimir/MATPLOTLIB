import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

languages = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23, 17, 35, 29, 12]

ax.bar(languages, students, color='#6136B4')

plt.savefig("02_BAR")

plt.show()
