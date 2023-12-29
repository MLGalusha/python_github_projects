import sys

import pygame

from rocket_settings import Settings

from rocket_ship import RocketShip

class RocketGame:

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Mr. Rocket")

        self.rocket_ship = RocketShip(self)
    
    def run_game(self):
        while True:
            self._check_events()
            self._update_events()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
   
    def _update_events(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket_ship.blitme()

        pygame.display.flip()

if __name__ == "__main__":
    ai = RocketGame()
    ai.run_game()