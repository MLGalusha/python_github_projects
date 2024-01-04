from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('/Users/masongalusha/Downloads/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

[print(index, column) for index, column in enumerate(header_row)]

# Find the information on specific rows and add to corresponding list
dates, rains = [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain = float(row[5])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        rains.append(rain)

# Create a plot for the information
plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(dates, rains, color='blue')

# Format plot
ax.set_title("Skita Dailey Rainfall for 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Precipitation Amount (in)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()