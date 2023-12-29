import sys

import pygame

from blue_sky_settings_two import Settings

from blue_sky_character_two import Character

class BlueSkyGame:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky Game")

        self.character = Character(self)

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
        self.screen.fill(self.settings.bg_colors)
        self.character.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    ai = BlueSkyGame()
    ai.run_game()