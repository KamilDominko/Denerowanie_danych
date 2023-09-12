import matplotlib.pyplot as plt
from matplotlib.axes import Axes

ax: Axes

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Zdefiniowanie tytułu wykresu i etykiet osi.
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartości", fontsize=24)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet.
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
