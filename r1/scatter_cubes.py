"""Automatycznie generuje ogromną ilość sześcianów liczb i na ich podstawie
tworzy wykres oraz zapisuje go do pliku PNG."""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

ax: Axes

x_values = range(5001)
y_values = [x ** 3 for x in x_values]

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

# Zdefiniowanie tytułu wykresu i etykiet osi.
ax.set_title("Sześciany liczb", fontsize=24)
ax.set_xlabel("Wartości", fontsize=14)
ax.set_ylabel("Sześciany wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet.
ax.tick_params(axis="both", which="major", labelsize=14)

# Zdefiniowanie zakresu dla każdej osi.
ax.axis([0, 5100, 0, 135000000000])

plt.show()

# Zapisanie do pliku PNG.
plt.savefig("cubes_plot.png", bbox_inches="tight")
