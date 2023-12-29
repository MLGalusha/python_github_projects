import sys

import pygame

from rocket_settings import Settings

from rocket_ship import RocketShip

class RocketGame:

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Mr. Rocket")

        self.rocket_ship = RocketShip(self)
    
    def run_game(self):
        while True:
            self._check_events()
            self.rocket_ship.update()
            self._update_events()
            self.clock.tick(60)
    
    def _update_events(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket_ship.blitme()

        pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket_ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket_ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket_ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket_ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket_ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket_ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket_ship.moving_down = False
 

if __name__ == "__main__":
    ai = RocketGame()
    ai.run_game()