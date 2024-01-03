from random import randint

class Die:
    #A class to represt one die

    def __init__(self, num_sides=6):
        #Assume die has 6 sides unless theres an arguemnt otherwise
        self.num_sides = num_sides

    def roll(self):
        # Return a random value between 1 and number of sides
        return randint(1, self.num_sides)