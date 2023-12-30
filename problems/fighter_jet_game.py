import sys

import pygame

from fighter_jet_settings import Settings

from fighter_jet import FighterJet

class FighterJetGame:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Mr. Fighter Jet")

        self.fighter_jet = FighterJet(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_events()
            self.fighter_jet.update()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_w:
            self.fighter_jet.moving_up = True
        elif event.key == pygame.K_s:
            self.fighter_jet.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_w:
            self.fighter_jet.moving_up = False
        elif event.key == pygame.K_s:
            self.fighter_jet.moving_down = False


    def _update_events(self):
        self.screen.fill(self.settings.bg_colors)
        self.fighter_jet.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ai = FighterJetGame()
    ai.run_game()