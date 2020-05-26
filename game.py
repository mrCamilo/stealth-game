import sys
import pygame

from settings import Settings

class StealthGame:
    """Overall Class"""

    def __init__(self):
        """Initialize game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))

    def run_game(self):
        """Main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 

            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()

if __name__ == "__main__":
   sg = StealthGame()
   sg.run_game()
