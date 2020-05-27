import pygame

class Player:
    """Manages player bmp"""

    def __init__(self, sg_game):
        """Initialize player and starting position"""
        self.screen = sg_game.screen
        self.screen_rect = sg_game.screen.get_rect()

        # Load image and rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw image at current location."""
        self.screen.blit(self.image, self.rect)
