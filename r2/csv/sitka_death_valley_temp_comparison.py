import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

ax: Axes
fig: Figure


def get_data(filename, data_row, max_temp_row, min_temp_row):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[data_row], '%Y-%m-%d')
            try:
                high = int(row[max_temp_row])
                low = int(row[min_temp_row])
            except ValueError:
                print(f"Brak danych dla {current_date}.")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        return dates, highs, lows


sitka_dates, sitka_highs, sitka_lows = get_data(
    'data/sitka_weather_2018_simple.csv', 2, 5, 6)
death_valley_dates, death_valley_highs, death_valley_lows = get_data(
    'data/death_valley_2018_simple.csv', 2, 4, 5)

plt.style.use('seaborn-v0_8-bright')
fig, ax = plt.subplots()

# Sitka
ax.plot(sitka_dates, sitka_highs,
        c='red', label='Sitka Max. Temp.', linestyle='--')
ax.plot(sitka_dates, sitka_lows,
        c='blue', label='Sitka Min. Temp.', linestyle='--')
ax.fill_between(sitka_dates, sitka_highs, sitka_lows,
                facecolor='blue', alpha=0.1)

# Death Valley
ax.plot(death_valley_dates, death_valley_highs,
        c='red', label='Death Valley Max. Temp', linestyle='-')
ax.plot(death_valley_dates, death_valley_lows,
        c='blue', label='Death Valley Min. Temp', linestyle='-')
ax.fill_between(death_valley_dates, death_valley_highs, death_valley_lows,
                facecolor='blue', alpha=0.1)

# Formatowanie wykresu
ax.set_title("Różnica najwyższych temperatur w Sitka a Death Valley 2018")
fig.autofmt_xdate()
ax.set_ylabel("Temperatura [F]")
ax.legend()

plt.show()
