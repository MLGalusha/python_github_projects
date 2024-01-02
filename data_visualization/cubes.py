import matplotlib.pyplot as plt

values = range(1, 5001)
cubes = ([x**3 for x in values])

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(values, cubes, c=cubes, cmap=plt.cm.Reds, s=5)

#set the title and label axis as well as ticklabels
ax.set_title("Cubed Numbers", fontsize=20)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)
ax.tick_params(labelsize=14)

#Set range for each axis in chart
ax.axis([0, 5100, 0, 5100 **3])

plt.show()