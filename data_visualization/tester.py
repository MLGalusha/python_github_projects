import matplotlib.pyplot as plt

# Example lists of x and y values
x_values = [1, 2, 3, 4, 5]
y_values = [10, 8, 5, 2, 7]

# Plot the points
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')

# Add labels and title
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Scatter Plot of X and Y Values')

# Show the plot
plt.show()
