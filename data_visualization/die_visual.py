from die import Die

import plotly.express as px

# Create two D6
die1 = Die()
die2 = Die(10)

#Make some rolls and store the results in a list
results = []
for roll_num in range(50_000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die1.num_sides + die2.num_sides
poss_results = range(2, max_result +1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
title = "Results of Rolling a D6 and a D10 50,000 Times"
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
# fig.write_html("dice_visual_d6d10.html")
