import matplotlib.pyplot as plt

from random_walk import RandomWalk 

while True:
    # Able to automatically generate another random walk if the user wants to
    # Assign rw to Random walk and call fill_walk 
    rw = RandomWalk()
    rw.fill_walk()

    # Give the plot attributes and descriptions
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(16,9))
    point_numbers = len(rw.x_values)
    ax.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)
    ax.set_aspect('equal')

    #Emphasize the first and last points in the plot
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Get rid of the numbers on each axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    run_again = input("Do you want to make a new walk? (y/n): ").lower()
    if run_again == 'n':
        break


