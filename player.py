import pygame

class Player:
    """Manages player bmp"""

    def __init__(self, sg_game):
        """Initialize player and starting position"""
        self.screen = sg_game.screen
        self.settings = sg_game.settings
        self.screen_rect = sg_game.screen.get_rect()

        # Load image and rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update ship position based on movement flag."""
        if self.moving_right:
            self.rect.x += 1 
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_up:
            self.rect.y -= 1
        if self.moving_down:
            self.rect.y += 1
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw image at current location."""
        self.screen.blit(self.image, self.rect)
