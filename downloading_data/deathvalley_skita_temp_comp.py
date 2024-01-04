from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

#Make a path the the csv files containing the needed data
path_death = Path('/Users/masongalusha/Downloads/death_valley_2021_full.csv')
path_sitka = Path('/Users/masongalusha/Downloads/sitka_weather_2021_full.csv')
lines_death, lines_sitka = path_death.read_text().splitlines(), path_sitka.read_text().splitlines()

# Read both files
reader_death, reader_sitka = csv.reader(lines_death), csv.reader(lines_sitka)

# Look at the first columns in both files to see what rows they have
header_death, header_sitka = next(reader_death), next(reader_sitka)
[print(index, column) for index, column in enumerate(header_death)]
[print(index, column) for index, column in enumerate(header_sitka)]

# Get rain and date data for death valley 2021
dates_death, high_death, low_death = [], [], []
for row in reader_death:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[6])
        low = int(row[7])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates_death.append(date)
        high_death.append(high)
        low_death.append(low)

# Get rain and date data for sitka alaska 2021
dates_sitka, high_sitka, low_sitka = [], [], []
for row in reader_sitka:
    date1 = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high1 = int(row[7])
        low1 = int(row[8])
    except ValueError:
        print(f"Missing data for {date1}")
    else:
        dates_sitka.append(date1)
        high_sitka.append(high1)
        low_sitka.append(low1)

# Plot the chart using the data
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(dates_death, high_death, color='red', alpha=0.9)
ax.plot(dates_death, low_death, color='blue', alpha=0.9)
ax.plot(dates_sitka, high_sitka, color='red', alpha=0.9)
ax.plot(dates_sitka, low_sitka, color='blue', alpha=0.9)
ax.fill_between(dates_death, high_death, low_death, color='red', alpha=0.3)
ax.fill_between(dates_sitka, high_sitka, low_sitka, color='blue', alpha=0.3)

#Format plot
ax.set_title("Temperature Comparison Between Sitka, AK (blue) and Death Valley, CA (red)", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()


