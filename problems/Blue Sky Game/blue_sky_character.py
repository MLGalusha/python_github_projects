import pygame

class Character:

    def __init__(self, ai_game):
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("/Users/masongalusha/Downloads/smilling_sun.png")
        self.rect = self.image.get_rect()


        self.rect.midtop = self.screen_rect.midtop


    def blitme(self):
        self.screen.blit(self.image, self.rect)