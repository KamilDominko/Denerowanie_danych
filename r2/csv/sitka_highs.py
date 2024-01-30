import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

ax: Axes
fig: Figure

filename = "data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pobranie temperatur maksymalnych z pliku.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
    print(highs)

# Wygenerowanie wykresu najwyższych temperatur.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")

# Formatowanie wykresu.
ax.set_title("Najwyższa temperatura dnia, lipiec 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()  # Wyświetlenie etykiet dat ukośnie.
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()
