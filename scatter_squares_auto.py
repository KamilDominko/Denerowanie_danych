import matplotlib.pyplot as plt
from matplotlib.axes import Axes

ax: Axes

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use("ggplot")
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c="green", s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Zdefiniowanie tytułu wykresu i etykiet osi.
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartości", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet.
ax.tick_params(axis="both", which="major", labelsize=14)

# Zdefiniowanie zakresu dla każdej osi.
ax.axis([0, 1100, 0, 1100000])

plt.show()

# Zapisanie do pliku PNG.
plt.savefig("squares_plot.png", bbox_inches="tight")
