import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

ax: Axes

filename = "data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pobranie temperatur maksymalnych z pliku.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
    print(highs)

# Dane wykresu.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(highs, c="red")

# Formatowanie wykresu.
ax.set_title("Najwyższa temperatura dnia, lipiec 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()

# for index, column_header in enumerate(header_row):
#     print(index, column_header)
