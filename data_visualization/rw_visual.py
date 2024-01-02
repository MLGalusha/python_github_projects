import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Make a random walk
rw = RandomWalk()
rw.fill_walk()

#Plot the points in the walk
plt.style.use("dark_background")
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, s=5)
ax.set_aspect('equal')

plt.show()