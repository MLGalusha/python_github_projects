from random import choice

class RandomWalk:
    # A class to generate random walks

    def __init__(self, num_points=5000):
        #Initialize attributes of a walk
        self.num_points = num_points

        #All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        #calculate all points in a walk
        #Keep taking steps until the walk has reached a desired length
        while len(self.x_values) < self.num_points:
            x_step = self._get_step()
            y_step = self._get_step()

            #Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    
    def _get_step(self):
            # Decide which direction to go and how far
            direction = choice([1, -1])
            distance = choice([0, 1, 1000])
            step = direction * distance
            return step
            