import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    # class to represent a single alien in the fleet
    def __init__(self, ai_game):
        # Initialize the alien and set its starting point
        super().__init__()
        self.screen = ai_game.screen
        
        # Load the alien image and set its rect attriubute
        og_image = pygame.image.load("/Users/masongalusha/Downloads/Nave.png")

        og_width = 60
        og_height = 30

        self.image = pygame.transform.scale(og_image, (og_width, og_height))
        self.rect = self.image.get_rect()

        #Start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the aliens exact horizontal position
        self.x = float(self.rect.x)
