from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('/Users/masongalusha/Desktop/python_work/zz-assets/sitka_weather.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# # Convert the reader to a list to allow reiteration from the beginning
rows = list(reader)

# Iterate over reader to find the dates, low and high temperatures
dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in rows]
highs = [int(row[4]) for row in rows]
lows = [int(row[5]) for row in rows]

#Plot the high temperatures
plt.style.use("seaborn-v0_8-darkgrid")
fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, color='blue', alpha=0.2)

#Format plot
ax.set_title("Daily High and Low Temperatures of 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
