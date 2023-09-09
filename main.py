import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Zdefiniowanie tytułu wykresu i etykiety osi.
ax.set_title("Kwadrat liczb", fontsize=24)
ax.set_xlabel("Wartości", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wartości etykiet.
ax.tick_params(axis='both', labelsize=14)

plt.show()
