import sys
import pygame

from settings import Settings
from player import Player

class StealthGame:
    """Overall Class"""

    def __init__(self):
        """Initialize game"""
        pygame.init()
        self.settings = Settings()
        #self.player = Player(self)
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        self.player = Player(self)

    def run_game(self):
        """Main loop"""
        while True:
            self._check_events()
            self.player.update()
            self._update_screen()

    def _check_events(self):
        """respond to keypresses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.player.moving_left = True
                elif event.key == pygame.K_UP:
                    self.player.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.player.moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.player.moving_left = False
                elif event.key == pygame.K_UP:
                    self.player.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.player.moving_down = False

    def _update_screen(self):
        """Update images on screen, flip to new screen"""
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        pygame.display.flip()

if __name__ == "__main__":
   sg = StealthGame()
   sg.run_game()
