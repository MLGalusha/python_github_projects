from die6_0 import Die

import plotly.express as px

die1 = Die()
die2 = Die()
die3 = Die()

# make some rolls and store the results
results = []
for roll_num in range(50_000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

# Analize the results
frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
poss_results = range(3, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
 
# Visualize the results
title = ("Rolling Two D8's 50,000 Times")
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(
    xaxis_dtick=1,
    font=dict(
        family="Arial, sans-serif",
        size=35,
        color="RebeccaPurple"
    )
)

fig.show()