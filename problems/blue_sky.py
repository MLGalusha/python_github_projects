import sys

import pygame

from blue_sky_settings import Settings


class BlueSky:
    # Overall class to manage the game assets and behavior

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky Game")

    def run_game(self):
        # Make a loop that updates the game
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = BlueSky()
    ai.run_game()
