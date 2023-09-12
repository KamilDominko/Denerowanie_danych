"""Tworzy wykres na podstawie kwadratów liczb 1,2,3,4,5 i zapisuje go do
pliku PNG."""

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

ax: Axes

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use("ggplot")
fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
ax.scatter(x_values, y_values, s=100)

# Zdefiniowanie tytułu wykresu i etykiet osi.
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartości", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet.
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
