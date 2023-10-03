"""Wizualizacja błądzenia losowego."""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from random_walk import RandomWalk

ax: Axes

# Przygotowanie danych błądzenia losowego i wyświetlewnioe punktów.
rw = RandomWalk()
rw.fill_walk()

# Wyświetlenie punktów błądzenia losowego.
plt.style.use("classic")
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

# o