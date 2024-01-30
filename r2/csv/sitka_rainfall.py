import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

ax: Axes
fig: Figure

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Pobranie danych.
    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            rain_fall = float(row[3])
        except ValueError:
            print(f"Brak danych dla {current_date}.")
        else:
            dates.append(current_date)
            rainfall.append(rain_fall)

# Wygenerowanie wykresu
plt.style.use('seaborn-v0_8-bright')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='blue', alpha=0.5)

# Formatowanie wykresu
ax.set_title("Opady deszczu Sitka 2018")
fig.autofmt_xdate()

plt.show()