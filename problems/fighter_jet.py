import pygame

class FighterJet:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ships image and get its rect
        self.image = pygame.image.load("/Users/masongalusha/Downloads/jetfighter.png")
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.jet_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.jet_speed

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)