"""Wyświetlenie prostego wykresu kwadratów liczb 1, 2, 3, 4 i 5."""

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Zdefiniowanie tytułu wykresu i etykiety osi.
ax.set_title("Kwadrat liczb", fontsize=24)
ax.set_xlabel("Wartości", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wartości etykiet.
ax.tick_params(axis='both', labelsize=14)

plt.show()
