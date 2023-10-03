"""Wizualizacja symulacji śceiżki poruszania się pyłku kwiatów po powierzchni
kropli wody. """

import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from random_walk import RandomWalk

ax: Axes

rw = RandomWalk()
rw.fill_walk()

plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(rw.x_values, rw.y_values, linewidth=3)
plt.show()
