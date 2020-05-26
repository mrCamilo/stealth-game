import sys
import pygame

class StealthGame:
    """Overall Class"""

    def __init__(self):
        """Initialize game"""
        pygame.init()
        pygame.display.set_caption("hey it me")
        screen = pygame.display.set_mode((480,360))

    #Loading image
    #ball = pygame.image.load("images/ball.gif")
    #ballrect = ball.get_rect()

    def run_game(self):
        """Main loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   sys.exit() 

        #screen.blit(ball,(0,0))
        pygame.display.flip()

if __name__ == "__main__":
   sg = StealthGame()
   sg.run_game()
