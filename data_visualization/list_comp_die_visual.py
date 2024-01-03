from die6_0 import Die
import plotly.express as px

die1 = Die()
die2 = Die()
die3 = Die()

# Make some rolls and store the results
results = [die1.roll() + die2.roll() + die3.roll() for _ in range(50_000)]

# Analyze the results using list comprehensions
max_result = die1.num_sides + die2.num_sides + die3.num_sides
poss_results = range(3, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results
title = "Rolling Two D8's 50,000 Times"
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
