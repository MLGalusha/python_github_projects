import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    # a class to manage bullets fired by fighter jet

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.fighter_jet.rect.midright

        self.x = float(self.rect.x)

    def update(self):
        #move bullet right across the screen
        #update the exact position of the bullet
        self.x += self.settings.bullet_speed
        #update rect position
        self.rect.x = self.x

    def draw_bullets(self):
        #draw bullets to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)