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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 

            self.screen.fill(self.settings.bg_color)
            self.player.blitme()
            pygame.display.flip()

if __name__ == "__main__":
   sg = StealthGame()
   sg.run_game()
