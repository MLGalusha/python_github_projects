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
dates_death, rain_death = [], []
for row in reader_death:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain = float(row[3])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates_death.append(date)
        rain_death.append(rain)

# Get rain and date data for sitka alaska 2021
dates_sitka, rain_sitka = [], []
for row in reader_sitka:
    date1 = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain1 = float(row[5])
    except ValueError:
        print(f"Missing data for {date1}")
    else:
        dates_sitka.append(date1)
        rain_sitka.append(rain1)

# Plot the chart using the data
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(dates_death, rain_death, color='red', alpha=0.7)
ax.plot(dates_sitka, rain_sitka, color='blue', alpha=0.7)

#Format plot
ax.set_title("Rainfall Comparison Between Sitka, Alaska(blue) and Death Valley(red)", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Precipitation Amount (in)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()


